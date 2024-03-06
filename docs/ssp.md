<!--TOC-->

- [NIST SP 800-53 Revision 5](#nist-sp-800-53-revision-5)
  - [AC: Access Control](#ac-access-control)
  - [AT: Awareness and Training](#at-awareness-and-training)
  - [AU: Audit and Accountability](#au-audit-and-accountability)
  - [CA: Assessment Authorization and Monitoring](#ca-assessment-authorization-and-monitoring)
  - [CM: Configuration Management](#cm-configuration-management)
  - [CP: Contingency Planning](#cp-contingency-planning)
  - [IA: Identification and Authentication](#ia-identification-and-authentication)
  - [IR: Incident Response](#ir-incident-response)
  - [MA: Maintenance](#ma-maintenance)
  - [MP: Media Protection](#mp-media-protection)
  - [PE: Physical and Environmental Protection](#pe-physical-and-environmental-protection)
  - [PL: Planning](#pl-planning)
  - [PS: Personnel Security](#ps-personnel-security)
  - [RA: Risk Assessment](#ra-risk-assessment)
  - [SA: System and Services Acquisition](#sa-system-and-services-acquisition)
  - [SC: System and Communications Protection](#sc-system-and-communications-protection)
  - [SI: System and Information Integrity](#si-system-and-information-integrity)

<!--TOC-->

# Reusable Component Library System Security Plan

## NIST SP 800-53 Revision 5


### AC: Access Control


#### AC-1: ACCESS CONTROL POLICY AND PROCEDURES
```text
- a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
  - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] access control policy that:
    - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
    - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
  - 2. Procedures to facilitate the implementation of the access control policy and the associated access controls;
- b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the access control policy and procedures; and - c. Review and update the current access control:
  - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
  - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].
```
**Status:** complete
##### Contractor
CivicActions has developed, documented and disseminated to personnel an access control policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Access Control (AC) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.

##### Project
This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

Access control policy and procedures are documented in the Project Full Name SSP. Access to Project operational information or system resources is limited to only authorized users, programs or processes. The Department enforces access control policies to protect the integrity of the Project Full Name. This Department reviews and updates this policy as necessary and it has been being updated, as necessary, since April 2008.

#### AC-2: ACCOUNT MANAGEMENT
```text
 - a. Define and document the types of accounts allowed and specifically prohibited for use within the system;
 - b. Assign account managers;
 - c. Require [Assignment: organization-defined prerequisites and criteria] for group and role membership;
 - d. Specify:
   - 1. Authorized users of the system;
   - 2. Group and role membership; and
   - 3. Access authorizations (i.e., privileges) and [Assignment: organization-defined attributes (as required)] for each account;
 - e. Require approvals by [Assignment: organization-defined personnel or roles] for requests to create accounts;
 - f. Create, enable, modify, disable, and remove accounts in accordance with [Assignment: organization-defined policy, procedures, prerequisites, and criteria];
 - g. Monitor the use of accounts;
 - h. Notify account managers and [Assignment: organization-defined personnel or roles] within:
   - 1. [Assignment: organization-defined time period] when accounts are no longer required;
   - 2. [Assignment: organization-defined time period] when users are terminated or transferred; and
   - 3. [Assignment: organization-defined time period] when system usage or need-to-know changes for an individual;
 - i. Authorize access to the system based on:
   - 1. A valid access authorization;
   - 2. Intended system usage; and
   - 3. [Assignment: organization-defined attributes (as required)];
 - j. Review accounts for compliance with account management requirements [Assignment: organization-defined frequency];
 - k. Establish and implement a process for changing shared or group account authenticators (if deployed) when individuals are removed from the group; and
 - l. Align account management processes with personnel termination and transfer processes.

```
**Status:** partial
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS account management.

#### a
##### AWS
In this architecture, the baseline AWS Identity and Access Management (IAM) groups and roles are associated with access policies to align user accounts with personnel functions related to infrastructure/platform management (e.g. Billing, Amazon EC2/VPC/Amazon RDS systems administration, I.T. auditing, etc.)

##### Drupal
Drupal provides the following information system account types to support organizational mission/business functions:

- Anonymous user - readers of the site who either do not have an account or are not
  logged in.

- Authenticated user - All non-anonymous users inherit the "authenticated user role"
  that supports personal account management capabilities.

- Administrator - This role has all permissions enabled by default.

##### Ilias
Ilias provides user accounts for individuals who participate in visiting, contributing to and administering the site with the following roles:
- Anonymous user – Readers of the site who either do not have an account or are not logged in.
- Guest – This role has limited visibility and read permissions
- User - Standard role for registered users. This role grants read access to most objects.
- Administrator - This role has all permissions enabled by default.

##### Project
SSH system accounts are provided to contractors on an as-needed basis.

Access privileges are used to ensure that only authorized personnel access certain areas of the Project system. User access is controlled by the completion and submission of Project system Rules of Behavior and New User Account Request forms by the user and management. These items are completed and submitted whenever a new user requires access or an existing user requires access changes. The system administrator, based on need-to-know, assigns the proper permissions. The employee’s manager approves the access rights before the initial account is created. Finally, the system administrator implements the access rights according to the New User Account Request form. The security staff and the support contractor review accounts periodically. Accounts no longer in use are removed from the system by the system administrator.

The Project has implemented user account procedures to disable inactive user accounts after 90-days of inactivity. The Project support staff monitors all user accounts to ensure this procedure is enforced. Section 6.3, Authentication Management, of the Project SSP illustrates the exact procedures the contractor support staff follows to ensure accounts are properly managed.
The Project system does not have guest or anonymous accounts.

##### SSH
Operations, in collaboration with the Security Office, will set up privileged accounts accounts for the following roles:
- Developer - user level account that has access to application features and sanitized databases
- System Administrator - user accounts that enjoy full system administrator (`sudo`) access

#### g
##### AWS
In this architecture, AWS CloudTrail and Amazon S3 Bucket logging are enabled, which provide the audit trail capability for the organization to monitor the use of AWS Identity and Access Management (IAM) accounts. An Amazon S3 bucket centrally contains the CloudTrail audit logs. Amazon CloudWatch Alarm is configured to send an alert when any of the following happen:
  - an API call is made to create, update, or delete a Network ACL/Security Group
  - AWS account *root user* activity is detected
  - multiple API actions or login attempts fail
  - IAM Configuration changes are detected
  - new IAM access key was created
  - changes to the CloudTrail log configuration are detected

##### Contractor
All CivicActions systems log the usage of information accounts.
##### Drupal
Drupal monitors the usage of information accounts in the Watchdog log.
##### Ilias
Ilias monitors the usage of information accounts in a log on the server.
#### b
##### Contractor
The CivicActions Project Manager assigns the "administrator" role for the management of all accounts issued to internal admin roles supporting the information system.  Account requests are initiated by the Project Manager by completing a ticket request and the CivicActions Operation staff manages the account creation process.

##### Drupal
Drupal defines a default set of roles; Anonymous, Authenticated, and Administrator, as well as providing for the creation of additional organizational-defined roles identified by Project Full Name

##### Project
The system Owner has oversight over all permissions that the Project Manager and Operations Staff manages.

#### d
##### Contractor
All accounts issued for application administrators and SSH are documented in CivicActions' ticketing system. Account request tickets contain details that explain the attributes for the account including authorized users of Drupal, system infrastructure, group and role membership, and access authorizations.

##### Drupal
Drupal has a sophisticated permissions and role-based access control built-in. Each role within Drupal can only access the documents and controls for which their privilege allows.
##### Ilias
Ilias' permissions and role-based access controls are built-in. Each role within Ilias can only access the pages and controls for which their privilege allows.
##### Project
Project user privileges vary depending on the type of user role assigned. Only users with the role of Administrator have the ability to create and modify user roles for other users.

#### e
##### Contractor
All accounts issued for the admin management of Application or SSH access must be approved by the System Owner or Project Manager who must create an account request. The CivicActions Operations staff applies appropriate account permissions and settings based on the job role and function documented within the request ticket using processes defined by the CivicActions' Security Office.
##### Project
The System Owner approves, and CivicActions Operations set up the initial Administrator account for Project. Subsequent client access and related approvals are managed by CivicActions Operations in collaboration with the System Owner.

#### f
##### Contractor
CivicActions Operations staff is responsible for the following account management activities for both internal administrative users and customer accounts:

- Establishing account justification
- Activating accounts
- Modifying accounts
- Expiring accounts
- Disabling accounts
- Removing accounts

#### h
##### Contractor
In accordance with the CivicActions Access Control (AC-01) Policy when an account is no longer required, the Project Manager notifies the Operations Team to immediately disable all access. Users upon reassignment, change in roles, termination, or leaving employment are initially removed from all roles and groups, effectively denying them all access to privileged accounts.

#### i
##### Contractor
System accounts require access authorizations prior to accounts being created. The Project Manager must initiate an access request for an account to be created. CivicActions Operations staff reviews the request to ensure accuracy, including intended system usage and other attributes of the user access being requested.

##### Project
Project governs their own administrative access. Users with
the Administrator roles are empowered to designate and approve
Administrators.

#### j
##### Contractor
All privileged accounts are reviewed by CivicActions Operations staff every 180 days.

##### Project
Administrators are empowered to and responsible for reviewing their own accounts and determining whether the accounts should still be authorized.

#### k
##### Contractor
In accordance with standard security best practices and CivicActions policy, shared and reissued accounts for internal accounts of any kind are not created nor used for any purpose in any system.

#### c
##### Project
In accordance with Project Access Control Policy, Project group membership is determined according to the individual's position and role within the organization. A ticket request is used to request accounts and group membership. The request is authorized by the appropriate manager.

#### AC-3: ACCESS ENFORCEMENT
```text
Enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

```
**Status:** partial
##### AWS
In this architecture, AWS Identify and Access Management (IAM) and Amazon Amazon S3 enforce access to the AWS infrastructure and data in Amazon S3 buckets. The baseline IAM groups and roles are associated with access policies to align user accounts with personnel functions related to infrastructure/platform management (e.g. Billing, Amazon EC2/VPC/Amazon RDS systems administration, I.T. auditing, etc.) Login/API access is restricted to those users for whom the organization has authorized and created, or federated, IAM user accounts, and assigned the appropriate IAM group and/or role memberships. Amazon S3 buckets have specific access control policies assigned to restrict access to those IAM users who are assigned the appropriate IAM roles/groups.

##### Drupal
Access control in Drupal is enforced by authentication via a unique username/password for every type of user except Anonymous user. The user’s privileges, permissions, and access are provided on the principle of least privilege.
The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves. Drupal Administrators are the only user roles that can create new user accounts.

##### Ilias
Access control in Ilias is enforced by authentication via Shibboleth single sing on (SSO) for every type of user except Anonymous user. The user’s privileges, permissions, and access are provided on the principle of least privilege.
The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves. Project Administrators, HR Managers, and Org Managers are the only roles that can create new user accounts.

##### Project
The Project Full Name ensures that assigned authorizations for controlling access to the system is enforced in accordance with the user definitions noted in Section 1.1.1 of the Project SSP. The technical support staff ensures that access to security functions and protected information is restricted to authorized personnel. Access will be controlled with access control list used on each instance. Members of one group cannot access resources defined for other groups unless explicitly permitted.

#### AC-3 (9): CONTROLLED RELEASE
```text
Release information outside of the system only if:
 - (a) The receiving [Assignment: organization-defined system or system component] provides [Assignment: organization-defined controls]; and
 - (b) [Assignment: organization-defined controls] are used to validate the appropriateness of the information designated for release.

```
**Status:** complete
##### Project
The Project information system does not release information outside of the established system boundary.

#### AC-6: LEAST PRIVILEGE
```text
Employ the principle of least privilege, allowing only authorized accesses for users (or processes acting on behalf of users) that are necessary to accomplish assigned organizational tasks.

```
**Status:** incomplete
##### SSH
SSH access is provided on a least privilege basis and analyzed on an ongoing basis, at least quarterly. Findings related to these audits of accounts are reported and reviewed by the Security Office and evaluated to determine roles that need to be revoked.
#### AC-7: UNSUCCESSFUL LOGIN ATTEMPTS
```text
 - a. Enforce a limit of [Assignment: organization-defined number] consecutive invalid logon attempts by a user during a [Assignment: organization-defined time period]; and
 - b. Automatically [Selection (one or more): lock the account or node for an [Assignment: organization-defined time period], lock the account or node until released by an administrator, delay next logon prompt per [Assignment: organization-defined delay algorithm], notify system administrator, take other [Assignment: organization-defined action]] when the maximum number of unsuccessful attempts is exceeded.

```
**Status:** complete
#### a
##### Drupal
Drupal can be configured to lock an account after a specified number of invalid login attempts within a specified time period. The default for Drupal is 5 failed login attempts within six hours.
#### b
##### Drupal
Lockdown following unsuccessful attempts is configurable by Drupal administrators to conform to defined requirements. When a user exceeds the limit of invalid login attempts, their account is automatically locked for a specified time and requires administrator action to unlock the account before the lockout period expires.
##### Project
The Project system locks out users after three unsuccessful login attempts. The information system automatically locks the account permanently, unless an administrator unlocks the account before then, when the maximum number of unsuccessful attempts (3) is exceeded.

#### AC-8: SYSTEM USE NOTIFICATION
```text
 - a. Display [Assignment: organization-defined system use notification message or banner] to users before granting access to the system that provides privacy and security notices consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines and state that:
   - 1. Users are accessing a U.S. Government system;
   - 2. System usage may be monitored, recorded, and subject to audit;
   - 3. Unauthorized use of the system is prohibited and subject to criminal and civil penalties; and
   - 4. Use of the system indicates consent to monitoring and recording;
 - b. Retain the notification message or banner on the screen until users acknowledge the usage conditions and take explicit actions to log on to or further access the system; and
 - c. For publicly accessible systems:
   - 1. Display system use information [Assignment: organization-defined conditions], before granting further access to the publicly accessible system;
   - 2. Display references, if any, to monitoring, recording, or auditing that are consistent with privacy accommodations for such systems that generally prohibit those activities; and
   - 3. Include a description of the authorized uses of the system.

```
**Status:** incomplete
##### Ilias
System Use Notification is inherited from the Project.
##### Project
A warning banner ensures that all persons attempting to gain access to the system know that the system and its information are “Authorized User Only” and that attempts to illegally log on to the system could lead to criminal prosecution. The warning message displayed notifies unauthorized users that they have accessed a U.S. Government computer system and continued, unauthorized use can be punishable by fines or imprisonment. Each device logged into will display a system use notification message before the log in window is displayed. The system use notification banner will remain on the screen until the user takes an explicit action to log on to the device. The following is the notification banner displayed on all system instances:

"You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions:

- The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.
- At any time, the USG may inspect and seize data stored on this IS.
- Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.
- This IS includes security measures (e.g., authentication and access controls) to protect USG interests -- not for your personal benefit or privacy.
- Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."

#### AC-14: PERMITTED ACTIONS WITHOUT IDENTIFICATION OR AUTHENTICATION
```text
 - a. Identify [Assignment: organization-defined user actions] that can be performed on the system without identification or authentication consistent with organizational mission and business functions; and
 - b. Document and provide supporting rationale in the security plan for the system, user actions not requiring identification or authentication.

```
**Status:** complete
#### a
##### Drupal
The anonymous user role has the least access to the site of all roles. Drupal sites can be configured to allow actions identified by Project Full Name

##### Ilias
The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves.
##### Project
The Project Full Name allows the general public user to read the web pages, do searches on the resource database and to review online forum information without identification and authentication for the public web site. Program and Privilege users cannot access the Project system without identification or authentication.

#### AC-17: REMOTE ACCESS
```text
 - a. Establish and document usage restrictions, configuration/connection requirements, and implementation guidance for each type of remote access allowed; and
 - b. Authorize each type of remote access to the system prior to allowing such connections.

```
**Status:** complete
##### Contractor
The CivicActions Access Control (AC) policy defines policy for remote usage restrictions. The Project Manager or System Owner may additionally provision users according to their Access Control policies.

##### Project
The Project Full Name permits remote access for privileged functions to support operational needs. The technical staff documents, monitors, and controls all methods of remote access to the information system including remote access for privileged functions. Privileged user access is only permitted through the use of Secure Shell (SSH) where the user will authenticate to the device through this secure channel. Virtual Private Networking (VPN) is not enabled in any form within the Project accreditation boundary.

#### AC-18: WIRELESS ACCESS
```text
 - a. Establish configuration requirements, connection requirements, and implementation guidance for each type of wireless access; and
 - b. Authorize each type of wireless access to the system prior to allowing such connections.

```
**Status:** complete
##### Contractor
This control is not applicable. The system does not provide wireless access points.

#### AC-19: ACCESS CONTROL FOR MOBILE DEVICES
```text
 - a. Establish configuration requirements, connection requirements, and implementation guidance for organization-controlled mobile devices, to include when such devices are outside of controlled areas; and
 - b. Authorize the connection of mobile devices to organizational systems.

```
**Status:** complete
##### Contractor
This control is not applicable. The system does not maintain a facility in which mobile device access limitations are required.

#### AC-20: USE OF EXTERNAL INFORMATION SYSTEMS
```text
 - a. [Selection (one or more): Establish [Assignment: organization-defined terms and conditions], Identify [Assignment: organization-defined controls asserted to be implemented on external systems]], consistent with the trust relationships established with other organizations owning, operating, and/or maintaining external systems, allowing authorized individuals to:
   - 1. Access the system from external systems; and
   - 2. Process, store, or transmit organization-controlled information using external systems; or
 - b. Prohibit the use of [Assignment: organizationally-defined types of external systems].

```
**Status:** complete
##### Contractor
This control is not applicable. The system does not connect with external information systems.

#### AC-22: PUBLICLY ACCESSIBLE CONTENT
```text
 - a. Designate individuals authorized to make information publicly accessible;
 - b. Train authorized individuals to ensure that publicly accessible information does not contain nonpublic information;
 - c. Review the proposed content of information prior to posting onto the publicly accessible system to ensure that nonpublic information is not included; and
 - d. Review the content on the publicly accessible system for nonpublic information [Assignment: organization-defined frequency] and remove such information, if discovered.

```
**Status:** complete
#### a
##### Project
The Client Full Name grants certain Project support staff members the authority to post publicly accessible content. These individuals must complete Project system security training before being granted access to the Project and before they can post publicly accessible content within the Project Full Name. Furthermore, each authorized individual must follow the procedures delineated within the “Using Drupal” Instruction to ensure they are following a verifiable procedure throughout the entire process. This covers the Project Discussion Lists administration areas, Project Quarterly Reporting and training tools, and Drupal Content Management systems. Public content is only edited via the Drupal Content Management System. All other content is only viewable by Project system users and protected by hardened access controls.

#### b
##### Project
It is the Project responsibility to train authorized Project individuals ensuring publicly accessible information does not contain nonpublic information.

#### c
##### Project
Authorized Project individuals review the proposed content of information prior to posting onto the publicly accessible information system to ensure that nonpublic information is not included.

Project Users have been authorized for creation of publicly accessible content with publishing authority from an Administrator role. The publishing authority ensures the information being published does not contain nonpublic information.

#### d
##### Project
Authorized Project individuals review the content on the publicly accessible information system for nonpublic information at least every 365 days and removes such information.

### AT: Awareness and Training


#### AT-1: SECURITY AWARENESS AND TRAINING POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] awareness and training policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the awareness and training policy and the associated awareness and training controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the awareness and training policy and procedures; and
 - c. Review and update the current awareness and training:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete
##### Contractor
CivicActions has developed, documented and disseminated to personnel awareness and training policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Awareness and Training (AT) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.

##### Project
Security awareness and training policy and procedures are formally documented in None, which provides the roles and responsibilities as it pertains to security awareness and training. The Department will ensure all users, including managers and senior executives, are exposed to basic information system security awareness materials before authorizing access to the system and at least annually thereafter. Client documents and monitors all individual information system security training activities including basic security awareness training. OMB reviews and updates the policy as necessary.

#### AT-2: SECURITY AWARENESS TRAINING
```text
 - a. Provide security and privacy literacy training to system users (including managers, senior executives, and contractors):
   - 1. As part of initial training for new users and [Assignment: organization-defined frequency] thereafter; and
   - 2. When required by system changes or following [Assignment: organization-defined events];
 - b. Employ the following techniques to increase the security and privacy awareness of system users [Assignment: organization-defined awareness techniques];
 - c. Update literacy training and awareness content [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
 - d. Incorporate lessons learned from internal or external security or privacy incidents into literacy training and awareness techniques.

```
**Status:** complete
#### a
##### Contractor
Both regular and ad hoc training to all CivicActions personnel, including those who support the system infrastructure and applications, is provided. All employees and contractors must complete Security Awareness training upon being hired and at least annually thereafter. CivicActions Operations staff will not create accounts for individuals until they have successfully completed the trainings. Additional training will be provided as required by system changes. Training takes the following forms:

Annual Knowledge Survey (i.e., Security Awareness Training): All employees are required to review trainings covering Security Awareness. After the training, a survey-style security awareness test is taken by employees. All CivicActions personnel are required to complete and pass the survey, and new employees are required to pass before being granted access to the Information System. In order to successfully pass the test, a score of 80% is required. This survey tests CivicActions personnel’s knowledge of critical security subjects, policies and procedures. Results from this survey are compiled by the Office of Human Resources and used to refine future training efforts.

Ad Hoc Security Awareness: The CivicActions' Security Office oversees the approximately bi-monthly distribution of security awareness tips and articles to all CivicActions employees. This can include general tips as well as articles tailored to the specific requirements of CivicActions users.

#### b
##### Contractor
In the event of a major system change, the Project Manager is responsible for delivering additional training to impacted personnel. Specific training types, mediums, and delivery methods are dependent upon the nature of the system change.

#### c
##### Contractor
CivicActions provides annual security awareness training to its personnel.

##### Project
Client personnel and contractor employees involved with the management, operation, programming, maintenance, or use of Project system receive training in acceptable computer security practices prior to system access. All Client employees and contractors are required to complete annual IT security awareness training. This security awareness training covers issues and policies associated with information security, including end user security roles and responsibilities and rules of behavior. Some topics addressed in the training are:

- Password protection
- System rules of behavior
- Protection of hardware, software, and data
- Proper handling of copyrighted materials
- Reporting of security breaches and violations
- Proper procedures for software installation, uploading, and use on
  workstations.

#### AT-3: ROLE-BASED SECURITY TRAINING
```text
 - a. Provide role-based security and privacy training to personnel with the following roles and responsibilities: [Assignment: organization-defined roles and responsibilities]:
   - 1. Before authorizing access to the system, information, or performing assigned duties, and [Assignment: organization-defined frequency] thereafter; and
   - 2. When required by system changes;
 - b. Update role-based training content [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
 - c. Incorporate lessons learned from internal or external security or privacy incidents into role-based training.

```
**Status:** complete
#### a
##### Contractor
CivicActions personnel with security responsibilities are required to complete role-based security training before being provided with access to the information system. The CivicActions' Security Office is responsible for creating the content of the training. The role-based training is provided and tracked by the CivicActions Security Office.

#### b
##### Contractor
The Project Manager in collaboration with CivicActions Security Office determines whether a change to the information system requires any modifications and updates to the security awareness training program and if so, works with the CivicActions' Security Office to implement the change.

#### c
##### Contractor
CivicActions Security Office provides users with security responsibilities role-based security training on an annual basis. The training is provided and tracked by the CivicActions Security Office.

##### Project
Completion of role-based training is an annual requirement for personnel in roles with significant information security responsibilities that require specialized role-based training. Role-based cybersecurity training is developed and implemented to meet identified training needs and competencies associated with the various target audiences/functional roles (federal and contractor employees) that comprise the Client workforce, as is identified in and required by the FISMA and OMB A-130, Appendix III. The appropriate content of security training is determined based on the assigned roles and responsibilities of individuals and the specific security requirements of the Department, PO and the information systems to which personnel have authorized access. Annual training requirements may be met by completing one or more course(s) within the Department’s learning management systems, participating in instructor-led training provided by the OCIO, or completing an external role-based course or courses offered within their specific functional area of expertise.

#### AT-4: SECURITY TRAINING RECORDS
```text
 - a. Document and monitor information security and privacy training activities, including security and privacy awareness training and specific role-based security and privacy training; and
 - b. Retain individual training records for [Assignment: organization-defined time period].

```
**Status:** complete
#### a
##### Contractor
The CivicActions' Security Office tracks all security awareness training within the organization and ensures that all employees have successfully completed training when required. The training records are stored and tracked in a spreadsheet maintained by the CivicActions Security Office.

##### Project
Client documents and monitors all individual information system security training activities including basic security awareness training. New users are required to take security training within 30 days of hire. This information is kept in the appropriate personnel files to verify users have met the training requirements. Training requirement notifications are sent to individuals as deadline for re-training approaches.

#### b
##### Contractor
Training records are tracked and maintained by the CivicActions Security Office. Records are maintained permanently.

##### Project
Client maintains training certifications for the specified period.

### AU: Audit and Accountability


#### AU-1: AUDIT AND ACCOUNTABILITY POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] audit and accountability policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the audit and accountability policy and the associated audit and accountability controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the audit and accountability policy and procedures; and
 - c. Review and update the current audit and accountability:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** incomplete
##### Contractor
CivicActions has developed, documented and disseminated to personnel an audit and accountability policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Audit and Accountability (AU) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.

##### Project
The Project maintains a record of system activity by application process and by user activity. Audit and accountability policy and procedures are documented within the Project SSP. Security software features are used to automatically generate and store security audit log records for use in monitoring security-related events on all multi-user systems. The Client reviews and updates this policy as necessary and it was last updated in April 2008. Additional information is contained within the None.

#### AU-2: AUDITABLE EVENTS
```text
 - a. Identify the types of events that the system is capable of logging in support of the audit function: [Assignment: organization-defined event types that the system is capable of logging];
 - b. Coordinate the event logging function with other organizational entities requiring audit-related information to guide and inform the selection criteria for events to be logged;
 - c. Specify the following event types for logging within the system: [Assignment: organization-defined event types (subset of the event types defined in AU-2a.) along with the frequency of (or situation requiring) logging for each identified event type];
 - d. Provide a rationale for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations of incidents; and
 - e. Review and update the event types selected for logging [Assignment: organization-defined frequency].

```
**Status:** partial
#### a
##### AWS
In this architecture, the following audit methods log all security-relevant user/API activities and Amazon S3 data access activities, and support the capability to audit organizationally defined events:

- AWS CloudTrail logging
- Amazon S3 bucket logging
- Elastic Load Balancing (ELB) logging
- Amazon RDS MySQL error logging

##### Contractor
CivicActions' Security Policy provides information about auditing and logging of CivicActions internal users and end-user activity on the servers and within the system application.

##### Drupal
Drupal's Watchdog log are configured to track all relevant auditable events as defined by Client

- Apache access log: Contains a list of requests for your website that have bypassed Varnish. These requests include pages, theme files, and static media files.
- Apache error log: Records any Apache-level issues. The issues reported here are usually caused by general server issues, including capacity problems, .htaccess problems, and missing files.
- Drupal page request log: Records all Drupal page loads on your website.
- Drupal Watchdog log: Records Drupal-related actions on your website. The Watchdog log is recorded on your database if you have enabled the syslog module.
- MySQL slow query log: Contains a list of MySQL queries that have taken longer than one second to complete.
- PHP error log: Records any issues that occur during the PHP processing portion of a page load. Issues reported here are usually caused by a website’s code, configuration, or content.

##### Ilias
Transaction logs are generated by the Apache web server, Ilias CMS, MySQL database and PHP page processing. Specifically, the following server, application, database and network device audit log events are captured:
- Apache access log: Contains a list of requests for your website that have bypassed Varnish. These requests include pages, theme files, and static media files.
- Apache error log: Records any Apache-level issues. The issues reported here are usually caused by general server issues, including capacity problems, .htaccess problems, and missing files.
- Ilias page request log: Records all Ilias page loads on your website.
- Ilias log: Records Ilias-related actions on your website. The log is recorded on your server.
- MySQL slow query log: Contains a list of MySQL queries that have taken longer than one second to complete.
- PHP error log: Records any issues that occur during the PHP processing portion of a page load. Issues reported here are usually caused by a website’s code, configuration, or content.

#### c
##### AWS
In this architecture, the following audit methods provide data on activities occurring within the infrastructure:

- AWS CloudTrail logging
- Amazon S3 bucket logging
- Elastic Load Balancing (ELB) logging
- Amazon RDS MySQL error logging

##### Ilias
CivicActions has extensive experience and specialization as a host of websites that are built using the Ilias web learning platform. Should the need for additional logging become evident, we have the ability to do so by modifying the website's source code to insert additional Ilias logging hooks.

#### d
##### AWS
In this architecture, the following audit methods log all security-relevant events and errors related to IAM user and API activities, Amazon S3 data access, network access, and Amazon RDS database errors, and support the capability to audit organizationally defined events:

- AWS CloudTrail logging
- Amazon S3 bucket logging
- Elastic Load Balancing (ELB) logging
- Amazon RDS MySQL error logging

##### Drupal
Information captured in the transaction logs includes, but is not limited to, the following auditable events:

- Failed login attempts
- Successful login attempts
- User account deletions
- User account blocking/unblocking
- Changes in user role assignments
- Unauthorized attempts to alter protected user fields
- New user account creation
- Password reset instructions mailed
- User logins via a one-time login link
- User logouts
- Content creation (datasets, resources and other content types)
- Content modification
- Content deletion
- Content publishing
- Content unpublishing
- File uploads
- Web page not found
- Website configuration changes
- System administration activities
- Slow query logs.
- PHP error logs: Captures any errors logged during execution of the PHP programming language.

##### Ilias
Information captured in the transaction logs includes, but is not limited to, the following auditable events:
- Failed login attempts
- Successful login attempts
- New user account creation
- Password reset instructions mailed
- User logins via a one-time login link
- Content creation
- Content publishing
- Web page not found
- Website configuration changes
- System administration activities
- Slow query logs.
- PHP error logs: Captures any errors logged during execution of the PHP programming
  language.

#### b
##### Contractor
Auditable events may change due to changes in the threat environment. CivicActions teams collaborate internally and also communicate with customers and partner organizations to identify and select auditable events. The teams that participate in this process are described in control SA-3(b).

##### Ilias
All security-related issues and events, including requests for server log analysis, are recorded in CivicActions' JIRA tracking system.
#### AU-3: CONTENT OF AUDIT RECORDS
```text
Ensure that audit records contain information that establishes the following:
 - a. What type of event occurred;
 - b. When the event occurred;
 - c. Where the event occurred;
 - d. Source of the event;
 - e. Outcome of the event; and
 - f. Identity of any individuals, subjects, or objects/entities associated with the event.

```
**Status:** partial
##### AWS
In this architecture, the following audit methods generate records with the level of detail specified for the control:

- **AWS CloudTrail logging**: Provides information on activities
  related to infrastructure changes.

- **Amazon S3 bucket logging**: Provides data on activities related to the
  access or manipulation of data stored in Amazon S3.

- **Elastic Load Balancing (ELB) logging**: Provides information about
  requests or connections.

- **Amazon RDS MySQL error logging**: Captures errors encountered by the
  database engine. In addition, the MySQL general query log can be enabled
  by the customer organization to capture when clients connect or disconnect
  and SQL statements received from clients.


AWS logging information:

- AWS native logging: https://aws.amazon.com/answers/logging/aws-native-security-logging-capabilities/
- AWS CloudTrail logs: http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference.html
- Amazon S3 bucket logs: http://docs.aws.amazon.com/amazons3/latest/dev/ServerLogs.html
- ELB logs: http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html
    http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html

- Amazon RDS logs: http://docs.aws.amazon.com/amazonrds/latest/UserGuide/USER_LogAccess.html

##### Drupal
The logs collected for Drupal sites include the following types of information:

- IP number of the request originator
- Timestamp
- Request URL
- HTTP status code returned
- Username
- Drupal Watchdog message (if applicable)
- Unique numerical ID of the content being modified (for content creation, modification and deletion events)
When auditing a Drupal incident, the CivicActions developers aggregate log sources from multiple servers into the Graylog dashboard so that all log entries for a single managed security incident can be analyzed in a single document. Log sources are sorted, filtered and reviewed. Application logs are maintained primarily for an after-the-fact investigation of critical systems or security events.

##### Ilias
The logs collected for Ilias sites include the following types of information:
- IP number of the request originator
- Timestamp
- Username
- Ilias log message (if applicable)
- Unique numerical ID of the content being modified (for content creation, modification and deletion events)
When auditing an Ilias incident, CivicActions' developers aggregate log sources from multiple servers into the Graylog dashboard so that all log entries for a single managed security incident can be analyzed in a single document. Log sources are sorted, filtered and reviewed. Application logs are maintained primarily for an after-the-fact investigation of critical systems or security events.

#### AU-4: AUDIT STORAGE CAPACITY
```text
Allocate audit log storage capacity to accommodate [Assignment: organization-defined audit log retention requirements].

```
**Status:** partial
##### AWS
In this architecture, logs track dynamic capacity growth to accommodate organizationally defined storage capacity requirements. Amazon S3 buckets are established to store audit logs from the following audit methods:

- AWS CloudTrail logging
- Amazon S3 bucket logging
- Elastic Load Balancing (ELB) logging
- Amazon RDS MySQL error logging

##### Contractor
CivicActions ensures adequate storage capability requirements listed in AU-11 for all events from the application, database, and hosting environment.

#### AU-5: RESPONSE TO AUDIT PROCESSING FAILURES
```text
 - a. Alert [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time period] in the event of an audit logging process failure; and
 - b. Take the following additional actions: [Assignment: organization-defined additional actions].

```
**Status:** partial
#### a
##### AWS
In this architecture, AWS CloudTrail is enabled, and provides the basis for audit processing within the infrastructure.

AWS built-in features include customer alerting of AWS CloudTrail and other service failures through the following:

- AWS Service Health Dashboard (http://status.aws.amazon.com)
- RSS feeds to which the customer organization can subscribe
- email
- alerts sent directly to the AWS account *root user* for critical events
- AWS internal Incident Response and corporate communications processes

##### Contractor
When notified (e.g., via CloudWatch) of an auditing failure, CivicActions Operations staff will review the causes and take corrective action.

#### AU-6: AUDIT REVIEW, ANALYSIS, AND REPORTING
```text
 - a. Review and analyze system audit records [Assignment: organization-defined frequency] for indications of [Assignment: organization-defined inappropriate or unusual activity] and the potential impact of the inappropriate or unusual activity;
 - b. Report findings to [Assignment: organization-defined personnel or roles]; and
 - c. Adjust the level of audit record review, analysis, and reporting within the system when there is a change in risk based on law enforcement information, intelligence information, or other credible sources of information.

```
**Status:** Planned
#### a
##### Contractor
CivicActions security audit data is collected by the AWS CloudWatch monitoring and observability service to support real time and after-the-fact investigation at the application level for the following:

- Indications of inappropriate or unusual activity
- Assurance that logging is functioning properly
- Adherence to logging standards identified in this procedure

#### b
##### Contractor
Any significant findings observed during the inspection are reported to CivicActions' Security Office. If these are considered to constitute a security incident, then the Incident Response process is invoked as described in the implementation of the Incident Response Plan (IR-8).

#### AU-8: TIME STAMPS
```text
 - a. Use internal system clocks to generate time stamps for audit records; and
 - b. Record time stamps for audit records that meet [Assignment: organization-defined granularity of time measurement] and that use Coordinated Universal Time, have a fixed local time offset from Coordinated Universal Time, or that include the local time offset as part of the time stamp.

```
**Status:** partial
#### a
##### AWS
AWS includes the Amazon Time Sync Service. Running over Network Time Protocol (NTP), this service synchronizes the time on AWS instances using redundant satellite-connected and atomic clocks in all public AWS regions. The Amazon Time Sync Service provides accurate time stamp data to the following audit methods:

- AWS CloudTrail logging
- Amazon S3 bucket logging
- Elastic Load Balancing (ELB) logging
- Amazon RDS MySQL error logging

#### b
##### AWS
The Amazon Time Sync Service provides accurate time stamp data to the following audit methods:

- AWS CloudTrail logging
- Amazon S3 bucket logging
- Elastic Load Balancing (ELB) logging
- Amazon RDS MySQL error logging

Time stamps are recorded as specified in the ISO 8601 standard. ISO 8601 represents local time (with the location unspecified), as UTC, or as an offset from UTC.

##### Project
The Project system clocks are synchronized system-wide and provide time stamps with audit records.

#### AU-9: PROTECTION OF AUDIT INFORMATION
```text
 - a. Protect audit information and audit logging tools from unauthorized access, modification, and deletion; and
 - b. Alert [Assignment: organization-defined personnel or roles] upon detection of unauthorized access, modification, or deletion of audit information.

```
**Status:** partial
##### AWS
Access to audit data and tools is determined by access control policies for IAM groups and roles. Only users assigned to IAM groups and roles with access to audit data and tools can access them. Additionally, AWS uses server-side encryption on Amazon S3 bucket logs, and maintains them as read-only files.

##### Contractor
CivicActions ensures that audit logs are created, stored and maintained. Developers who have been assigned as members of the CivicActions Security Office are the only CivicActions personnel with logical permission to access and review audit logs.

#### AU-11: AUDIT RECORD RETENTION
```text
Retain audit records for [Assignment: organization-defined time period consistent with records retention policy] to provide support for after-the-fact investigations of incidents and to meet regulatory and organizational information retention requirements.

```
**Status:** partial
##### AWS
AWS CloudTrail logs are stored in an Amazon S3 bucket, which dynamically allocates storage capacity to support continuous collection and storage of AWS CloudTrail log data. The storage capacity supports indefinite retention, but with 7 year retention specified, and migration to Amazon Glacier after 90 days in AWS regions where Glacier is available.

##### Contractor
CivicActions audits events from the application, database, and hosting environment, and retains these records for at least 180 days.

#### AU-12: AUDIT GENERATION
```text
 - a. Provide audit record generation capability for the event types the system is capable of auditing as defined in AU-2a on [Assignment: organization-defined system components];
 - b. Allow [Assignment: organization-defined personnel or roles] to select the event types that are to be logged by specific components of the system; and
 - c. Generate audit records for the event types defined in AU-2c that include the audit record content defined in AU-3.

```
**Status:** partial
#### a
##### AWS
In this architecture, AWS CloudTrail, Amazon S3 bucket logging, Elastic Load Balancing (ELB) logging, and Amazon RDS MySQL error logging are  enabled, but initial Amazon EC2 instances launched by this deployment (bastion host, application servers, proxy servers, and any Amazon EC2-based NAT servers) do not have auditing enabled within the OS, as these are for example purposes only.

AWS built-in features of logging mechanisms provide the audit record generation capability for the auditable events defined in AU-2a. by logging all security-relevant IAM user and API activities which address AWS infrastructure components (AWS Products and services), ELB

##### Contractor
CivicActions ensures audit records are generated for its web and event logs as required in AU-2 and AU-3 for servers, application, database, and network components.

#### b
##### AWS
In this architecture, AWS CloudTrail, Amazon S3 bucket logging, Elastic Load Balancing (ELB) logging, and Amazon RDS MySQL error logging are enabled AWS CloudTrail is enabled to log all available API events automatically within the AWS infrastructure and Amazon S3 bucket logging is enabled to log bucket activity.

AWS built-in features of Identity and Access Management (IAM) allows policy to be applied to privileged users for administrator/audit access, allowing them to modify Amazon CloudWatch alarms, AWS Config rules, and Amazon S3 bucket logging to select the CloudTrail and Amazon S3 events that are to cause notification, alerting and automated reaction.

##### Contractor
The selected auditable events described in AU-2 are coordinated by CivicActions internal admins and client security/operations officers for each component of the production system.

#### c
##### AWS
In this architecture, AWS CloudTrail, Amazon S3 bucket logging, Elastic Load Balancing (ELB) logging, and Amazon RDS MySQL error logging are enabled. However, the initial Amazon EC2 instances launched by this deployment (bastion host, application servers, proxy servers, and any Amazon EC2-based NAT servers) DO NOT have any auditing enabled within the OS, as these are in place for example purposes only.

AWS built-in features of native logging generates audit records with the content defined in AU-3.

AWS logging information:

- AWS native logging: https://aws.amazon.com/answers/logging/aws-native-security-logging-capabilities/
- AWS CloudTrail logs: http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference.html
- Amazon S3 bucket logs: http://docs.aws.amazon.com/amazons3/latest/dev/ServerLogs.html
- ELB logs: http://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html

    http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html

- Amazon RDS logs: http://docs.aws.amazon.com/amazonrds/latest/UserGuide/USER_LogAccess.html

##### Contractor
CivicActions maintained applications generate audit records for their web and event logs as described in AU-2 and AU-3.

### CA: Assessment Authorization and Monitoring


#### CA-1: SECURITY ASSESSMENT AND AUTHORIZATION POLICIES AND PROCEDURES
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
##### Contractor
CivicActions has developed, documented and disseminated to personnel a certification, accreditation, and security assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Security Assessment and Authorization Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.

##### Project
Project follows the None. The Project System Security Policy (SSP) provides guidance on all aspects of security for the protection of Project information technology resources.

Project will periodically review and update the SSP when there is a significant change to the regulatory, operational, or technical environment.

#### CA-2: SECURITY ASSESSMENTS
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
#### a
##### Contractor
CivicActions will develop a security assessment plan (SAP) that describes the security controls and control enhancements under assessment, assessment procedures used to determine effectiveness, the assessment environment, the assessment team, and the assessment roles and responsibilities.

##### Project
The Project Full Name follows the None. The Project Full Name will conduct annual security assessments to comply with FISMA and NIST regulations. Project will draw on NIST Special Publications 800-53A security controls to complete the assessment. All controls and sub-set security controls will be evaluated and a risk assessment will be conducted. The scope of the assessment includes:

1. Security controls and control enhancements under assessment
2. Assessment procedures to be used to determine security control effectiveness
3. Assessment environment, assessment team, and assessment roles and responsibilities

#### b
##### Contractor
CivicActions will assess the security controls in their system and its environment of operation to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting established security requirements.

All controls assigned and documented in this System Security Plan (SSP) will be tested at least annually or when there is a major change to the system.

#### c
##### Contractor
CivicActions will produce a security assessment report that documents the results of the assessment. The Security Assessment Report must contain the results of the assessment, and may also contain recommendations and suggestions for plans of actions and milestones (POA&Ms).

##### Project
The Project Authorizing Official or Designated Representative will create a Security Assessment Report (SAR). A full assessment shall be conducted by an independent third party assessor at least every three years.

#### d
##### Contractor
CivicActions will provide the results of the security control assessment to the System Owner, Project Manager, CivicActions Security, and the Authorization Official (AO)). The security control assessment package includes the following:

- Security Control Matrix
- Privacy Impact Assessment
- E-Authentication
- Contingency Plan
- Configuration Management Plan
- Rules of Behavior
- Incident Response Plan

#### CA-3: SYSTEM INTERCONNECTIONS
```text
 - a. Approve and manage the exchange of information between the system and other systems using [Selection (one or more): interconnection security agreements, information exchange security agreements, memoranda of understanding or agreement, service level agreements, user agreements, nondisclosure agreements, [Assignment: organization-defined type of agreement]];
 - b. Document, as part of each exchange agreement, the interface characteristics, security and privacy requirements, controls, and responsibilities for each system, and the impact level of the information communicated; and
 - c. Review and update the agreements [Assignment: organization-defined frequency].

```
**Status:** none
##### Contractor
This control is not applicable. CivicActions systems do not have system interconnections. The only communication conducted to CivicActions' systems is through the Internet.

#### CA-5: PLAN OF ACTION AND MILESTONES
```text
 - a. Develop a plan of action and milestones for the system to document the planned remediation actions of the organization to correct weaknesses or deficiencies noted during the assessment of the controls and to reduce or eliminate known vulnerabilities in the system; and
 - b. Update existing plan of action and milestones [Assignment: organization-defined frequency] based on the findings from control assessments, independent audits or reviews, and continuous monitoring activities.

```
**Status:** complete
##### Contractor
CivicActions documents all deficiencies and vulnerabilities identified during the security certification and/or continuous monitoring phase (via security assessment, vulnerability scanning, risk assessment, etc.) within the Plan of Action and Milestones (POA&M).

The POA&M document provides a platform for CivicActions to monitor and track the deficiency and its mitigation strategy. POA&M items will include:

- The description of the deficiency,
- Dedicated point of contact for this deficiency.
- Cost of the mitigation strategy
- Associated risk and NIST control
- Recommended mitigation strategy

POA&Ms are tracked throughout the lifecycle of the system until its mitigation. All POA&Ms are reviewed on a monthly basis by CivicActions Information System Security Officer to ensure all mitigation strategies are continuing as documented.

##### Project
The Project follows the None procedures in managing POA&Ms.

#### CA-6: SECURITY AUTHORIZATION
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
##### Project
The Project follows the None. The Project system received its first three-year security accreditation on March 3, 2009, and most recently received an ATO on February 5, 2016.

ATO re-assessment will be performed every three years or when there is a major change to the application, in which a senior organizational official will sign and approve the security accreditation.

#### CA-7: CONTINUOUS MONITORING
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
#### a
##### Contractor
CivicActions implements a continuous monitoring strategy that incorporates configuration management, system scanning and log analysis processes:

- Configuration management includes the assessment of security impact analyses of proposed and implemented changes.
- System scanning is managed by running the OpenSCAP vulnerability scanner using the DISA STIG profile.
- Log analysis is managed by feeding logs to a Graylog dashboard for analysis.

##### Drupal
CivicActions follows recommendations and best practices developed by the Drupal community for monitoring. Examples of specific logs and metrics are included in AU-2 and AU-3.

##### Ilias
CivicActions follows recommendations and best practices developed by the Ilias community for monitoring. Examples of specific logs and metrics are included in AU-2 and AU-3.
#### b
##### Contractor
Configuration management and log analysis is carried out in real time. OpenSCAP security scans are performed and reviewed monthly. See also: RA-5 and SI-4.

Quarterly review of the control assessments supporting the monitoring is conducted by CivicActions Operations in collaboration with the CivicActions Security Office.

#### d
##### Contractor
CivicActions conducts or oversees continuous system security monitoring.

#### e
##### Contractor
CivicActions Security reviews the results of the security scans and security assessments with associated JIRA and/or GitLab Issue tickets created to correlate and analyze security-related information generated from the monitoring tools becoming POA&M items for tracking.

#### f
##### Contractor
POA&M items are tracked by CivicActions Security through JIRA tickets with a security categorization assigned. The information included in the POA&M item include the severity, the due date, the weakness source identifier, and the plugin ID that identified the vulnerability.

#### g
##### Contractor
The security status of the system is reported up to the System Owner and Project Manager via the CivicActions Security Office to be reviewed alongside other security issues relating to the system.

#### c
##### Drupal
CivicActions works closely with the Drupal security community and reviews security announcements as part of the continuous monitoring strategy. Items found to require immediate remediation will be addressed.

##### Ilias
CivicActions works closely with the Ilias security community and reviews security announcements as part of the continuous monitoring strategy. Items found to require immediate remediation will be addressed.
#### CA-9: INTERNAL SYSTEM CONNECTIONS
```text
 - a. Authorize internal connections of [Assignment: organization-defined system components or classes of components] to the system;
 - b. Document, for each internal connection, the interface characteristics, security and privacy requirements, and the nature of the information communicated;
 - c. Terminate internal system connections after [Assignment: organization-defined conditions]; and
 - d. Review [Assignment: organization-defined frequency] the continued need for each internal connection.

```
**Status:** none
##### Contractor
Not applicable.
### CM: Configuration Management


#### CM-1: CONFIGURATION MANAGEMENT POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] configuration management policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the configuration management policy and the associated configuration management controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the configuration management policy and procedures; and
 - c. Review and update the current configuration management:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete
##### Contractor
CivicActions has developed, documented and disseminated to personnel a configuration management policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Configuration Management (CM) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.
Configuration changes are overseen by the Change Control Board (CCB) consisting of the System Owner, Project Manager, CivicActions Operations staff and the engineering team.

##### Project
The configuration management policy and procedures are formally documented in the Project Configuration Management Plan (CMP), which provides the roles and responsibilities as it pertains to physical and environmental protection. It defines responsibilities for the implementation and oversight of the guidance contained herein. Client reviews and updates the policy as necessary.

#### CM-2: BASELINE CONFIGURATION
```text
 - a. Develop, document, and maintain under configuration control, a current baseline configuration of the system; and
 - b. Review and update the baseline configuration of the system:
   - 1. [Assignment: organization-defined frequency];
   - 2. When required due to [Assignment: Assignment organization-defined circumstances]; and
   - 3. When system components are installed or upgraded.

```
**Status:** partial
##### AWS
Hardware Baselines

All hardware is maintained by the AWS cloud. The system inherits hardware configuration aspects of this control from the FedRAMP Provisional ATO granted to AWS, dated 1 May 2013, for the following: baseline configuration.

##### Contractor
A current baseline configuration is always available - stored as a tag in the Git repository - such that the site can be regenerated or rolled back should unauthorized or failing changes be applied.

##### Ilias
The baseline configuration is maintained in Git and described in the Configuration Management Plan, which describes the change workflow and software configuration. In the context of Security Configuration Management, the baseline configuration is a collection of formally approved configuration state(s) of one or more configuration items ("features") that compose the system. The baseline configuration is used to restore and serves as the basis against which the next change or set of changes to the system is made.
The features for the system are maintained in the website's source code, which is managed in Git, a source code version control system. Once the source code is updated, Git maintains the new version of staged code once committed in the Git repository as the new baseline. All code prior to it being staged is documented, tested and approved by CivicActions Development, which is described in control SA-3. The production environment is configured to take database snapshots daily.

##### Project
A CM process has been established and documented in the Project CMP. All updates are made in accordance with the procedures outlined in the CMP. The CM process establishes a baseline of hardware, software, firmware and documentation, as well as changes thereto, throughout the development and life cycle of the information system. CM ensures the control of the information system through its life cycle. It assures that additions, deletions, or changes made to the Project system do not unintentionally or unknowingly diminish security. If the change is major, the security of the system must be re-analyzed.

#### CM-4: SECURITY IMPACT ANALYSIS
```text
Analyze changes to the system to determine potential security and privacy impacts prior to change implementation.

```
**Status:** complete
##### Contractor
Security impact analysis is conducted and documented within the Change Request (CR) process described in CM-3(b). All proposed configuration- controlled changes to the application are tested first in a sandboxed development environment before being pushed to a staging environment to be tested by another developer and by the Engineering team prior to final approval from CCB to move changes to the production environment.

##### Project
An Information Security Program is in place to ensure all security-centric impacts to the Project are properly analyzed and conducted by personnel with information security responsibilities (i.e., Project SSO, IT Security Officer, etc.). These individuals have the appropriate skills and technical expertise to analyze the changes to the Project and their associated security ramifications. In support of continuous monitoring and to ensure the Project system lifecycle is fully sustained, a risk assessment process, be it formal or informal, is performed when changes are occur. This ensures that Client Full Name understands the security impacts and can determine if additional security controls are required.

#### CM-6: CONFIGURATION SETTINGS
```text
 - a. Establish and document configuration settings for components employed within the system that reflect the most restrictive mode consistent with operational requirements using [Assignment: organization-defined common secure configurations];
 - b. Implement the configuration settings;
 - c. Identify, document, and approve any deviations from established configuration settings for [Assignment: organization-defined system components] based on [Assignment: organization-defined operational requirements]; and
 - d. Monitor and control changes to the configuration settings in accordance with organizational policies and procedures.

```
**Status:** complete
#### b
##### Contractor
CivicActions developers follow security best practices according to the guidelines set by the CivicActions Security Office.

##### Project
Configuration settings are implemented, monitored, and controlled in accordance with the organizational Configuration Management Plan for the security configuration management processes and tools.

#### d
##### Contractor
All changes to the configuration settings are logged in the Git source code version control system, which records the identity of the developer who committed each change. Version control is enforced, with previous tagged code releases kept for rollback purposes.

#### a
##### Project
The Project is configured in compliance with the applicable baseline security standards. The Department and its technical support staff configure the security settings of all IT products to the most restrictive mode consistent with information system operational requirements. Project utilizes the NIST Special Publication 800-70 for guidance on configuration settings (checklists) for information technology products. When security setting checklist are not available from NIST for a particular device, good security engineering practices along with manufacture guidelines is used to develop the security settings. The CM Manager conducts configuration audits to ensure baseline compliance and documentation of hardware/software configurations throughout the system lifecycle.

#### c
##### Project
Currently, deviations do not exist for established configuration settings. In the event this changes, the following notes the process that will take place.
The CivicActions CCB, identifies, approves, and documents exceptions to mandatory configuration settings for individual components within its cloud offering only when operationally necessary. All variances identified during the monthly and annual system testing scans that must be accepted for operational purposes are tracked.

#### CM-7: LEAST FUNCTIONALITY
```text
 - a. Configure the system to provide only [Assignment: organization-defined mission essential capabilities]; and
 - b. Prohibit or restrict the use of the following functions, ports, protocols, software, and/or services: [Assignment: organization-defined prohibited or restricted functions, system ports, protocols, software, and/or services].

```
**Status:** partial
#### a
##### AWS
In this architecture, only essential capabilities for a multi-tiered web service are configured. AWS Identity and Access Management (IAM) baseline Groups and Roles are configured to support restricted access to AWS resources by privileged users and non-person entities (Amazon EC2 systems operating with a role) authorized and assigned by the organization.

##### Project
Services are limited to provide only essential capabilities.

#### b
##### AWS
In this architecture, ports, protocols, and services are restricted to those that are required for a multi-tiered web service, via AWS security group rules.

##### Project
The Project maintains strict default deny policy with access controls at the firewall, and on individual systems. Inbound access across the system boundary is only allowed on ports 22 (ssh), 80 (http) and 443 (https), with an additional port, 25 (smtp) open on the mail server.

#### CM-8: INFORMATION SYSTEM COMPONENT INVENTORY
```text
 - a. Develop and document an inventory of system components that:
   - 1. Accurately reflects the system;
   - 2. Includes all components within the system;
   - 3. Does not include duplicate accounting of components or components assigned to any other system;
   - 4. Is at the level of granularity deemed necessary for tracking and reporting; and
   - 5. Includes the following information to achieve system component accountability: [Assignment: organization-defined information deemed necessary to achieve effective system component accountability]; and
 - b. Review and update the system component inventory [Assignment: organization-defined frequency].

```
**Status:** partial
#### a
##### AWS
AWS built-in features dynamically build and maintain an inventory of system components (infrastructure inventory)

1. AWS built-in features provide an accurate, real time inventory of all infrastructure system and network components within the customer account and provides a single view for granularity for tracking and reporting.
2. AWS built-in features provide an accurate, real time inventory of all infrastructure system and network components within the AWS account, and  AWS CloudFormation creates a unique set of stack names, and associated resource names  incorporate the stack name, for tracking components deployed by CloudFormation templates that align with an authorization boundary.
3. AWS built-in features provide a level of granularity for tracking and reporting on all infrastructure system and network components and configuration settings for those components.
4. AWS built-in features provide all available information about all infrastructure system and network components to achieve effective component accountability.

#### b
##### AWS
AWS built-in features provides a dynamically updated inventory of all infrastructure system and network components within the customer account. The AWS management console and AWS API calls support the capability for the organization to review the inventory.

##### Ilias
The software inventory for the application is maintained in the codebase stored CivicActions' Git source code version control system. It consists of the following components:
- The Ilias open-source web learning management system
- Ilias add-on modules, themes, and libraries available from the Ilias.de website which extend Ilias core
- Custom code written by CivicActions' developers
The inventory is reviewed monthly by CivicActions Product Engineering teams in accordance with the Configuration Management Plan.
Website content is backed up daily using CPM snapshots. This allows CivicActions to build an inventory of the system on demand.

#### CM-10: SOFTWARE USAGE RESTRICTIONS
```text
 - a. Use software and associated documentation in accordance with contract agreements and copyright laws;
 - b. Track the use of software and associated documentation protected by quantity licenses to control copying and distribution; and
 - c. Control and document the use of peer-to-peer file sharing technology to ensure that this capability is not used for the unauthorized distribution, display, performance, or reproduction of copyrighted work.

```
**Status:** none
##### Contractor
Drupal is hosted on a LAMP platform (Linux, Apache, MySQL, and PHP). These are all compatible with the Free Software Foundation's General Public License (GPL) version 2 or later and are freely available for use under copyright law.

##### Ilias
Ilias is hosted on a LAMP platform (Linux, Apache, MySQL, and PHP). These are all compatible with the Free Software Foundation's General Public License (GPL) version 2 or later and are freely available for use under copyright law.
#### CM-11: USER-INSTALLED SOFTWARE
```text
 - a. Establish [Assignment: organization-defined policies] governing the installation of software by users;
 - b. Enforce software installation policies through the following methods: [Assignment: organization-defined methods]; and
 - c. Monitor policy compliance [Assignment: organization-defined frequency].

```
**Status:** complete
#### a
##### Contractor
All software installed in the system environment must be first approved via the CCB resulting in a Change Request (CR) being initiated and executed. Software installation on the computing nodes within the authorization boundary is restricted to administrators. All CivicActions internal administrators are informed of this during their initial training and as part of the rules of behavior document.

#### b
##### Contractor
CivicActions enforces software installation policies through required acknowledgment and sign-off on acceptable use policy by CivicActions personnel. CivicActions Development is responsible for enforcing compliance with the acceptable use policy.

#### c
##### Contractor
CivicActions monitors policy compliance continuously via the code release planning and quality control systems built into the System Development Life Cycle described in control SA-3.

### CP: Contingency Planning


#### CP-1: CONTINGENCY PLANNING POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] contingency planning policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the contingency planning policy and the associated contingency planning controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the contingency planning policy and procedures; and
 - c. Review and update the current contingency planning:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete
##### Contractor
CivicActions has developed, documented and disseminated to personnel a contingency planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in Contingency Planning (CP) Policy and Procedure that can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.

##### Project
This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

The Project and has developed a contingency planning policy consistent with NIST 800-34. Contingency planning procedures are formally documented within the Project Contingency Plan, which provides the roles and responsibilities as it pertains to contingency planning. The Project reviews and updates the policy as necessary and the policy was last updated in July 2012.

#### CP-2: CONTINGENCY PLAN
```text
 - a. Develop a contingency plan for the system that:
   - 1. Identifies essential mission and business functions and associated contingency requirements;
   - 2. Provides recovery objectives, restoration priorities, and metrics;
   - 3. Addresses contingency roles, responsibilities, assigned individuals with contact information;
   - 4. Addresses maintaining essential mission and business functions despite a system disruption, compromise, or failure;
   - 5. Addresses eventual, full system restoration without deterioration of the controls originally planned and implemented;
   - 6. Addresses the sharing of contingency information; and
   - 7. Is reviewed and approved by [Assignment: organization-defined personnel or roles];
 - b. Distribute copies of the contingency plan to [Assignment: organization-defined key contingency personnel (identified by name and/or by role) and organizational elements];
 - c. Coordinate contingency planning activities with incident handling activities;
 - d. Review the contingency plan for the system [Assignment: organization-defined frequency];
 - e. Update the contingency plan to address changes to the organization, system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing;
 - f. Communicate contingency plan changes to [Assignment: organization-defined key contingency personnel (identified by name and/or by role) and organizational elements];
 - g. Incorporate lessons learned from contingency plan testing, training, or actual contingency activities into contingency testing and training; and
 - h. Protect the contingency plan from unauthorized disclosure and modification.

```
**Status:** complete
#### a
##### Contractor
CivicActions has developed a contingency plan for that addresses:
1. Essential missions, business functions, and associated contingency requirements
2. Recovery objectives, restoration priorities, and metrics
3. Roles and responsibilities are identified in the CP and include the ISCP Director, Incident Commander (IC), CivicActions Coordinator, and CivicActions Information System Security Officer (ISSO).
4. Maintaining essential missions and business functions despite an information system disruption, compromise, or failure
5. Full information system restoration without deterioration of the security safeguards originally planned and implemented
6. The ISCP is reviewed and approved by ISCP Director, Incident Commander (IC), CivicActions ISSO and the System Owner annually.

#### b
##### Contractor
The CivicActions Information System Contingency Plan (ISCP) has been distributed to all CivicActions team members. The ISCP can be found in the CivicActions Handbook at <https://guidebook.civicactions.com/en/latest/common-practices-tools/security/contingency-plan/>.

##### Project
The Project Information System Contingency Plan (ISCP) has been distributed to all members who have roles in Contingency Planning and Incident Response Team. Direction by the System Owner will update who is required to receive a copy of the contingency plan. The ISCP can be found in the Project GitHub wiki at <https://guidebook.civicactions.com/en/latest/common-practices-tools/security/contingency-plan/>.

#### c
##### Contractor
The Information System Contingency Plan (ISCP) is closely integrated with the Incident Response Plan (IRP). Coordination is the responsibility of the ISCP Director and CivicActions Operations staff.

#### d
##### Contractor
The ISCP Director and CivicActions' Security Office are responsible to review the ISCP annually and when a change to the system occurs.

#### e
##### Contractor
CivicActions Operations staff and ISCP Director are required to update the ISCP to address changes to the organization, information system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing.

#### f
##### Contractor
The ISCP requires that changes to the plan be communicated to those on the Incident Response/Contingency Plan Contact List.

#### g
##### Contractor
The ISCP is available on CivicActions GitHub repository. This repository provides the configuration management capabilities for the ISCP to be protected from unauthorized disclosure and modification.

#### CP-3: CONTINGENCY TRAINING
```text
 - a. Provide contingency training to system users consistent with assigned roles and responsibilities:
   - 1. Within [Assignment: organization-defined time period] of assuming a contingency role or responsibility;
   - 2. When required by system changes; and
   - 3. [Assignment: organization-defined frequency] thereafter; and
 - b. Review and update contingency training content [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete
##### Contractor
The ISCP stipulates that all CivicActions system assigned roles in the Contingency Plan Team are trained in their duties within three months of first being assigned a role in the CP, and then annually thereafter or when changes are required. CivicActions uses the Contingency Plan as described in controls CP-1 and CP-2 as a basis for personnel contingency training.

#### CP-4: CONTINGENCY PLAN TESTING
```text
 - a. Test the contingency plan for the system [Assignment: organization-defined frequency] using  the following tests to determine the effectiveness of the plan and the readiness to execute the plan: [Assignment: organization-defined tests].
 - b. Review the contingency plan test results; and
 - c. Initiate corrective actions, if needed.

```
**Status:** complete
##### Contractor
Real-world tests of the contingency plan will be held at least annually, with supplemental tests (checklist/table-top) as needed for specific scenarios. The ISCP Coordinator is responsible to facilitate annual testing exercises. The testing process for the ISCP includes a review of the ISCP, exercise, and identification of corrective actions and other improvements.

#### CP-9: INFORMATION SYSTEM BACKUP
```text
 - a. Conduct backups of user-level information contained in [Assignment: organization-defined system components]
                  [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives];
 - b. Conduct backups of system-level information contained in the system [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives];
 - c. Conduct backups of system documentation, including security- and privacy-related documentation [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives]; and
 - d. Protect the confidentiality, integrity, and availability of backup information.

```
**Status:** partial
#### a
##### AWS
In this architecture, user data is limited to that which is stored in the Amazon RDS database. Amazon RDS is fully backed up by a daily snapshot as well as through transaction logging conducted by AWS as part of this managed service. Full database recovery from snapshot or point-in-time can be initiated from the Amazon RDS console/API.

##### Contractor
CivicActions conducts system user-level information backup in accordance with requirements (at a minimum, incremental backups must be conducted at least weekly and full backups must be conducted at least monthly).

#### b
##### AWS
AWS built-in features automatically backs up system-level information limited to infrastructure CONFIGURATION information within the AWS account. While individual running Amazon EC2 instances and attached EBS volumes are NOT backed up, they can be reconstituted from Amazon Machine Images (AMIs) provided by AWS (which are backed up by AWS) and user data scripts included in CloudFormation templates. Once deployed, the CloudFormation template contents are backed up by AWS R488within the CloudFormation service. These AWS backups of AWS services are transparent to the customer as part of AWS backend processes.

##### Contractor
System-level information for the application is replicated and backed up in the same way as user-level information as defined in CP-9(a).

#### c
##### AWS
AWS built-in features back up online administrator and developer documentation, limited to that which is published at https://aws.amazon.com/documentation.

##### Contractor
System documentation is backed up from the GitHub repository on a daily basis with a minimum two-week retention period and off-site storage.

#### d
##### AWS
AWS built-in features protect the confidentiality, integrity, and availability of information that AWS services back up. This information includes the service configuration information within an account, AWS online administrator and developer documentation, and AWS CloudFormation stacks for templates once deployed into an account. R612

##### Contractor
CivicActions employees must authenticate prior to being granted access to the GitHub repository. Roles and responsibilities within GitHub determine the proper level of access for the documentation being accessed. The folder structure of GitHub protects though permissions and ownership prohibiting users from accessing unauthorized documentation.

#### CP-10: INFORMATION SYSTEM RECOVERY AND RECONSTITUTION
```text
Provide for the recovery and reconstitution of the system to a known state within [Assignment: organization-defined time period consistent with recovery time and recovery point objectives] after a disruption, compromise, or failure.

```
**Status:** complete
##### Contractor
The Contingency Plan documents the mechanisms with supporting procedures that allow all system components to be recovered and reconstituted to the system’s original state after a disruption or failure. This original state means that all system parameters (either default or organization- established) are reset, patches are reinstalled, system and security configuration settings are reestablished, system documentation and operating procedures are available, application and system software is reinstalled, information from the most recent backups is available and the system is fully tested.

### IA: Identification and Authentication


#### IA-1: IDENTIFICATION AND AUTHENTICATION POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] identification and authentication policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the identification and authentication policy and the associated identification and authentication controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the identification and authentication policy and procedures; and
 - c. Review and update the current identification and authentication:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete
##### Contractor
CivicActions has developed, documented and disseminated to personnel an identification and authentication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained by the CivicActions Identification and Authentication (IA) Policy. This document can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs>.

##### Project
The Project system owners/managers manage user identifiers by: (i) uniquely identifying each user; (ii) verifying the identity of each user; (iii) receiving authorization to issue a user identifier from an appropriate official; (iv) ensuring that the user identifier is issued to the intended party; (v) disabling user identifier after a reasonable period of inactivity as documented in its security procedures; and (vi) archiving user identifiers. Project reviews and updates this policy as necessary.

#### IA-2: IDENTIFICATION AND AUTHENTICATION (ORGANIZATIONAL USERS)
```text
Uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users.

```
**Status:** partial
##### AWS
AWS built-in features of Identity and Access Management (IAM) provides the capability for uniquely identifying and authenticating users and processes acting on their behalf to both organizational and non-organizational users operating within the AWS account and infrastructure, providing privileges based on the credentials, group memberships, and access policies assigned to them. The customer organization, at its discretion, provides individual user accounts and privileges to both organizational non-organizational users in addition to organizational users.

#### IA-2 (1): NETWORK ACCESS TO PRIVILEGED ACCOUNTS
```text
Implement multi-factor authentication for access to privileged accounts.

```
**Status:** complete
##### Contractor
CivicActions system administrators employ a personal public- key pair for basic access and must originate from a whitelisted IP address. The whitelist is maintained by an Ansible inventory file, the current complete list (includes dev sites) of users with whitelisted IPs is in artifact: None

To access root (sudo) privileges an additional password is required. The passwords are maintained in encrypted form in the Ansible inventory file. The mechanism to enable select users to use a password to obtain root access can be viewed in artifact: None

##### Drupal
Drupal administrators and other roles with unrestricted access to live content and/or user accounts are required to use two-factor authentication. See artifact None

##### Project
The Project employs multi-factor authentication for privileged users.

#### IA-2 (12): ACCEPTANCE OF PIV CREDENTIALS
```text
Accept and electronically verify Personal Identity Verification-compliant credentials.

```
**Status:** none
##### Project
The Project system allows users to access the system using Common Access Cards (CAC).

#### IA-4: IDENTIFIER MANAGEMENT
```text
Manage system identifiers by:
 - a. Receiving authorization from [Assignment: organization-defined personnel or roles] to assign an individual, group, role, service, or device identifier;
 - b. Selecting an identifier that identifies an individual, group, role, service, or device;
 - c. Assigning the identifier to the intended individual, group, role, service, or device; and
 - d. Preventing reuse of identifiers for [Assignment: organization-defined time period].

```
**Status:** partial
#### a
##### Contractor
Access to the system is authorized by the System Owner or Project Manager for each role as described in AC-2.

##### Drupal
Upon account creation, the Drupal software assigns each user account a unique numerical user ID (UID). This UID is used internally by the system to track user actions such as content creation or editing. The numerical user IDs are never reused even if their user accounts are subsequently blocked or deleted.

##### Ilias
Upon account creation, the Ilias software assigns each user account a unique numerical user ID (UID). This UID is used internally by the system to track user actions such as content creation or editing. The numerical user IDs are never reused even if their user accounts are subsequently blocked or deleted.
#### b
##### Contractor
User accounts are assigned a unique identifier in the form of a unique username, password and email address based on the system for allocating user accounts described in AC-2.

In accordance with CivicActions Identification and Authentication (IA) Policy outlined at <https://github.com/CivicActions/compliance-docs>, CivicActions internal users are uniquely identified by the creation of an organizational account with a username based on each user's first and last names.

##### Drupal
When Drupal user accounts are created, users' email addresses are verified by sending a single-use activation link to the user’s mailbox. The email recipient then uses the activation link to log in to the website and supply a password which must meet the system's password complexity requirements.

##### Ilias
When Ilias user accounts are created, users' email addresses are verified by sending a single-use activation link to the user’s mailbox. The email recipient then uses the activation link to log in to the website and supply a password which must meet the system's password complexity requirements.
#### c
##### Contractor
User accounts are assigned a unique identifier in the form of a unique username, password and email address based on the system for allocating user accounts described in AC-2.

##### Drupal
Identifiers for CivicActions internal personnel include a username based on the individual's full first and last name and are reviewed for uniqueness by the admin group when it approves the creation of the user account.

##### Ilias
Identifiers for CivicActions internal personnel include a username based on the individual's full first and last name and are reviewed for uniqueness by the admin group when it approves the creation of the user account.
#### d
##### Contractor
Account usernames may not be re-used for at least two years.
##### Drupal
Drupal user's unique identifier (the numeric user ID, or UID) is never reused.
##### Ilias
Ilias user's unique identifier (the numeric user ID, or UID) is never reused.
#### e
##### Contractor
All user accounts are required to change their passwords every 90 days. The website will automatically block the accounts of users who fail to change their password within that time period, after which the account may only be unblocked by a website Administrator or CivicActions Operations staff.

#### IA-5: AUTHENTICATOR MANAGEMENT
```text
Manage system authenticators by:
 - a. Verifying, as part of the initial authenticator distribution, the identity of the individual, group, role, service, or device receiving the authenticator;
 - b. Establishing initial authenticator content for any authenticators issued by the organization;
 - c. Ensuring that authenticators have sufficient strength of mechanism for their intended use;
 - d. Establishing and implementing administrative procedures for initial authenticator distribution, for lost or compromised or damaged authenticators, and for revoking authenticators;
 - e. Changing default authenticators prior to first use;
 - f. Changing or refreshing authenticators [Assignment: organization-defined time period by authenticator type] or when [Assignment: organization-defined events] occur;
 - g. Protecting authenticator content from unauthorized disclosure and modification;
 - h. Requiring individuals to take, and having devices implement, specific controls to protect authenticators; and
 - i. Changing authenticators for group or role accounts when membership to those accounts changes.

```
**Status:** complete
#### i
##### Contractor
CivicActions users are required to take appropriate measures in the handling of passwords including:

- Not transmitting user names and passwords together in an unencrypted format
- Not permitting the sending of passwords in an unencrypted format via email
- Not listing passwords in tickets
- Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.

##### Drupal
Drupal users are required to take appropriate measures in the handling of passwords including:

- Not transmitting user names and passwords together in an unencrypted format
- Not permitting the sending of passwords in an unencrypted format via email
- Not listing passwords in tickets
- Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.

##### Ilias
Ilias users are required to take appropriate measures in the handling of passwords including:
- Not transmitting user names and passwords together in an unencrypted format
- Not permitting the sending of passwords in an unencrypted format via email
- Not listing passwords in tickets
- Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.

#### a
##### Drupal
Refer to control AC-2 in this SSP for further details on account provisioning.
CivicActions will create and maintain an initial Drupal Administrator (highest level of Drupal Account). New Administrators are able to provide additional Administrator access at their own discretion and are ultimately responsible for managing their own Administrator and other user accounts that they create.

##### Ilias
Refer to control AC-2 in this SSP for further details on account provisioning.
CivicActions will create and maintain an initial Ilias Administrator (highest level of Ilias Account). New Administrators are able to provide additional Administrator access at their own discretion and are ultimately responsible for managing their own Administrator and other user accounts that they create.

##### Project
Authentication for Project internal personnel are created during the personnel assignment process where requests are made to the Project admin group for proper access levels. The Project admin group verifies the identity of the user. The website performs further verification by sending an email to the user's mailbox containing a single-use activation link which must be used to log in to the account for the first time and to create a password.

#### b
##### Drupal
Initial authenticator content (a unique email address – not previously used in any other account) is provided by the user. Internal initial password requirements set by CivicActions Operations and ongoing password refreshes by internal users follow the requirements set in the Identification and Authentication Policy.

##### Ilias
Initial authenticator content (a unique email address – not previously used in any other account) is provided by the user. Internal initial password requirements set by CivicActions Operations and ongoing password refreshes by internal users follow the requirements set in the Identification and Authentication Policy.
##### Project
Project admins in collaboration with CivicActions Operations are responsible for provisioning and de-provisioning end user accounts in compliance with the authentication requirements described herein.

#### c
##### Drupal
The system partially inherits this control from Drupal standard password strength mechanisms.
##### Ilias
The system partially inherits this control from Ilias standard password strength mechanisms.
##### Project
When entering a user account password upon initial login, all users must comply with the following password policies, which are enforced by the website's software configuration:

- Password must be at least 14 characters in length.
- Password must contain at least one digit.
- Password must contain at least one special character (not whitespace or an alphanumeric).
- Password must contain at least one uppercase character.
- Password must contain at least one lowercase character.

#### d
##### Drupal
The system partially inherits this control from Drupal standard password management. All password creation/change/reset operations are recorded in the website's "Drupal Watchdog" logs.

##### Ilias
The system partially inherits this control from Ilias standard password management.
All password creation/change/reset operations are recorded in the website's Ilias logs.

##### Project
Project is responsible for provisioning and de-provisioning end user accounts, which must comply with the strict password policies that are enforced by the website's software configuration, as described in IA-5(d).

In accordance with Project site configuration, the following administrative procedures exist for initial authenticator distribution, for lost/compromised/damaged authenticators, and for revoking authenticators.

- Initial authenticator distribution: Users receive a one-time login link
  by email upon creating of their user account. They use that link to log
  in and then must enter a password themselves which complies with the
  password complexity requirements described in IA-4(b).

- Lost/compromised/damaged authenticators: Users who have forgotten their
  password may request a new password by submitting their username or
  email address. The website responds by emailing a one-time login link
  to the user's email address. After using the link to log in, the user
  is required to enter a new password.

- Revoking authenticators: Users who have not changed their password in
  the last 90 days are automatically blocked. Administrators may block
  any user account if they believe there is a reason to do so.

#### e
##### Drupal
Drupal requires users to change their password upon initial login, and the application website enforces this. Each user account is assigned a default password that is randomly generated, not possible to guess, and not shared with anyone, including site administrators. When the user logs in and creates a new password, the default password is erased from the website database.

##### Ilias
Ilias requires users to change their password upon initial login, and the application website enforces this. Each user account is assigned a default password that is randomly generated, not possible to guess, and not shared with anyone, including site administrators. When the user logs in and creates a new password, the default password is erased from the website database.
#### h
##### Drupal
For all Drupal users, passwords are protected by the website's software, which only stores an encrypted string based on the password. This means that even if the website's database should be compromised, an attacker would still be unable to know users' actual passwords. Internal users receive training in security awareness and acceptable use and are instructed never to reveal their passwords to anyone.

##### Ilias
For all Ilias users, passwords are protected by the website's software, which only stores an encrypted string based on the password. This means that even if the website's database should be compromised, an attacker would still be unable to know users' actual passwords. Internal users receive training in security awareness and acceptable use and are instructed never to reveal their passwords to anyone.
#### j
##### Drupal
This control is not applicable due to the fact that group accounts are not created within the Drupal application per IA Policy.
##### Ilias
This control is not applicable due to the fact that group accounts are not created within the Ilias application per IA Policy.
#### f
##### Project
Project authenticators follow these password lifetime restrictions:

- Maximum password age = 90
- Minimum password age = 1
- Password reuse restriction = 10

#### g
##### Project
Project enforces password lifetime restrictions. The password lifetime settings for internal accounts is as follows:

- Minimum restriction of zero (1) days and
- Maximum restriction of ninety (90) days before a password change is required.

#### IA-5 (1): PASSWORD-BASED AUTHENTICATION
```text
For password-based authentication:
 - (a) Maintain a list of commonly-used, expected, or compromised passwords and update the list [Assignment: organization-defined frequency] and when organizational passwords are suspected to have been compromised directly or indirectly;
 - (b) Verify, when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5(1)(a);
 - (c) Transmit passwords only over cryptographically-protected channels;
 - (d) Store passwords using an approved salted key derivation function, preferably using a keyed hash;
 - (e) Require immediate selection of a new password upon account recovery;
 - (f) Allow user selection of long passwords and passphrases, including spaces and all printable characters;
 - (g) Employ automated tools to assist the user in selecting strong password authenticators; and
 - (h) Enforce the following composition and complexity rules: [Assignment: organization-defined composition and complexity rules].

```
**Status:** partial
#### a
##### AWS
AWS built-in features of Identity and Access Management (IAM) provides minimum password complexity enforcement, but the characteristics to enforce must be manually configured by the customer. Refer to http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html

##### Drupal
Drupal supports the requirement for password-based authentication complexity. New users of Drupal are required to specify their password authentication as soon as they log in to the website for the first. The website requires all submitted passwords to comply with validation rules, as described above in IA-5(c).
Changing password lifetime, length, reuse or strength requirements requires a code setting change that therefore needs to be planned and approved by CivicActions Change Control Board before being implemented.

##### Ilias
Ilias supports the requirement for password-based authentication complexity. New users of Ilias are required to specify their password authentication as soon as they log in to the website for the first. The website requires all submitted passwords to comply with validation rules, as described above in IA-5(c).
Changing password lifetime, length, reuse or strength requirements requires a code setting change that therefore needs to be planned and approved by {'name': 'CivicActions, Inc', 'name_short': 'CivicActions', 'address': {'street': '3527 Mt Diablo Blvd, Unit 269', 'city': 'Lafayette', 'state': 'CA', 'zip': 94549, 'country': None}, 'phone': '510-408-7510', 'website': 'www.civicactions.com', 'compliance_docs_url': 'https://github.com/CivicActions/compliance-docs', 'email_support': 'support@civicactions.com', 'security_policy_url': 'https://github.com/CivicActions/security-policy'}' Change Control Board before being implemented.

#### c
##### AWS
AWS built-in features of AWS Identity and Access Management (IAM) and the AWS Console store passwords on AWS systems in a cryptographically-protected format and only support TLS connectivity to the console web site to protect passwords in transit via encryption.

##### Drupal
All Drupal passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.

##### Ilias
All Ilias passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.
#### f
##### AWS
AWS built-in features of AWS Identity and Access Management (IAM) provides the capability to require new password to be entered upon login. The customer organization, at its discretion, configures IAM to enforce that requirement.

##### Drupal
When website users request a password reset, the website sends a temporary login link to the email address associated with their user account. After a user logs in via the temporary login link, the website requires the user to enter a new password before proceeding further.

##### Ilias
When website users request a password reset, the website sends a temporary login link to the email address associated with their user account. After a user logs in via the temporary login link, the website requires the user to enter a new password before proceeding further.
#### b
##### Drupal
When required to change passwords, Drupal users are required to change their authenticator password by changing at least one character. Enforcement of this control is implemented through the website's software configuration.

##### Ilias
When required to change passwords, Ilias users are required to change their authenticator password by changing at least one character. Enforcement of this control is implemented through the website's software configuration.
#### d
##### Drupal
The website requires all submitted passwords to comply with lifetime rules, as described above in IA-5(g).
##### Ilias
The website requires all submitted passwords to comply with lifetime rules, as described above in IA-5(g).
#### e
##### Drupal
Password reuse is limited through software configuration.
##### Ilias
Password reuse is limited through software configuration.
##### Project
Project is responsible for provisioning and de-provisioning end user accounts, which must comply with the strict password policies that are enforced by the website's software configuration, as described in IA-5.

#### IA-5 (11): HARDWARE TOKEN-BASED AUTHENTICATION
```text

```
**Status:** partial
##### AWS
AWS built-in features of AWS Identity and Access Management (IAM) provides the capability for Hardware MFA using Gemalto SafeNet IDProve 100 and 700 OTP Tokens which are compliant to OATH open standard (time based - 6 digits) Expected battery life is 3-5 years or approximately 15,000 - 20,000 clicks. These products are handheld devices that provide strong authentication by generating a unique password that is valid for only one attempt and for 30 seconds.

It is the customer organization's responsibility to implement Hardware MFA. Refer to http://aws.amazon.com/iam/details/mfa/ and http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html

##### Project
Project does not support physical hardware token-based authentication. Therefore this control is Not Applicable.

#### IA-6: AUTHENTICATOR FEEDBACK
```text
Obscure feedback of authentication information during the authentication process to protect the information from possible exploitation and use by unauthorized individuals.

```
**Status:** partial
##### AWS
In this architecture, All Amazon EC2 instances (bastion host, web/proxy servers, application servers) employ SSH for interactive login, and when a key passphrase is prompted for, the SSH prompting mechanism obscures the feedback by default.

AWS built-in features obscure keystroke feedback for password input during AWS console login with AWS Identity and Access Management (IAM) user credentials, and when the CloudFormation console prompts for an initial database password during Quick Start template deployment.

##### Drupal
Feedback of authentication information is obscured during the authentication process into the Drupal application by displaying “dots” in the place of a password, as is standard for web-based applications. In transmission, passwords are encrypted using SSL via HTTPS.

##### Ilias
Feedback of authentication information is obscured during the authentication process into the Ilias application by displaying “dots” in the place of a password, as is standard for web-based applications. In transmission, passwords are encrypted using SSL via HTTPS.
#### IA-7: CRYPTOGRAPHIC MODULE AUTHENTICATION
```text
Implement mechanisms for authentication to a cryptographic module that meet the requirements of applicable laws, executive orders, directives, policies, regulations, standards, and guidelines for such authentication.

```
**Status:** partial
##### AWS
AWS built-in features of AWS Identity and Access Management (IAM) authentication employs cryptographic modules that meet requirements as specified and assessed in the AWS FedRAMP authorization package.

##### Drupal
All Drupal passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. SHA-512 is an approved security function under FIPS PUB 140-2. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.

##### Ilias
All Ilias passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. SHA-512 is an approved security function under FIPS PUB 140-2. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.
#### j
##### Contractor
CivicActions systems employ authentication methods consistent with NIST FIPS 140-2 requirements. General public access to system web pages does not require cryptographic authentication. Privileged users accessing systems use the public-key cryptographic functionality of Secure Shell (SSH) to encrypt the exchange of information (including the password) between the remote user and the server. Where Transport Layer Security (TLS, aka SSL) is used, cryptographic modules will be configured in accordance with FIPS 140-2.

#### IA-8: IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS)
```text
Uniquely identify and authenticate non-organizational users or processes acting on behalf of non-organizational users.

```
**Status:** partial
##### AWS
AWS built-in features of AWS Identity and Access Management (IAM) provide the capability for uniquely identifying and authenticating users and processes acting on their behalf to both organizational and non-organizational users, providing privileges based on the credentials, group memberships, and access policies assigned to them.

The customer organization at its discretion provides user accounts and privileges to both organizational non-organizational users in addition to organizational users.

#### IA-8 (1): ACCEPTANCE OF PIV CREDENTIALS FROM OTHER AGENCIES
```text
Accept and electronically verify Personal Identity Verification-compliant credentials from other federal agencies.

```
**Status:** none
##### Project
Project allows the use of customer agency supplied Common Access Cards (CAC).

#### IA-8 (2): ACCEPTANCE OF THIRD-PARTY CREDENTIALS
```text
 - (a) Accept only external authenticators that are NIST-compliant; and
 - (b) Document and maintain a list of accepted external authenticators.

```
**Status:** none
##### Project
Project does not utilize FICAM approved credentials.

#### IA-8 (3): USE OF FICAM-APPROVED PRODUCTS
```text

```
**Status:** none
##### Project
Project does not utilize FICAM approved products.

#### IA-8 (4): USE OF FICAM-ISSUED PROFILES
```text
Conform to the following profiles for identity management [Assignment: organization-defined identity management profiles].

```
**Status:** none
##### Project
CivicActions does not utilize FICAM approved products or profiles.

### IR: Incident Response


#### IR-1: INCIDENT RESPONSE POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] incident response policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the incident response policy and the associated incident response controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the incident response policy and procedures; and
 - c. Review and update the current incident response:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.

##### Contractor
CivicActions has developed, documented and disseminated to personnel an incident response planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in Incident Response (IR) Policy and Procedure that can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.

##### Project
This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

The Project maintains an Incident Response Plan (IRP), consistent with NIST 800-61, which addresses purpose, scope, roles, and responsibilities. The incident response procedures address any activity or occurrence that compromises the integrity of a system, denies access to or use of IT resources, and compromises the sensitivity of the information stored in, processed by or transmitted by a system.

Additionally, the IRP includes procedures to respond to waste, fraud, misuse, or abuse of any departmental IT system, damage or loss of software or data contained in any system, Use of unlicensed (pirated) software products, discovery of hardware or software vulnerabilities

The Project Incident Response Plan can be found in the CivicActions GitHub repository at <https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>

#### IR-2: INCIDENT RESPONSE TRAINING
```text
 - a. Provide incident response training to system users consistent with assigned roles and responsibilities:
   - 1. Within [Assignment: organization-defined time period] of assuming an incident response role or responsibility or acquiring system access;
   - 2. When required by system changes; and
   - 3. [Assignment: organization-defined frequency] thereafter; and
 - b. Review and update incident response training content [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident response training.

##### Contractor
All CivicActions employees are required to participate in incident response training, as required by Incident Response Plan changes, and annually. The CivicActions Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) is the basis for the training and the incident response workflow created by the Security Office. Upon a review of past incidents, the training is updated to ensure processes and workflows are updated.

##### Project
CivicActions Operations and users of the Project system with incident response responsibilities are required to participate in incident response training once the role is assumed within 10 days, as required by Project changes, and annually. The Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) is the basis for the training and the incident response workflow created by the Security team. Upon a review of past incidents, the training is updated to ensure processes and workflows are updated.

#### IR-4: INCIDENT HANDLING
```text
 - a. Implement an incident handling capability for incidents that is consistent with the incident response plan and includes preparation, detection and analysis, containment, eradication, and recovery;
 - b. Coordinate incident handling activities with contingency planning activities;
 - c. Incorporate lessons learned from ongoing incident handling activities into incident response procedures, training, and testing, and implement the resulting changes accordingly; and
 - d. Ensure the rigor, intensity, scope, and results of incident handling activities are comparable and predictable across the organization.

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident handling.

##### Project
The Client Computer Security Officer (CSO) handles all incidents for the Project Full Name.

The Client Full Name utilizes proven incident handling methodologies for security incidents that includes preparation, detection and analysis, containment, eradication, and recovery. Client Full Name maintains a list of lessons learned from ongoing incident handling activities and uses those lessons to update the incident response procedures accordingly.

Preparation activities includes all CivicActions and Project internal users are trained if their role includes incident response. Detection monitoring tools providing notification to incident response personnel for analysis and action. Containment, eradication and recovery activities include AWS and LAMP-stack inherited fixes and Project system administrators adjusting IP port blocking security groups and SELinux policies.

#### a
##### Contractor
CivicActions has implemented an Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) that explains the process for incident handling and discusses preparation, detection and analysis, containment, eradication, and recovery.
Preparation activities include all CivicActions team members who are trained in incident response. Detection and monitoring tools providing notification to incident response personnel for analysis and action.

#### b
##### Contractor
CivicActions' Operations staff and Security Office team members are members of the CivicActions Contingency and Incident Response Plan teams which coordinates activities accordingly through the life of the incident event.

#### c
##### Contractor
The CivicActions Operations staff and Security Office conduct a post-incident analysis to assist in documenting lessons learned and suggesting changes to improve the incident response process. Tickets created in response to the incident event are reviewed upon completion by the Operations staff and Security Office. Changes to the Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) require a team review session for approval.

#### IR-5: INCIDENT MONITORING
```text
Track and document incidents.

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident monitoring.

##### Contractor
CivicActions utilizes the JIRA ticketing tool for tracking and reporting of incident events from reporting to resolution and post- incident analysis. Initial reporting can come from continuous monitoring tools as well as client and public submissions made to support@civicactions.com. Jira processes the tickets for the public submissions and the CivicActions Support Team creates associated GitHub Issues. Internal incidents reported are processed within the GitHub Issue queue. Details of the handling procedures are included in the CivicActions Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan//#response-process>) Response Process.

##### Project
The Project utilizes network and host-based intrusion detection systems, monitoring the system and application logs for anomalous events. Incidents are tracked using the same ticketing system that is used to track all system-related changes and events.

#### IR-6: INCIDENT REPORTING
```text
 - a. Require personnel to report suspected incidents to the organizational incident response capability within [Assignment: organization-defined time period]; and
 - b. Report incident information to [Assignment: organization-defined authorities].

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident reporting.

##### Project
If an incident involves suspicious activity, CivicActions Operations will contact the Project System Owner who may then contact the Project CSO.

The CivicActions Computer Security Officer (CSO) handles all incidents for the Project. The CSO is prepared to report all incidents to the Client Full Name.

#### a
##### Contractor
CivicActions personnel, as soon as an incident event is detected and/or communicated, are required to report the incident event to the CivicActions Security Office. Methods of detection and/or communication may include one or more of:

- Through continuous monitoring tools (StatusCake, OSSEC, others).
- As a result of application notifications where CivicActions Security receives notifications (AIDE, OpsGenie, others).
- Event logging described in AC-2
- Host-based alerts from the cloud infrastructure or platform.

#### b
##### Contractor
CivicActions personnel, as soon as the incident event is detected and/or communicated, are required to report the incident event to the CivicActions Security Office.

#### IR-7: INCIDENT RESONSE ASSISTANCE
```text
Provide an incident response support resource, integral to the organizational incident response capability, that offers advice and assistance to users of the system for the handling and reporting of incidents.

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident resonse assistance.

##### Contractor
CivicActions Help Desk team provides first response assistance to any users of the system. Response time for external reporting of incidents through e-mail is one business day. Internal users are able to request support thought the same process or initiate the incident response workflow. Tickets created in the Jira (customer ticketing system) and GitLab (internal ticketing system) documents all details related to the incident to assist the Incident Response Teams in handling the incident.

#### IR-8: INCIDENT RESPONSE PLAN
```text
 - a. Develop an incident response plan that:
   - 1. Provides the organization with a roadmap for implementing its incident response capability;
   - 2. Describes the structure and organization of the incident response capability;
   - 3. Provides a high-level approach for how the incident response capability fits into the overall organization;
   - 4. Meets the unique requirements of the organization, which relate to mission, size, structure, and functions;
   - 5. Defines reportable incidents;
   - 6. Provides metrics for measuring the incident response capability within the organization;
   - 7. Defines the resources and management support needed to effectively maintain and mature an incident response capability;
   - 8. Addresses the sharing of incident information;
   - 9. Is reviewed and approved by [Assignment: organization-defined personnel or roles]
                     [Assignment: organization-defined frequency]; and
   - 10. Explicitly designates responsibility for incident response to [Assignment: organization-defined entities, personnel, or roles].
 - b. Distribute copies of the incident response plan to [Assignment: organization-defined incident response personnel (identified by name and/or by role) and organizational elements];
 - c. Update the incident response plan to address system and organizational changes or problems encountered during plan implementation, execution, or testing;
 - d. Communicate incident response plan changes to [Assignment: organization-defined incident response personnel (identified by name and/or by role) and organizational elements]; and
 - e. Protect the incident response plan from unauthorized disclosure and modification.

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident response plan.

##### Project
The Project Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) includes a comprehensive incident response program, which details the implementation of procedures and tools required for incident handling. The incident response program details the roles and responsibilities of Project/ CivicActions IR Team. The IR Team includes members from CivicActions Security and Operations teams. Incident response plays a pivotal role in monitoring, detecting and handling security incidents of the entire information system. The IRP details categorization of incidents in accordance with NIST 800-61 and accordingly documents and reports incidents. The IRP is reviewed annually and updated as needed by ISSO, with the assistance of the Incident Response Team.

#### a
##### Contractor
Incident response plays a pivotal role in monitoring, detecting and handling security incidents of the entire information system. CivicActions has developed an Incident Response Plan (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>) that:

1. Provides CivicActions with procedures and tools required for incident handling;
2. Describes the structure and organization of the incident response capability;
3. Provides a high-level approach for how the incident response capability fits into CivicActions and the systems it maintains;
4. Meets the mission, size, structure, and functions of CivicActions;
5. Defines reportable incidents;
6. Provides metrics for measuring the incident response capability and details categorization of incidents in accordance with NIST 800-61;
7. Defines the roles and responsibilities of CivicActions IR Team;
8. Is reviewed annually and updated as needed by the CivicActions Security Office, with the assistance of the Incident Response Team.

#### b
##### Contractor
The CivicActions Incident Response Plan is distributed to all CivicActions team members as part of the CivicActions Handbook (<https://guidebook.civicactions.com/en/latest/common-practices-tools/security/incident-response-plan/>).
 The Incident Response Team includes members from the Security Office,
 Operations staff, and Drupal Engineering teams.

#### c
##### Contractor
The CivicActions Security Office and the Incident Response team is responsible for reviewing the Incident Response Plan annually. The entire Incident Response Team will review the plan and update it as necessary. Ultimately, the Security Office has the final say and will approve all updates to the plan.

#### d
##### Contractor
The CivicActions Security Office is responsible for managing the IR Plan, including annual reviews and updates. The IR Plan is updated to reflect any changes to processes, systems or applications. In addition, any concerns or difficulties encountered during IR Plan implementation, execution, or testing are addressed in an update to the IR Plan.

#### e
##### Contractor
Modifications to the IR Plan are conducted by the IR team the (CivicActions Security Office, Operations staff and Engineering teams) and communicated to the CivicActions team.

#### f
##### Contractor
The IR Plan is available in the CivicActions Handbook and is maintained in the CivicActions GitHub repository. GitHub provides the configuration management capabilities for the IR Plan to be protected from unauthorized disclosure and modification.

### MA: Maintenance


#### MA-1: SYSTEM MAINTENANCE POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] maintenance policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the maintenance policy and the associated maintenance controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the maintenance policy and procedures; and
 - c. Review and update the current maintenance:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete
##### AWS
This System Maintenance control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

##### Contractor
CivicActions has developed, documented and disseminated to personnel a system maintenance policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Maintenance (MA) Policy and Procedure document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs>.

##### Project
System maintenance policy and procedures are formally documented in the Project SSP, which provides the roles and responsibilities as it pertains to software and systems maintenance and updates. The Project Full Name ensures that maintenance controls are developed, disseminated, reviewed, and updated as necessary.

Physical and environmental protection is fully inherited from the AWS FedRAMP certified us-east cloud.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

#### MA-2: CONTROLLED MAINTENANCE
```text
 - a. Schedule, document, and review records of maintenance, repair, and replacement on system components in accordance with manufacturer or vendor specifications and/or organizational requirements;
 - b. Approve and monitor all maintenance activities, whether performed on site or remotely and whether the system or system components are serviced on site or removed to another location;
 - c. Require that [Assignment: organization-defined personnel or roles] explicitly approve the removal of the system or system components from organizational facilities for off-site maintenance, repair, or replacement;
 - d. Sanitize equipment to remove the following information from associated media prior to removal from organizational facilities for off-site maintenance, repair, or replacement: [Assignment: organization-defined information];
 - e. Check all potentially impacted controls to verify that the controls are still functioning properly following maintenance, repair, or replacement actions; and
 - f. Include the following information in organizational maintenance records: [Assignment: organization-defined information].

```
**Status:** complete
##### AWS
This System Maintenance control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

##### Project
The Project schedules, performs, and documents regular maintenance on the software components of all systems, including but not limited to:

- Hourly automated snapshot backups
- Daily disaster recovery remote backups
- Daily Intrusion Detection (OSSEC) / Data Integrity Assurance (AIDE)
- As needed help desk support
- Twice-monthly OS updates/patches

#### MA-4: NON-LOCAL MAINTENANCE
```text
 - a. Approve and monitor nonlocal maintenance and diagnostic activities;
 - b. Allow the use of nonlocal maintenance and diagnostic tools only as consistent with organizational policy and documented in the security plan for the system;
 - c. Employ strong authentication in the establishment of nonlocal maintenance and diagnostic sessions;
 - d. Maintain records for nonlocal maintenance and diagnostic activities; and
 - e. Terminate session and network connections when nonlocal maintenance is completed.

```
**Status:** complete
##### AWS
This System Maintenance control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### a
##### Contractor
System maintenance is done from remote sites as there is no direct access to the server instances in the AWS cloud; this is the government-approved method of doing business. Approval, QA, and monitoring are conducted by the team performing the specific maintenance.

#### b
##### Contractor
Remote diagnostics tools, such as OSSEC, AIDE, fail2ban, and OpenSCAP are used to verify the integrity of files, perform log analysis, monitor login attempts and check for rootkits and other vulnerabilities.

#### c
##### Contractor
All nonlocal maintenance requires the same authentication requirements to perform the maintenance activities to access the system as defined in controls AC-3 and IA-2. SSH is used to secure all communications between the remote user and the components located in the AWS cloud.

#### d
##### Contractor
CivicActions records for nonlocal maintenance is managed through JIRA tickets and the Git issue queue as well as normal system logs. CivicActions administrator activity to the system is also logged through the implementation of the AU-2 (Audit Events) and AU-3 (Content of Audit Records).

#### e
##### Contractor
Any session for internal maintenance activities is terminated when the user completes their session, disconnects from the system, or logs out. In addition, sessions are terminated after 15 minutes of inactivity.

#### MA-5: MAINTENANCE PERSONNEL
```text
 - a. Establish a process for maintenance personnel authorization and maintain a list of authorized maintenance organizations or personnel;
 - b. Verify that non-escorted personnel performing maintenance on the system possess the required access authorizations; and
 - c. Designate organizational personnel with required access authorizations and technical competence to supervise the maintenance activities of personnel who do not possess the required access authorizations.

```
**Status:** complete
##### AWS
This System Maintenance control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

##### Contractor
Maintenance of the system and applications can only be performed by personnel designated as having internal administrator privileges and responsibilities. Access rights for the internal administrators are assigned and granted access to perform their specific job responsibilities. All physical maintenance requirements are inherited from AWS.

##### Project
Client maintains a list of authorized contract (CivicActions) personnel who perform maintenance and repair activities on the Project Project system components, and only these authorized personnel may perform the maintenance. All maintenance personnel have the required personnel security elements in place.

### MP: Media Protection


#### MP-1: MEDIA PROTECTION POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] media protection policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the media protection policy and the associated media protection controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the media protection policy and procedures; and
 - c. Review and update the current media protection:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete
##### AWS
This Media Protection control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

##### Contractor
CivicActions has developed, documented and disseminated to personnel a media protection policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in CivicActions Media Protection (MP) Policy and Procedure document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs>.

##### Project
This is Agency common control. More data about implementation can be obtained from the Agency common control catalog. Media protection policy and procedures are fully inherited from AWS Cloud.

#### MP-2: MEDIA ACCESS
```text
Restrict access to [Assignment: organization-defined types of digital and/or non-digital media] to [Assignment: organization-defined personnel or roles].

```
**Status:** complete
##### AWS
This Media Protection control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### MP-6: MEDIA SANITIZATION
```text
 - a. Sanitize [Assignment: organization-defined system media] prior to disposal, release out of organizational control, or release for reuse using [Assignment: organization-defined sanitization techniques and procedures]; and
 - b. Employ sanitization mechanisms with the strength and integrity commensurate with the security category or classification of the information.

```
**Status:** complete
##### AWS
This Media Protection control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### MP-7: MEDIA USE
```text
 - a. [Selection: Restrict, Prohibit] the use of [Assignment: organization-defined types of system media] on [Assignment: organization-defined systems or system components] using [Assignment: organization-defined controls]; and
 - b. Prohibit the use of portable storage devices in organizational systems when such devices have no identifiable owner.

```
**Status:** complete
##### AWS
This Media Protection control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

### PE: Physical and Environmental Protection


#### PE-1: PHYSICAL AND ENVIRONMENTAL PROTECTION POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] physical and environmental protection policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the physical and environmental protection policy and the associated physical and environmental protection controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the physical and environmental protection policy and procedures; and
 - c. Review and update the current physical and environmental protection:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete
##### AWS
This Physical Environment control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### PE-2: PHYSICAL ACCESS AUTHORIZATIONS
```text
 - a. Develop, approve, and maintain a list of individuals with authorized access to the facility where the system resides;
 - b. Issue authorization credentials for facility access;
 - c. Review the access list detailing authorized facility access by individuals [Assignment: organization-defined frequency]; and
 - d. Remove individuals from the facility access list when access is no longer required.

```
**Status:** complete
##### AWS
This Physical Environment control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### PE-3: PHYSICAL ACCESS CONTROL
```text
 - a. Enforce physical access authorizations at [Assignment: organization-defined entry and exit points to the facility where the system resides] by:
   - 1. Verifying individual access authorizations before granting access to the facility; and
   - 2. Controlling ingress and egress to the facility using [Selection (one or more): [Assignment: organization-defined physical access control systems or devices], guards];
 - b. Maintain physical access audit logs for [Assignment: organization-defined entry or exit points];
 - c. Control access to areas within the facility designated as publicly accessible by implementing the following controls: [Assignment: organization-defined physical access controls];
 - d. Escort visitors and control visitor activity [Assignment: organization-defined circumstances requiring visitor escorts and control of visitor activity];
 - e. Secure keys, combinations, and other physical access devices;
 - f. Inventory [Assignment: organization-defined physical access devices] every [Assignment: organization-defined frequency]; and
 - g. Change combinations and keys [Assignment: organization-defined frequency] and/or when keys are lost, combinations are compromised, or when individuals possessing the keys or combinations are transferred or terminated.

```
**Status:** complete
##### AWS
This Physical Environment control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### PE-6: MONITORING PHYSICAL ACCESS
```text
 - a. Monitor physical access to the facility where the system resides to detect and respond to physical security incidents;
 - b. Review physical access logs [Assignment: organization-defined frequency] and upon occurrence of [Assignment: organization-defined events or potential indications of events]; and
 - c. Coordinate results of reviews and investigations with the organizational incident response capability.

```
**Status:** complete
##### AWS
This Physical Environment control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### PE-8: VISITOR ACCESS RECORDS
```text
 - a. Maintain visitor access records to the facility where the system resides for [Assignment: organization-defined time period];
 - b. Review visitor access records [Assignment: organization-defined frequency]; and
 - c. Report anomalies in visitor access records to [Assignment: organization-defined personnel].

```
**Status:** complete
##### AWS
This Physical Environment control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### PE-12: EMERGENCY LIGHTING
```text
Employ and maintain automatic emergency lighting for the system that activates in the event of a power outage or disruption and that covers emergency exits and evacuation routes within the facility.

```
**Status:** complete
##### AWS
This Physical Environment control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### PE-13: FIRE PROTECTION
```text
Employ and maintain fire detection and suppression systems that are supported by an independent energy source.

```
**Status:** complete
##### AWS
This Physical Environment control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### PE-14: TEMPERATURE AND HUMIDITY CONTROLS
```text
 - a. Maintain [Selection (one or more): temperature, humidity, pressure, radiation, [Assignment: organization-defined environmental control]] levels within the facility where the system resides at [Assignment: organization-defined acceptable levels]; and
 - b. Monitor environmental control levels [Assignment: organization-defined frequency].

```
**Status:** complete
##### AWS
This Physical Environment control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### PE-15: WATER DAMAGE PROTECTION
```text
Protect the system from damage resulting from water leakage by providing master shutoff or isolation valves that are accessible, working properly, and known to key personnel.

```
**Status:** complete
##### AWS
This Physical Environment control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/

#### PE-16: DELIVERY AND REMOVAL
```text
 - a. Authorize and control [Assignment: organization-defined types of system components] entering and exiting the facility; and
 - b. Maintain records of the system components.

```
**Status:** complete
##### AWS
This Physical Environment control associated with hardware components within AWS is generally either partially or fully inherited from the AWS physical infrastructure, while the customer organization is responsible for any part of the control that is applicable to customer-controlled equipment and facilities, and the customer's configurable portion of the AWS logical infrastructure, including the Operating systems on Amazon EC2 instances and the customer's applications.

For the U.S. East, U.S. West, and GovCloud regions, this control is inherited from pre-existing Agency Authority to Operate (ATO) or JAB provisional Authority to Operate under the Federal Risk and Authorization Management Program (FedRAMP).

Refer to the AWS FedRAMP SSP artifacts, including the Control Implementation Summary and Customer Responsibility Matrix, available from the AWS Compliance Team. http://aws.amazon.com/compliance/fedramp/"

### PL: Planning


#### PL-1: SECURITY PLANNING POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] planning policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the planning policy and the associated planning controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the planning policy and procedures; and
 - c. Review and update the current planning:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.

##### Contractor
CivicActions has developed, documented and disseminated to personnel a system planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Planning (PL) Policy and Procedure document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs/>.

##### Project
This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

The Project developed its security policy planning and procedures based on None, guidance from NIST, the Office of Management and Budget and industry best practices. Security policies and procedures are formally documented within the Project SSP, which provides the roles and responsibilities as it pertains to security planning. It provides guidance on all aspects of security for the protection of Project information technology resources. It defines responsibilities for the implementation and oversight of the guidance contained herein. The plan was last updated in December, 2015.

#### PL-2: SYSTEM SECURITY PLAN
```text
 - a. Develop security and privacy plans for the system that:
   - 1. Are consistent with the organization’s enterprise architecture;
   - 2. Explicitly define the constituent system components;
   - 3. Describe the operational context of the system in terms of mission and business processes;
   - 4. Identify the individuals that fulfill system roles and responsibilities;
   - 5. Identify the information types processed, stored, and transmitted by the system;
   - 6. Provide the security categorization of the system, including supporting rationale;
   - 7. Describe any specific threats to the system that are of concern to the organization;
   - 8. Provide the results of a privacy risk assessment for systems processing personally identifiable information;
   - 9. Describe the operational environment for the system and any dependencies on or connections to other systems or system components;
   - 10. Provide an overview of the security and privacy requirements for the system;
   - 11. Identify any relevant control baselines or overlays, if applicable;
   - 12. Describe the controls in place or planned for meeting the security and privacy requirements, including a rationale for any tailoring decisions;
   - 13. Include risk determinations for security and privacy architecture and design decisions;
   - 14. Include security- and privacy-related activities affecting the system that require planning and coordination with [Assignment: organization-defined individuals or groups]; and
   - 15. Are reviewed and approved by the authorizing official or designated representative prior to plan implementation.
 - b. Distribute copies of the plans and communicate subsequent changes to the plans to [Assignment: organization-defined personnel or roles];
 - c. Review the plans [Assignment: organization-defined frequency];
 - d. Update the plans to address changes to the system and environment of operation or problems identified during plan implementation or control assessments; and
 - e. Protect the plans from unauthorized disclosure and modification.

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS system security plan.

##### Project
The System Security Plan (SSP) was developed and implemented for Project system in accordance with None, NIST SP 800-18 and NIST SP 800-37. The SSP includes a description of the management, operational, and technical controls in place or planned for the application. The SSP is included as a key document in an application’s C&A package and is reviewed and approved by designated officials. The SSP identifies the system owner and responsible parties for managing system access and the overall security of the system. The Chief Information Security Officer reviews and approves the SSP. The SSP will be reviewed at least annually and updated to account for any changes to the Project system and to address any changes in security controls.

#### a
##### Contractor
CivicActions has developed this system security plan (SSP) for the information system as part of compliance with NIST 800-53 and FIPS 199. The SSP defines the security categorization, system boundary, and security requirements and controls meeting the requirements of the NIST Risk Management Framework (RMF). Specifically the SSP:

1. Is consistent with the organization’s enterprise architecture
2. Explicitly defines the authorization boundary for the system
3. Describes the operational context of the information system in terms of missions and business processes
4. Provides the security categorization of the information system including supporting rationale
5. Describes the operational environment for the information system and relationships with or connections to other information systems
6. Provides an overview of the security requirements for the system
7. Identifies any relevant overlays, if applicable
8. Describes the security controls in place or planned for meeting those requirements including a rationale for the tailoring decisions
9. Is reviewed and approved by the authorizing official or designated representative prior to plan implementation

#### b
##### Contractor
The SSP is reviewed and approved by the authorizing official prior to plan implementation. A copy of the SSP is provided to authorized CivicActions and assessing personnel including the System Owner, Authorizing Official, Information System Security Officer, System/Network Administrator, and the CivicActions Operations staff. The SSP is maintained by the CivicActions Security Office.

#### c
##### Contractor
The SSP is reviewed at least annually by the System Owner and the CivicActions Operations staff in collaboration with the CivicActions Security Office.

#### d
##### Contractor
The CivicActions Operations staff in collaboration with the CivicActions Security Office updates the system description and control descriptions within the SSP as needed to verify the SSP is an accurate description of the system.

#### e
##### Contractor
The SSP is currently available to authorized users on GitLab. Per the Acceptable Use Policy, all entities granted access to CivicActions information assets are required to complete a non-disclosure agreement (NDA) to uphold information confidentiality. GitLab provides the configuration management capabilities for the SSP to be protected from unauthorized disclosure and modification.

#### PL-4: RULES OF BEHAVIOR
```text
 - a. Establish and provide to individuals requiring access to the system, the rules that describe their responsibilities and expected behavior for information and system usage, security, and privacy;
 - b. Receive a documented acknowledgment from such individuals, indicating that they have read, understand, and agree to abide by the rules of behavior, before authorizing access to information and the system;
 - c. Review and update the rules of behavior [Assignment: organization-defined frequency]; and
 - d. Require individuals who have acknowledged a previous version of the rules of behavior to read and re-acknowledge [Selection (one or more): [Assignment: organization-defined frequency], when the rules are revised or updated].

```
**Status:** complete
#### a
##### Contractor
CivicActions has created and made readily available to individuals requiring access to the information system the rules that describe their responsibilities and expected behavior with regard to information and information system usage. These rules, defined as the Acceptable Use Policy, are included in the CivicActions Security Policy accessible here: <https://guidebook.civicactions.com/en/latest/company-policies/security/#acceptable-use-policy> which has also been uploaded to CSAM as ''Appendix J1 - System Rules of Behavior - Privileged User'' (CivicActions Security Policy 20190226.docx).'

##### Project
Project has created and made readily available to individuals requiring access to the information system the rules that describes their responsibilities and expected behavior with regard to information and information system usage. These rules are captured in ‘Appendix J2 - System Rules of Behavior - General User’ (ProjectSystemRoB2019-template.docx).

Project has reviewed and accepted as a superset alternative the CivicActions Acceptable Use Policy.

#### b
##### Contractor
CivicActions HR receives a signed acknowledgment from all employees, indicating that they have read, understand, and agree to abide by the rules of behavior, before authorizing access to information and the information system. The text of the electronically signed (via DocuSign) acknowledgment document has been uploaded to CSAM as artifact: ''CivicActions Security Policy Acknowledgement.docx''

##### Project
The Project System Owner receives a signed acknowledgment from such individuals that are not CivicActions employees, indicating that they have read, understand, and agree to abide by the rules of behavior, before authorizing access to information and the information system.

#### c
##### Contractor
CivicActions reviews the CivicActions Security Policy at least annually and updates as required.

##### Project
Project reviews the Rules of Behavior at least annually and updates it as required.

#### d
##### Contractor
CivicActions requires individuals who have signed a previous version of the CivicActions Security Policy to read and re-sign when any part of it, including the Acceptable Use Policy/Rules of Behavior, is revised/updated.

##### Project
Project requires individuals who have signed a previous version of the rules of behavior to read and re-sign when the Rules of Behavior are revised/updated.

### PS: Personnel Security


#### PS-1: PERSONNEL SECURITY POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] personnel security policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the personnel security policy and the associated personnel security controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the personnel security policy and procedures; and
 - c. Review and update the current personnel security:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.

##### Contractor
CivicActions has developed, documented and disseminated to personnel a personnel security policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in CivicActions Personnel Security (PS) Policy document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs>.

##### Project
The Project documents the security policy and procedures in addressing position categorization, personnel screening, personnel termination, personnel transfer, and access agreements within the Project SSP. Project adopts the Client personnel security standards and determines position risks levels based on public trust responsibilities.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

#### PS-2: POSITION RISK DESIGNATION
```text
 - a. Assign a risk designation to all organizational positions;
 - b. Establish screening criteria for individuals filling those positions; and
 - c. Review and update position risk designations [Assignment: organization-defined frequency].

```
**Status:** complete
#### a
##### Contractor
Risk designations are assigned to all CivicActions positions. The CivicActions Office of Human Resources works in coordination with the CivicActions Security Office to assign risk designations.

#### b
##### Contractor
The CivicActions Office of Human Resources works in coordination with the CivicActions Security Office to establish screening criteria for all CivicActions positions.

#### c
##### Contractor
At least every three (3) years, the CivicActions Office of Human Resources reviews and revises position risk designations. If the Office of Human Resources determines that significant changes must be made to the position risk descriptions the Office of Human Resources works in coordination with the CivicActions Security Office to implement changes as required.

##### Project
Project position sensitivity levels are assigned by the Client Full Name. Each position designation is documented on the Standard Position Description (SPD) and assigned a risk level (or sensitivity level) commensurate with the sensitivity of the information, the risk to that information and the system maintaining that information. The levels of risk still need to be designated by Client for employee and contractor positions but since Project system does not have any sensitive data, a low risk scenario can be assumed.

- Employee risk levels and background investigations are: Low Risk= NACI, Moderate Risk= LBI, High Risk= BI.
- Contractor risk levels and background investigations are: Low Risk= NACI, Moderate Risk= NACC, High Risk= BI.

In order to ensure every employee is assigned to a position, which has been reviewed for sensitivity by the NCC, the SPD is a required data attribute of an employee’s HR record. Position risks designations are reviewed and revised when NCC or OPM publish changes to sensitivity levels.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog

#### PS-3: PERSONNEL SCREENING
```text
 - a. Screen individuals prior to authorizing access to the system; and
 - b. Rescreen individuals in accordance with [Assignment: organization-defined conditions requiring rescreening and, where rescreening is so indicated, the frequency of rescreening].

```
**Status:** complete
#### a
##### Contractor
Prospective CivicActions employees undergo background checks commensurate with the individual’s job duties, the classification of the information they will access, and the risks associated with the role. At the discretion of the CivicActions Security Office, these checks may also be conducted on contractors and/or third party users in cases where they will have access to application data that is not meant to be consumed by the public. In these instances, the Security Office will instruct the Office of Human Resources to conduct a background check before granting access to the information system.

#### b
##### Contractor
Rescreening is conducted as required by the individual’s job duties, the classification of the information they will access, and the risks associated with the role. A basic background check is performed for all CivicActions employees.

##### Project
Minimum background investigations are conducted, since all data is non-sensitive, for individuals requiring access to Project information and information systems. The type of background investigation conducted for an individual is determined by the individual’s position risk categorization noted in control PS-2. Client conducts periodic reinvestigations in accordance with OPM and NIST guidelines.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

#### PS-4: PERSONNEL TERMINATION
```text
Upon termination of individual employment:
 - a. Disable system access within [Assignment: organization-defined time period];
 - b. Terminate or revoke any authenticators and credentials associated with the individual;
 - c. Conduct exit interviews that include a discussion of [Assignment: organization-defined information security topics];
 - d. Retrieve all security-related organizational system-related property; and
 - e. Retain access to organizational information and systems formerly controlled by terminated individual.

```
**Status:** complete
#### a
##### Contractor
Information system access is terminated immediately upon the voluntary or involuntary departure of an employee. In the case of involuntary departure, in addition to immediate termination of system access, at no point is a departing employee allowed access to any part of the CivicActions infrastructure.
In the case of voluntary departure, employees are permitted access to the information system for the duration of their offboarding period. The departing employee’s manager is responsible for informing the Information Technology department when the employee offboarding period concludes. At this time system and facility, access is terminated.

#### b
##### Contractor
The terminated user’s accounts are disabled and all access associated with the individual is revoked.

#### c
##### Contractor
The employee's manager or the Office of Human Resources conducts exit interviews with all employees who leave CivicActions voluntarily. There is a general discussion about the process of turning in any/all company-issued devices, laptops, etc.

#### d
##### Contractor
CivicActions employees provide their own equipment that must be hardened to security requirements depending upon their roles and duties. CivicActions supplies two-factor authentication tokens that become the property of the employee.
Some employees may receive company-issued hardware for working on particular projects. These items are collected before the employee exits CivicActions. In the case of an involuntary termination, the Office of Human Resources works to collect company-issued devices and provides paperwork highlighting confidential protections for customers.

#### e
##### Contractor
Access to CivicActions information and information systems is always shared so that the termination of an individual will not prevent CivicActions from having access to needed resources.

#### f
##### Contractor
When a person is terminated, a standard off-boarding process is used to notify management and CivicActions' Operations staff, and to track the process of disabling access to the information system/information system components. The CivicActions Operations staff and Security Office are given at least four hours notice to schedule the deactivation of access upon termination. Deactivation is a manual process that is tracked via a Trello card in order to meet the four hour turnaround time before termination.

##### Project
Client Full Name HR policy states that managers or designated officials are responsible for recovering and properly securing employee badges and returning it to the local physical security office. The Client executes termination procedures that remove personnel access privileges, computer accounts. When an employee is terminated, the employee’s manager or designated official completes a form requesting termination of access for the user. Local management and the security manager coordinate disabling or removing Project privileged access with the system administrator. The employee’s manager or designated official is responsible for recovering and properly securing his/her ID badge and returning it to the local physical security office. The employee’s manager or designated official ensures that any information on the system that the employee was responsible for will be available to the appropriate personnel.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

#### PS-5: PERSONNEL TRANSFER
```text
 - a. Review and confirm ongoing operational need for current logical and physical access authorizations to systems and facilities when individuals are reassigned or transferred to other positions within the organization;
 - b. Initiate [Assignment: organization-defined transfer or reassignment actions] within [Assignment: organization-defined time period following the formal transfer action];
 - c. Modify access authorization as needed to correspond with any changes in operational need due to reassignment or transfer; and
 - d. Notify [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time period].

```
**Status:** complete
#### a
##### Contractor
When an employee, third party personnel and/or contractor is transferred to a new project or position within CivicActions, they may maintain access to the previous system they were working on in order to facilitate the process of maintenance and knowledge transfer. However, as part of the practices of account management (AC-2) and least privilege (AC-6), regular audits of privileged users are conducted and access privileges may be removed when no longer needed. Additionally, adherence to specific client SLAs may enhance the frequency of such audits or the timeliness of privilege removal during personnel transfer.

#### b
##### Contractor
When an employee, third party personnel and/or contractor is transferred to a new position within CivicActions and there is a requirement for access change, such access changes are normally completed within five business days.

#### c
##### Contractor
Access authorizations are modified as needed to coincide with changes in duties or operational needs upon personnel transfer or reassignment.

#### d
##### Contractor
CivicActions Operations staff is informed of transfers that require access authorization modifications within five business days by the Project Manager, System Owner or Office of Human Resources.

##### Project
When an employee is reassigned or transferred, the employee’s manager or designated official is required to request transfer of access (as appropriate) for the user.

In accordance with the Client Full Name HR policy, the employee’s manager or designated official is responsible for recovering and properly securing his/her ID badge and returning it to the local physical security office. The manager provides prompt notification to the Project system/security administrator when an employee changes assignments and/or location. This includes taking prompt and appropriate action to change employee access profile and/or remove employee from the system; and ensure that users’ system access is cancelled when the need no longer exists.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

#### PS-6: ACCESS AGREEMENTS
```text
 - a. Develop and document access agreements for organizational systems;
 - b. Review and update the access agreements [Assignment: organization-defined frequency]; and
 - c. Verify that individuals requiring access to organizational information and systems:
   - 1. Sign appropriate access agreements prior to being granted access; and
   - 2. Re-sign access agreements to maintain access to organizational systems when access agreements have been updated or [Assignment: organization-defined frequency].

```
**Status:** complete
#### a
##### Project
All users of the Project system must read and accept access agreements upon every login.

#### b
##### Project
The Access Agreements are reviewed at least annually or when a significant change occurs.

#### c
##### Project
All individuals requiring access to the Project system are required to sign the Access Agreements before login is granted. When the Access Agreements are updated, the individual will be required to sign the new copy before regaining access.

#### PS-7: THIRD-PARTY PERSONNEL SECURITY
```text
 - a. Establish personnel security requirements, including security roles and responsibilities for external providers;
 - b. Require external providers to comply with personnel security policies and procedures established by the organization;
 - c. Document personnel security requirements;
 - d. Require external providers to notify [Assignment: organization-defined personnel or roles] of any personnel transfers or terminations of external personnel who possess organizational credentials and/or badges, or who have system privileges within [Assignment: organization-defined time period]; and
 - e. Monitor provider compliance with personnel security requirements.

```
**Status:** complete
#### a
##### Project
Personnel security requirements including security roles and responsibilities that apply to primary contracting organizations flow down to their subcontractors.

#### b
##### Project
Personnel security policies and procedures that apply to primary contracting organizations flow down to their subcontractors.

#### c
##### Project
All personnel security requirements are documented in PS-1 and other related Personnel Security controls.

#### d
##### Project
For personnel transfers and terminations of third-party personnel, the procedures defined in employee termination (PS-4) and employee transfer (PS-5) flow down to subcontractors.

#### e
##### Project
Compliance measures for assessing third-party personnel and/or contractors are determined on a case-by-case basis. Third-party personnel are monitored to ensure compliance with personnel security requirements.

#### PS-8: PERSONNEL SANCTIONS
```text
 - a. Employ a formal sanctions process for individuals failing to comply with established information security and privacy policies and procedures; and
 - b. Notify [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time period] when a formal employee sanctions process is initiated, identifying the individual sanctioned and the reason for the sanction.

```
**Status:** complete
#### a
##### Contractor
The CivicActions Security Office and/or the Office of Human Resources is responsible for determining and enforcing sanctions for failing to comply with established information security policies and procedures. Coaching may be considered prior to sanctions. Sanctions may include but are not limited to written warnings, reduction in system access, demotion, or termination.

#### b
##### Contractor
When employee sanctions processes are initiated, the Office of Human Resources notifies the respective Project Manager(s) and CivicActions' Security Office within five business days.

##### Project
The disciplinary sanctions for personnel failing to comply with establish IT security policies and procedures are included in Client Full Name HR policy. If an employee violates the Client information security policies and procedures, the employee may be subject to disciplinary action at the discretion of management. Actions may range from verbal or written warning, removal of system access for a specific period of time, reassignment to other duties, or termination, depending on the severity of the violation. Disciplinary sanctions are reported to the OCIO.

### RA: Risk Assessment


#### RA-1: RISK ASSESSMENT POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] risk assessment policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the risk assessment policy and the associated risk assessment controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the risk assessment policy and procedures; and
 - c. Review and update the current risk assessment:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.

##### Contractor
CivicActions has developed, documented and disseminated to personnel a risk assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Risk Assessment (RA) Policy and Procedure that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs/>.

##### Project
The Client follows the risk assessment policy and procedures formally documented within None. Furthermore, a Risk Assessment Plan was originally initiated to determine the extent of the potential threat and the risk associated with Project throughout its System Development Life Cycle (SDLC). The Project Risk Assessment defines the methodology approach to determine the likelihood risks, and identify potential mitigation options to reduce risks to the Project system.

The Project Risk Assessment will be conducted in accordance with the Department’s risk assessment policy and procedures. By doing so, the responsible parties associated with the Project will be able to determine the risk, likelihood and impact that could result from exploiting vulnerabilities within the system.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

#### RA-2: SECURITY CATEGORIZATION
```text
 - a. Categorize the system and information it processes, stores, and transmits;
 - b. Document the security categorization results, including supporting rationale, in the security plan for the system; and
 - c. Verify that the authorizing official or authorizing official designated representative reviews and approves the security categorization decision.

```
**Status:** complete
#### a
##### Project
In accordance with FIPS 199 requirement and guidelines provided in NIST SP800-60 Rev.1, the organization categorized the system as a Low system: Confidentiality (Low), Integrity (Low), Availability (Low).

#### b
##### Project
The security categorization was determined by evaluating the type of information that is stored, processed, and/or transmitted by the application and the potential impact levels associated with the confidentiality, integrity, and availability of that information. The application’s security categorization has been documented in this SSP.

#### c
##### Project
The security categorizations have been reviewed by the designated application POCs, were approved during the C&A effort. The formal security categorization document is available upon request. The system inventory for the Project Project is revalidated semiannually.

#### RA-3: RISK ASSESSMENT
```text
 - a. Conduct a risk assessment, including:
   - 1. Identifying threats to and vulnerabilities in the system;
   - 2. Determining the likelihood and magnitude of harm from unauthorized access, use, disclosure, disruption, modification, or destruction of the system, the information it processes, stores, or transmits, and any related information; and
   - 3. Determining the likelihood and impact of adverse effects on individuals arising from the processing of personally identifiable information;
 - b. Integrate risk assessment results and risk management decisions from the organization and mission or business process perspectives with system-level risk assessments;
 - c. Document risk assessment results in [Selection: security and privacy plans, risk assessment report, [Assignment: organization-defined document]];
 - d. Review risk assessment results [Assignment: organization-defined frequency];
 - e. Disseminate risk assessment results to [Assignment: organization-defined personnel or roles]; and
 - f. Update the risk assessment [Assignment: organization-defined frequency] or when there are significant changes to the system, its environment of operation, or other conditions that may impact the security or privacy state of the system.

```
**Status:** Planned
#### a
##### Project
CivicActions/Project will perform risk assessments for the Project system based on SP 800-30 Rev. 1 Guide for Conducting Risk Assessments at least annually and as part of the change management activities for the Project system that warrant a new or updated risk assessment.

#### b
##### Project
The results of risk assessments will be compiled into a risk assessment report to be reviewed by CivicActions Security and relevant personnel, and also added to the GitLab system for the Project system.

#### c
##### Project
CivicActions/Project reviews risk assessment
results at least annually.

#### d
##### Project
The Risk Assessment report will be disseminated to the appropriate
personnel through the Project Manager and CivicActions
Security.

#### e
##### Project
Risk assessments are conducted annually or whenever there are significant changes to the information system or environment of operation (including the identification of new threats and vulnerabilities), or other conditions that may impact the security state of the system, as defined in NIST Special Publication 800-37 Revision 1.
A significant change includes:

- Changing authentication or access control implementations;
- Changing storage implementations;
- Changing a COTS product to another product;
- Changing the backup mechanisms and process; and,
- Adding new interconnections to an outside service provide.

#### RA-5: VULNERABILITY SCANNING
```text
 - a. Monitor and scan for vulnerabilities in the system and hosted applications [Assignment: organization-defined frequency and/or randomly in accordance with organization-defined process] and when new vulnerabilities potentially affecting the system are identified and reported;
 - b. Employ vulnerability monitoring tools and techniques that facilitate interoperability among tools and automate parts of the vulnerability management process by using standards for:
   - 1. Enumerating platforms, software flaws, and improper configurations;
   - 2. Formatting checklists and test procedures; and
   - 3. Measuring vulnerability impact;
 - c. Analyze vulnerability scan reports and results from vulnerability monitoring;
 - d. Remediate legitimate vulnerabilities [Assignment: organization-defined response times] in accordance with an organizational assessment of risk;
 - e. Share information obtained from the vulnerability monitoring process and control assessments with [Assignment: organization-defined personnel or roles] to help eliminate similar vulnerabilities in other systems; and
 - f. Employ vulnerability monitoring tools that include the capability to readily update the vulnerabilities to be scanned.

```
**Status:** In Place
##### AWS
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: vulnerability scanning.

##### Project
The Project uses vulnerability scanning software to document and determine risks to the system. These scans are run monthly and the results of these scans are being used to inform changes to the system and verify that security controls are working correctly. These scans are used to document the current state of the system, and to analyze security trends as changes are made over time.

#### a
##### Contractor
CivicActions Operations uses vulnerability scanning software to document and determine risks to the system. Operating system and application vulnerability scans include:

- The CivicActions system environment employs the OpenSCAP scanner with the Red Hat STIG baseline to check for vulnerabilities.
- The CivicActions application environment is tested by the penetration tester OWASP ZAP, an open-source web application security scanner to report on needed updates based on known flaws.

CivicActions Operations has automated the process to perform the scans on a monthly basis. The resulting reports list vulnerabilities and rank them by severity. These reports are stored in Amazon S3 buckets and are used to inform changes to the system and verify that security controls are working correctly. These scans are used to document the current state of the system, and to analyze security trends as changes are made over time.

#### b
##### Contractor
CivicActions employs the automated vulnerability scanning tools OpenSCAP and OWASP ZAP which are interoperable with standard web browsers, the Open Source Ansible infrastructure provisioning system and other Open Source tools.

#### c
##### Contractor
The CivicActions Security Office reviews all vulnerabilities identified from automated scans and security assessments. "False positive" findings are documented and may be tailored out. Vulnerabilities found and deemed legitimate are assigned an impact rating and response time thought creation of an issue or ticket. The CivicActions Operations staff reviews current scans and compare with older scans to identify trends and to verify previous vulnerabilities have been mitigated.

#### d
##### Contractor
Identified and reported vulnerabilities are assigned an impact rating and response time by CivicActions' Security and must be remediated according to the following time requirements:

- Critical - Within 15 days of discovery (usually within 1 week))
- High - Within 30 days of discovery (usually within 1 week))
- Moderate - Within 90 days of discovery (usually within 2 weeks)
- Low - Within 180 days of discovery

#### e
##### Contractor
Results of the vulnerability scans and security assessments are shared with all appropriate CivicActions personnel supporting continuous monitoring requirements. CivicActions Security assigns each vulnerability an impact rating and response time through JIRA or the Git issue tool for tracking to the established remediation deadlines listed in RA-5(d).

### SA: System and Services Acquisition


#### SA-1: SYSTEM AND SERVICES ACQUISITION POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] system and services acquisition policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the system and services acquisition policy and the associated system and services acquisition controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the system and services acquisition policy and procedures; and
 - c. Review and update the current system and services acquisition:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete
##### Contractor
CivicActions has developed, documented and disseminated to personnel a system and services acquisition policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained by the CivicActions System and Services Acquisition (SA) Policy document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs/>.

##### Project
The Project complies with the None. The Project will identify new threats/vulnerabilities and technologies that may require updating of solicitation documents.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

#### SA-2: ALLOCATION OF RESOURCES
```text
 - a. Determine the high-level information security and privacy requirements for the system or system service in mission and business process planning;
 - b. Determine, document, and allocate the resources required to protect the system or system service as part of the organizational capital planning and investment control process; and
 - c. Establish a discrete line item for information security and privacy in organizational programming and budgeting documentation.

```
**Status:** complete
#### a
##### Contractor
CivicActions' Security Office, in collaboration with the System Owner, act and/or meet on a pre-determined basis to determine information system security requirements and to develop implementation budgets and plans.

#### b
##### Contractor
The CivicActions Security Office, in collaboration with the System Owner, determines, designates, documents, and allocates the resources required to protect the system as part of its capital planning and investment control processes.

#### c
##### Contractor
The annual budget developed by the System Owner includes explicit budgetary line items for FISMA security requirements. Additional security-related expenditures that fall outside of explicit compliance requirements are addressed in sub-lines under the CivicActions Information Technology budget.

##### Project
The Project System Owner is responsible for leading the annual budgeting process and for tracking organizational spending. The System Owner coordinates with the CivicActions Project Manager and CivicActions Security on at least monthly basis to track security priorities and spending patterns and determine financial requirements. The System Owner also coordinates the approval process for interim increases to the security budget, if required. This data is used to support the development of the annual budget.

Security costs are included in Exhibit 53 in the Department's on-line electronic Capital Planning and Investment Control system (eCPIC) in order to provide adequate business case information for budget purposes. Security costs are represented across the life cycle in the business case (Exhibit 300) for major investments and (Exhibit 53) for non-major projects - Project is a non-major project. Security costs are summarized and listed as a line item on the Exhibit 53 in the budget submitted to Treasury.

Costs for providing security at the infrastructure level are contained in the business cases for infrastructure supporting computing platforms, desktop processing, the network environment, and web capability. Since the Exhibit 53 includes projections for multiple fiscal years, its intention is to identify and anticipate security resources required.

#### SA-3: SYSTEM DEVELOPMENT LIFE CYCLE
```text
 - a. Acquire, develop, and manage the system using [Assignment: organization-defined system development life cycle] that incorporates information security and privacy considerations;
 - b. Define and document information security and privacy roles and responsibilities throughout the system development life cycle;
 - c. Identify individuals having information security and privacy roles and responsibilities; and
 - d. Integrate the organizational information security and privacy risk management process into system development life cycle activities.

```
**Status:** complete
#### a
##### Contractor
The system and application(s) are managed by CivicActions using the Agile software development methodology, which provides a continuous System Development Life Cycle (SDLC) methodology. CivicActions Agile management continues to improve the software through ongoing planned code releases. The process is overseen by the Change Control Board (CCB) as described in CM-1. Each point release introduces code and configuration changes to the website through the following SDLC methodology:

- Code release planning: A code release ticket is created in the Change Request project of the CivicActions ticketing system which describes the overall goals of the code release. The code release ticket is linked to other tickets in the ticketing system which describe issues to be addressed by the planned code release. Those issues may include bug fixes and feature enhancements as well as upgrades to newer versions of the software packages that have been used to build the website.
- Sprints: The tickets covered by the planned code release are then implemented through a series of planned sprints, each of which typically lasts two weeks. Each sprint begins with a sprint planning session at which the CCB selects a list of tickets to be implemented. CivicActions Development holds daily coordination meetings throughout the sprint to share information and resolve any problems that may be blocking progress toward completion. At the end of the sprint, a retrospective is performed in which progress is reviewed to determine which issues have been resolved and which need further work.
- Development/unit testing: Work on each ticket is performed within a separate code branch within the CivicActions Git repository, and tested using the GitLab Runner continuous integration platform. Developers also write unit tests to prove their code behaves as expected and address security considerations such as information leakage, bounds checking, and input validation. Once work on a ticket is completed, the developer creates a merge request, and the changes are submitted to at least one other developer for review to ensure they meet functional requirements and address security considerations before the pull request is merged into the Git repository's development branch for the planned code release.
- Integration testing: Once all work tickets have been completed, the code and configuration necessary to implement the changes are merged into the website's staging server, where it undergoes additional testing to ensure there are no conflicts between the work that has been done on individual tickets.
- User acceptance testing (UAT): The code release undergoes manual testing against a checklist of expected site behaviors and options each of the website's defined user roles to further verify that the functional changes work as expected and to identify any changes in user experience that need to be documented in release notes to be shared with the customer.
- Approval for deployment: After all the planned code release has passed all of the above tests, the code release is scheduled for deployment to production and presented to CivicActions' Change Control Board (CCB) for review and approval.
- Deployment to production: A full backup of the website is performed immediately prior to the deployment.
- Security scan: After the deployment to production, the website undergoes a security scan using a web vulnerability scanner.

  Security issues to be addressed in the planned code release may come from a variety of sources:

- Customer support requests received by the CivicActions Help Desk
- Security concerns, incidents, and site performance issues reported by users
- Security incident reports, including server log analysis and root cause analysis of those incidents performed by the CivicActions Security Office and Operations staff
- Security notifications received by the CivicActions Security Office from external security teams and other software vendors
- Vulnerabilities detected during security scans of the website performed by the CivicActions Security Office
- Issues reported by the CivicActions Security Office, Operations staff and Development
- Security issues reported through continuous monitoring

#### b
##### Contractor
The CivicActions organization defines and documents information security roles and responsibilities throughout the SDLC. The following teams participate in this process:

- Customer Support: Files tickets when incidents are reported and shares incident reports with customers
- The CivicActions Security Office: Receives security notifications from the Drupal security team and other software vendors; performs security scans; uses CivicActions JIRA ticketing system to request mitigation of all reported vulnerabilities
- CivicActions Development: Performs server log analysis when security incidents are reported; assists in root cause analysis
- Change Control Board: Meets weekly to review and approve upcoming planned code changes to the website, include security-related code releases.
- AWS Cloud: Monitors server and application events; proactively respond to security incidents, and reports incidents to CivicActions
- Users: Communicates customer security requirements and expectations, and alerts the CivicActions customer support team whenever it detects a security or site performance issue

Security responsibilities performed by these teams include the following:

- Perform configuration management during information system design, development, implementation, and operation;
- Implement only organization-approved changes;
- Document approved changes;
- Manage and control changes to the system;
- Fully test all changes, taking into account security considerations as well as other functional requirements;
- Track security flaws and flaw resolution; and
- Employ code analysis tools to examine software for common flaws and document the results of the analysis.

#### c
##### Contractor
Each of the CivicActions teams described in SA-3(b) has a team leader who is responsible for defining the roles and responsibilities of individual personnel members within that team. CivicActions uses role-based management for access and authentication implementation and enforcement.

#### d
##### Contractor
The CivicActions organization integrates the organizational information security risk management process into system development life cycle activities by requiring that the processes defined in SA-3(a) and (b) above are adhered to by all information system developers and associated security personnel.

##### Project
The Project draws from the None, NIST SP 800-64, and Agile software development methodology to ensure security requirements are incorporated during each phase of the life cycle. This helps to ensure the development of secure systems and effective risk management.

#### SA-4: ACQUISITION PROCESS
```text
Include the following requirements, descriptions, and criteria, explicitly or by reference, using [Selection (one or more): standardized contract language, [Assignment: organization-defined contract language]] in the acquisition contract for the system, system component, or system service:
 - a. Security and privacy functional requirements;
 - b. Strength of mechanism requirements;
 - c. Security and privacy assurance requirements;
 - d. Controls needed to satisfy the security and privacy requirements.
 - e. Security and privacy documentation requirements;
 - f. Requirements for protecting security and privacy documentation;
 - g. Description of the system development environment and environment in which the system is intended to operate;
 - h. Allocation of responsibility or identification of parties responsible for information security, privacy, and supply chain risk management; and
 - i. Acceptance criteria.

```
**Status:** partial
##### Contractor
The CivicActions System and Services Acquisition Policy affects all personnel with purchasing authorization and applies to all purchases or deployments including infrastructure, software or hardware. The CivicActions System and Services Acquisition Policy contains the process for determining acceptance criteria for all system software and application services.

The Acquisition Security Policy includes an assessment that evaluates the product based on the vendor’s security practices, policies, and past performance. It also details the potential maintenance and end-of-life ramifications with regards to security.

The CivicActions Security Office is responsible for determining the security documentation that must be included in the information system or services acquisition contracts.

Configuration and design of the development and production environments are hosted in the CivicActions Git repository. All documentation is strictly controlled regarding transportation and storage in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs.

##### Project
The Project follows the guidelines and procedures within the overarching None. The requirements in the information system acquisition contract permit updating security controls as new threat/vulnerabilities are identified and new technologies are implemented.

The Project System and Services Acquisition Policy contains the process for determining acceptance criteria for all Project system software and services.

The Project organization reviews and approves all acquisition contracts in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs.

#### SA-4 (10): USE OF APPROVED PIV PRODUCTS
```text
Employ only information technology products on the FIPS 201-approved products list for Personal Identity Verification (PIV) capability implemented within organizational systems.

```
**Status:** incomplete
##### Project
CivicActions/Project and AWS describes this control as “not applicable”, as PIV credentials are not applicable to the Project system. Access and Authentication requirements for the Project system for internal CivicActions and customer are implemented under access management and enforcement (AC-2 and AC-3) and identification and authentication for all users (IA-2 and IA-8).

It is the responsibility of CivicActions for implementation of PIV capability for authentication as required.

#### SA-5: INFORMATION SYSTEM DOCUMENTATION
```text
 - a. Obtain or develop administrator documentation for the system, system component, or system service that describes:
   - 1. Secure configuration, installation, and operation of the system, component, or service;
   - 2. Effective use and maintenance of security and privacy functions and mechanisms; and
   - 3. Known vulnerabilities regarding configuration and use of administrative or privileged functions;
 - b. Obtain or develop user documentation for the system, system component, or system service that describes:
   - 1. User-accessible security and privacy functions and mechanisms and how to effectively use those functions and mechanisms;
   - 2. Methods for user interaction, which enables individuals to use the system, component, or service in a more secure manner and protect individual privacy; and
   - 3. User responsibilities in maintaining the security of the system, component, or service and privacy of individuals;
 - c. Document attempts to obtain system, system component, or system service documentation when such documentation is either unavailable or nonexistent and take [Assignment: organization-defined actions] in response; and
 - d. Distribute documentation to [Assignment: organization-defined personnel or roles].

```
**Status:** partial
#### a
##### AWS
In this architecture, documentation of the infrastructure configuration in the form of AWS CloudFormation templates in JSON or YAML format, architecture diagrams, deployment user guide and security controls implementation details is included.

AWS built-in features include online documentation for management of the infrastructure at http://aws.amazon.com/documentation/

##### Contractor
Some application features are built on a custom basis and are not part of standard FOSS packages. Administrator documentation for those custom features is maintained in the CivicActions Git repository documentation system.

##### Ilias
Public documentation related to Ilias is maintained by the Ilias Association and is located at <https://Ilias.de/documentation>. This documentation contains administrator documentation for the information system that describes:
- secure configuration, installation, and operation of the system, component, or service;
- effective use and maintenance of security functions/mechanisms; and
- known vulnerabilities regarding configuration and use of administrative functions;

#### b
##### AWS
AWS built-in features include online documentation of AWS services at http://aws.amazon.com/documentation/

1. AWS built-in features include online documentation for AWS account users at
   http://aws.amazon.com/documentation/ such as user Guides, API reference guides, CLI
   reference guides and developer reference guides to provide information on how to
   effectively use security functions.

2. AWS built-in features include online documentation for AWS account users within the
   infrastructure at http://aws.amazon.com/documentation/ such as user Guides, API
   reference guides, CLI reference guides and developer reference guides to provide
   information on how to access AWS services and components in a more secure manner.

3. AWS built-in features include online documentation for AWS account users at
   https://aws.amazon.com/security/security-resources/ that provides information
   related to security responsibilities of customers using AWS services.

##### Contractor
The publicly-available FOSS package documentation described in control SA-5(a) also includes user documentation for non-administrators as described in control AC-3. This includes documentation on how to create and manage user accounts as well as how to create, update and delete content.

CivicActions follows the user documentation standard practice to provide context-sensitive help as well as access to a Help Desk in publicly facing applications.

The CivicActions Customer Support team, described in control SA-3(b), handles questions about how to use the system. Questions are submitted by sending an email to support@civicactions.com, which triggers the creation of a ticket in the CivicActions customer support ticketing system.

##### Ilias
The public documentation at Ilias.de contains user documentation for the information system that describes:
- user-accessible security functions/mechanisms and how to effectively use those
  security functions/mechanisms;
- methods for user interaction, which enables individuals to use the system,
  component, or service in a more secure manner; and
- user responsibilities in maintaining the security of the system, component, or service;

#### d
##### AWS
AWS built-in features include online documentation that is protected by AWS from unauthorized modification or deletion within AWS system.

##### Contractor
All administrator documentation is housed in a protected Git repository. User documentation is publicly available.

##### Ilias
The Ilias.de documentation is multi-sourced on GitHub and private repositories.
#### e
##### AWS
AWS built-in features include online documentation located at http://aws.amazon.com/documentation/ that is publicly available.

##### Contractor
As needed and approved by the CivicActions Security Office, documentation is available to appropriate personnel by granting access to the private Git repository.

##### Ilias
As the Ilias.de documentation is publicly available, there is no need to provide distribution mechanisms.
#### c
##### Contractor
If the information needed to answer a question is not already included in the website's public-facing documentation, a ticket is created to determine whether the question is sufficiently general in nature to warrant adding the answer to the website's documentation.

##### Ilias
As a popular and well-used and maintained free and open source (FOSS) project, in the event that sought after documentation is not available on Ilias.de, it can usually be found in one of the many forums, mailing lists or Stack Exchange sites covering Ilias and its many contributed modules.
##### Project
Client maintains adequate documentation for the Project system. The Project system documentation is protected as required and made available to authorized personnel. Procedures for protecting system documentation include management in the private CivicActions Git repository and the publicly available documentation trees for Free and Open Source Software (FOSS). The documentation maintained for the Project system includes:

- System Security Plan (SSP) – this document
- Configuration documentation
- Incident Response and Contingency Plans
- Rules of Behavior (Acceptable Use Policy)
- FOSS Reference Manuals (Drupal, GNU/Linux, Apache, MySQL, PHP, Postfix,
  etc.)

#### SA-9: EXTERNAL INFORMATION SYSTEM SERVICES
```text
 - a. Require that providers of external system services comply with organizational security and privacy requirements and employ the following controls: [Assignment: organization-defined controls];
 - b. Define and document organizational oversight and user roles and responsibilities with regard to external system services; and
 - c. Employ the following processes, methods, and techniques to monitor control compliance by external service providers on an ongoing basis: [Assignment: organization-defined processes, methods, and techniques].

```
**Status:** complete
##### Contractor
CivicActions does not have any dedicated interconnections between information system components within the authorization boundary and external third-party vendor information systems for the purposes of storing, processing or transmitting federal agency data.

##### Project
Project does not have any dedicated interconnections between information system components within the authorization boundary and external third-party vendor information systems for the purposes of storing, processing, or transmitting federal agency data.

Project is hosted on the AWS Cloud platform, which was approved under the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.

### SC: System and Communications Protection


#### SC-1: SYSTEM AND COMMUNICATIONS PROTECTION POLICY AND PROCEDURES
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

#### SC-5: DENIAL OF SERVICE PROTECTION
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

#### SC-7: BOUNDARY PROTECTION
```text
 - a. Monitor and control communications at the external managed interfaces to the system and at key internal managed interfaces within the system;
 - b. Implement subnetworks for publicly accessible system components that are [Selection: physically, logically] separated from internal organizational networks; and
 - c. Connect to external networks or systems only through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.

```
**Status:** partial
#### a
##### AWS
In this architecture, network communications to, from, and between VPCs, subnets and Amazon S3 buckets are controlled as follows: AWS Route Tables specify which subnets in each VPC are accessible through gateways and which are isolated/private. AWS Security Groups provide stateful inbound/outbound port/protocol restrictions, Amazon Simple Storage Service (Amazon S3) buckets support access control restrictions based on network source/destination.

#### b
##### AWS
In this architecture, subnetworks for publicly accessible system components are logically separated from internal private subnetworks via AWS security groups, refined routing tables, and NACLs.

#### c
##### AWS
In this architecture, connection to external networks is possible only through Internet Gateways (IGWs) or NAT gateways (in regions where supported by AWS VPC) and are restricted based on ports/protocols via AWS Security groups, and default subnet rules provided by NACLs.

##### Drupal
Drupal, when deployed on SELinux in full enforcing mode, minimizes the number of services and computing nodes that are exposed to the Internet. Drupal employs both the AWS platform safeguards and the Drupal Watchdog module in monitoring and recording system events. All other computing nodes used in the system are isolated within AWS.

##### Ilias
Ilias, when deployed on SELinux in full enforcing mode, minimizes the number of services and computing nodes that are exposed to the Internet. Ilias employs both the AWS platform safeguards and the Ilias logging in monitoring and recording system events. All other computing nodes used in the system are isolated within AWS.
##### Project
The Project system has monitored and controlled communications at the external boundary of the information system and at key internal boundaries within the system, where appropriate. The Project allocates publicly accessible information system components (e.g., public web servers) specific IP address and port combinations. Public access into the organization’s internal networks is prevented except as appropriately mediated.

#### SC-12: CRYPTOGRAPHIC KEY ESTABLISHMENT AND MANAGEMENT
```text
Establish and manage cryptographic keys when cryptography is employed within the system in accordance with the following key management requirements: [Assignment: organization-defined requirements for key generation, distribution, storage, access, and destruction].

```
**Status:** partial
##### AWS
In this architecture, initial private/public SSH keys stored in Identity and Access Management (IAM) are supplied to Amazon EC2 instances upon launch, and the public key portion is managed within the AWS Amazon EC2 service. In addition, server-side encryption is used for Amazon S3 storage and Amazon RDS databases, using key management provided by AWS for the storage buckets and Amazon RDS databases.

##### Project
Use of cryptographic key management for the Project system is in use for at the time of implementation for authentication. CivicActions utilizes customer agency supplied PIV credentials for access to customer instances of the Project. Access enforcement and authentication requirements for Project are described in AC-2 & IA-2. AWS platform does not utilize or manage cryptographic keys within the ACE boundary.

#### SC-13: CRYPTOGRAPHIC PROTECTION
```text
 - a. Determine the [Assignment: organization-defined cryptographic uses]; and
 - b. Implement the following types of cryptography required for each specified cryptographic use: [Assignment: organization-defined types of cryptography for each specified cryptographic use].

```
**Status:** partial
##### AWS
In this architecture, encryption mechanisms are employed for data at rest and in transit. For data at rest, AES-256 Server Side encryption is employed for data stored in Amazon S3, and Amazon RDS databases. For data in transit, to protect against exposure of any cleartext data transmitted deliberately (upload/download) or incidentally during interactive systems management operations, Amazon S3 object access can only be conducted over encrypted sessions via TLS; the bastion host, Amazon EC2 instances and associated security groups are configured for encrypted SSH sessions only. For web user access, the Elastic Load Balancing (ELB) employs a TLS endpoint.

AWS built-in features employ TLS for AWS Management Console sessions, AWS API calls, and AWS Command Line Interface connections.

##### Contractor
The information system implements:

- Cryptographic modules through Secure Shell (SSH) to allow administrators to securely logon to the various system components
- HTTPS/SSL (TLS) for connection to web-based services
- TLS for connection to email services
- AES-256 (FIPS 140-2 validated) for data at rest (with Elastic Block Store (EBS) volumes)

#### SC-15: COLLABORATIVE COMPUTING DEVICES
```text
 - a. Prohibit remote activation of collaborative computing devices and applications with the following exceptions: [Assignment: organization-defined exceptions where remote activation is to be allowed]; and
 - b. Provide an explicit indication of use to users physically present at the devices.

```
**Status:** none
##### Project
This control is not applicable, as the Project system does
employ any collaborative computing devices.

#### SC-20: SECURE NAME / ADDRESS RESOLUTION SERVICE
```text
 - a. Provide additional data origin authentication and integrity verification artifacts along with the authoritative name resolution data the system returns in response to external name/address resolution queries; and
 - b. Provide the means to indicate the security status of child zones and (if the child supports secure resolution services) to enable verification of a chain of trust among parent and child domains, when operating as part of a distributed, hierarchical namespace.

```
**Status:** incomplete
##### Contractor
The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (authoritative source)

#### SC-21: SECURE NAME / ADDRESS RESOLUTION SERVICE
```text
Request and perform data origin authentication and data integrity verification on the name/address resolution responses the system receives from authoritative sources.

```
**Status:** incomplete
##### Contractor
The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (recursive or caching resolver)

#### SC-22: ARCHITECTURE AND PROVISIONING FOR NAME / ADDRESS RESOLUTION SERVICE
```text
Ensure the systems that collectively provide name/address resolution service for an organization are fault-tolerant and implement internal and external role separation.

```
**Status:** none
##### Contractor

#### SC-39: PROCESS ISOLATION
```text
Maintain a separate execution domain for each executing system process.

```
**Status:** partial
##### AWS
In this architecture, the AMIs that make up the operating systems deployed on Amazon EC2 instances maintain separate execution domains/address spaces for executing processes within the customer operating environment.

AWS built-in features of the hypervisors that support the infrastructure maintain separate execution domains/address spaces for executing processes.

##### Contractor
Process isolation is maintained on the Linux platform. Linux is the only operating system that is part of the boundary.

### SI: System and Information Integrity


#### SI-1: SYSTEM AND INFORMATION INTEGRITY POLICY AND PROCEDURES
```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] system and information integrity policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the system and information integrity policy and the associated system and information integrity controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the system and information integrity policy and procedures; and
 - c. Review and update the current system and information integrity:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete
##### Contractor
CivicActions has developed, documented and disseminated to personnel a system and information integrity policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Information Integrity (SI) Policy document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs/>.

##### Project
System and information integrity policy and procedures for the Project system are formally documented in the Project SSP, which provides the roles and responsibilities as it pertains to physical and environmental protection systems. The Project system support staff monitors the network on a daily basis and employs up-to-date patches to protect the integrity of the system.

Additional information is contained within the None.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

#### SI-2: FLAW REMEDIATION
```text
 - a. Identify, report, and correct system flaws;
 - b. Test software and firmware updates related to flaw remediation for effectiveness and potential side effects before installation;
 - c. Install security-relevant software and firmware updates within [Assignment: organization-defined time period] of the release of the updates; and
 - d. Incorporate flaw remediation into the organizational configuration management process.

```
**Status:** complete
#### a
##### Contractor
Identification of information system security flaws are detected as early as possible by the following methods:

- Vulnerability scans, as described in RA-5.
- Log analysis from monitoring described in SI-4.
- Service flaw notifications (CVEs, etc.) are received by the
  CivicActions Security Office and passed on to
  CivicActions Operations staff when relevant.

Any security issues found are ticketed through JIRA and/or the Git issue queue. CivicActions Operations staff prioritizes high findings. Changes made to correct the information system as a result of the system flaws are scheduled and coordinated through the CCB Change Request Process and appropriate approvals required from the CCB as implemented in CM-3.

#### b
##### Contractor
CivicActions testing of the system as a result of security flaw remediation is done through a development environment through the use of internal software and automated testing that ensures the system is working as intended. When a change is made by a developer, testing though a peer review is conducted as part of the Change Request process to ensure the correct analysis is completed. Then the changed code is tested in an automatic test environment as described in the Configuration Management Plan (CMP). Tracking of the testing is documented in JIRA and/or the Git issue queue.

#### c
##### Contractor
CivicActions security-software updates are tested prior to implementation on production. The CivicActions Security framework for installation requires updates to be made within 30 days for high vulnerabilities, 90 days for moderate vulnerabilities, and 240 for low vulnerabilities. An issue ticket is created to track any updates made to the system.

#### d
##### Contractor
Flaw remediation is part of the CivicActions configuration management process. Any security issues found are ticketed through JIRA or the Git issue queue. The CivicActions Security Office prioritizes the high findings within the application. Changes made to correct the system as a result of the system flaws are scheduled and coordinated through the CCB Change Request Process and appropriate approvals required from the CCB Chair as implemented in CM-3.

##### Ilias
Ilias contains built-in security status monitoring of the core application and contributed modules.
#### SI-3: MALICIOUS CODE PROTECTION
```text
 - a. Implement [Selection (one or more): signature based, non-signature based] malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code;
 - b. Automatically update malicious code protection mechanisms as new releases are available in accordance with organizational configuration management policy and procedures;
 - c. Configure malicious code protection mechanisms to:
   - 1. Perform periodic scans of the system [Assignment: organization-defined frequency] and real-time scans of files from external sources at [Selection (one or more): endpoint, network entry and exit points] as the files are downloaded, opened, or executed in accordance with organizational policy; and
   - 2. [Selection (one or more): block malicious code, quarantine malicious code, take [Assignment: organization-defined action]]; and send alert to [Assignment: organization-defined personnel or roles] in response to malicious code detection; and
 - d. Address the receipt of false positives during malicious code detection and eradication and the resulting potential impact on the availability of the system.

```
**Status:** partial
#### a
##### Contractor
Virus scans are performed by ClamAV, a server-hosted tool protecting the application from Trojans, Viruses and other malicious cyber-threats. Real-time scans are conducted whenever files are uploaded from any external source and malicious code is blocked or quarantined when detected. All file-based traffic traversing the server is sanitized before being delivered. All input form text is validated and sanitized.

#### b
##### Contractor
Anti-virus definitions and malicious code protection mechanisms are configured and updated automatically on a nightly basis.

#### c
##### Contractor
CivicActions Operations staff receives information system security alerts, advisories, and notifications in response to malicious code detection. These messages are sent to group email distribution lists to ensure all members of the team receive the proper information in a timely manner.

#### d
##### Contractor
False positives during malicious code detection and eradication are dealt with on a case by case basis. Potential impacts on the availability of the information system are detailed in a false positive report depending on if the report is for the OS, database or web application.

#### SI-4: INFORMATION SYSTEM MONITORING
```text
 - a. Monitor the system to detect:
   - 1. Attacks and indicators of potential attacks in accordance with the following monitoring objectives: [Assignment: organization-defined monitoring objectives]; and
   - 2. Unauthorized local, network, and remote connections;
 - b. Identify unauthorized use of the system through the following techniques and methods: [Assignment: organization-defined techniques and methods];
 - c. Invoke internal monitoring capabilities or deploy monitoring devices:
   - 1. Strategically within the system to collect organization-determined essential information; and
   - 2. At ad hoc locations within the system to track specific types of transactions of interest to the organization;
 - d. Analyze detected events and anomalies;
 - e. Adjust the level of system monitoring activity when there is a change in risk to organizational operations and assets, individuals, other organizations, or the Nation;
 - f. Obtain legal opinion regarding system monitoring activities; and
 - g. Provide [Assignment: organization-defined system monitoring information] to [Assignment: organization-defined personnel or roles]
                  [Selection (one or more): as needed, [Assignment: organization-defined frequency]].

```
**Status:** complete
#### a
##### Contractor
CivicActions systems use a collection of monitoring systems, including:

- ClamAV - provides signature-based malware detection/quarantine
- OSSEC host-based intrusion detection system (HIDS)
- AIDE Advanced Intrusion Detection Environment (IDS))
- fail2ban, an intrusion prevention system (IPS) framework
- SELinux - a Mandatory Access Control (MAC) IPS
- auditd - a secure system audit daemon
- CloudWatch - AWS monitoring and measurement system
- StatusCake - website monitoring tool
- OpsGenie - a slack/email/text/phone incident escalation tool

#### b
##### Contractor
Logs from the systems described in SI-4(a) are sent to the CivicActions SIEM tool for analysis. These logs can identify unauthorized use of the information system.

#### c
##### Contractor
Monitoring and log collection occur throughout the system.
#### d
##### Contractor
The Configuration Management process, remote log gathering, and SELinux MAC protects information obtained from intrusion-monitoring tools from unauthorized access, modification, and deletion.

#### e
##### Contractor
In the event of a performance score lower than CivicActions standards, a notification is sent to the CivicActions Security Office. CivicActions subscribes to security mailing lists in the event the monitoring activity is required based on law enforcement information, intelligence information, or other credible sources of information.

#### f
##### Contractor
Internal legal counsel is utilized as required when system notifications indicate such action based on user and/or malicious activity. Legal counsel is engaged for any actions that may necessitate increased user monitoring or evidence/forensic actions.

#### g
##### Contractor
System alerts generated by CivicActions internal monitors (StatusCake, OSSEC, ClamAV, others) are sent to the Incident Response team via OpsGenie.

#### SI-5: SECURITY ALERTS, ADVISORIES, AND DIRECTIVES
```text
 - a. Receive system security alerts, advisories, and directives from [Assignment: organization-defined external organizations] on an ongoing basis;
 - b. Generate internal security alerts, advisories, and directives as deemed necessary;
 - c. Disseminate security alerts, advisories, and directives to: [Selection (one or more): [Assignment: organization-defined personnel or roles], [Assignment: organization-defined elements within the organization], [Assignment: organization-defined external organizations]]; and
 - d. Implement security directives in accordance with established time frames, or notify the issuing organization of the degree of noncompliance.

```
**Status:** complete
#### a
##### Contractor
The CivicActions Security Office and Operations staff receive the following security alerts, advisories, and directives on an ongoing basis:

- Mailing lists relevant to web application security
- US-CERT
- Technical Cyber Security Alerts
- Drupal Security Advisories

#### b
##### Contractor
CivicActions utilizes StatusCake for front line monitoring for real time system status and events of the application. StatusCake can feed to the OpsGenie incident escalation system.

#### c
##### Contractor
The CivicActions Security Office disseminates security alerts, advisories, and directives to all CivicActions internal personnel and client personnel as directed.

#### d
##### Contractor
The CivicActions Security Office is responsible for ensuring the dissemination and implementation of relevant security alerts and advisories.

##### Ilias
CivicActions Security and Operations receive Ilias Security Advisories on a regular basis.
##### Project
Project representatives and system administrators receive alerts from US-CERT on a regular basis. Support personnel take appropriate action in response to relevant areas of concern.

#### SI-12: INFORMATION OUTPUT HANDLING AND RETENTION
```text
Manage and retain information within the system and information output from the system in accordance with applicable laws, executive orders, directives, regulations, policies, standards, guidelines and operational requirements.

```
**Status:** complete
##### Contractor
The CivicActions organization retains all information, system-related information, incident-related information, and system output in accordance with customers’ requirements retention periods and other NIST guidance and standards, Federal policies, procedures, federal laws, and executive orders. Audit records are retained for 365 days.

##### Project
Project representatives and systems administrators receive annual training from Client regarding information assurance and information handling requirements. These personnel are required to operate the system and handle system data and output in accordance with legal requirements. Personnel training and system guidelines ensure that data and programs are handled appropriately.
