# Incident Response (IR) Standard (SOP)

*Reviewed and updated 2023-12-20*

----

**Table of Contents**
<!--TOC-->

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Standards](#standards)
  - [IR-01 Incident Response Policy And Procedures](#ir-01-incident-response-policy-and-procedures)
  - [IR-02 Incident Response Training](#ir-02-incident-response-training)
  - [IR-04 Incident Handling](#ir-04-incident-handling)
  - [IR-05 Incident Monitoring](#ir-05-incident-monitoring)
  - [IR-06 Incident Reporting](#ir-06-incident-reporting)
  - [IR-07 Incident Resonse Assistance](#ir-07-incident-resonse-assistance)
  - [IR-07 Incident Response Assistance](#ir-07-incident-response-assistance)
  - [IR-08 Incident Response Plan](#ir-08-incident-response-plan)

<!--TOC-->

----

## Introduction

### Purpose

The Office of the Chief Information Officer (OCIO) Information Assurance Services (IAS) publication Information  Technology (IT) System Access Controls Standard of February 11, 2022 provides a comprehensive basis for  management across all systems in the Department. This document provides specific guidance as defined and implemented  by the Project.

### Scope

This system has been categorized as a FIPS-199 LOW system, and as such this document applies only to relevant  controls, policies, processes and procedures as defined within the system.

## Standards

### IR-01 Incident Response Policy And Procedures

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

The Project maintains an Incident Response Plan (IRP), consistent with NIST 800-61, which addresses purpose, scope, roles, and responsibilities. The incident response procedures address any activity or occurrence that compromises the integrity of a system, denies access to or use of IT resources, and compromises the sensitivity of the information stored in, processed by or transmitted by a system.

Additionally, the IRP includes procedures to respond to waste, fraud, misuse, or abuse of any departmental IT system, damage or loss of software or data contained in any system, Use of unlicensed (pirated) software products, discovery of hardware or software vulnerabilities

The Project Incident Response Plan can be found in the CivicActions GitHub repository at <https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>


The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


CivicActions has developed, documented and disseminated to personnel an incident response planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in Incident Response (IR) Policy and Procedure that can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


### IR-02 Incident Response Training

CivicActions Operations and users of the Project system with incident response responsibilities are required to participate in incident response training once the role is assumed within 10 days, as required by Project changes, and annually. The Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) is the basis for the training and the incident response workflow created by the Security team. Upon a review of past incidents, the training is updated to ensure processes and workflows are updated.


The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident response training.


All CivicActions employees are required to participate in incident response training, as required by Incident Response Plan changes, and annually. The CivicActions Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) is the basis for the training and the incident response workflow created by the Security Office. Upon a review of past incidents, the training is updated to ensure processes and workflows are updated.


### IR-04 Incident Handling

The Client Computer Security Officer (CSO) handles all incidents for the Project Full Name.

The Client Full Name utilizes proven incident handling methodologies for security incidents that includes preparation, detection and analysis, containment, eradication, and recovery. Client Full Name maintains a list of lessons learned from ongoing incident handling activities and uses those lessons to update the incident response procedures accordingly.

Preparation activities includes all CivicActions and Project internal users are trained if their role includes incident response. Detection monitoring tools providing notification to incident response personnel for analysis and action. Containment, eradication and recovery activities include AWS and LAMP-stack inherited fixes and Project system administrators adjusting IP port blocking security groups and SELinux policies.


The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident handling.


**a.**	CivicActions has implemented an Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) that explains the process for incident handling and discusses preparation, detection and analysis, containment, eradication, and recovery.
Preparation activities include all CivicActions team members who are trained in incident response. Detection and monitoring tools providing notification to incident response personnel for analysis and action.

**b.**	CivicActions' Operations staff and Security Office team members are members of the CivicActions Contingency and Incident Response Plan teams which coordinates activities accordingly through the life of the incident event.

**c.**	The CivicActions Operations staff and Security Office conduct a post-incident analysis to assist in documenting lessons learned and suggesting changes to improve the incident response process. Tickets created in response to the incident event are reviewed upon completion by the Operations staff and Security Office. Changes to the Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) require a team review session for approval.

### IR-05 Incident Monitoring

The Project utilizes network and host-based intrusion detection systems, monitoring the system and application logs for anomalous events. Incidents are tracked using the same ticketing system that is used to track all system-related changes and events.


The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident monitoring.


CivicActions utilizes the JIRA ticketing tool for tracking and reporting of incident events from reporting to resolution and post- incident analysis. Initial reporting can come from continuous monitoring tools as well as client and public submissions made to support@civicactions.com. Jira processes the tickets for the public submissions and the CivicActions Support Team creates associated GitHub Issues. Internal incidents reported are processed within the GitHub Issue queue. Details of the handling procedures are included in the CivicActions Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan//#response-process>) Response Process.


### IR-06 Incident Reporting

If an incident involves suspicious activity, CivicActions Operations will contact the Project System Owner who may then contact the Project CSO.

The CivicActions Computer Security Officer (CSO) handles all incidents for the Project. The CSO is prepared to report all incidents to the Client Full Name.


The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident reporting.


**a.**	CivicActions personnel, as soon as an incident event is detected and/or communicated, are required to report the incident event to the CivicActions Security Office. Methods of detection and/or communication may include one or more of:

- Through continuous monitoring tools (StatusCake, OSSEC, others).
- As a result of application notifications where CivicActions Security receives notifications (AIDE, OpsGenie, others).
- Event logging described in AC-2
- Host-based alerts from the cloud infrastructure or platform.

**b.**	CivicActions personnel, as soon as the incident event is detected and/or communicated, are required to report the incident event to the CivicActions Security Office.

### IR-07 Incident Resonse Assistance

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident resonse assistance.


### IR-07 Incident Response Assistance

CivicActions Help Desk team provides first response assistance to any users of the system. Response time for external reporting of incidents through e-mail is one business day. Internal users are able to request support thought the same process or initiate the incident response workflow. Tickets created in the Jira (customer ticketing system) and GitLab (internal ticketing system) documents all details related to the incident to assist the Incident Response Teams in handling the incident.


### IR-08 Incident Response Plan

The Project Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) includes a comprehensive incident response program, which details the implementation of procedures and tools required for incident handling. The incident response program details the roles and responsibilities of Project/ CivicActions IR Team. The IR Team includes members from CivicActions Security and Operations teams. Incident response plays a pivotal role in monitoring, detecting and handling security incidents of the entire information system. The IRP details categorization of incidents in accordance with NIST 800-61 and accordingly documents and reports incidents. The IRP is reviewed annually and updated as needed by ISSO, with the assistance of the Incident Response Team.


The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident response plan.


**a.**	Incident response plays a pivotal role in monitoring, detecting and handling security incidents of the entire information system. CivicActions has developed an Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) that:

1. Provides CivicActions with procedures and tools required for incident handling;
2. Describes the structure and organization of the incident response capability;
3. Provides a high-level approach for how the incident response capability fits into CivicActions and the systems it maintains;
4. Meets the mission, size, structure, and functions of CivicActions;
5. Defines reportable incidents;
6. Provides metrics for measuring the incident response capability and details categorization of incidents in accordance with NIST 800-61;
7. Defines the roles and responsibilities of CivicActions IR Team;
8. Is reviewed annually and updated as needed by the CivicActions Security Office, with the assistance of the Incident Response Team.

**b.**	The CivicActions Incident Response Plan is distributed to all CivicActions team members as part of the CivicActions Handbook (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>).
 The Incident Response Team includes members from the Security Office,
 Operations staff, and Drupal Engineering teams.

**c.**	The CivicActions Security Office and the Incident Response team is responsible for reviewing the Incident Response Plan annually. The entire Incident Response Team will review the plan and update it as necessary. Ultimately, the Security Office has the final say and will approve all updates to the plan.

**d.**	The CivicActions Security Office is responsible for managing the IR Plan, including annual reviews and updates. The IR Plan is updated to reflect any changes to processes, systems or applications. In addition, any concerns or difficulties encountered during IR Plan implementation, execution, or testing are addressed in an update to the IR Plan.

**e.**	Modifications to the IR Plan are conducted by the IR team the (CivicActions Security Office, Operations staff and Engineering teams) and communicated to the CivicActions team.

**f.**	The IR Plan is available in the CivicActions Handbook and is maintained in the CivicActions GitHub repository. GitHub provides the configuration management capabilities for the IR Plan to be protected from unauthorized disclosure and modification.


