# Maintenance (MA) Standard (SOP)

*Reviewed and updated 2023-12-20*

----

**Table of Contents**
<!--TOC-->

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Standards](#standards)
  - [MA-01 System Maintenance Policy And Procedures](#ma-01-system-maintenance-policy-and-procedures)
  - [MA-02 Controlled Maintenance](#ma-02-controlled-maintenance)
  - [MA-04 Non-Local Maintenance](#ma-04-non-local-maintenance)
  - [MA-05 Maintenance Personnel](#ma-05-maintenance-personnel)

<!--TOC-->

----

## Introduction

### Purpose

The Office of the Chief Information Officer (OCIO) Information Assurance Services (IAS) publication Information  Technology (IT) System Access Controls Standard of February 11, 2022 provides a comprehensive basis for  management across all systems in the Department. This document provides specific guidance as defined and implemented  by the Project.

### Scope

This system has been categorized as a FIPS-199 LOW system, and as such this document applies only to relevant  controls, policies, processes and procedures as defined within the system.

## Standards

### MA-01 System Maintenance Policy And Procedures

System maintenance policy and procedures are formally documented in the Project SSP, which provides the roles and responsibilities as it pertains to software and systems maintenance and updates. The Project Full Name ensures that maintenance controls are developed, disseminated, reviewed, and updated as necessary.

Physical and environmental protection is fully inherited from the AWS FedRAMP certified us-east cloud.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.


This System Maintenance control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/


CivicActions has developed, documented and disseminated to personnel a system maintenance policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Maintenance (MA) Policy and Procedure document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs>.


### MA-02 Controlled Maintenance

The Project schedules, performs, and documents regular maintenance on the software components of all systems, including but not limited to:

- Hourly automated snapshot backups
- Daily disaster recovery remote backups
- Daily Intrusion Detection (OSSEC) / Data Integrity Assurance (AIDE)
- As needed help desk support
- Twice-monthly OS updates/patches


This System Maintenance control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/


### MA-04 Non-Local Maintenance

This System Maintenance control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/


**a.**	System maintenance is done from remote sites as there is no direct access to the server instances in the AWS cloud; this is the government-approved method of doing business. Approval, QA, and monitoring are conducted by the team performing the specific maintenance.

**b.**	Remote diagnostics tools, such as OSSEC, AIDE, fail2ban, and OpenSCAP are used to verify the integrity of files, perform log analysis, monitor login attempts and check for rootkits and other vulnerabilities.

**c.**	All nonlocal maintenance requires the same authentication requirements to perform the maintenance activities to access the system as defined in controls AC-3 and IA-2. SSH is used to secure all communications between the remote user and the components located in the AWS cloud.

**d.**	CivicActions records for nonlocal maintenance is managed through JIRA tickets and the Git issue queue as well as normal system logs. CivicActions administrator activity to the system is also logged through the implementation of the AU-2 (Audit Events) and AU-3 (Content of Audit Records).

**e.**	Any session for internal maintenance activities is terminated when the user completes their session, disconnects from the system, or logs out. In addition, sessions are terminated after 15 minutes of inactivity.

### MA-05 Maintenance Personnel

Client maintains a list of authorized contract (CivicActions) personnel who perform maintenance and repair activities on the Project Project system components, and only these authorized personnel may perform the maintenance. All maintenance personnel have the required personnel security elements in place.


This System Maintenance control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/


Maintenance of the system and applications can only be performed by personnel designated as having internal administrator privileges and responsibilities. Access rights for the internal administrators are assigned and granted access to perform their specific job responsibilities. All physical maintenance requirements are inherited from AWS.



