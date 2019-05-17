# HPE Storage for Containers Workshop at KubeCon US 2018
Welcome to the HPE workshop around persistent storage for containers using Kubernetes. You may follow this tutorial at any time after the show. TL;DR, there is now a [YouTube version](https://youtu.be/sECNuM268GI) of this workshop and the slides from the talk you can find on [slideshare](https://www.slideshare.net/dri374/hpe-storage-kubecon-us-2018-workshop).

# Table of Contents
- [Objectives](#objectives)
- [Prerequisites](#prerequisites)
  * [Installing lab using Vagrant and VMware Fusion](#installing-lab-using-vagrant-and-vmware-fusion)
  * [Installing lab to anything else](#installing-lab-to-anything-else)
  * [Deploying Nemo, Dory & Co](#deploying-nemo-dory--co)
  * [Validation steps (optional)](#validation-steps-optional)
- [Workshop labs](#workshop-labs)
  * [Create a StorageClass](#create-a-storageclass)
  * [Create a PersistentVolumeClaim](#create-a-persistentvolumeclaim)
  * [Deploy a Stateful workload referencing a PersistentVolumeClaim](#deploy-a-stateful-workload-referencing-a-persistentvolumeclaim)
  * [Inspecting the workload](#inspecting-the-workload)
  * [Clone a PersistentVolumeClaim and start another workload](#clone-a-persistentvolumeclaim--and-start-another-workload)

# Objectives
In this workshop/tutorial/lab we'll jump through the hoops to setup a single node sandbox Kubernetes instance with a dynamic provisioner to illustrate how to use a `StorageClass` to provision `PersistentVolumes` through `PersistentVolumeClaims`.

# Prerequisites 
The lab environment we're going to use is deployed in a clean single virtual machine. A Vagrantfile is provided (using the vmware_fusion provider) and it may be adapted to your favorite Vagrant provider.

Prior knowledge of Kubernetes nomenclature and storage terminology will be helpful going through these labs.

Please chose the method to bring up the sandbox:
- [Installing lab using Vagrant and VMware Fusion](#installing-lab-using-vagrant-and-vmware-fusion)
- [Installing lab to anything else](#installing-lab-to-anything-else)

## Installing lab using Vagrant and VMware Fusion
Please jump to the [next section](#installing-lab-to-anything-else) if you don't have a Mac with VMware Fusion.

The Vagrant install method assumes `kubectl` being installed prior on your Mac. `kubectl` is availble through either [Homebrew](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-homebrew-on-macos) or [Macports](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-macports-on-macos).

Create a suitable home for your lab machine and then:
```
git clone https://github.com/NimbleStorage/container-examples/ 
cd container-examples/misc/KubeConUS18
```
Edit the `Vagrantfile` and stick a static IP address on the `private_network` interface. Second, add that same IP address to the Ansible extra var further down the Vagrantfile. Then:
```
vagrant up
```
You should now have a `config` file in your current directory on your Mac. This is your `KUBECONFIG`. Reference it to access your API server.
```
export KUBECONFIG=$(pwd)/config
kubectl get nodes
```
You should something similar to this:
```
NAME      STATUS   ROLES    AGE   VERSION
kubecon   Ready    master   39m   v1.13.0
```
You're now ready to [Deploy Nemo, Dory & Co](#deploying-nemo-dory--co).

## Installing lab to anything else
These steps assumes you have a VM or cloud instances with the following characteristics:

* Ubuntu 18.04
* Access via SSH 
* User has password-less sudo access to root 
* Has python installed

Where you execute the Ansible playbook has very little importance. Let's assume the rest of the steps are being executed in the VM itself as an `ansible.cfg` and an `inventory` for `localhost` is provided in the repo.

```
sudo apt-get update && sudo apt-get install -y ansible 
git clone https://github.com/NimbleStorage/container-examples/
cd container-examples/misc/KubeConUS18
ansible-playbook  kubecon.yml -e local_listener=192.168.59.40
```
**Note:** Pay attention to `local_listener`, it needs to match the IP address you want the API server to listen on.

The Ansible playbook copies the `KUBECONFIG` into place, so this should just work:
```
kubectl get nodes
```
You should something similar to this:
```
NAME      STATUS   ROLES    AGE   VERSION
kubecon   Ready    master   31s   v1.13.0
```
**Note:** Copy the `$HOME/.kube/config` file to any host you want to access your Kubernetes API server from, like your laptop, if it has `kubectl` installed.

You're now ready to [Deploy Nemo, Dory & Co](#deploying-nemo-dory--co).

## Deploying Nemo, Dory & Co
Nemo and Dory is deployed as a `DaemonSet`. Doryd runs as a `Deployment`. 

Declare with:
```
kubectl create -f https://raw.githubusercontent.com/NimbleStorage/Nemo/master/runtime/k8s/daemonset-nemod.yaml
kubectl create -f https://raw.githubusercontent.com/NimbleStorage/Nemo/master/runtime/k8s/deploy-doryd.yaml
```

You may now jump to the [labs](#workshop-labs).

**Note:** The Nemo `DaemonSet` will create an OpenZFS pool on a loopback device and store with your node. It's not really practical for anything else but to test with. 

## Validation steps (optional)
If you're uncertain if everything installed and deploy correctly, you may deploy this test `StatefulSet` to ensure the `Pod` comes up:
```
kubectl create -f https://raw.githubusercontent.com/NimbleStorage/Nemo/master/runtime/k8s/sc-transactionaldb.yaml
kubectl create -f https://raw.githubusercontent.com/NimbleStorage/Nemo/master/runtime/k8s/statefulset-mariadb.yaml
kubectl get pod -w
```

Hit CTRL+C when it says:
```
NAME        READY   STATUS              RESTARTS   AGE
mariadb-0   0/1     Pending             0          2s
mariadb-0   0/1     ContainerCreating   0          2s
mariadb-0   1/1     Running             0          19s
```

# Workshop labs
If everything worked out in the prequisite steps, a dynamic provisioner is now listening on `dev.hpe.com` and have `nemo` as a registered driver.

The follow labs need do be done in sequence with cluster-admin privileges (as provided in the generated `KUBECONFIG` used in this tutorial). In a real world scenario, the cluster-admin would only create the StorageClass and have restricted users deploying apps and creating `PersistentVolumeClaims`. Kubernetes RBAC is out of scope for this tutorial.

**Tip:** If you want to play around with the different parameters, you may call the online help with the `docker` command on the Kubernetes node itself:
```
sudo docker volume create -d nemo -o help
```

**Note:** The rest of the workshop assumes you're in the `labs` sub-directory.

## Create a StorageClass
First we'll create a default `StorageClass`. Any `PersistentVolumeClaim` created that does not ask for a particular `StorageClass` will have its `PersistentVolume` provisioned by this `StorageClass`.

To show how practical `allowOverrides` is, we let the users set a custom description, this follows all the way down to the storage subsystem if you would've used Nimble. In the case of Nemo, it's just a metadata field on the OpenZFS dataset.

The "general" `StorageClass`:
```
---
kind: StorageClass
apiVersion: storage.k8s.io/v1beta1
metadata:
  name: general
  annotations:
    storageclass.beta.kubernetes.io/is-default-class: "true"
provisioner: dev.hpe.com/nemo
parameters:
  allowOverrides: description
  description: "Volume provisioned from default StorageClass"
```

Create the `StorageClass`:
```
kubectl create -f sc-general.yml 
```

## Create a PersistentVolumeClaim
We'll create a `PersistentVolumeClaim` that will be caught by the default `StorageClass` and we'll override with a custom description:

The "mariadb" `PersistentVolumeClaim`:
```
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mariadb
  annotations:
    dev.hpe.com/description: My MariaDB Claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 32Gi
```

Create the `PersistentVolumeClaim`:
```
kubectl create -f pvc-mariadb.yml
```

The `PersistentVolumeClaim` should immeditely be bound to a `PersistentVolume`, inspecting:
```
kubectl get pvc -o yaml
```

As a cluster-admin, you're also allowed to inspect the `PersistentVolume`:
```
kubectl get pv -o yaml
```

## Deploy a Stateful workload referencing a PersistentVolumeClaim
We now have a `PersistentVolumeClaim` we can reference from a workload to mount inside a `Pod`. You may pick any workload type or stateful app, the example provided uses MariaDB to replace `/var/lib/mysql` with the `PersistentVolumeClaim`. 

**Heads-up:** Since Nemo is a locally scoped Docker Volume driver it's not really practical to use for anything else than `StatefulSet` where locality remain static throughout its lifecycle of the workload. However, `StatefulSets` uses `persistentVolumeClaimTemplates`, which is not what we want to showcase in this lab. You may also experience a few side-effects of this if you run this lab on an actual cluster where the dynamic provisioner may create the `PersistentVolume` on one node in the cluster and the workload starts up somewhere else. The FlexVolume driver will still create the volume wherever the workload is started but it may not be what you expected.

MariaDB will be deployed as a standalone `Pod`:
```
---
apiVersion: v1
kind: Pod
metadata:
  name: mariadb
  labels:
    app: mariadb
spec:
  containers:
    - image: mariadb:latest
      name: mariadb
      env:
        - name: MYSQL_ROOT_PASSWORD
          value: YOUR_PASSWORD
      ports:
        - containerPort: 3306
          name: mariadb
      volumeMounts:
        - name: mariadb
          mountPath: /var/lib/mysql
  volumes:
    - name: mariadb
      persistentVolumeClaim: 
        claimName: mariadb
```

Let's create the `Pod`:
```
kubectl create -f pod-mariadb.yml
```

You may want to wait here until the workload comes up:
```
kubectl get pod -w
```

## Inspecting the workload
The MariaDB instance will intialize the `mysql` database and later be ready for use once the `Pod` starts. Let's `exec` ourselves into the `Pod` and examine what is going on:
```
kubectl exec -i mariadb -- df -h /var/lib/mysql
```

You should now see something similar:
```
Filesystem                                             Size  Used Avail Use% Mounted on
tank/k8s/general-1d12b4c1-fb45-11e8-865a-000c295816df   32G  3.7M   32G   1% /var/lib/mysql
```

For the next exercise, we need to create some unique data, let's create a new database and create a "Hello World" table and data:
```
kubectl exec -i mariadb -- mysql -pYOUR_PASSWORD < kubecon.sql 
kubectl exec -i mariadb -- mysql kubecon -pYOUR_PASSWORD <<< "insert into main (k,v) values ('mykey','myUniqueValueGoesHere');"
kubectl exec -i mariadb -- mysql kubecon -pYOUR_PASSWORD <<< "select * from main;"
```

You should now see your inserted data:
```
k      v
mykey  myUniqueValueGoesHere
```

## Clone a PersistentVolumeClaim  and start another workload
From the previous step, we created a database with some scrap data. We now want to clone that into a new `PersistentVolumeClaim` and use in a second workload. Let's pretend we want to debug an issue that is potentially disruptive to the "production" database.

Create a new `PersistentVolumeClaim` with an annotation that instructs the dynamic provisioner to clone from the previously created `PersistentVolumeClaim`. The `PersistentVolumeClaim` that you clone from must exist in the same Kubernetes `Namespace` where you create the new `PersistentVolumeClaim`.

This is what the clone `PersistentVolumeClaim` looks like:
```
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mariadb-clone
  annotations:
    dev.hpe.com/description: My MariaDB Clone Claim
    dev.hpe.com/cloneOfPVC: "mariadb"
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Let's create the `PersistentVolumeClaim`:
```
kubectl create -f pvc-mariadb-clone.yml
```

Now, create another `Pod` that references the new `PersistentVolumeClaim`:
```
---
apiVersion: v1
kind: Pod
metadata:
  name: mariadb-clone
  labels:
    app: mariadb-clone
spec:
  containers:
    - image: mariadb:latest
      name: mariadb
      env:
        - name: MYSQL_ROOT_PASSWORD
          value: YOUR_PASSWORD
      ports:
        - containerPort: 3306
          name: mariadb
      volumeMounts:
        - name: mariadb
          mountPath: /var/lib/mysql
  volumes:
    - name: mariadb
      persistentVolumeClaim: 
        claimName: mariadb-clone
```
**Note:** The difference is the naming of the `Pod` and which `PersistentVolumeClaim` we're referencing. 

Execute:
```
kubectl create -f pod-mariadb-clone.yml
```

After it's up, let's inspect the database:
```
kubectl exec -i mariadb-clone -- mysql kubecon -pYOUR_PASSWORD <<< "select * from main;"
```

You should now see your data cloned from the previous steps:
```
k      v
mykey  myUniqueValueGoesHere
```

Presto! The database is now offically cloned and whatever you do to it won't affect the original. Let's drop it and inspect the source:
```
kubectl exec -i mariadb-clone -- mysql kubecon -pYOUR_PASSWORD <<< "drop database kubecon;"
kubectl exec -i mariadb -- mysql kubecon -pYOUR_PASSWORD <<< "select * from main;"
```

**Important:** Notice the difference in the `Pod` name above.

# Congratulations!
You have successfully completed this tutorial!
