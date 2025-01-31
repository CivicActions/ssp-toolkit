# Contingency Planning (CP) Standard (SOP)

*Reviewed and updated 2025-01-31*

----

**Table of Contents**
<!--TOC-->

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Standards](#standards)
  - [CP-01 Contingency Planning Policy And Procedures](#cp-01-contingency-planning-policy-and-procedures)
  - [CP-02 Contingency Plan](#cp-02-contingency-plan)
  - [CP-03 Contingency Training](#cp-03-contingency-training)
  - [CP-04 Contingency Plan Testing](#cp-04-contingency-plan-testing)
  - [CP-09 Information System Backup](#cp-09-information-system-backup)
  - [CP-10 Information System Recovery And Reconstitution](#cp-10-information-system-recovery-and-reconstitution)

<!--TOC-->

----

## Introduction

### Purpose

The Office of the Chief Information Officer (OCIO) Information Assurance Services (IAS) publication Information Technology (IT) System Access Controls Standard of February 11, 2022 provides a comprehensive basis for management across all systems in the Department. This document provides specific guidance as defined and implemented by the Project.

### Scope

This system has been categorized as a FIPS-199 LOW system, and as such this document applies only to relevant controls, policies, processes and procedures as defined within the system.

## Standards

### CP-01 Contingency Planning Policy And Procedures

CivicActions has developed, documented and disseminated to personnel a contingency planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in Contingency Planning (CP) Policy and Procedure that can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

The Project and has developed a contingency planning policy consistent with NIST 800-34. Contingency planning procedures are formally documented within the Project Contingency Plan, which provides the roles and responsibilities as it pertains to contingency planning. The Project reviews and updates the policy as necessary and the policy was last updated in July 2012.


### CP-02 Contingency Plan

**a.**	CivicActions has developed a contingency plan for that addresses:
1. Essential missions, business functions, and associated contingency requirements
2. Recovery objectives, restoration priorities, and metrics
3. Roles and responsibilities are identified in the CP and include the ISCP Director, Incident Commander (IC), CivicActions Coordinator, and CivicActions Information System Security Officer (ISSO).
4. Maintaining essential missions and business functions despite an information system disruption, compromise, or failure
5. Full information system restoration without deterioration of the security safeguards originally planned and implemented
6. The ISCP is reviewed and approved by ISCP Director, Incident Commander (IC), CivicActions ISSO and the System Owner annually.

**b.**	The CivicActions Information System Contingency Plan (ISCP) has been distributed to all CivicActions team members. The ISCP can be found in the CivicActions Handbook at <https://guidebook.civicactions.com/en/latest/common-practices-tools/security/contingency-plan/>.


The Project Information System Contingency Plan (ISCP) has been distributed to all members who have roles in Contingency Planning and Incident Response Team. Direction by the System Owner will update who is required to receive a copy of the contingency plan. The ISCP can be found in the Project GitHub wiki at <https://guidebook.civicactions.com/en/latest/common-practices-tools/security/contingency-plan/>.

**c.**	The Information System Contingency Plan (ISCP) is closely integrated with the Incident Response Plan (IRP). Coordination is the responsibility of the ISCP Director and CivicActions Operations staff.

**d.**	The ISCP Director and CivicActions' Security Office are responsible to review the ISCP annually and when a change to the system occurs.

**e.**	CivicActions Operations staff and ISCP Director are required to update the ISCP to address changes to the organization, information system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing.

**f.**	The ISCP requires that changes to the plan be communicated to those on the Incident Response/Contingency Plan Contact List.

**g.**	The ISCP is available on CivicActions GitHub repository. This repository provides the configuration management capabilities for the ISCP to be protected from unauthorized disclosure and modification.

### CP-03 Contingency Training

The ISCP stipulates that all CivicActions system assigned roles in the Contingency Plan Team are trained in their duties within three months of first being assigned a role in the CP, and then annually thereafter or when changes are required. CivicActions uses the Contingency Plan as described in controls CP-1 and CP-2 as a basis for personnel contingency training.


### CP-04 Contingency Plan Testing

Real-world tests of the contingency plan will be held at least annually, with supplemental tests (checklist/table-top) as needed for specific scenarios. The ISCP Coordinator is responsible to facilitate annual testing exercises. The testing process for the ISCP includes a review of the ISCP, exercise, and identification of corrective actions and other improvements.


### CP-09 Information System Backup

**a.**	CivicActions conducts system user-level information backup in accordance with requirements (at a minimum, incremental backups must be conducted at least weekly and full backups must be conducted at least monthly).


In this architecture, user data is limited to that which is stored in the Amazon RDS database. Amazon RDS is fully backed up by a daily snapshot as well as through transaction logging conducted by AWS as part of this managed service. Full database recovery from snapshot or point-in-time can be initiated from the Amazon RDS console/API.

**b.**	System-level information for the application is replicated and backed up in the same way as user-level information as defined in CP-9(a).


AWS built-in features automatically backs up system-level information limited to infrastructure CONFIGURATION information within the AWS account. While individual running Amazon EC2 instances and attached EBS volumes are NOT backed up, they can be reconstituted from Amazon Machine Images (AMIs) provided by AWS (which are backed up by AWS) and user data scripts included in CloudFormation templates. Once deployed, the CloudFormation template contents are backed up by AWS R488within the CloudFormation service. These AWS backups of AWS services are transparent to the customer as part of AWS backend processes.

**c.**	System documentation is backed up from the GitHub repository on a daily basis with a minimum two-week retention period and off-site storage.


AWS built-in features back up online administrator and developer documentation, limited to that which is published at https://aws.amazon.com/documentation.

**d.**	CivicActions employees must authenticate prior to being granted access to the GitHub repository. Roles and responsibilities within GitHub determine the proper level of access for the documentation being accessed. The folder structure of GitHub protects though permissions and ownership prohibiting users from accessing unauthorized documentation.


AWS built-in features protect the confidentiality, integrity, and availability of information that AWS services back up. This information includes the service configuration information within an account, AWS online administrator and developer documentation, and AWS CloudFormation stacks for templates once deployed into an account. R612

### CP-10 Information System Recovery And Reconstitution

The Contingency Plan documents the mechanisms with supporting procedures that allow all system components to be recovered and reconstituted to the system’s original state after a disruption or failure. This original state means that all system parameters (either default or organization- established) are reset, patches are reinstalled, system and security configuration settings are reestablished, system documentation and operating procedures are available, application and system software is reinstalled, information from the most recent backups is available and the system is fully tested.
