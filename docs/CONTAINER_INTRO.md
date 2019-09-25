# Containers Intro
A container is operating system-level virtualization and has been around for quite some time. By definition, the container share the kernel of the host and relies on certain abstractions to be useful. Docker the company made the technology approachable and incredibly more convenient than any predecessor. In the simplest of forms, a container image contains a virtual filesystem that contains only the dependencies the application needs. An example would be to include the Python interpreter if you wrote a program in Python. 

Containerized applications are primarily designed to run headless. In most cases these applications need to communicate with the outside world or allow inbound traffic depending on the application. Docker containers should be treated as transient, each instance starts in a known state and any data stored inside the virtual filesystem should be treated as ephemeral. This makes it extremely easy and convenient to upgrade and rollback a container. 

If data is required to persist between upgrades and rollbacks of the container, it needs to be stored outside of the container mapped from the host operating system.

The wide adoption of containers are because they're lightweight, reproducible and runs everywhere. Iterations of software delivery lifecycles may be cut down to seconds from weeks with the right processes and tools.

## Key Attributes
These are some of the key elements of Containers.

- Runs on modern architectures and operating systems. Not necessarily as a single source image. 
- Headless services (webservers, databases etc) in microservice architectures.
- Often orchestrated on compute clusters like Kubernetes, Apache Mesos Marathon or Docker Swarm.
- Software vendors often provide official and well tested container images for their applications.

## Learning Resources
Curated list of learning resources for Containers.

- **Interactive:** [Play with Docker](https://training.play-with-docker.com/)<br />
  Great interactive tutorials where you learn how to build, ship and run containers. Also has a follow-on interactive training on Kubernetes.
- **Cartoon:** [The Illustrated Children's Guide to Kubernetes](https://www.youtube.com/watch?v=4ht22ReBjno)<br />
  Illustrative and easy to grasp story of what Kubernetes is.
- **Bonus cartoon:** [A Kubernetes story: Phippy goes to the zoo](https://www.youtube.com/watch?v=R9-SOzep73w)<br />
  A high production quality cartoon explaining Kubernetes API objects.
- **Blog:** [How to choose the right container orchestration and how to deploy it](https://www.freecodecamp.org/news/how-to-choose-the-right-container-orchestration-and-how-to-deploy-it-41844021c241/})<br />
  A brief overview of container orchestrators.

## Practical Exercises
How to get hands-on experience of Containers.

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop) or just Docker if using Linux.
  - Click through the [Get Started](https://docs.docker.com/get-started/) tutorial.
  - Advanced: Run any of the images built in the tutorial on a public cloud service.

## Next Topic
Next up is [CONTAINER TOOLING](CONTAINER_TOOLING.md).
