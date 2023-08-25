# Reusable OpenControl Components (SSP-Toolkit).

## CA: Assessment Authorization and Monitoring

### CA-1: Security Assessment And Authorization Policies And Procedures

```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] assessment, authorization, and monitoring policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the assessment, authorization, and monitoring policy and the associated assessment, authorization, and monitoring controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the assessment, authorization, and monitoring policy and procedures; and
 - c. Review and update the current assessment, authorization, and monitoring:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete

#### Contractor

CivicActions has developed, documented and disseminated to personnel a certification, accreditation, and security assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Security Assessment and Authorization Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.



#### Project

Project follows the None. The Project System Security Policy (SSP) provides guidance on all aspects of security for the protection of Project information technology resources.

Project will periodically review and update the SSP when there is a significant change to the regulatory, operational, or technical environment.


### CA-2: Security Assessments

```text
 - a. Select the appropriate assessor or assessment team for the type of assessment to be conducted;
 - b. Develop a control assessment plan that describes the scope of the assessment including:
   - 1. Controls and control enhancements under assessment;
   - 2. Assessment procedures to be used to determine control effectiveness; and
   - 3. Assessment environment, assessment team, and assessment roles and responsibilities;
 - c. Ensure the control assessment plan is reviewed and approved by the authorizing official or designated representative prior to conducting the assessment;
 - d. Assess the controls in the system and its environment of operation [Assignment: organization-defined frequency] to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting established security and privacy requirements;
 - e. Produce a control assessment report that document the results of the assessment; and
 - f. Provide the results of the control assessment to [Assignment: organization-defined individuals or roles].

```
**Status:** Planned
a
#### Contractor

CivicActions will develop a security assessment plan (SAP) that describes the security controls and control enhancements under assessment, assessment procedures used to determine effectiveness, the assessment environment, the assessment team, and the assessment roles and responsibilities.


a
#### Project

The Project Full Name follows the None. The Project Full Name will conduct annual security assessments to comply with FISMA and NIST regulations. Project will draw on NIST Special Publications 800-53A security controls to complete the assessment. All controls and sub-set security controls will be evaluated and a risk assessment will be conducted. The scope of the assessment includes:

1. Security controls and control enhancements under assessment
2. Assessment procedures to be used to determine security control effectiveness
3. Assessment environment, assessment team, and assessment roles and responsibilities


b
#### Contractor

CivicActions will assess the security controls in their system and its environment of operation to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting established security requirements.

All controls assigned and documented in this System Security Plan (SSP) will be tested at least annually or when there is a major change to the system.


c
#### Contractor

CivicActions will produce a security assessment report that documents the results of the assessment. The Security Assessment Report must contain the results of the assessment, and may also contain recommendations and suggestions for plans of actions and milestones (POA&Ms).


c
#### Project

The Project Authorizing Official or Designated Representative will create a Security Assessment Report (SAR). A full assessment shall be conducted by an independent third party assessor at least every three years.


d
#### Contractor

CivicActions will provide the results of the security control assessment to the System Owner, Project Manager, CivicActions Security, and the Authorization Official (AO)). The security control assessment package includes the following:

- Security Control Matrix
- Privacy Impact Assessment
- E-Authentication
- Contingency Plan
- Configuration Management Plan
- Rules of Behavior
- Incident Response Plan


### CA-3: System Interconnections

```text
 - a. Approve and manage the exchange of information between the system and other systems using [Selection (one or more): interconnection security agreements, information exchange security agreements, memoranda of understanding or agreement, service level agreements, user agreements, nondisclosure agreements, [Assignment: organization-defined type of agreement]];
 - b. Document, as part of each exchange agreement, the interface characteristics, security and privacy requirements, controls, and responsibilities for each system, and the impact level of the information communicated; and
 - c. Review and update the agreements [Assignment: organization-defined frequency].

```
**Status:** none

#### Contractor

This control is not applicable. CivicActions systems do not have system interconnections. The only communication conducted to CivicActions' systems is through the Internet.


### CA-5: Plan Of Action And Milestones

```text
 - a. Develop a plan of action and milestones for the system to document the planned remediation actions of the organization to correct weaknesses or deficiencies noted during the assessment of the controls and to reduce or eliminate known vulnerabilities in the system; and
 - b. Update existing plan of action and milestones [Assignment: organization-defined frequency] based on the findings from control assessments, independent audits or reviews, and continuous monitoring activities.

