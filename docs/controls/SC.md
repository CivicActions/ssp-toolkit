# SYSTEM AND COMMUNICATIONS PROTECTION

## SC-01 SYSTEM AND COMMUNICATIONS PROTECTION POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=SC-1>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

System and communications protection policy and procedures are formally documented in the Department of Education, Handbook for Information Assurance Security Policy (Handbook OCIO-01) and the LINCS SSP. The Department reviews and updates the policy as necessary and has been continually updated since April 2008.

This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.



#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a system and communication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Communications Protection (SC) Policy CivicActions document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## SC-05 DENIAL OF SERVICE PROTECTION

> Control description: <http://800-53.govready.com/control?id=SC-5>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The LINCS Technology Project system is configured to reduce vulnerabilities in its operating system and applications to protect against Denial of Service (DoS) attacks.

The LINCS support staff ensures the system is protected against or limits the effect of DoS attacks as specified in the Department of Education, Handbook for Information Security Incident Response and Reporting Procedures (Handbook OCIO-14).



#### Drupal specific control support

Drupal has a manual ability to block IP addresses in cases where attacks bypass cloud protection. This is managed by CivicActions Operations.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: denial of service protection.



## SC-07 BOUNDARY PROTECTION

> Control description: <http://800-53.govready.com/control?id=SC-7>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The LINCS Technology Project system has monitored and controlled communications at the external boundary of the information system and at key internal boundaries within the system, where appropriate. The LINCS allocates publicly accessible information system components (e.g., public web servers) specific IP address and port combinations. Public access into the organization’s internal networks is prevented except as appropriately mediated.



#### Drupal specific control support

Drupal, when deployed on SELinux in full enforcing mode, minimizes the number of services and computing nodes that are exposed to the Internet. Drupal employs both the AWS platform safeguards and the Drupal Watchdog module in monitoring and recording system events. All other computing nodes used in the system are isolated within AWS.



### Part a)

#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: boundary protection.



### Part b)

#### Amazon Web Services (AWS) US-East/West control support

The authorization boundary is completely contained within a Virtual Private Cloud (VPC) created and managed by the AWS Infrastructure as a Service (IaaS). External connections must be explicitly configured via the AWS Security Groups (SG) mechanism.

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: boundary protection.



### Part c)

#### Amazon Web Services (AWS) US-East/West control support

Internal organizational networks (e.g. CivicActions private networks) are physically separate from the AWS platform and are protected by managed boundary devices that include FIPS 140-2 validated encryption modules at all entry points.

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: boundary protection.



## SC-12 CRYPTOGRAPHIC KEY ESTABLISHMENT AND MANAGEMENT

> Control description: <http://800-53.govready.com/control?id=SC-12>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

Use of cryptographic key management for the LINCS system is not in use for at the time of implementation for authentication. CivicActions does not utilize customer agency supplied PIV credentials for access to customer instances of the LINCS. Access enforcement and authentication requirements for LINCS are described in AC-2 & IA-2. AWS platform does not utilize or manage cryptographic keys within the ACE boundary.



## SC-13 CRYPTOGRAPHIC PROTECTION

> Control description: <http://800-53.govready.com/control?id=SC-13>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

The information system implements:

* cryptographic modules through Secure Shell (SSH) to allow administrators to securely logon to the various system components

* HTTPS/SSL (TLS) for connection to web-based services

* TLS for connection to email services

* AES-256 (FIPS 140-2 validated) for data at rest (with Elastic Block Store (EBS) volumnes)



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: cryptographic protection for data in motion (with SSH and HTTPS/SSL) and for data at rest (with Elastic Block Store (EBS) volumnes).



## SC-15 COLLABORATIVE COMPUTING DEVICES

> Control description: <http://800-53.govready.com/control?id=SC-15>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

This control is not applicable, as the LINCS system does not employ any collaborative computing devices.



## SC-20 SECURE NAME / ADDRESS RESOLUTION SERVICE (AUTHORITATIVE SOURCE)

> Control description: <http://800-53.govready.com/control?id=SC-20>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (authoritative source)



## SC-21 SECURE NAME / ADDRESS RESOLUTION SERVICE (RECURSIVE OR CACHING RESOLVER)

> Control description: <http://800-53.govready.com/control?id=SC-21>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (recursive or caching resolver)



## SC-22 ARCHITECTURE AND PROVISIONING FOR NAME / ADDRESS RESOLUTION SERVICE

> Control description: <http://800-53.govready.com/control?id=SC-22>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: architecture and provisioning for name / address resolution service.



## SC-39 PROCESS ISOLATION

> Control description: <http://800-53.govready.com/control?id=SC-39>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### CivicActions Responsibility

Process isolation is maintained on the Linux platform. Linux is the only operating system that is part of the boundary.



