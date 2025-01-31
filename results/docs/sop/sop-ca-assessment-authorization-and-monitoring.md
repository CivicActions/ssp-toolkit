# Assessment Authorization And Monitoring (CA) Standard (SOP)

*Reviewed and updated 2025-01-31*

----

**Table of Contents**
<!--TOC-->

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Standards](#standards)
  - [CA-01 Security Assessment And Authorization Policies And Procedures](#ca-01-security-assessment-and-authorization-policies-and-procedures)
  - [CA-02 Security Assessments](#ca-02-security-assessments)
  - [CA-03 System Interconnections](#ca-03-system-interconnections)
  - [CA-05 Plan Of Action And Milestones](#ca-05-plan-of-action-and-milestones)
  - [CA-06 Security Authorization](#ca-06-security-authorization)
  - [CA-07 Continuous Monitoring](#ca-07-continuous-monitoring)
  - [CA-09 Internal System Connections](#ca-09-internal-system-connections)

<!--TOC-->

----

## Introduction

### Purpose

The Office of the Chief Information Officer (OCIO) Information Assurance Services (IAS) publication Information Technology (IT) System Access Controls Standard of February 11, 2022 provides a comprehensive basis for management across all systems in the Department. This document provides specific guidance as defined and implemented by the Project.

### Scope

This system has been categorized as a FIPS-199 LOW system, and as such this document applies only to relevant controls, policies, processes and procedures as defined within the system.

## Standards

### CA-01 Security Assessment And Authorization Policies And Procedures

CivicActions has developed, documented and disseminated to personnel a certification, accreditation, and security assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Security Assessment and Authorization Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


Project follows the None. The Project System Security Policy (SSP) provides guidance on all aspects of security for the protection of Project information technology resources.

Project will periodically review and update the SSP when there is a significant change to the regulatory, operational, or technical environment.


### CA-02 Security Assessments

**a.**	CivicActions will develop a security assessment plan (SAP) that describes the security controls and control enhancements under assessment, assessment procedures used to determine effectiveness, the assessment environment, the assessment team, and the assessment roles and responsibilities.


The Project Full Name follows the None. The Project Full Name will conduct annual security assessments to comply with FISMA and NIST regulations. Project will draw on NIST Special Publications 800-53A security controls to complete the assessment. All controls and sub-set security controls will be evaluated and a risk assessment will be conducted. The scope of the assessment includes:

1. Security controls and control enhancements under assessment
2. Assessment procedures to be used to determine security control effectiveness
3. Assessment environment, assessment team, and assessment roles and responsibilities

**b.**	CivicActions will assess the security controls in their system and its environment of operation to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting established security requirements.

All controls assigned and documented in this System Security Plan (SSP) will be tested at least annually or when there is a major change to the system.

**c.**	CivicActions will produce a security assessment report that documents the results of the assessment. The Security Assessment Report must contain the results of the assessment, and may also contain recommendations and suggestions for plans of actions and milestones (POA&Ms).


The Project Authorizing Official or Designated Representative will create a Security Assessment Report (SAR). A full assessment shall be conducted by an independent third party assessor at least every three years.

**d.**	CivicActions will provide the results of the security control assessment to the System Owner, Project Manager, CivicActions Security, and the Authorization Official (AO)). The security control assessment package includes the following:

- Security Control Matrix
- Privacy Impact Assessment
- E-Authentication
- Contingency Plan
- Configuration Management Plan
- Rules of Behavior
- Incident Response Plan

### CA-03 System Interconnections

This control is not applicable. CivicActions systems do not have system interconnections. The only communication conducted to CivicActions' systems is through the Internet.


### CA-05 Plan Of Action And Milestones

CivicActions documents all deficiencies and vulnerabilities identified during the security certification and/or continuous monitoring phase (via security assessment, vulnerability scanning, risk assessment, etc.) within the Plan of Action and Milestones (POA&M).

The POA&M document provides a platform for CivicActions to monitor and track the deficiency and its mitigation strategy. POA&M items will include:

- The description of the deficiency,
- Dedicated point of contact for this deficiency.
- Cost of the mitigation strategy
- Associated risk and NIST control
- Recommended mitigation strategy

POA&Ms are tracked throughout the lifecycle of the system until its mitigation. All POA&Ms are reviewed on a monthly basis by CivicActions Information System Security Officer to ensure all mitigation strategies are continuing as documented.


The Project follows the None procedures in managing POA&Ms.


### CA-06 Security Authorization

The Project follows the None. The Project system received its first three-year security accreditation on March 3, 2009, and most recently received an ATO on February 5, 2016.

ATO re-assessment will be performed every three years or when there is a major change to the application, in which a senior organizational official will sign and approve the security accreditation.


### CA-07 Continuous Monitoring

**a.**	CivicActions follows recommendations and best practices developed by the Ilias community for monitoring. Examples of specific logs and metrics are included in AU-2 and AU-3.

CivicActions follows recommendations and best practices developed by the Drupal community for monitoring. Examples of specific logs and metrics are included in AU-2 and AU-3.


CivicActions implements a continuous monitoring strategy that incorporates configuration management, system scanning and log analysis processes:

- Configuration management includes the assessment of security impact analyses of proposed and implemented changes.
- System scanning is managed by running the OpenSCAP vulnerability scanner using the DISA STIG profile.
- Log analysis is managed by feeding logs to a Graylog dashboard for analysis.

**b.**	Configuration management and log analysis is carried out in real time. OpenSCAP security scans are performed and reviewed monthly. See also: RA-5 and SI-4.

Quarterly review of the control assessments supporting the monitoring is conducted by CivicActions Operations in collaboration with the CivicActions Security Office.

**c.**	CivicActions works closely with the Ilias security community and reviews security announcements as part of the continuous monitoring strategy. Items found to require immediate remediation will be addressed.

CivicActions works closely with the Drupal security community and reviews security announcements as part of the continuous monitoring strategy. Items found to require immediate remediation will be addressed.

**d.**	CivicActions conducts or oversees continuous system security monitoring.

**e.**	CivicActions Security reviews the results of the security scans and security assessments with associated JIRA and/or GitLab Issue tickets created to correlate and analyze security-related information generated from the monitoring tools becoming POA&M items for tracking.

**f.**	POA&M items are tracked by CivicActions Security through JIRA tickets with a security categorization assigned. The information included in the POA&M item include the severity, the due date, the weakness source identifier, and the plugin ID that identified the vulnerability.

**g.**	The security status of the system is reported up to the System Owner and Project Manager via the CivicActions Security Office to be reviewed alongside other security issues relating to the system.

### CA-09 Internal System Connections

Not applicable.
