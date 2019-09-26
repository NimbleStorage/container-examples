# Cloud Native Computing Tooling
*Reading time, about 2 minutes. External study not included*

Tools to interact with infrastructure and applications come in many shapes and forms. A common pattern is to learn by visually creating and deleting resources to understand an end-state. Once a pattern has been established, either APIs, 3rd party or a custom CLI is used to manage the life-cycle of the deployment in a declarative manner by manipulating RESTful APIs. Also known as Infrastructure-as-Code.

## Key Attributes
These are some of the key elements of Cloud Native Computing Tooling.

- State stored in a Source Code Control System (SCCS).
- Changes made to state is peer reviewed and automatically tested in non-production environments before merged and deployed.
- Industry standard IT automation tools are often used to implement changes. Ansible, Puppet, Salt and Chef are example tools.
- Public clouds often provide CLIs to manage resources. These are great to prepare, inspect and test deployments with.
- Configuration and deployment files are often written in a human and machine readable format, such as JSON, YAML or TOML.

## Learning Resources
Curated list of learning resources for Cloud Native Computing Tooling.

- **Blog:** [Imperative vs Declarative](https://dev.to/stereobooster/imperative-vs-declarative-1f09)<br />
  A blog that highlight the fundamental differences between the two.
- **Reference:** [json.org](https://www.json.org/)<br />
  Definitive guide on JavaScript Object Notation (JSON) data structures.
- **Reference:** [YAML Syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)<br />
  Simple guide for YAML Ain't Markup Language (YAML). 
- **Reference:** [RESTful API Tutorial](https://restfulapi.net/)<br />
  Learn the design principles of REpresentational State Transfer (REST).
- **Screencast:** [Super-basic Introduction to Ansible](https://www.youtube.com/watch?v=xew7CMkL7jY)<br />
  The simplest of Ansible tutorials starting with nothing.

## Practical Exercises
How to get hands-on experience of Cloud Native Computing Tooling.

- Sign-up on AWS.
  - Install the [AWS CLI](https://aws.amazon.com/cli/) and [Ansible](https://www.ansible.com/resources/get-started) in a Linux instance.
  - Configure [BOTO](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration).
  - Use the Ansible [EC2 module](https://docs.ansible.com/ansible/latest/modules/ec2_module.html#ec2-module) to create and delete an instance.

## Next Topic
Next up is [CLOUD NATIVE STORAGE](CLOUD_NATIVE_STORAGE.md).
