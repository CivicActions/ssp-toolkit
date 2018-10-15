# SYSTEM AND COMMUNICATIONS PROTECTION

## SC-01 SYSTEM AND COMMUNICATIONS PROTECTION POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=SC-1>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a system and communication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Communications Protection (SC) Policy CivicActions document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.



#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel a system and communication policy  that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls.The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating the System and Communications Protection Policy and Procedures annually.  The Chief Operating Officer is responsible for approving System and Communications Protection. All procedures are consistent with requirements of FISMA, FedRAMP, ISO 27001, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## SC-05 DENIAL OF SERVICE PROTECTION

> Control description: <http://800-53.govready.com/control?id=SC-5>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

Drupal has a manual ability to block IP addresses in cases where attacks bypass cloud protection. This is managed by the support team.



#### LINCS specific control or LINCS Responsibility

Denial of service (DoS) attacks impair the performance of network devices and server hosts, and thence the application itself.  LINCS relies on the AWS platform for the protection of DoS attacks defined by LINCS SC-5.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: denial of service protection.

Monitoring is conducted though AWS Operations in analyzing capacity and traffic patterns in potential DoS attacks.



## SC-07 BOUNDARY PROTECTION

> Control description: <http://800-53.govready.com/control?id=SC-7>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

The lincs.ed.gov authorization boundary is completely contained within the AWS Platform as a Service.

The Drupal Server and Static Files computing nodes are the only computing nodes in the system that are exposed to the Internet. LINCS employs both the AWS platform safeguards and the Drupal Watchdog module in monitoring and recording system events. All other computing nodes used in the system are isolated within AWS.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: monitoring and controlling at the external boundary and key internal boundaries.



### Part b)

#### LINCS specific control or LINCS Responsibility

The lincs.ed.gov authorization boundary is completely contained within the AWS Platform as a Service.

Internal organizational networks (e.g. CivicActions private networks) are physically separate from the AWS platform and are protected by managed boundary devices that include FIPS 140-2 validated encryption modules at all entry points.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: implementation of subnetworks for publically accessible system components.



### Part c)

#### LINCS specific control or LINCS Responsibility

The lincs.ed.gov authorization boundary is completely contained within the AWS Platform as a Service.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: monitoring and controlling at the external boundary and key internal boundaries.



## SC-12 CRYPTOGRAPHIC KEY ESTABLISHMENT AND MANAGEMENT

> Control description: <http://800-53.govready.com/control?id=SC-12>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

This is a planned control. Use of cryptographic key management for the LINCS system is not in use for at the time of implementation for authentication. CivicActions does not utilize customer agency supplied PIV credentials for access to customer instances of the LINCS. Access enforcement and authentication requirements for LINCS are described in AC-2 & IA-2. AWS platform does not utilize or manage cryptographic keys within the ACE boundary.



## SC-13 USE OF CRYPTOGRAPHY

> Control description: <http://800-53.govready.com/control?id=SC-13>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

LINCS servers use SSH data is encrypted during transit. LINCS utilizes HTTPS for any inbound traffic accessing the LINCS and must authenticate according to established LINCS access enforcement and authentication rules described in AC-2 & IA-2. AWS Cloud data volumes are encrypted with FIPS-142 encryption.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: use of cryptography for data in motion (with SSH and HTTPS/SSL) and for data at rest (with Elastic Block Store (EBS) volumnes).



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
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

This control is inherited from AWS and currently does not employ a distributed, hierarchical namespace. LINCS does not provide additional data origin authentication and integrity verification artifacts along with the authoritative name resolution data the system returns in response to external name/address resolution queries. LINCS does not provide the means to indicate the security status of child zones and (if the child supports secure resolution services) to enable verification of a chain of trust among parent and child domains, when operating as part of a distributed, hierarchical namespace.



## SC-21 SECURE NAME / ADDRESS RESOLUTION SERVICE (RECURSIVE OR CACHING RESOLVER)

> Control description: <http://800-53.govready.com/control?id=SC-21>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

This control is inherited from AWS and currently and does not employ the measures to request and perform data origin authentication and data integrity verification on the name/address resolution responses the system receives from authoritative sources.



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



#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: Process isolation.



