# Cloud Native Storage
*Reading time, about 2 minutes. External study not included*

Storage for cloud computing come in many shapes and forms. Compute instances boot off block devices provided by the IaaS through the hypervisor. More devices may be attached for application data to keep host OS and application separate. Most clouds allow these devices to be snapshotted, cloned and reattached to other instances. These block devices are normally offered with different backend media, such as flash or spinning disks. Depending on the use cases and budgets parameters may be tuned to be just right.

For unstructured workloads, API driven object storage is the dominant technology due to the dramatic difference in cost and simplicity vs cloud provided block storage. An object is uploaded through an API endpoint with HTTP and automatically distributed (highly configurable) to provide high durability. The URL of the object will remain static for the duration of its lifetime. The main prohibitor for object storage adoption is that existing applications relying on POSIX filesystems need to be rewritten. 

## Key Attributes
These are some of the key elements of Cloud Native Storage.

- Provisioned and attached via APIs through IaaS if using block storage.
- Data and metadata is managed with RESTful APIs if using object. No backend to manage. Consumers use standard URLs to retrieve data.
- Highly durable with object storage. Durability equal to a local RAID device for block storage.
- Some cloud providers offer Filesystem-as-a-Service, normally standard NFS or CIFS.
- Backup and recovery of application data still needs to managed like traditional storage for block. Multi-region multi-copy persistence for object storage.

## Learning Resources
Curated list of learning resources for Cloud Native Storage.

- **Wikipedia:** [Object storage](https://en.wikipedia.org/wiki/Object_storage)<br />
  Digestible overview of Object Storage.
- **Tutorial:** [Host images on Amazon S3](https://www.channelape.com/uncategorized/host-images-amazon-s3-cheap-5-minutes/)<br />
  A five minute step-by-step guide how to host images on Amazon S3.
- **Reference:** [Amazon EBS features](https://aws.amazon.com/ebs/features/)<br />
  An overview of typical attributes for cloud provided block storage.
- **Reference:** [HPE Cloud Storage Cost Calculator](https://hpe.valuestoryapp.com/bvc/cloudvolumes)<br />
  Calculate the real costs of cloud storage based on highly dynamic data management environments.

## Practical Exercises
How to get hands-on experience of Cloud Native Storage.

- Setup a S3 compatible object storage server or use a public cloud.
  - Scality has a open source [S3 server](https://github.com/scality/cloudserver) for non-production use.
  - Configure [s3cmd](https://s3tools.org/s3cmd) to upload and retrieve files from a bucket.
- Analyze costs of 100TB of data for one year on Amazon S3 vs Azure Manage Disks.

## Next Topic
Next up is [CONTAINER INTRO](CONTAINER_INTRO.md).
