# Container Storage
*Reading time, about 3 minutes. External study not included*

Due to the ephemeral nature of a container, storage is predominantly served from the host the container is running on and is dependent on which container runtime is being used where data is stored. In the case of Docker, the overlay filesystems are under `/var/lib/docker`. If a certain path inside the container need to persist between upgrades, restarts on a different host or any other operation that will lose the locality of the data, the mount point needs to be replaced with a "bind" mount from the host.

There are also container runtime technologies that are designed to persist the entire container, effectively treating the container more like a long-lived Virtual Machine. Examples are Canonical LXD, WeaveWorks Footloose and HPE BlueData. This is particularly important for applications that rely on its projected node info to remain static throughout its entire lifecycle.

We can then begin to categorize containers into three main categories based on their lifecycle vs persistence needs.

- **Stateless Containers**<br />
  No persistence needed across restarts/upgrades/rollbacks
- **Stateful Containers**<br />
  Require certain mountpoints to persist across restarts/upgrades/rollbacks
- **Persistent Containers**<br />
  Require static node identity information across restarts/upgrades/rollbacks

Some modern Software-defined Storage solutions are offered to run alongside applications in a distributed fashion. Effectively enforcing multi-way replicas for reliability and eat into CPU and memory resources of the IaaS bill. This also introduces the dilemma of effectively locking the data into the container orchestrator and its compute nodes. Although it's convenient for developers to become self-entitled storage administrators. 

To stay in control of the data and remain mobile, storing data outside of the container orchestrator is preferable. Many container orchestrators provide plugins for external storage, some are built-in and some are supplied and supported by the storage vendor. Public clouds provide storage drivers for their IaaS storage services directly to the container orchestrator. This is widely popular pattern we're also seeing in BYO IaaS solutions such as VMware vSphere.

## Key Attributes
These are some of the key elements of Container Storage.

- Ephemeral storage needs to be fast and expandable as environments scale with more diverse applications.
- Data for stateful containers  is ideally stored outside of the container orchestrator, either the IaaS or external highly-available storage.
- Persistent containers require niche storage solution tightly coupled with the container runtime and the container orchestrator or scheduler.
- Most storage solutions provide an "access mode" often referred to as ReadWriteOnce (RWO) which only allow one Pod (in the Kubernetes case or containers from the same host access the volume. To allow multiple Pods and containers from multiple hosts, a distributed filesystem or an NFS server (widely adopted) is required to provide ReadWriteMany (RWX) access.

## Learning Resources
Curated list of learning resources for Container Storage.

- **Talk:** [Kubernetes Storage Lingo 101](https://youtu.be/uSxlgK1bCuA)<br />
  A talk that lays out the nomenclature for storage in Kubernetes in an understandable way.
- **Reference:** [Docker: Volumes](https://docs.docker.com/storage/volumes/)<br />
  Fundamental reference on how to make mount points persist for containers.
- **Reference:** [Kubernetes: Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)<br />
  Using volumes in Kubernetes Pods.
- **Podcast:** [Kubernetes Storage with Saad Ali](https://softwareengineeringdaily.com/2019/06/10/kubernetes-storage-with-saad-ali/)<br />
  Essential listen understand the difference between high-availability and automatic recovery.

## Practical Exercises
How to get hands-on experience of Container Storage.

- Use Docker Desktop.
  - Replace a mount point in an interactive container with a mount point from the host
- Deploy a Amazon EKS or equivalent cluster.
  - Create a Persistent Volume Claim.
  - Run `kubectl get pv -o yaml` and match the Persistent Volume against the IaaS block volumes.

## Next Topic
Next up is [DEVOPS INTRO](DEVOPS_INTRO.md).
