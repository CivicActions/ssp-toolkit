# System And Communications Protection (SC) Standard (SOP)

*Reviewed and updated 2025-01-31*

----

**Table of Contents**
<!--TOC-->

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Standards](#standards)
  - [SC-01 System And Communications Protection Policy And Procedures](#sc-01-system-and-communications-protection-policy-and-procedures)
  - [SC-05 Denial Of Service Protection](#sc-05-denial-of-service-protection)
  - [SC-07 Boundary Protection](#sc-07-boundary-protection)
  - [SC-12 Cryptographic Key Establishment And Management](#sc-12-cryptographic-key-establishment-and-management)
  - [SC-13 Cryptographic Protection](#sc-13-cryptographic-protection)
  - [SC-15 Collaborative Computing Devices](#sc-15-collaborative-computing-devices)
  - [SC-20 Secure Name / Address Resolution Service](#sc-20-secure-name--address-resolution-service)
  - [SC-21 Secure Name / Address Resolution Service](#sc-21-secure-name--address-resolution-service)
  - [SC-22 Architecture And Provisioning For Name / Address Resolution Service](#sc-22-architecture-and-provisioning-for-name--address-resolution-service)
  - [SC-39 Process Isolation](#sc-39-process-isolation)

<!--TOC-->

----

## Introduction

### Purpose

The Office of the Chief Information Officer (OCIO) Information Assurance Services (IAS) publication Information Technology (IT) System Access Controls Standard of February 11, 2022 provides a comprehensive basis for management across all systems in the Department. This document provides specific guidance as defined and implemented by the Project.

### Scope

This system has been categorized as a FIPS-199 LOW system, and as such this document applies only to relevant controls, policies, processes and procedures as defined within the system.

## Standards

### SC-01 System And Communications Protection Policy And Procedures

CivicActions has developed, documented and disseminated to personnel a system and communication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Communications Protection (SC) Policy CivicActions document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs/>.


System and communications protection policy and procedures are formally documented in the None and the Project SSP. The Department reviews and updates the policy as necessary and has been continually updated since April 2008.
This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.


### SC-05 Denial Of Service Protection

Ilias has a manual ability to block IP addresses in cases where attacks bypass cloud protection. This is managed by CivicActions Operations.

Drupal has a manual ability to block IP addresses in cases where attacks bypass cloud protection. This is managed by CivicActions Operations.

The Project system is configured to reduce vulnerabilities in its operating system and applications to protect against Denial of Service (DoS) attacks.
The Project support staff ensures the system is protected against or limits the effect of DoS attacks as specified in the None.


### SC-07 Boundary Protection

Ilias, when deployed on SELinux in full enforcing mode, minimizes the number of services and computing nodes that are exposed to the Internet. Ilias employs both the AWS platform safeguards and the Ilias logging in monitoring and recording system events. All other computing nodes used in the system are isolated within AWS.

Drupal, when deployed on SELinux in full enforcing mode, minimizes the number of services and computing nodes that are exposed to the Internet. Drupal employs both the AWS platform safeguards and the Drupal Watchdog module in monitoring and recording system events. All other computing nodes used in the system are isolated within AWS.


The Project system has monitored and controlled communications at the external boundary of the information system and at key internal boundaries within the system, where appropriate. The Project allocates publicly accessible information system components (e.g., public web servers) specific IP address and port combinations. Public access into the organization’s internal networks is prevented except as appropriately mediated.


**a.**	In this architecture, network communications to, from, and between VPCs, subnets and Amazon S3 buckets are controlled as follows: AWS Route Tables specify which subnets in each VPC are accessible through gateways and which are isolated/private. AWS Security Groups provide stateful inbound/outbound port/protocol restrictions, Amazon Simple Storage Service (Amazon S3) buckets support access control restrictions based on network source/destination.

**b.**	In this architecture, subnetworks for publicly accessible system components are logically separated from internal private subnetworks via AWS security groups, refined routing tables, and NACLs.

**c.**	In this architecture, connection to external networks is possible only through Internet Gateways (IGWs) or NAT gateways (in regions where supported by AWS VPC) and are restricted based on ports/protocols via AWS Security groups, and default subnet rules provided by NACLs.

### SC-12 Cryptographic Key Establishment And Management

In this architecture, initial private/public SSH keys stored in Identity and Access Management (IAM) are supplied to Amazon EC2 instances upon launch, and the public key portion is managed within the AWS Amazon EC2 service. In addition, server-side encryption is used for Amazon S3 storage and Amazon RDS databases, using key management provided by AWS for the storage buckets and Amazon RDS databases.


Use of cryptographic key management for the Project system is in use for at the time of implementation for authentication. CivicActions utilizes customer agency supplied PIV credentials for access to customer instances of the Project. Access enforcement and authentication requirements for Project are described in AC-2 & IA-2. AWS platform does not utilize or manage cryptographic keys within the ACE boundary.


### SC-13 Cryptographic Protection

The information system implements:

- Cryptographic modules through Secure Shell (SSH) to allow administrators to securely logon to the
  various system components

- HTTPS/SSL (TLS) for connection to web-based services
- TLS for connection to email services
- AES-256 (FIPS 140-2 validated) for data at rest (with Elastic Block Store (EBS) volumes)


In this architecture, encryption mechanisms are employed for data at rest and in transit. For data at rest, AES-256 Server Side encryption is employed for data stored in Amazon S3, and Amazon RDS databases. For data in transit, to protect against exposure of any cleartext data transmitted deliberately (upload/download) or incidentally during interactive systems management operations, Amazon S3 object access can only be conducted over encrypted sessions via TLS; the bastion host, Amazon EC2 instances and associated security groups are configured for encrypted SSH sessions only. For web user access, the Elastic Load Balancing (ELB) employs a TLS endpoint.

AWS built-in features employ TLS for AWS Management Console sessions, AWS API calls, and AWS Command Line Interface connections.


### SC-15 Collaborative Computing Devices

This control is not applicable, as the Project system does
employ any collaborative computing devices.


### SC-20 Secure Name / Address Resolution Service

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (authoritative source)


### SC-21 Secure Name / Address Resolution Service

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (recursive or caching resolver)


### SC-22 Architecture And Provisioning For Name / Address Resolution Service



### SC-39 Process Isolation

Process isolation is maintained on the Linux platform. Linux is the only operating system that is part of the boundary.


In this architecture, the AMIs that make up the operating systems deployed on Amazon EC2 instances maintain separate execution domains/address spaces for executing processes within the customer operating environment.

AWS built-in features of the hypervisors that support the infrastructure maintain separate execution domains/address spaces for executing processes.
