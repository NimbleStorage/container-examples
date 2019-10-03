# Container Tooling
*Reading time, about 2 minutes. External study not included*

Most of the tooling around containers is centered around what particular container orchestrator or development environment is being utilized. Usage of the tools differ greatly depending on the role of the user. As an operator the toolkit includes both IaaS and managing the platform to perform upgrades, user management and peripheral services such as storage and ingress load balancers. 

While many popular platforms today are based on Kubernetes, the tooling has nuances. Upstream Kubernetes uses `kubectl`, Red Hat OpenShift uses the OpenShift CLI, `oc`. With other platforms such as Rancher, nearly all management can be done through a web UI.

## Key Attributes
These are some of the key elements of Container Tooling.

- Most tools are simple, yet powerful and follow UNIX principles of doing one thing and doing it well.
- The `docker` and `kubectl` CLIs are the two most dominant for low level management.
- Workload management usually relies on external tools for simplicity, such as `docker-compose`, `kompose` and `helm`.
- Some platforms have ancillary tools to marry the IaaS with the cluster orchestrator. Such an example is `rke` for Rancher and `gkectl` for GKE On-Prem.
- The public clouds have builtin container orchestrator and container management into their native CLIs, such as `aws` and `gcloud`.
- Client side tools normally rely on environment variables and user environment configuration files that store credentials, API endpoint locations and other security aspects.

## Learning Resources
Curated list of learning resources for Container Tooling.

- **Reference:** [Use the Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)<br />
  Docker CLI reference.
- **Reference:** [The kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)<br />
  The kubectl cheat sheet.
- **Utility:** [kustomize.io](https://kustomize.io/)<br />
  Kubernetes native configuration managment.
- **Tutorial:** [The Ultimate Guide to Podman, Skopeo and Buildah](https://www.opensource.sa/2019/06/20/the-ultimate-guide-to-podman-skopeo-and-buildah/)<br />
  An alternative container toolchain to Docker using Podman, Buildah and Skopeo.

## Practical Exercises
How to get hands-on experience of Container Tooling.

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop) or just Docker if using Linux.
  - Build a container image of an application you understand (docker build).
  - Run the container image locally (docker run).
  - Ship it to Docker Hub (docker push).
- Create an Amazon EKS cluster or equivalent.
  - Retrieve the `kubeconfig` file.
  - Run `kubectl get nodes` on your local machine.
  - Start a `Pod` using the container image built in previous exercise.

## Next Topic
Next up is [CONTAINER STORAGE](CONTAINER_STORAGE.md).
