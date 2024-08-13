# Reusable OpenControl Components (SSP-Toolkit).

## SC: System and Communications Protection

### SC-1: Policy and Procedures

```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] system and communications protection policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the system and communications protection policy and the associated system and communications protection controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the system and communications protection policy and procedures; and
 - c. Review and update the current system and communications protection:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete


##### Contractor

CivicActions has developed, documented and disseminated to personnel a system and communication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Communications Protection (SC) Policy CivicActions document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs/>.





##### Project

System and communications protection policy and procedures are formally documented in the None and the Project SSP. The Department reviews and updates the policy as necessary and has been continually updated since April 2008.
This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.



### SC-5: Denial-of-service Protection

```text
 - a. [Selection: Protect against, Limit] the effects of the following types of denial-of-service events: [Assignment: organization-defined types of denial-of-service events]; and
 - b. Employ the following controls to achieve the denial-of-service objective: [Assignment: organization-defined controls by type of denial-of-service event].

```
**Status:** partial


##### Drupal

Drupal has a manual ability to block IP addresses in cases where attacks bypass cloud protection. This is managed by CivicActions Operations.




##### Ilias

Ilias has a manual ability to block IP addresses in cases where attacks bypass cloud protection. This is managed by CivicActions Operations.




##### Project

The Project system is configured to reduce vulnerabilities in its operating system and applications to protect against Denial of Service (DoS) attacks.
The Project support staff ensures the system is protected against or limits the effect of DoS attacks as specified in the None.



### SC-7: Boundary Protection

```text
 - a. Monitor and control communications at the external managed interfaces to the system and at key internal managed interfaces within the system;
 - b. Implement subnetworks for publicly accessible system components that are [Selection: physically, logically] separated from internal organizational networks; and
 - c. Connect to external networks or systems only through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.

```
**Status:** complete


##### Drupal

Drupal, when deployed on SELinux in full enforcing mode, minimizes the number of services and computing nodes that are exposed to the Internet. Drupal employs both the AWS platform safeguards and the Drupal Watchdog module in monitoring and recording system events. All other computing nodes used in the system are isolated within AWS.





##### Ilias

Ilias, when deployed on SELinux in full enforcing mode, minimizes the number of services and computing nodes that are exposed to the Internet. Ilias employs both the AWS platform safeguards and the Ilias logging in monitoring and recording system events. All other computing nodes used in the system are isolated within AWS.




##### Project

The Project system has monitored and controlled communications at the external boundary of the information system and at key internal boundaries within the system, where appropriate. The Project allocates publicly accessible information system components (e.g., public web servers) specific IP address and port combinations. Public access into the organization’s internal networks is prevented except as appropriately mediated.



#### a

##### AWS

In this architecture, network communications to, from, and between VPCs, subnets and Amazon S3 buckets are controlled as follows: AWS Route Tables specify which subnets in each VPC are accessible through gateways and which are isolated/private. AWS Security Groups provide stateful inbound/outbound port/protocol restrictions, Amazon Simple Storage Service (Amazon S3) buckets support access control restrictions based on network source/destination.



#### b

##### AWS

In this architecture, subnetworks for publicly accessible system components are logically separated from internal private subnetworks via AWS security groups, refined routing tables, and NACLs.



#### c

##### AWS

In this architecture, connection to external networks is possible only through Internet Gateways (IGWs) or NAT gateways (in regions where supported by AWS VPC) and are restricted based on ports/protocols via AWS Security groups, and default subnet rules provided by NACLs.



### SC-12: Cryptographic Key Establishment and Management

```text
Establish and manage cryptographic keys when cryptography is employed within the system in accordance with the following key management requirements: [Assignment: organization-defined requirements for key generation, distribution, storage, access, and destruction].

```
**Status:** none


##### AWS

In this architecture, initial private/public SSH keys stored in Identity and Access Management (IAM) are supplied to Amazon EC2 instances upon launch, and the public key portion is managed within the AWS Amazon EC2 service. In addition, server-side encryption is used for Amazon S3 storage and Amazon RDS databases, using key management provided by AWS for the storage buckets and Amazon RDS databases.





##### Project

Use of cryptographic key management for the Project system is in use for at the time of implementation for authentication. CivicActions utilizes customer agency supplied PIV credentials for access to customer instances of the Project. Access enforcement and authentication requirements for Project are described in AC-2 & IA-2. AWS platform does not utilize or manage cryptographic keys within the ACE boundary.



### SC-13: Cryptographic Protection

```text
 - a. Determine the [Assignment: organization-defined cryptographic uses]; and
 - b. Implement the following types of cryptography required for each specified cryptographic use: [Assignment: organization-defined types of cryptography for each specified cryptographic use].

```
**Status:** none


##### AWS

In this architecture, encryption mechanisms are employed for data at rest and in transit. For data at rest, AES-256 Server Side encryption is employed for data stored in Amazon S3, and Amazon RDS databases. For data in transit, to protect against exposure of any cleartext data transmitted deliberately (upload/download) or incidentally during interactive systems management operations, Amazon S3 object access can only be conducted over encrypted sessions via TLS; the bastion host, Amazon EC2 instances and associated security groups are configured for encrypted SSH sessions only. For web user access, the Elastic Load Balancing (ELB) employs a TLS endpoint.

AWS built-in features employ TLS for AWS Management Console sessions, AWS API calls, and AWS Command Line Interface connections.





##### Contractor

The information system implements:

- Cryptographic modules through Secure Shell (SSH) to allow administrators to securely logon to the
  various system components

- HTTPS/SSL (TLS) for connection to web-based services
- TLS for connection to email services
- AES-256 (FIPS 140-2 validated) for data at rest (with Elastic Block Store (EBS) volumes)



### SC-15: Collaborative Computing Devices and Applications

```text
 - a. Prohibit remote activation of collaborative computing devices and applications with the following exceptions: [Assignment: organization-defined exceptions where remote activation is to be allowed]; and
 - b. Provide an explicit indication of use to users physically present at the devices.

```
**Status:** none


##### Project

This control is not applicable, as the Project system does
employ any collaborative computing devices.



### SC-20: Secure Name/address Resolution Service (authoritative Source)

```text
 - a. Provide additional data origin authentication and integrity verification artifacts along with the authoritative name resolution data the system returns in response to external name/address resolution queries; and
 - b. Provide the means to indicate the security status of child zones and (if the child supports secure resolution services) to enable verification of a chain of trust among parent and child domains, when operating as part of a distributed, hierarchical namespace.

```
**Status:** None


##### Contractor

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (authoritative source)



### SC-21: Secure Name/address Resolution Service (recursive or Caching Resolver)

```text
Request and perform data origin authentication and data integrity verification on the name/address resolution responses the system receives from authoritative sources.

```
**Status:** None


##### Contractor

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (recursive or caching resolver)



### SC-22: Architecture and Provisioning for Name/address Resolution Service

```text
Ensure the systems that collectively provide name/address resolution service for an organization are fault-tolerant and implement internal and external role separation.

```
**Status:** none


##### Contractor




### SC-39: Process Isolation

```text
Maintain a separate execution domain for each executing system process.

```
**Status:** none


##### AWS

In this architecture, the AMIs that make up the operating systems deployed on Amazon EC2 instances maintain separate execution domains/address spaces for executing processes within the customer operating environment.

AWS built-in features of the hypervisors that support the infrastructure maintain separate execution domains/address spaces for executing processes.





##### Contractor

Process isolation is maintained on the Linux platform. Linux is the only operating system that is part of the boundary.