```
**Status:** complete

#### Contractor

CivicActions documents all deficiencies and vulnerabilities identified during the security certification and/or continuous monitoring phase (via security assessment, vulnerability scanning, risk assessment, etc.) within the Plan of Action and Milestones (POA&M).

The POA&M document provides a platform for CivicActions to monitor and track the deficiency and its mitigation strategy. POA&M items will include:

- The description of the deficiency,
- Dedicated point of contact for this deficiency.
- Cost of the mitigation strategy
- Associated risk and NIST control
- Recommended mitigation strategy

POA&Ms are tracked throughout the lifecycle of the system until its mitigation. All POA&Ms are reviewed on a monthly basis by CivicActions Information System Security Officer to ensure all mitigation strategies are continuing as documented.



#### Project

The Project follows the None procedures in managing POA&Ms.


### CA-6: Security Authorization

```text
 - a. Assign a senior official as the authorizing official for the system;
 - b. Assign a senior official as the authorizing official for common controls available for inheritance by organizational systems;
 - c. Ensure that the authorizing official for the system, before commencing operations:
   - 1. Accepts the use of common controls inherited by the system; and
   - 2. Authorizes the system to operate;
 - d. Ensure that the authorizing official for common controls authorizes the use of those controls for inheritance by organizational systems;
 - e. Update the authorizations [Assignment: organization-defined frequency].

```
**Status:** partial

#### Project

The Project follows the None. The Project system received its first three-year security accreditation on March 3, 2009, and most recently received an ATO on February 5, 2016.

ATO re-assessment will be performed every three years or when there is a major change to the application, in which a senior organizational official will sign and approve the security accreditation.


### CA-7: Continuous Monitoring

```text
Develop a system-level continuous monitoring strategy and implement continuous monitoring in accordance with the organization-level continuous monitoring strategy that includes:
 - a. Establishing the following system-level metrics to be monitored: [Assignment: organization-defined system-level metrics];
 - b. Establishing [Assignment: organization-defined frequencies] for monitoring and [Assignment: organization-defined frequencies] for assessment of control effectiveness;
 - c. Ongoing control assessments in accordance with the continuous monitoring strategy;
 - d. Ongoing monitoring of system and organization-defined metrics in accordance with the continuous monitoring strategy;
 - e. Correlation and analysis of information generated by control assessments and monitoring;
 - f. Response actions to address results of the analysis of control assessment and monitoring information; and
 - g. Reporting the security and privacy status of the system to [Assignment: organization-defined personnel or roles]
                  [Assignment: organization-defined frequency].

```
**Status:** partial
a
#### Contractor

CivicActions implements a continuous monitoring strategy that incorporates configuration management, system scanning and log analysis processes:

- Configuration management includes the assessment of security impact analyses of proposed and implemented changes.
- System scanning is managed by running the OpenSCAP vulnerability scanner using the DISA STIG profile.
- Log analysis is managed by feeding logs to a Graylog dashboard for analysis.


a
#### Drupal

CivicActions follows recommendations and best practices developed by the Drupal community for monitoring. Examples of specific logs and metrics are included in AU-2 and AU-3.


a
#### Ilias

CivicActions follows recommendations and best practices developed by the Ilias community for monitoring. Examples of specific logs and metrics are included in AU-2 and AU-3.

b
#### Contractor

Configuration management and log analysis is carried out in real time. OpenSCAP security scans are performed and reviewed monthly. See also: RA-5 and SI-4.

Quarterly review of the control assessments supporting the monitoring is conducted by CivicActions Operations in collaboration with the CivicActions Security Office.


c
#### Drupal

CivicActions works closely with the Drupal security community and reviews security announcements as part of the continuous monitoring strategy. Items found to require immediate remediation will be addressed.


c
#### Ilias

CivicActions works closely with the Ilias security community and reviews security announcements as part of the continuous monitoring strategy. Items found to require immediate remediation will be addressed.

d
#### Contractor

CivicActions conducts or oversees continuous system security monitoring.


e
#### Contractor

CivicActions Security reviews the results of the security scans and security assessments with associated JIRA and/or GitLab Issue tickets created to correlate and analyze security-related information generated from the monitoring tools becoming POA&M items for tracking.


f
#### Contractor

POA&M items are tracked by CivicActions Security through JIRA tickets with a security categorization assigned. The information included in the POA&M item include the severity, the due date, the weakness source identifier, and the plugin ID that identified the vulnerability.


g
#### Contractor

The security status of the system is reported up to the System Owner and Project Manager via the CivicActions Security Office to be reviewed alongside other security issues relating to the system.


### CA-9: Internal System Connections

```text
 - a. Authorize internal connections of [Assignment: organization-defined system components or classes of components] to the system;
 - b. Document, for each internal connection, the interface characteristics, security and privacy requirements, and the nature of the information communicated;
 - c. Terminate internal system connections after [Assignment: organization-defined conditions]; and
 - d. Review [Assignment: organization-defined frequency] the continued need for each internal connection.

```
**Status:** none

#### Contractor

Not applicable.
