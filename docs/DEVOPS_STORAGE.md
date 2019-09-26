# DevOps Storage
*Reading time, about 2 minutes. External study not included*

There aren't any particular storage paradigm (file/block/object) that is associated with DevOps. It's the implementation of the application and how it consumes storage that we vaguely may associate with DevOps. It's more of the practice of that the right security controls are in place and whomever needs storage resource are fully self serviced. Human or machine.

## Key Attributes
These are some of the key elements of DevOps Storage.

- API driven through RBAC. Ensuring automation may put in place for the endpoint or person that needs access to the resource.
- Rich data management. If a value stream only needs a low performing read-only view of a certain dataset, resources supporting the value stream should only have read-only access with performance constrains.
- Agile and mobile. At will, data should be made available for a certain application or resource for its purpose. Whether it's in the public cloud, on-prem or as-a-service through safe and secure automation.

## Learning Resources
Curated list of learning resources for DevOps Storage.

- **Blog:** [Is Your Storage Too Slow for DevOps?](https://devops.com/is-your-storage-too-slow-for-devops/)<br />
  Characterization of DevOps Storage attributes.

## Practical Exercises
How to get hands-on experience of DevOps Storage.

- Familiarize yourself with a storage system's RESTful API and automation capabilities.
  - Deploy an [Ansible Tower](https://www.ansible.com/products/tower/trial) trial.
  - Write an Ansible playbook that creates a storage resource on said system.
  - Create a job in Ansible Tower with the playbook and make it available to a restricted user.

## The End
You have successfully completed the [CONTAINERS 101](README.md) topics provided by HPE. If you have time, please provide your feedback [through this survey](https://www.surveymonkey.com/r/CZZX63T).
