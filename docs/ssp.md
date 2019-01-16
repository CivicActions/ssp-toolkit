
Table of Contents
=================

* [LINCS System Security Plan](#lincs-system-security-plan)
* [NIST SP 800-53 Revision 4](#nist-sp-800-53-revision-4)
   * [AC: Access Control](#ac-access-control)
   * [AT: Awareness and Training](#at-awareness-and-training)
   * [AU: Audit and Accountability](#au-audit-and-accountability)
   * [CA: Security Assessment and Authorization](#ca-security-assessment-and-authorization)
   * [CM: Configuration Management](#cm-configuration-management)
   * [CP: Contingency Planning](#cp-contingency-planning)
   * [IA: Identification and Authentication](#ia-identification-and-authentication)
   * [IR: Incident Response](#ir-incident-response)
   * [MA: Maintenance](#ma-maintenance)
   * [MP: Media Protection](#mp-media-protection)
   * [PE: Physical and Environmental Protection](#pe-physical-and-environmental-protection)
   * [PL: Planning](#pl-planning)
   * [PS: Personnel Security](#ps-personnel-security)
   * [RA: Risk Assessment](#ra-risk-assessment)
   * [SA: System and Services Acquisition](#sa-system-and-services-acquisition)
   * [SC: System and Communications Protection](#sc-system-and-communications-protection)
   * [SI: System and Information Integrity](#si-system-and-information-integrity)
* [NIST SP 800-53 Revision 4 Privacy](#nist-sp-800-53-revision-4-privacy)
   * [AP: AP](#ap-ap)
   * [AR: Accountability, Audit, and Risk Management](#ar-accountability-audit-and-risk-management)
   * [DI: Data Quality and Integrity](#di-data-quality-and-integrity)
   * [DM: Data Minimization and Retention](#dm-data-minimization-and-retention)
   * [IP: Individual Participation and Redress](#ip-individual-participation-and-redress)
   * [SE: Security](#se-security)
   * [TR: Transparency](#tr-transparency)
   * [UL: Use Limitation](#ul-use-limitation)

<!-- Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc) -->

# LINCS System Security Plan

# NIST SP 800-53 Revision 4

## AC: Access Control

### AC-1: Access Control Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  An access control policy that addresses purpose, scope, roles, responsibilities,
> management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the access control policy
> and associated access controls; and
>   b.  Reviews and updates the current:
>     1.  Access control policy [Assignment: organization-defined frequency]; and
>     2.  Access control procedures [Assignment: organization-defined frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel an access control policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Access Control (AC) Policy.  This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


##### LINCS

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.
Access control policy and procedures are documented in the LINCS SSP. Access to LINCS Technology Project operational information or system resources is limited to only authorized users, programs or processes. The Department enforces access control policies to protect the integrity of the LINCS Technology Project system. This Department reviews and updates this policy as necessary and it has been being updated, as necessary, since April 2008.
Additional information is contained within the Department of Education, OCIO-01, Handbook for Information Assurance Cybersecurity Policy.


### AC-2: Account Management

> The organization:
>   a.  Identifies and selects the following types of information system accounts
> to support organizational missions/business functions: [Assignment: organization-defined information system account types];
>   b.  Assigns account managers for information system accounts;
>   c.  Establishes conditions for group and role membership;
>   d.  Specifies authorized users of the information system, group and role membership,
> and access authorizations (i.e., privileges) and other attributes (as required) for each account;
>   e.  Requires approvals by [Assignment: organization-defined personnel or roles]
> for requests to create information system accounts;
>   f.  Creates, enables, modifies, disables, and removes information system accounts
> in accordance with [Assignment: organization-defined procedures or conditions];
>   g.  Monitors the use of information system accounts;
>   h.  Notifies account managers:
>     1.  When accounts are no longer required;
>     2.  When users are terminated or transferred; and
>     3.  When individual information system usage or need-to-know changes;
>   i.  Authorizes access to the information system based on:
>     1.  A valid access authorization;
>     2.  Intended system usage; and
>     3.  Other attributes as required by the organization or associated missions/business
> functions;
>   j.  Reviews accounts for compliance with account management requirements [Assignment:
> organization-defined frequency]; and
>   k.  Establishes a process for reissuing shared/group account credentials (if
> deployed) when individuals are removed from the group.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS account management.


#### a

##### CivicActions

CivicActions Operations, in collaboration with CivicActions Security, will set up privileged accounts accounts for the following roles:
• Developer - user level account that has access to application features and sanitized databases
• System Administrator - user accounts that enjoy full system administrator access


##### Drupal

Drupal provides user accounts for individuals who participate in visiting, contributing to and administering the site with the following roles:
• Anonymous user – readers of the site who either do not have an account or are not logged in.
• Authenticated user – All non-anonymous users inherit the "authenticated user role."
• Administrator - This role has all permissions enabled by default.


##### LINCS

SSH system accounts are provided to contractors on an as-needed basis.
Access privileges are used to ensure that only authorized personnel access certain areas of the LINCS Technology Project system. User access is controlled by the completion and submission of LINCS Technology Project System Rules of Behavior and New User Account Request forms by the user and management. These items are completed and submitted whenever a new user requires access or an existing user requires access changes. The system administrator, based on need-to-know, assigns the proper permissions. The employee’s manager approves the access rights before the initial account is created. Finally, the system administrator implements the access rights according to the New User Account Request form. The security staff and the support contractor review accounts periodically. Accounts no longer in use are removed from the system by the system administrator.
The LINCS Technology Project has implemented user account procedures to disable inactive user accounts after 90-days of inactivity. The LINCS support staff monitors all user accounts to ensure this procedure is enforced. Section 6.3, Authentication Management, of the LINCS SSP illustrates the exact procedures the contractor support staff follows to ensure accounts are properly managed.
The LINCS Technology Project system does not have guest or anonymous accounts.


#### b

##### CivicActions

CivicActions' Project Manager assigns the "admininstrator" role for the management of all accounts issued to internal admin roles supporting the information system. Account requests are initiated by the Project Manager by completing a ticket request and the CivicActions Operation Team manages the entire account creation process.


##### LINCS

The System Owner has oversight over all permissions that the Project Manager and Operations Staff manages.


#### c

##### LINCS

In accordance with LINCS Access Control Policy, LINCS group membership is determined according to the individual's position and role within the organization. A ticket request is used to request accounts and group membership. The request is authorized by the appropriate manager.


#### d

##### CivicActions

All accounts issued for application administrators and SSH are documented in CivicActions' ticketing system. Account request tickets contain details that explain the attributes for the account including authorized users of Drupal, system infrastructure, group and role membership, and access authorizations.


##### Drupal

Drupal has a sophisticated permissions and role-based access control built in. Each role within Drupal can only access the documents and controls for which their privilege allows.


##### LINCS

LINCS user privileges vary depending on the type of user role assigned. Only users with the role of Administrator have the ability to create and modify user roles for other users.


#### e

##### CivicActions

All accounts issued for the admin management of Application or SSH access must be approved by the System Owner or Project Manager who must create an account request. The CivicActions Operations Team applies appropriate account permissions and settings based on the job role and function documented within the request ticket using processes defined by the CivicActions Security Team.


##### LINCS

The System Owner approves, and CivicActions Operations set up the initial Administrator account for LINCS. Subsequent client access and related approvals are managed by CivicActions Operations in collaboaration with the System Owner.


#### f

##### CivicActions

CivicActions Operations is responsible for the following account management activities for both internal administrative users and customer accounts:
• Establishing account justification
• Activating accounts
• Modifying accounts
• Expiring accounts
• Disabling accounts
• Removing accounts


#### g

##### CivicActions

All CivicActions systems log the usage of information accounts.


##### Drupal

Drupal monitors the usage of information accounts in the watchdog.log.


#### h

##### CivicActions

In accordance with the CivicActions Access Control (AC-01) Policy when an account is no longer required, the Project Manager notifies the Operations Team to immediately disable all access. Users upon reassignment, change in roles, termination, or leaving employment are initially removed from all roles and groups, effectively denying them all access to privileged accounts.


#### i

##### CivicActions

System accounts require access authorizations prior to accounts being created. The Project Manager must initiate an access request for an account to be created. CivicActions Operations reviews the request to ensure accuracy, including intended system usage and other attributes of the user access being requested.


##### LINCS

LINCS governs their own administrative access. Users with the Administrator roles are empowered to designate and approve Administrators.


#### j

##### CivicActions

All privileged accounts are reviewed by CivicActions Operations every 180 days.


##### LINCS

Administrators are empowered to and responsible for reviewing their own accounts and determining whether the accounts should still be authorized.


#### k

##### CivicActions

In accordance with standard security best practices and CivicActions policy, shared and reissued accounts for internal accounts of any kind are not created nor used for any purpose in any system.


### AC-3: Access Enforcement

> The information system enforces approved authorizations for logical access to information           and system resources in accordance with applicable access control policies.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS account management.


##### Drupal

Access control in Drupal is enforced by authentication via unique username/password for every type of user except Anonymous user. The user’s privileges, permissions and access are provided on "least privilege" principle.
The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves. Drupal Administrators are the only user roles that can create new user accounts.


##### LINCS

The LINCS Technology Project ensures that assigned authorizations for controlling access to the system is enforced in accordance with the user definitions noted in Section 1.1.1 of the LINCS SSP. The technical support staff ensures that access to security functions and protected information is restricted to authorized personnel. Access will be controlled with access control list used on each instance. Members of one group cannot access resources defined for other groups unless explicitly permitted.


### AC-6: Least Privilege

> The organization employs the principle of least privilege, allowing only authorized accesses for users (or processes acting on behalf of users) which are necessary to accomplish assigned tasks in accordance with organizational missions and business functions.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: application of least privilege.


##### CivicActions

CivicActions performs regular audits of privileged users as part of the practice of enforcing least privilege.


##### Drupal

CivicActions implements the policy of least privilege for all logical components of Drupal by allowing only authorized access for users, which are necessary to accomplish assigned tasks in accordance with business functions and organizational need.
At the application layer, Drupal is designed with a role based user access system, a least privileged approach based on assignment of privileges to roles. Drupal‘s permission systems enables control of what users can do and see on the site. CivicActions has defined a specific set of permissions for each of the user roles mentioned in control AC-5.
SSH access is provided on a least privilege basis and analyzed on an ongoing basis, at least quarterly. Findings related to these audits of accounts are reported and reviewed by the CivicActions Data team and evaluated to determine roles that need to be revoked.


##### LINCS

Drupal privileged access roles are designated by LINCS which is responsible for determining who will have administrator privileges and the ability to create other user accounts, including user accounts with the role of "administrator".


### AC-6 (9): Auditing Use Of Privileged Functions

> The information system audits the execution of privileged functions.

##### Drupal

CivicActions, at least quarterly, audits all team accounts based on the concept of least privilege. Each member of the developer team is assigned a role of which defines access needed to perform only the member’s job function.  The audit of accounts is reported and reviewed by the CivicActions Operations and evaluated to determine whether roles or membership within the developer team should be changed.


### AC-7: Unsuccessful Logon Attempts

> The information system:
>   a.  Enforces a limit of [Assignment: organization-defined number] consecutive
> invalid logon attempts by a user during a [Assignment: organization-defined time period]; and
>   b.  Automatically [Selection: locks the account/node for an [Assignment: organization-defined
> time period]; locks the account/node until released by an administrator; delays next logon prompt according to [Assignment: organization-defined delay algorithm]] when the maximum number of unsuccessful attempts is exceeded.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: unsuccessful logon attempts.


##### LINCS

The LINCS Technology Project system locks out users after three unsuccessful login attempts. The information system automatically locks the account permanently, unless an administrator unlocks the account before then, when the maximum number of unsuccessful attempts (3) is exceeded.


#### a

##### Drupal

Drupal can be configured to lock an account after a specified number of invalid login attempts within specified time period.


#### b

##### Drupal

Lock down following unsuccessful attempts is configurable by Drupal administrators to conform to defined requirements.  When a user exceeds the limit of invalid logon attempts, their account is automatically locked for a specfied time and requires administrator action to unlock the account before the lockout period expires.


### AC-8: System Use Notification

> The information system:
>   a.  Displays to users [Assignment: organization-defined system use notification
> message or banner] before granting access to the system that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance and states that:
>     1.  Users are accessing a U.S. Government information system;
>     2.  Information system usage may be monitored, recorded, and subject to audit;
>     3.  Unauthorized use of the information system is prohibited and subject to
> criminal and civil penalties; and
>     4.  Use of the information system indicates consent to monitoring and recording;
>   b.  Retains the notification message or banner on the screen until users acknowledge
> the usage conditions and take explicit actions to log on to or further access the information system; and
>   c.  For publicly accessible systems:
>     1.  Displays system use information [Assignment: organization-defined conditions],
> before granting further access;
>     2.  Displays references, if any, to monitoring, recording, or auditing that
> are consistent with privacy accommodations for such systems that generally prohibit those activities; and
>     3.  Includes a description of the authorized uses of the system.

##### LINCS

A warning banner ensures that all persons attempting to gain access to the system know that the system and its information are “Authorized User Only” and that attempts to illegally log on to the system could lead to criminal prosecution. The warning message displayed notifies unauthorized users that they have accessed a U.S. Government computer system and continued, unauthorized use can be punishable by fines or imprisonment. Each device logged into will display a system use notification message before the log in window is displayed. The system use notification banner will remain on the screen until the user takes an explicit action to log on to the device. The following is the notification banner displayed on all Department instances:
"You are accessing a U.S. Federal Government computer system intended to be solely accessed by individual users expressly authorized to access the system by the U.S. Department of Education. Usage may be monitored, recorded, and/or subject to audit. For security purposes and in order to ensure that the system remains available to all expressly authorized users, the U.S. Department of Education monitors the system to identify unauthorized users. Anyone using this system expressly consents to such monitoring and recording. Unauthorized use of this information system is prohibited and subject to criminal and civil penalties. Except as expressly authorized by the U.S. Department of Education, unauthorized attempts to access, obtain, upload, modify, change, and/or delete information on this system are strictly prohibited and are subject to criminal prosecution under 18 U.S.C § 1030, and other applicable statutes, which may result in fines and imprisonment. For purposes of this system, unauthorized access includes, but is not limited to:
• Any access by an employee or agent of a commercial entity, or other third party, who is not the individual user, for purposes of commercial advantage or private financial gain (regardless of whether the commercial entity or third party is providing a service to an authorized user of the system); and
• Any access in furtherance of any criminal or tortious act in violation of the Constitution or laws of the United States or any State.
If system monitoring reveals information indicating possible criminal activity, such evidence may be provided to law enforcement personnel."


### AC-14: Permitted Actions Without Identification Or Authentication

> The organization:
>   a.  Identifies [Assignment: organization-defined user actions] that can be performed
> on the information system without identification or authentication consistent with organizational missions/business functions; and
>   b.  Documents and provides supporting rationale in the security plan for the
> information system, user actions not requiring identification or authentication.

##### Drupal

The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves.


##### LINCS

The Department of Education allows the general public user to read the web pages, do searches on the resource database and to review online forum information without identification and authentication for the public web site. Program and Privilege users cannot access LINCS Technology Project system without identification or authentication.


### AC-17: Remote Access

> The organization:
>   a.  Establishes and documents usage restrictions, configuration/connection requirements,
> and implementation guidance for each type of remote access allowed; and
>   b.  Authorizes remote access to the information system prior to allowing such
> connections.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: remote access.


##### CivicActions

The CivicActions Access Control (AC) policy defines policy for remote usage restrictions.  The Project Manager or System Owner may additionally provision users according to their Access Control policies.


##### LINCS

The LINCS Technology Project permits remote access for privileged functions to support operational needs. The technical staff documents, monitors, and controls all methods of remote access to the information system including remote access for privileged functions. Privileged user access is only permitted through the use of Secure Shell (SSH) or the Remote Desktop Protocol (RDP) where the user will authenticate to the device through this secure channel. Virtual Private Networking (VPN) is not enabled in any form within the LINCS accreditation boundary.


### AC-18: Wireless Access

> The organization:
>   a.  Establishes usage restrictions, configuration/connection requirements, and
> implementation guidance for wireless access; and
>   b.  Authorizes wireless access to the information system prior to allowing such
> connections.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: wireless access.


##### CivicActions

This control is not applicable. The system does not provide wireless access points.


### AC-19: Access Control For Mobile Devices

> The organization:
>   a.  Establishes usage restrictions, configuration requirements, connection requirements,
> and implementation guidance for organization-controlled mobile devices; and
>   b.  Authorizes the connection of mobile devices to organizational information
> systems.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: mobile device restrictions.


##### CivicActions

This control is not applicable. The system does not maintain a facility in which mobile device access limitations are required.


### AC-20: Use Of External Information Systems

> The organization establishes terms and conditions, consistent with any trust relationships established with other organizations owning, operating, and/or maintaining external information systems, allowing authorized individuals to:
>   a.  Access the information system from external information systems; and
>   b.  Process, store, or transmit organization-controlled information using external
> information systems.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: use of external information systems.


##### CivicActions

This control is not applicable. The system does not connect with external information systems.


### AC-22: Publicly Accessible Content

> The organization:
>   a.  Designates individuals authorized to post information onto a publicly accessible
> information system;
>   b.  Trains authorized individuals to ensure that publicly accessible information
> does not contain nonpublic information;
>   c.  Reviews the proposed content of information prior to posting onto the publicly
> accessible information system to ensure that nonpublic information is not included; and
>   d.  Reviews the content on the publicly accessible information system for nonpublic
> information [Assignment: organization-defined frequency] and removes such information, if discovered.

#### a

##### LINCS

The Department of Education grants certain LINCS support staff members the authority to post publicly accessible content. These individuals must complete LINCS system security training before being granted access to the LINCS and before they can post publicly accessible content within the LINCS. Furthermore, each authorized individual must follow the procedures delineated within the “Using Drupal” Instruction to ensure they are following a verifiable procedure throughout the entire process. This covers the LINCS Discussion Lists administration areas, LINCS Quarterly Reporting and training tools, and Drupal Content Management systems. Public content is only edited via the Drupal Content Management System. All other content is only viewable by LINCS system users and protected by hardened access controls.


#### b

##### LINCS

It is the LINCS responsibility to train authorized LINCS individuals ensuring publicly accessible information does not contain nonpublic information.


#### c

##### LINCS

Authorized LINCS individuals review the proposed content of information prior to posting onto the publicly accessible information system to ensure that nonpublic information is not included.
LINCS Program Users have been authorized for creation of publicly accessible content with publishing authority from an Administrator role. The publishing authority ensures the information being published does not contain nonpublic information.


#### d

##### LINCS

Authorized LINCS individuals review the content on the publicly accessible information system for nonpublic information at least every 365 days and removes such information.


## AT: Awareness and Training

### AT-1: Security Awareness And Training Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A security awareness and training policy that addresses purpose, scope,
> roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the security awareness
> and training policy and associated security awareness and training controls; and
>   b.  Reviews and updates the current:
>     1.  Security awareness and training policy [Assignment: organization-defined
> frequency]; and
>     2.  Security awareness and training procedures [Assignment: organization-defined
> frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel awareness and training policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Awareness and Training (AT) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


##### LINCS

Security awareness and training policy and procedures are formally documented in Department of Education, Office of the Chief Information Officer, Handbook for Information Assurance Security Policy, Information Assurance Program (Handbook OCIO-01), which provides the roles and responsibilities as it pertains to security awareness and training. The Department will ensure all users, including managers and senior executives, are exposed to basic information system security awareness materials before authorizing access to the system and at least annually thereafter. The Department documents and monitors all individual information system security training activities including basic security awareness training. The Department reviews and updates the policy as necessary.


### AT-2: Security Awareness Training

> The organization provides basic security awareness training to information system users (including managers, senior executives, and contractors):
>   a.  As part of initial training for new users;
>   b.  When required by information system changes; and
>   c.  [Assignment: organization-defined frequency] thereafter.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### LINCS

The Department personnel and contractor employees involved with the management, operation, programming, maintenance, or use of LINCS Technology Project system receive training in acceptable computer security practices prior to system access.
All Department employees and contractors are required to complete annual IT security awareness training. This security awareness training covers issues and policies associated with information security, including end user security roles and responsibilities and rules of behavior. Some topics addressed in the training are:
* Password protection
* System rules of behavior
* Protection of hardware, software, and data
* Proper handling of copyrighted materials
* Reporting of security breaches and violations
* Proper procedures for software installation, uploading, and use on workstations. 
The security and awareness training is consistent with Department of Education IT Security Training Program Plan and the guidance in NIST Special Publication 800-50.


#### a

##### CivicActions

Both regular and ad hoc training to all CivicActions personnel, including those who support the system infrastructure and applications, is provided. All employees and contractors must complete Security Awareness trainings upon being hired and at least annually thereafter. CivicActions Operations will not create accounts for individuals until they have successfully completed the trainings. Additional training will be provided as required by system changes. Training takes the following forms:
Annual Knowledge Survey (i.e., Security Awareness Training): All employees are required to review trainings covering Security Awareness. After the training, a survey-style security awareness test is taken by employees. All CivicActions personnel are required to complete and pass the survey, and new employees are required to pass before being granted access to the Information System. In order to successfully pass the test, a score of 80% is required. This survey tests CivicActions personnel’s knowledge of critical security subjects, policies and procedures. Results from this survey are compiled by the Director of Human Resources and used to refine future training efforts.
Ad Hoc Security Awareness: The CivicActions ISSO oversees the approximately bi-monthly distribution of security awareness tips and articles to the all CivicActions employees. This can include general tips as well as articles tailored to the specific requirements of CivicActions users.


#### b

##### CivicActions

In the event of a major system change, the Project Manager is responsible for delivering additional training to impacted personnel. Specific training type, medium and delivery method is dependent upon the nature of the system change.


#### c

##### CivicActions

CivicActions provides annual security awareness training to its personnel.


### AT-3: Role-Based Security Training

> The organization provides role-based security training to personnel with assigned security roles and responsibilities:
>   a.  Before authorizing access to the information system or performing assigned
> duties;
>   b.  When required by information system changes; and
>   c.  [Assignment: organization-defined frequency] thereafter.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### LINCS

Completion of role-based training is an annual requirement for personnel in roles with significant information security responsibilities that require specialized role-based training. Role-based cybersecurity training is developed and implemented to meet identified training needs and competencies associated with the various target audiences/functional roles (federal and contractor employees) that comprise the Department workforce, as is identified in and required by the FISMA and OMB A-130, Appendix III. The appropriate content of security training is determined based on the assigned roles and responsibilities of individuals and the specific security requirements of the Department, PO and the information systems to which personnel have authorized access. Annual training requirements may be met by completing one or more course(s) within the Department’s learning management systems, participating in instructor-led training provided by the OCIO, or completing an external role-based course or courses offered within their specific functional area of expertise.


#### a

##### CivicActions

CivicActions personnel with security responsibilities are required to complete role-based security training before being provided with access to the information system. The CivicActions ISSO is responsible for creating the content of the training. The role-based training is provided and tracked by the CivicActions Information Security Office.


#### b

##### CivicActions

The Project manager in collaboration with CivicActions Security determines whether a change to the information system requires any modifications and updates to the security awareness training program and if so, works with the CivicActions Security to implement the change.


#### c

##### CivicActions

CivicActions' Security provides users with security responsibilities role-based security training on an annual basis. The training is provided and tracked by the CivicActions Information Security Office.


### AT-4: Security Training Records

> The organization:
>   a.  Documents and monitors individual information system security training activities
> including basic security awareness training and specific information system security training; and
>   b.  Retains individual training records for [Assignment: organization-defined
> time period].

#### a

##### CivicActions

The CivicActions Information Security Office tracks all security awareness training within the organization and ensures that all employees have successfully completed training when required. The training records are stored and tracked in a spreadsheet maintained by the CivicActions Information Security Office.


##### LINCS

The Department documents and monitors all individual information system security training activities including basic security awareness training. New users are required to take security training within 30 days of hire. This information is kept in the appropriate personnel files to verify users have met the training requirements. Training requirement notifications are sent to individuals as deadline for re-training approaches.


#### b

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

Training records are tracked and maintained by the CivicActions Information Security Office. Records are maintained permanently.


##### LINCS

The Office of Information Secuity maintains training certifications for the specified period.


## AU: Audit and Accountability

### AU-1: Audit And Accountability Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  An audit and accountability policy that addresses purpose, scope, roles,
> responsibilities, management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the audit and accountability
> policy and associated audit and accountability controls; and
>   b.  Reviews and updates the current:
>     1.  Audit and accountability policy [Assignment: organization-defined frequency];
> and
>     2.  Audit and accountability procedures [Assignment: organization-defined
> frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel an audit and accountability policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Audit and Accountability (AU) Policy.  This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


##### LINCS

The LINCS Technology Project maintains a record of system activity by application process and by user activity. Audit and accountability policy and procedures are documented within the LINCS SSP. Security software features are used to automatically generate and store security audit log records for use in monitoring security-related events on all multi-user systems. The Department reviews and updates this policy as necessary and it was last updated in April 2008. Additional information is contained within the Department of Education Handbook for Information Assurance Security policy (Handbook OCIO-01).


### AU-2: Audit Events

> The organization:
>   a.  Determines that the information system is capable of auditing the following
> events: [Assignment: organization-defined auditable events];
>   b.  Coordinates the security audit function with other organizational entities
> requiring audit-related information to enhance mutual support and to help guide the selection of auditable events;
>   c.  Provides a rationale for why the auditable events are deemed to be adequate
> to support after-the-fact investigations of security incidents; and
>   d.  Determines that the following events are to be audited within the information
> system: [Assignment: organization-defined audited events (the subset of the auditable events defined in AU-2 a.) along with the frequency of (or situation requiring) auditing for each identified event].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


#### a

##### CivicActions

CivicActions' Security Policy provides information about auditing and logging of CivicActions internal users and end-user activity on the servers and within the system application.


##### Drupal

Transaction logs are generated by the Apache web server, Drupal CMS, MySQL database and PHP page processing.  Specifically, the following server, application, database and network device audit log events are captured:
• Apache access log :: Contains a list of requests for your website that have bypassed Varnish. These requests include pages, theme files, and static media files.
• Apache error log :: Records any Apache-level issues. The issues reported here are usually caused by general server issues, including capacity problems, .htaccess problems, and missing files.
• Drupal page request log :: Records all Drupal page loads on your website.
• Drupal watchdog log :: Records Drupal-related actions on your website. The watchdog log is recorded on your server if you have enabled the syslog module.
• MySQL slow query log :: Contains a list of MySQL queries that have taken longer than one second to complete.
• PHP error log :: Records any issues that occur during the PHP processing portion of a page load. Issues reported here are usually caused by a website’s code, configuration, or content.


#### b

##### CivicActions

Auditable events may change due to changes in the threat environment. CivicActions teams collaborate internally and also communicate with customers and partner organizations to identify and select auditable events. The teams that participate in this process are described in control SA-3(b).


##### Drupal

All security-related issues and events, including requests for server log analysis, are recorded in CivicActions' JIRA tracking system.


#### c

##### Drupal

CivicActions has extensive experience and specialization as a host of websites that are built using the Drupal web hosting platform. Our list of auditable events is also informed by the experience and advice of Drupal's security team, which receives security vulnerability reports and publishes security updates related to Drupal and the more than 1 million websites that use the Drupal platform.  Should the need for additional logging become evident, we have the ability to do so by modifying the website's source code to insert additional Drupal watchdog hooks.


#### d

##### Drupal

Information captured in the transaction logs includes, but is not limited to, the following auditable events:
• Failed login attempts
• Successful login attempts
• User account deletions
• User account blocking/unblocking
• Changes in user role assignments
• Unauthorized attempts to alter protected user fields
• New user account creation
• Password reset instructions mailed
• User logins via one-time login link
• User logouts
• Content creation (datasets, resources and other content types)
• Content modification
• Content deletion
• Content publishing
• Content unpublishing
• File uploads
• Web page not found
• Website configuration changes
• System administration activities
• Slow query logs.
• PHP error logs: Captures any errors logged during execution of the PHP programming
  language.


### AU-3: Content Of Audit Records

> The information system generates audit records containing information that establishes what type of event occurred, when the event occurred, where the event occurred, the source of the event, the outcome of the event, and the identity of any individuals or subjects associated with the event.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


##### Drupal

The logs collected for Drupal sites include the following types of information:
• IP number of the request originator
• Timestamp
• Request URL
• HTTP status code returned
• Username
• Drupal watchdog message (if applicable)
• Unique numerical ID of the content being modified (for content creation, modification and deletion events)
When auditing a Drupal incident, CivicActions' developers aggregate log sources from multiple servers into the Graylog dashboard so that all log entries for a single managed security incident can be analyzed in a single document. Log sources are sorted, filtered and reviewed.  Application logs are maintained primarily for after-the-fact investigation of critical system or security events.


### AU-4: Audit Storage Capacity

> The organization allocates audit record storage capacity in accordance with [Assignment: organization-defined audit record storage requirements].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: disk space availability.


##### CivicActions

CivicActions ensures adequate storage capability requirements listed in AU-11 for all events from the application, database, and hosting environment.


### AU-5: Response To Audit Processing Failures

> The information system:
>   a.  Alerts [Assignment: organization-defined personnel or roles] in the event
> of an audit processing failure; and
>   b.  Takes the following additional actions: [Assignment: organization-defined
> actions to be taken (e.g., shut down information system, overwrite oldest audit records, stop generating audit records)].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013: response to audit processing failures.
In the event of low storage or other system issues affecting audit, the AWS CloudWatch monitoring system will alert CivicActions Operations via real-time alert mechanism such as OpsGenie.


##### CivicActions

When notified (e.g., via CloudWatch) of an auditing failure, CivicActions Operations will review the causes and take corrective action.


### AU-6: Audit Review, Analysis, And Reporting

> The organization:
>   a.  Reviews and analyzes information system audit records [Assignment: organization-defined
> frequency] for indications of [Assignment: organization-defined inappropriate or unusual activity]; and
>   b.  Reports findings to [Assignment: organization-defined personnel or roles].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


#### a

##### CivicActions

CivicActions security audit data is collected by a Graylog Security and Event Management (SIEM) dashboard to support real-time and after-the-fact investigation at the application level for the following:
• Indications of inappropriate or unusual activity
• Assurance that logging is functioning properly
• Adherence to logging standards identified in this procedure


#### b

##### CivicActions

Any significant findings observed during the inspection are reported to CivicActions Security. If these are considered to constitute a security incident, then the Incident Response process is invoked as described in the implementation of the Incident Response Plan (IR-8).


### AU-8: Time Stamps

> The information system:
>   a.  Uses internal system clocks to generate time stamps for audit records; and
>   b.  Records time stamps for audit records that can be mapped to Coordinated
> Universal Time (UTC) or Greenwich Mean Time (GMT) and meets [Assignment: organization-defined granularity of time measurement].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


##### LINCS

The LINCS Technology Project system clocks are synchronized system-wide and provide time stamps with audit records.


### AU-9: Protection Of Audit Information

> The information system protects audit information and audit tools from unauthorized access, modification, and deletion.

##### AWS

This system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


##### CivicActions

CivicActions ensures that audit logs are created, stored and maintained. Developers who have been assigned as members of the CivicActions Security Team are the only CivicActions personnel with logical permission to access and review audit logs.


### AU-11: Audit Record Retention

> The organization retains audit records for [Assignment: organization-defined time period consistent with records retention policy] to provide support for after-the-fact investigations of security incidents and to meet regulatory and organizational information retention requirements.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


##### CivicActions

CivicActions audits events from the application, database, and hosting environment, and retains these records for at least 180 days.


### AU-12: Audit Generation

> The information system:
>   a.  Provides audit record generation capability for the auditable events defined
> in AU-2 a. at [Assignment: organization-defined information system components];
>   b.  Allows [Assignment: organization-defined personnel or roles] to select which
> auditable events are to be audited by specific components of the information system; and
>   c.  Generates audit records for the events defined in AU-2 d. with the content
> defined in AU-3.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


#### a

##### CivicActions

CivicActions ensures audit records are generated for its web and event logs as required in AU-2 and AU-3 for servers, application, database and network components.


#### b

##### CivicActions

The selected auditable events described in AU-2 are coordinated by CivicActions internal admins and client security/operations officers for each component of the production system.


#### c

##### CivicActions

CivicActions maintained applications generate audit records for their web and event logs as described in AU-2 and AU-3.


## CA: Security Assessment and Authorization

### CA-1: Security Assessment And Authorization Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A security assessment and authorization policy that addresses purpose,
> scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the security assessment
> and authorization policy and associated security assessment and authorization controls; and
>   b.  Reviews and updates the current:
>     1.  Security assessment and authorization policy [Assignment: organization-defined
> frequency]; and
>     2.  Security assessment and authorization procedures [Assignment: organization-defined
> frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a certification, accreditation, and security assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Security Assessment and Authorization Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


##### LINCS

The Department has published the Department of Education, Office of the Chief Information Officer, Handbook for Information Assurance Security Policy, Information Assurance Program (Handbook OCIO-01) and U. S. Department of Education Information Technology Security, Handbook for Information Technology Security, Certification and Accreditation Procedures (Handbook OCIO-05). Both of these publications are revised periodically. The LINCS System Security Policy (SSP) provides guidance on all aspects of security for the protection of LINCS information technology resources.
The Department will periodically review and update the SSP when there is a significant change to the regulatory, operational, or technical environment.


### CA-2: Security Assessments

> The organization:
>   a.  Develops a security assessment plan that describes the scope of the assessment
> including:
>     1.  Security controls and control enhancements under assessment;
>     2.  Assessment procedures to be used to determine security control effectiveness;
> and
>     3.  Assessment environment, assessment team, and assessment roles and responsibilities;
>   b.  Assesses the security controls in the information system and its environment
> of operation [Assignment: organization-defined frequency] to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting established security requirements;
>   c.  Produces a security assessment report that documents the results of the
> assessment; and
>   d.  Provides the results of the security control assessment to [Assignment:
> organization-defined individuals or roles].

#### a

##### CivicActions

CivicActions will develop a security assessment plan (SAP) that describes the security controls and control enhancements under assessment, assessment procedures used to determine effectiveness, the assessment environment, the assessment team, and the assessment roles and responsibilities.


##### LINCS

The LINCS Technology Project follows the U. S. Department of Education Information Technology Security, Handbook for Information Technology Security, Certification and Accreditation Procedures (Handbook OCIO-05) procedures.  The LINCS Technology Project will conduct annual security assessments to comply with FISMA and NIST regulations. The Department will draw on NIST Special Publications 800-53A security controls to complete the assessment. All controls and sub-set security controls will be evaluated and a risk assessment will be conducted. The scope of the assessment includes:
1. Security controls and control enhancements under assessment
2. Assessment procedures to be used to determine security control effectiveness
3. Assessment environment, assessment team, and assessment roles and responsibilities


#### b

##### CivicActions

CivicActions will assess the security controls in their system and its environment of operation to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting established security requirements,
All controls assigned and documented in this System Security Plan (SSP) will be tested at least annually or when there is a major change to the system.


#### c

##### CivicActions

CivicActions will produce a security assessment report that documents the results of the assessment. The Security Assessment Report must contain the results of the assessment, and may also contain recommendations and suggestions for plans of actions and milestones (POA&Ms).


##### LINCS

The LINCS Authorizing Official or Designated Representative will create a Security Assessment Report (SAR). A full assessment shall be conducted by an independent third party assessor at least every three years.


#### d

##### CivicActions

CivicActions will provide the results of the security control assessment to the System Owner, Project Manager, CivicActions Security, and the Authorization Official (AO)). The security control assessment package includes the following:
• Security Control Matrix
• Privacy Impact Assessment
• E-Authentication
• Contingency Plan
• Configuration Management Plan
• Rules of Behavior
• Incident Response Plan


### CA-3: System Interconnections

> The organization:
>   a.  Authorizes connections from the information system to other information
> systems through the use of Interconnection Security Agreements;
>   b.  Documents, for each interconnection, the interface characteristics, security
> requirements, and the nature of the information communicated; and
>   c.  Reviews and updates Interconnection Security Agreements [Assignment: organization-defined
> frequency].

##### CivicActions

This control is not applicable. CivicActions systems do not have system interconnections. The only communication conducted to CivicActions systems is through the Internet.


### CA-5: Plan Of Action And Milestones

> The organization:
>   a.  Develops a plan of action and milestones for the information system to document
> the organization�s planned remedial actions to correct weaknesses or deficiencies noted during the assessment of the security controls and to reduce or eliminate known vulnerabilities in the system; and
>   b.  Updates existing plan of action and milestones [Assignment: organization-defined
> frequency] based on the findings from security controls assessments, security impact analyses, and continuous monitoring activities.

##### CivicActions

CivicActions documents all deficiencies and vulnerabilities identified during the security certification and/or continuous monitoring phase (via security assessment, vulnerability scanning, risk assessment, etc.) within the Plan of Action and Milestones (POA&M).
The POA&M document provides a platform for CivicActions to monitor and track the deficiency and its mitigation strategy. POA&M items will include:
• The description of the deficiency,
• Dedicated point of contact for this deficiency.
• Cost of the mitigation strategy
• Associated risk and NIST control
• Recommended mitigation strategy
POA&Ms are tracked throughout the lifecycle of the system until its mitigation. All POA&Ms are reviewed on a monthly basis by CivicActions Information System Security Officer to ensure all mitigation strategies are continuing as documented.


##### LINCS

The LINCS Technology Project follows the U.S. Department of Education Information Technology Security, Handbook for Information Technology Security, Certification and Accreditation Procedures (Handbook OCIO-05) procedures in managing POA&Ms.


### CA-6: Security Authorization

> The organization:
>   a.  Assigns a senior-level executive or manager as the authorizing official
> for the information system;
>   b.  Ensures that the authorizing official authorizes the information system
> for processing before commencing operations; and
>   c.  Updates the security authorization [Assignment: organization-defined frequency].

##### LINCS

The LINCS Technology Project follows the Department of Education, Office of the Chief Information Officer, Handbook for Information Assurance Security Policy, Information Assurance Program (Handbook OCIO-01) and U. S. Department of Education Information Technology Security, Handbook for Information Technology Security, Certification and Accreditation Procedures (Handbook OCIO-05) procedures. The LINCS Technology Project system received its first three-year security accreditation on March 3, 2009, and most recently received an ATO on February 5, 2016.
ATO re-assessment will be performed every three years or when there is a major change to the application, in which a senior organizational official will sign and approve the security accreditation.


### CA-7: Continuous Monitoring

> The organization develops a continuous monitoring strategy and implements a continuous monitoring program that includes:
>   a.  Establishment of [Assignment: organization-defined metrics] to be monitored;
>   b.  Establishment of [Assignment: organization-defined frequencies] for monitoring
> and [Assignment: organization-defined frequencies] for assessments supporting such monitoring;
>   c.  Ongoing security control assessments in accordance with the organizational
> continuous monitoring strategy;
>   d.  Ongoing security status monitoring of organization-defined metrics in accordance
> with the organizational continuous monitoring strategy;
>   e.  Correlation and analysis of security-related information generated by assessments
> and monitoring;
>   f.  Response actions to address results of the analysis of security-related
> information; and
>   g.  Reporting the security status of organization and the information system
> to [Assignment: organization-defined personnel or roles] [Assignment: organization-defined frequency].

#### a

##### CivicActions

CivicActions implements a continuous monitoring strategy that incorporates configuration management, system scanning and log analysis processes:
• Configuration management includes the assessment of security impact analyses of
  proposed and implemented changes.

• System scanning is managed by running the OpanSCAP vulnerability scanner using the
  DISA STIG profile.

• Log analysis is managed by feeding logs to a Graylog dashboard for analysis.


##### Drupal

CivicActions follows recommendations and best practices developed by the Drupal community for monitoring. Examples of specific logs and metrics are included in AU-2 and AU-3.


#### b

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: continuous monitoring.


##### CivicActions

Configuration management and log analysis is real time. OpenSCAP security scans are performed and reviewed monthly. See also: RA-5 and SI-4.
Quarterly review of the control assessments supporting the monitoring is conducted by CivicActions Operations in collaboration with CivicActions Security.


#### c

##### Drupal

CivicActions works closely with the Drupal security community and reviews security announcements as part of the continuous monitoring strategy. Items found to require immediate remediation will be addressed.


#### d

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: ongoing security status monitoring.


##### CivicActions

CivicActions conducts or oversees continuous system security monitoring.


#### e

##### CivicActions

CivicActions Security reviews the results of the security scans and security assessments with associated JIRA and/or GitLab Issue tickets created to correlate and analyze security related information generated from the monitoring tools becoming POA&M items for tracking.


#### f

##### CivicActions

POA&M items are tracked by CivicActions Security though JIRA tickets with a security categorization assigned.  Information included in the POA&M item include the severity, the due date, the weakness source identifier, and the plugin ID that identified the vulnerability.


#### g

##### CivicActions

The security status of the system is reported up to the System Owner and Project Manager via CivicActions Security to be reviewed alongside other security issues relating to the system.


### CA-9: Internal System Connections

> The organization:
>   a.  Authorizes internal connections of [Assignment: organization-defined information
> system components or classes of components] to the information system; and
>   b.  Documents, for each internal connection, the interface characteristics,
> security requirements, and the nature of the information communicated.

##### AWS

Not applicable: There are no internal systems that connect to the FedRAMP certified AWS cloud.


## CM: Configuration Management

### CM-1: Configuration Management Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A configuration management policy that addresses purpose, scope, roles,
> responsibilities, management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the configuration management
> policy and associated configuration management controls; and
>   b.  Reviews and updates the current:
>     1.  Configuration management policy [Assignment: organization-defined frequency];
> and
>     2.  Configuration management procedures [Assignment: organization-defined
> frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a configuration management policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Configuration Management (CM) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.
Configuration changes are overseen by the Change Control Board (CCB) consisting of the System Owner, Project Manager and CivicActions Development.


##### LINCS

The configuration management policy and procedures are formally documented in the LINCS Technology Project Configuration Management Plan (CMP), which provides the roles and responsibilities as it pertains to physical and environmental protection. It defines responsibilities for the implementation and oversight of the guidance contained herein. The Department reviews and updates the policy as necessary.
Additional information is contained within the Department of Education, Handbook forInformation Technology Security Configuration Management Planning Procedures (Handbook OCIO-11).


### CM-2: Baseline Configuration

> The organization develops, documents, and maintains under configuration control, a current baseline configuration of the information system.

##### AWS

Hardware Baselines
All hardware is maintained by AWS Cloud. The system therefore inherits hardware configuration aspects of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: baseline configuration.


##### CivicActions

A current baseline configuration is always available - stored as a tag in the Git repository - such that the site can be regenerated or rolled back should unauthorized or failing changes be applied.


##### Drupal

The baseline configuration is maintained in Git and described in the Configuration Management Plan, which describes the change workflow and software configuration. In the context of Security Configuration Management, the baseline configuration is a collection of formally approved configuration state(s) of one or more configuration items ("features") that compose the system. The baseline configuration is used to restore and serves as the basis against which the next change or set of changes to the system is made.
The features for the system are maintained in the website's source code, which is managed in git, a source code version control system. Once the source code is updated, git maintains the new version of staged code once committed in the git repository as the new baseline. All code prior to it being staged is documented, tested and approved by CivicActions Development, which is described in control SA-3. The production environment is configured to take database snapshots daily.


##### LINCS

A CM process has been established and documented in the LINCS Technology Project CMP. All updates are made in accordance with the procedures outlined in the CMP.  The CM process establishes a baseline of hardware, software, firmware and documentation, as well as changes thereto, throughout the development and life cycle of the information system. CM ensures the control of the information system through its life cycle. It assures that additions, deletions, or changes made to the LINCS Technology Project system do not unintentionally or unknowingly diminish security. If the change is major, the security of the system must be re-analyzed.


### CM-2 (1): Reviews And Updates

> The organization reviews and updates the baseline configuration of the information system:
>    (1)(a).  [Assignment: organization-defined frequency];
>    (1)(b).  When required due to [Assignment organization-defined circumstances];
> and
>    (1)(c).  As an integral part of information system component installations
> and upgrades.

##### Drupal

CivicActions reviews and updates baseline configurations for the system at least annually, when requested by the System Owner or required by law, and as an integral part of information system component installations, upgrades and maintenance.
Review of the CM baselines for the system is conducted and approved by CivicActions Development. Any changes made to the production environment are approved prior to deployment by the CCB or agile scrum process. Changes that may require updates to the baseline configuration for the application include:
• Significant upgrades or changes to applications or database software
• Security assessment findings
• Changes in internal/external security requirements
• A new security threat, incident, or event


### CM-2 (2): Automation Support For Accuracy / Currency

> The organization employs automated mechanisms to maintain an up-to-date, complete, accurate, and readily available baseline configuration of the information system.

##### Drupal

Drupal configuration settings use automated mechanisms to automate code deployment and baseline settings changes. The website's baseline configuration may be reapplied to the site at any time by manually retriggering a tagged code deployment.
The source code, which contains the site’s baseline configuration, is managed using git, a source code version control system. Git is used to track source code which allows administrators to easily deploy and roll back changes on production hosting environments.
The Features module is used to export configuration settings from the website's MySQL database and stores them as code so that the configuration settings can be managed within the git source code version control system.


### CM-2 (3): Retention Of Previous Configurations

> The organization retains [Assignment: organization-defined previous versions of baseline configurations of the information system] to support rollback.

##### Drupal

Previous baseline configurations are retained in git, which implements unlimited revision control. Each version of the codebase is given a unique tag when it is deployed to production. When new features are ready for deployment to production, the new code release is given a new tag. This makes it possible to roll back to a previous version of the baseline configuration if needed by redeploying the older release tag.


### CM-3: Configuration Change Control

> The organization:
>   a.  Determines the types of changes to the information system that are configuration-controlled;
>   b.  Reviews proposed configuration-controlled changes to the information system
> and approves or disapproves such changes with explicit consideration for security impact analyses;
>   c.  Documents configuration change decisions associated with the information
> system;
>   d.  Implements approved configuration-controlled changes to the information
> system;
>   e.  Retains records of configuration-controlled changes to the information system
> for [Assignment: organization-defined time period];
>   f.  Audits and reviews activities associated with configuration-controlled changes
> to the information system; and
>   g.  Coordinates and provides oversight for configuration change control activities
> through [Assignment: organization-defined configuration change control element (e.g., committee, board)] that convenes [Selection (one or more): [Assignment: organization-defined frequency]; [Assignment: organization-defined configuration change conditions]].

##### CivicActions

In accordance with the Configuration Management Plan and control SA-3, CivicActions manages changes to the baseline configuration of the application through an agile scrum-based process.  Examples of the types of changes that may be introduced through a code release include the following, ordered by increasing level of possible security risk:
1. Minor application code changes
2. New software releases for Drupal core, contributed Drupal modules, or other software components that are supplied by outside open source vendors
3. Significant software enhancement
4. Major application modification
The CCB meets bi-weekly during the sprint planning and backlog grooming meetings. In addition, the System Owner or Project Manager may convene the CCB in an emergency session to address time-critical topics as deemed necessary.


#### b

##### CivicActions

In accordance with the Configuration Management Plan, CivicActions performs security impact analysis of all planned code releases. Level of impact is assessed by CivicActions Development in collaboration with CivicActions Security before the planned code updates are presented at the sprint planning meeting for approval. Significant software enhancements and major application modifications require approval from the Tech Lead of the Development team. Once a code release is considered ready for deployment, a Security Review is done before scheduling deployment of the code release to production, in accordance with the Agile-based System Development Life Cycle methodology described in SA-3.


#### c

##### CivicActions

Configuration changes follow the CivicActions sprint planning process. The changes themselves are documented within a JIRA ticket tracking system. The JIRA ticket has an approval step built into the ticketing workflow that is required before the implementation phase. The CCB (agile sprint planning process) is responsible for reviewing the change and either approving or rejecting the proposal. These workflow changes are captured within an audit log in the ticket, and are available to anyone viewing the ticket.


#### d

##### CivicActions

See part b). Configuration changes are captured within tickets in the CivicActions ticketing system. Each CR follows a specific workflow within the ticketing system that follows our process:
1. Open (Backlog)
2. To Do
3. In Progress
4. QA
5. Signoff
All CRs must be approved before they are applied to the information system.


#### e

##### CivicActions

All changes are logged and retained for a minimum of three years in the ticketing system. The Change Request (CR) tickets contain a detailed record of the steps taken to implement the change, as well as dates of approval and implementation.


#### f

##### CivicActions

All changes are logged and retained for a minimum of three years in the ticketing system. The Change Request (CR) tickets contain a detailed record of the steps taken to implement the change, as well as dates of approval and implementation.


#### g

##### CivicActions

The CivicActions Change Control Board (or agile Sprint Planning team) meets bi-weekly, or when operational or security imperatives require, to address requested changes to the application.


### CM-3 (2): Test / Validate / Document Changes

> The organization tests, validates, and documents changes to the information system before implementing the changes on the operational system.

##### CivicActions

CivicActions tests and validates changes to the system before implementing the changes in production. Changes are documented as code and comments in the git source code version control system. Any changes made to system are first captured in a separate development branch of git that is used to create a pull request, which is reviewed for quality and security control before being merged into the master branch of the repository.


### CM-4: Security Impact Analysis

> The organization analyzes changes to the information system to determine potential security impacts prior to change implementation.

##### CivicActions

Security impact analysis is conducted and documented within the Change Request (CR) process described in in CM-3(b). All proposed configuration-controlled changes to the application are tested first in a sandboxed development environment before being pushed to a staging environment to be tested by another developer and by the Engineering team prior to final approval from CCB to move changes to the production environment.


##### LINCS

An Information Security Program is in place to ensure all security-centric impacts to the LINCS Technology Project are properly analyzed and conducted by personnel with information security responsibilities (i.e., LINCS SSO, IT Security Officer, etc.). These individuals have the appropriate skills and technical expertise to analyze the changes to the LINCS Technology Project and their associated security ramifications. In support of continuous monitoring and to ensure the LINCS Technology system lifecycle is fully sustained, a risk assessment process, be it formal or informal, is performed when changes are occur. This ensures the Department understands the security impacts and can determine if additional security controls are required.


### CM-5: Access Restrictions For Change

> The organization defines, documents, approves, and enforces physical and logical access restrictions associated with changes to the information system.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: physical and logical access restrictions to server instances. Development and staging environments are logged by default as part of the AWS Cloud system.


##### CivicActions

CivicActions restricts system logical access to only those internal personnel assigned to work on the application. Logical access is governed by the implementation described in AC-3 and the concept of least privilege requirements implemented by AC-6.
All access to server environments is via encrypted SSH session with public-key authentication, and all server access is logged.


### CM-5 (1): Automated Access Enforcement / Auditing

> The information system enforces access restrictions and supports auditing of the enforcement actions.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: automated access enforcement / access.


##### Drupal

Access enforcement is monitored within Drupal, which records an entry in the Drupal watchdog log for every successful or failed login attempt to the system.  Each successful login or logout event is logged with an entry that includes the username of the account being used.
All access to server environments is via encrypted SSH sessions with public-key authentication, and all server access is logged.  Specific implementation of auditing events are captured in AU-2. The same access control procedures and need-to-know and accountability principles are enforced for all systems storing baseline configuration policies.


### CM-5 (5): Limit Production / Operational Privileges

> The organization:
>    (5)(a).  Limits privileges to change information system components and system-related
> information within a production or operational environment; and
>    (5)(b).  Reviews and reevaluates privileges [Assignment: organization-defined
> frequency].

#### a

##### Drupal

Configuration changes that do not entail software code changes can only be performed by CivicActions internal administrators with privileges implemented by access enforcement (AC-3) and least privilege (AC-6).


#### b

##### CivicActions

CivicActions internal administrators user access rights are reviewed at least quarterly by CivicActions Information Security, which is responsible for approving all user account assignments to CivicActions developers.


### CM-6: Configuration Settings

> The organization:
>   a.  Establishes and documents configuration settings for information technology
> products employed within the information system using [Assignment: organization-defined security configuration checklists] that reflect the most restrictive mode consistent with operational requirements;
>   b.  Implements the configuration settings;
>   c.  Identifies, documents, and approves any deviations from established configuration
> settings for [Assignment: organization-defined information system components] based on [Assignment: organization-defined operational requirements]; and
>   d.  Monitors and controls changes to the configuration settings in accordance
> with organizational policies and procedures.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: configuration settings.


##### Drupal

CivicActions configuration settings for Drupal are guided by the Drupal Security Coding Standards <https://www.drupal.org/docs/develop/security> for the security configuration management processes and tools.


#### a

##### LINCS

The LINCS Technology Project is configured in compliance with the applicable baseline security standards. The Department and its technical support staff configure the security settings of all IT products to the most restrictive mode consistent with information system operational requirements. The Department utilizes the NIST Special Publication 800-70 for guidance on configuration settings (checklists) for information technology products. When security setting checklist are not available from NIST for a particular device, good security engineering practices along with manufacture guidelines is used to develop the security settings. The CM Manager conducts configuration audits to ensure baseline compliance and documentation of hardware/software configurations throughout the system lifecycle.


#### b

##### CivicActions

CivicActions developers follow security best practices according to the guidelines set by CivicActions Information Security.


##### LINCS

Configuration settings are implemented, monitored, and controlled in accordance with the organizational Configuration Management Plan for the security configuration management processes and tools.


#### c

##### LINCS

Currently, deviations do not exist for established configuration settings. In the event this changes, the following notes the process that will take place.
The CivicActions CCB, identifies, approves, and documents exceptions to mandatory configuration settings for individual components within its cloud offering only when operationally necessary. All variances identified during the monthly and annual system testing scans that must be accepted for operational purposes are tracked.


#### d

##### CivicActions

All changes to the configuration settings are logged in the Git source code version control system, which records the identity of the developer who committed each change. Version control is enforced, with previous tagged code releases kept for rollback purposes.


### CM-7: Least Functionality

> The organization:
>   a.  Configures the information system to provide only essential capabilities;
> and
>   b.  Prohibits or restricts the use of the following functions, ports, protocols,
> and/or services: [Assignment: organization-defined prohibited or restricted functions, ports, protocols, and/or services].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: least functionality.


#### a

##### LINCS

Services are limited to provide only essential capabilities.


#### b

##### LINCS

The LINCS Technology Project maintains strict default deny policy with access controls at the firewall, and on individual systems. Inbound access across the system boundary is only allowed on ports 22 (ssh), 80 (http) and 443 (https), with an additional port, 25 (smtp) open on the mail server.


### CM-8: Information System Component Inventory

> The organization:
>   a.  Develops and documents an inventory of information system components that:
>     1.  Accurately reflects the current information system;
>     2.  Includes all components within the authorization boundary of the information
> system;
>     3.  Is at the level of granularity deemed necessary for tracking and reporting;
> and
>     4.  Includes [Assignment: organization-defined information deemed necessary
> to achieve effective information system component accountability]; and
>   b.  Reviews and updates the information system component inventory [Assignment:
> organization-defined frequency].

##### AWS

The system inherits the platform software components of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: information system component inventory.


##### Drupal

The software inventory for the application is maintained in the codebase stored CivicActions' git source code version control system. It consists of the following components:
• The Drupal open source web content management system
• Drupal add-on modules, themes and libraries available from the Drupal.org website which extend Drupal core
• Custom code written by CivicActions' developers
The inventory is reviewed monthly by CivicActions Product Engineering teams in accordance with the Configuration Management Plan.
Website content is backed up daily using CPM snapshots. This allows CivicActions to build an inventory of the system on demand.


### CM-8 (1): Updates During Installations / Removals

> The organization updates the inventory of information system components as an integral part of component installations, removals, and information system updates.

##### AWS

Website content is backed up daily by the AWS Managed Cloud hosting system, which is configured to take daily database snapshots
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: components inventory updates.


##### CivicActions

CivicActions stores all software code in a git source version control repository which is updated for all component installations, removals, and information system updates. This allows CivicActions to build an inventory of the system on demand.


### CM-9: Configuration Management Plan

> The organization develops, documents, and implements a configuration management plan for the information system that:
>   a.  Addresses roles, responsibilities, and configuration management processes
> and procedures;
>   b.  Establishes a process for identifying configuration items throughout the
> system development life cycle and for managing the configuration of the configuration items;
>   c.  Defines the configuration items for the information system and places the
> configuration items under configuration management; and
>   d.  Protects the configuration management plan from unauthorized disclosure
> and modification.

##### LINCS

The LINCS Configuration Management Plan addresses roles, responsibilities, and configuration management processes and procedures. It defines the configuration items for the information system throughout the system development life cycle and a process for managing the configuration of the configuration items.


### CM-10: Software Usage Restrictions

> The organization:
>   a.  Uses software and associated documentation in accordance with contract agreements
> and copyright laws;
>   b.  Tracks the use of software and associated documentation protected by quantity
> licenses to control copying and distribution; and
>   c.  Controls and documents the use of peer-to-peer file sharing technology to
> ensure that this capability is not used for the unauthorized distribution, display, performance, or reproduction of copyrighted work.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013 for the following: software usage restrictions.


##### Drupal

Drupal is hosted on a LAMP platform (Linux, Apache, MySQL and PHP). These are all compatible with the Free Software Foundation's General Public License (GPL) version 2 or later and are freely available for use under copyright law.


### CM-11: User-Installed Software

> The organization:
>   a.  Establishes [Assignment: organization-defined policies] governing the installation
> of software by users;
>   b.  Enforces software installation policies through [Assignment: organization-defined
> methods]; and
>   c.  Monitors policy compliance at [Assignment: organization-defined frequency].

#### a

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013 for the following: governing user installed software.


##### CivicActions

All software installed in the system environment must be first approved via the CCB resulting in a Change Request (CR) being initiated and executed. Software installation on the computing nodes within the authorization boundary is restricted to administrators. All CivicActions internal administrators are informed of this during their initial training and as part of the rules of behavior document.


#### b

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013 for the following: enforcing software installation policies.


##### CivicActions

CivicActions enforces software installation policies through required acknowledgement and sign-off on acceptable use policy by CivicActions personnel. CivicActions Development is responsible for enforcing compliance with the acceptable use policy.


#### c

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013 for the following: monitoring compliance.


##### CivicActions

CivicActions monitors policy compliance continuously via the code release planning and quality control systems built into the System Development Life Cycle described in control SA-3.


## CP: Contingency Planning

### CP-1: Contingency Planning Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A contingency planning policy that addresses purpose, scope, roles, responsibilities,
> management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the contingency planning
> policy and associated contingency planning controls; and
>   b.  Reviews and updates the current:
>     1.  Contingency planning policy [Assignment: organization-defined frequency];
> and
>     2.  Contingency planning procedures [Assignment: organization-defined frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a contingency planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in Contingency Planning (CP) Policy and Procedure that can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>. 


##### LINCS

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.
The LINCS Technology Project has developed a contingency planning policy consistent with Department of Education, Handbook for Information Technology Security Contingency Planning Procedures (Handbook OCIO-10) and NIST 800-34. Contingency planning procedures are formally documented within the LINCS Technology Project Contingency Plan, which provides the roles and responsibilities as it pertains to contingency planning. The Department reviews and updates the policy as necessary and the policy was last updated in July 2012.


### CP-2: Contingency Plan

> The organization:
>   a.  Develops a contingency plan for the information system that:
>     1.  Identifies essential missions and business functions and associated contingency
> requirements;
>     2.  Provides recovery objectives, restoration priorities, and metrics;
>     3.  Addresses contingency roles, responsibilities, assigned individuals with
> contact information;
>     4.  Addresses maintaining essential missions and business functions despite
> an information system disruption, compromise, or failure;
>     5.  Addresses eventual, full information system restoration without deterioration
> of the security safeguards originally planned and implemented; and
>     6.  Is reviewed and approved by [Assignment: organization-defined personnel
> or roles];
>   b.  Distributes copies of the contingency plan to [Assignment: organization-defined
> key contingency personnel (identified by name and/or by role) and organizational elements];
>   c.  Coordinates contingency planning activities with incident handling activities;
>   d.  Reviews the contingency plan for the information system [Assignment: organization-defined
> frequency];
>   e.  Updates the contingency plan to address changes to the organization, information
> system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing;
>   f.  Communicates contingency plan changes to [Assignment: organization-defined
> key contingency personnel (identified by name and/or by role) and organizational elements]; and
>   g.  Protects the contingency plan from unauthorized disclosure and modification.

#### a

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: contingency plan.


##### CivicActions

CivicActions has developed a contingincy plan for that addresses:
1. Essential missions, business functions and associated contingency requirements
2. Recovery objectives, restoration priorities, and metrics
3. Roles and responsibilities are identified in the CP and includes the ISCP Director, Incident Commander (IC), CivicActions Coordinator, and CivicActions Information System Security Officer (ISSO).
4. Maintaining essential missions and business functions despite an information system disruption, compromise, or failure
5. Full information system restoration without deterioration of the security safeguards originally planned and implemented
6. The ISCP is reviewed and approved by ISCP Director, Incident Commander (IC), CivicActions ISSO and the System Owner annually.


#### b

##### CivicActions

The CivicActions Information System Contingency Plan (ISCP) has been distributed to all CivicActons team members. The ISCP can be found in the CivicActions Handbook at <https://civicactions-handbook.readthedocs.io/en/latest/09-security/contingency-plan/>.


##### LINCS

The LINCS Information System Contingency Plan (ISCP) has been distributed to all members who have roles in Contingency Planning and Incident Response team. Direction by the System Owner will update who is required to receive a copy of the contingency plan. The ISCP can be found in the LINCS GitHub wiki at <https://git.civicactions.net/lincs/compliance/blob/master/docs/contingency-plan.md>.


#### c

##### CivicActions

The Information System Contingency Plan (ISCP) is closely integrated with the Incident Response Plan (IRP). Coordination is the responsibility of the ISCP Director and CivicActions Operations.


#### d

##### CivicActions

The ISCP Director and CivicActions Security are responsible to review the ISCP annually and when a change to the system occurs.


#### e

##### CivicActions

CivicActions Operations and ISCP Director are required to update the ISCP to address changes to the organization, information system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing.


#### f

##### CivicActions

The ISCP requires that changes to the plan be communicated to those on the Incident Response / Contingency Plan Contact List.


#### g

##### CivicActions

The ISCP is available on CivicActions Github repository.  This repository provides the configuration management capabilities for the ISCP to be protected from unauthorized disclosure and modification.


### CP-3: Contingency Training

> The organization provides contingency training to information system users consistent with assigned roles and responsibilities:
>   a.  Within [Assignment: organization-defined time period] of assuming a contingency
> role or responsibility;
>   b.  When required by information system changes; and
>   c.  [Assignment: organization-defined frequency] thereafter.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: contingency plan training.


##### CivicActions

The ISCP stipulates that all CivicActions system assigned roles in the Contingency Plan Team are trained in their duties within three months of first being assigned a role in the CP, and then annually thereafter or when changes are required. CivicActions uses the Contingency Plan as described in controls CP-1 and CP-2 as a basis for personnel contingency training.


### CP-4: Contingency Plan Testing

> The organization:
>   a.  Tests the contingency plan for the information system [Assignment: organization-defined
> frequency] using [Assignment: organization-defined tests] to determine the effectiveness of the plan and the organizational readiness to execute the plan;
>   b.  Reviews the contingency plan test results; and
>   c.  Initiates corrective actions, if needed.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: contingency plan testing.


##### CivicActions

Real world tests of the contingency plan will be held at least annually, with supplemental tests (checklist/table-top) as needed for specific scenarios. The ISCP Coordinator is responsible to facilitate annual testing exercises. The testing process for the ISCP includes review of the ISCP, exercise and identification of corrective actions and other improvements.


### CP-6: Alternate Storage Site

> The organization:
>   a.  Establishes an alternate storage site including necessary agreements to
> permit the storage and retrieval of information system backup information; and
>   b.  Ensures that the alternate storage site provides information security safeguards
> equivalent to that of the primary site.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: alternate storage site


### CP-6 (1): Separation From Primary Site

> The organization identifies an alternate storage site that is separated from the primary storage site to reduce susceptibility to the same threats.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: alternate storage site separation.


### CP-9: Information System Backup

> The organization:
>   a.  Conducts backups of user-level information contained in the information
> system [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives];
>   b.  Conducts backups of system-level information contained in the information
> system [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives];
>   c.  Conducts backups of information system documentation including security-related
> documentation [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives]; and
>   d.  Protects the confidentiality, integrity, and availability of backup information
> at storage locations.

#### a

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: user level backup requirements.


##### CivicActions

CivicActions conducts system user-level information backup in accordance with requirements (at a minimum, incremental backups must be conducted at least weekly and full backups must be conducted at least monthly).


#### b

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: system level backup requirements.


##### CivicActions

System level information for the application is replicated and backed up in the same way as user-level information as defined in CP-9(a).


#### c

##### CivicActions

System documentation is backed up from the GitHub repository on a daily basis with a minimum two-week retention period and off-site storage.


#### d

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: protection of backup information.


##### CivicActions

CivicActions employees must authenticate prior to being granted access to the GitHub repository. Roles and responsibilities within GitHub determine the proper level of access for the documentation being accessed. The folder structure of GitHub protects though permissions and ownership prohibiting users from accessing unauthorized documentation.


### CP-10: Information System Recovery And Reconstitution

> The organization provides for the recovery and reconstitution of the information system to a known state after a disruption, compromise, or failure.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: information system recovery and reconstitution.


##### CivicActions

The Contingency Plan documents the mechanisms with supporting procedures that allow all system components to be recovered and reconstituted to the system’s original state after a disruption or failure. This original state means that all system parameters (either default or organization-established) are reset, patches are reinstalled, system and security configuration settings are reestablished, system documentation and operating procedures are available, application and system software is reinstalled, information from the most recent backups is available and the system is fully tested.


## IA: Identification and Authentication

### IA-1: Identification And Authentication Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  An identification and authentication policy that addresses purpose, scope,
> roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the identification and
> authentication policy and associated identification and authentication controls; and
>   b.  Reviews and updates the current:
>     1.  Identification and authentication policy [Assignment: organization-defined
> frequency]; and
>     2.  Identification and authentication procedures [Assignment: organization-defined
> frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel an identification and authentication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained the CivicActions Identification and Authentication (IA) Policy. This document can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.


##### LINCS

The LINCS Technology Project complies with identification and authentication policies contained within the Department of Education, Handbook for Information Assurance Security Policy (Handbook OCIO-01).
The LINCS system owners/managers manage user identifiers by: (i) uniquely identifying each user; (ii) verifying the identity of each user; (iii) receiving authorization to issue a user identifier from an appropriate official; (iv) ensuring that the user identifier is issued to the intended party; (v) disabling user identifier after a reasonable period of inactivity as documented in its security procedures; and (vi) archiving user identifiers. The Department reviews and updates this policy as necessary.


### IA-2: Identification And Authentication (Organizational Users)

> The information system uniquely identifies and authenticates organizational users (or processes acting on behalf of organizational users).

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: Identification and Authentication procedures for personnel who have rights to AWS platform.


##### CivicActions

Privileged users of the system are required to identify and authenticate in order to access any functions of the information system beyond viewing and downloading the publicly available website content that is available to all anonymous website visitors. Privileged users require the appropriate authorization described in AC-2.


##### Drupal

Drupal users authenticate using the standard login protocol prior to using application services. User roles are described in AC-3.
Privileged Drupal accounts can only be created by existing website users with the role of "administrator". Administrator users assign roles to each login account that govern the user's ability to create, publish, update or delete website content.


##### LINCS

The LINCS Technology Project system uniquely identifies and authenticates all privileged and program users. This is accomplished through the use of unique user identification and a secret user password. All user IDs are maintained in a database by the system administrator and no identical IDs may be issued.
Password requirements are listed under security control IA-5.


### IA-2 (1): Network Access To Privileged Accounts

> The information system implements multifactor authentication for network access to privileged accounts.

##### LINCS

The LINCS Technology Project system does not process sensitive information, thus it does not employ multifactor authentication.
Access to system services - SSH for GNU/Linux instances, RDP for Windows - is managed by a set of firewall rules on the systems. The network firewall is configured to only allow users to connect to these services from a configured and audited IP address.


### IA-2 (12): Acceptance Of Piv Credentials

> The information system accepts and electronically verifies Personal Identity Verification (PIV) credentials.

##### LINCS

The LINCS Technology Project system does not implement logical access control systems (LACS) or physical access control systems (PACS). Therefore Personal Identity Verification (PIV) credentials have not been issued for users.


### IA-3: Device Identification And Authentication

> The information system uniquely identifies and authenticates [Assignment: organization-defined specific and/or types of devices] before establishing a [Selection (one or more): local; remote; network] connection.

##### CivicActions

CivicActions systems do not support or allow device-to-device communications.


### IA-4: Identifier Management

> The organization manages information system identifiers by:
>   a.  Receiving authorization from [Assignment: organization-defined personnel
> or roles] to assign an individual, group, role, or device identifier;
>   b.  Selecting an identifier that identifies an individual, group, role, or device;
>   c.  Assigning the identifier to the intended individual, group, role, or device;
>   d.  Preventing reuse of identifiers for [Assignment: organization-defined time
> period]; and
>   e.  Disabling the identifier after [Assignment: organization-defined time period
> of inactivity].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: identifier management.


#### a

##### CivicActions

Access to the system is authorized by the System Owner or Project Manager for each role as described in AC-2.


##### Drupal

Upon account creation, the Drupal software assigns each user account a unique numerical user ID (uid). This uid is used internally by the system to track user actions such as content creation or editing. The numerical user IDs are never reused even if their user accounts are subsequently blocked or deleted.


#### b

##### CivicActions

User accounts are assigned a unique identifier in the form of a unique username, password and email address based on the system for allocating user accounts described in AC-2.
In accordance with CivicActions Identification and Authentication (IA) Policy <https://github.com/CivicActions/compliance-docs/blob/master/IA-Policy.md>, CivicActions internal users are uniquely identified by creation of an organizational account with a username based on each user's first and last names.


##### Drupal

When Drupal user accounts are created, users' email addresses are verified by sending a single-use activation link to the user’s mailbox. The email recipient then uses the activation link to log in to the website and supply a password which must meet the system's password complexity requirements.


#### c

##### CivicActions

User accounts are assigned a unique identifier in the form of a unique username, password and email address based on the system for allocating user accounts described in AC-2.


##### Drupal

Identifiers for CivicActions internal personnel include a username based on the individual's full first and last name and are reviewed for uniqueness by the admin group when it approves creation of the user account.


#### d

##### CivicActions

Account usernames may not be re-used for at least two years.


##### Drupal

Drupal users unique identifier (the numeric user id, or uid) is never reused.


#### e

##### CivicActions

All user accounts are required to change their passwords every 90 days. The website will automatically block the accounts of users who fail to change their password within that time period, after which the account may only be unblocked by a website Administrator or CivicActions Operations.


### IA-5: Authenticator Management

> The organization manages information system authenticators by:
>   a.  Verifying, as part of the initial authenticator distribution, the identity
> of the individual, group, role, or device receiving the authenticator;
>   b.  Establishing initial authenticator content for authenticators defined by
> the organization;
>   c.  Ensuring that authenticators have sufficient strength of mechanism for their
> intended use;
>   d.  Establishing and implementing administrative procedures for initial authenticator
> distribution, for lost/compromised or damaged authenticators, and for revoking authenticators;
>   e.  Changing default content of authenticators prior to information system installation;
>   f.  Establishing minimum and maximum lifetime restrictions and reuse conditions
> for authenticators;
>   g.  Changing/refreshing authenticators [Assignment: organization-defined time
> period by authenticator type];
>   h.  Protecting authenticator content from unauthorized disclosure and modification;
>   i.  Requiring individuals to take, and having devices implement, specific security
> safeguards to protect authenticators; and
>   j.  Changing authenticators for group/role accounts when membership to those
> accounts changes.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: authenticator management.


#### a

##### Drupal

Refer to control AC-2 in this SSP for further details on account provisioning.
CivicActions will create and maintain an initial Drupal Administrator (highest level of Drupal Account). New Administrators are able to provide additional Administrator access at their own discretion, and are ultimately responsible for managing their own Administrator and other user accounts that they create.


##### LINCS

Authentication for LINCS internal personnel are created during the personnel assignment process where requests are made to the LINCS admin group for proper access levels. The LINCS admin group verifies the identity of the user. The website performs further verification by sending an email to the user's mailbox containing a single-use activation link which must be used to log in to the account for the first time and to create a password.


#### b

##### Drupal

Initial authenticator content (a unique email address – not previously used in any other account) is provided by the user. Internal initial password requirements set by CivicActions Operations and ongoing password refreshes by internal user follow the requirements set in the Identification and Authentication Policy.


##### LINCS

LINCS admins in collaboration with CivicActions Operations are responsible for provisioning and de-provisioning end user accounts in compliance with the authentication requirements described herein.


#### c

##### Drupal

The system partially inherits this control from Drupal standard password strength mechanisms.


##### LINCS

When entering a user account password upon initial login to lincs.ed.gov, all users must comply with the following password policies, which are enforced by the website's software configuration:
• Password must be at least 14 characters in length.
• Password must contain at least one digit.
• Password must contain at least one special character (not whitespace or an alphanumeric).
• Password must contain at least one uppercase character.
• Password must contain at least one lowercase character.


#### d

##### Drupal

The system partially inherits this control from Drupal standard password management.
All password creation/change/reset operations are recorded in the website's "Drupal watchdog" logs.


##### LINCS

LINCS is responsible for provisioning and de-provisioning end user accounts, which must comply with the strict password policies that are enforced by the website's software configuration, as described in IA-5(d).
In accordance with LINCS site configuration, the following administrative procedures exist for initial authenticator distribution, for lost/compromised/damaged authenticators, and for revoking authenticators.
• Initial authenticator distribution: Users receive a one-time login link by email upon creating of their user account. They use that link to log in and then must enter a password themselves which complies with the password complexity requirements described in IA-4(b).
• Lost/compromised/damaged authenticators: Users who have forgotten their password may request a new password by submitting their username or email address. The website responds by emailing a one-time login link to the user's email address. After using the link to log in, the user is required to enter a new password.
• Revoking authenticators: Users who have not changed their password in the last 90 days are automatically blocked. Administrators may block any user account if they believe there is a reason to do so.


#### e

##### Drupal

Drupal requires users to change their password upon initial login, and the application website enforces this. User accounts are assigned a randomly-generated and unguessable default password that is not shared with anyone, including site Administrators. Once the user logs in and creates a new password, the default password erased from the website's database.


#### f

##### LINCS

LINCS authenticators follow these password lifetime restrictions:
• Maximum password age = 90
• Minimum password age = 1
• Password reuse restriction = 10


#### g

##### LINCS

LINCS enforces password lifetime restrictions.  The password lifetime settings for internal accounts is as follows:
• Minimum restriction of zero (1) days and
• Maximum restriction of ninety (90) days before a password change is required.


#### h

##### Drupal

For all Drupal users, passwords are protected by the website's software, which only stores an encrypted string based on the password. This means that even if the websites database should be compromised, an attacker would still be unable to know users actual passwords. Internal users receive training in security awareness and acceptable use and are instructed never to reveal their passwords to anyone.


#### i

##### CivicActions

CivicActions users are required to take appropriate measures in the handling of passwords including:
• Not transmitting user names and passwords together in an unencrypted format
• Not permitting the sending of passwords in an unencrypted format via email
• Not listing passwords in tickets
• Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.


##### Drupal

Drupal users are required to take appropriate measures in the handling of passwords including:
• Not transmitting user names and passwords together in an unencrypted format
• Not permitting the sending of passwords in an unencrypted format via email
• Not listing passwords in tickets
• Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.


#### j

##### CivicActions

This control is not applicable due to the fact that group accounts are not created within CivicActions Operations per IA Policy.


##### Drupal

This control is not applicable due to the fact that group accounts are not created within the Drupal application per IA Policy.


### IA-5 (1): Password-Based Authentication

> The information system, for password-based authentication:
>    (1)(a).  Enforces minimum password complexity of [Assignment: organization-defined
> requirements for case sensitivity, number of characters, mix of upper-case letters, lower-case letters, numbers, and special characters, including minimum requirements for each type];
>    (1)(b).  Enforces at least the following number of changed characters when
> new passwords are created: [Assignment: organization-defined number];
>    (1)(c).  Stores and transmits only cryptographically-protected passwords;
>    (1)(d).  Enforces password minimum and maximum lifetime restrictions of [Assignment:
> organization-defined numbers for lifetime minimum, lifetime maximum];
>    (1)(e).  Prohibits password reuse for [Assignment: organization-defined number]
> generations; and
>    (1)(f).  Allows the use of a temporary password for system logons with an immediate
> change to a permanent password.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: password based authentication.


##### LINCS

LINCS is responsible for provisioning and de-provisioning end user accounts, which must comply with the strict password policies that are enforced by the website's software configuration, as described in IA-5.


#### a

##### Drupal

Drupal supports the requirement for password based authentication complexity. New users of Drupal are required to specify their password authentication as soon as they log in to the website for the first.  The website requires all submitted passwords to comply with validation rules, as described above in IA-5(c).
Changing password lifetime, length, reuse or strength requirements requires a code setting change that therefore needs to be planned and approved by CivicActions' Change Control Board before being implemented.


#### b

##### Drupal

When required to change passwords, Drupal users are required to change their authenticator password by changing at least one character. Enforcement of this control is implemented through the website's software configuration.


#### c

##### Drupal

All Drupal passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.


#### d

##### Drupal

The website requires all submitted passwords to comply with lifetime rules, as described above in IA-5(g).


#### e

##### Drupal

Password reuse is limited through software configuration.


#### f

##### Drupal

When website users request a password reset, the website sends a temporary login link to the email address associated with their user account. After a user logs in via the temporary login link, the website requires the user to enter a new password before proceeding further.


### IA-5 (11): Hardware Token-Based Authentication

> The information system, for hardware token-based authentication, employs mechanisms that satisfy [Assignment: organization-defined token quality requirements].

##### LINCS

LINCS does not support physical hardware token-based authentication.  Therefore this control is Not Applicable.


### IA-6: Authenticator Feedback

> The information system obscures feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals.

##### Drupal

Feedback of authentication information is obscured during the authentication process into the Drupal application by displaying “dots” in the place of a password, as is standard for web-based applications. In transmission, passwords are encrypted using SSL via HTTPS.


### IA-7: Cryptographic Module Authentication

> The information system implements mechanisms for authentication to a cryptographic module that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for such authentication.

##### Drupal

All Drupal passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. SHA-512 is an approved security function under FIPS PUB 140-2. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.


#### j

##### CivicActions

CivicActions systems employ authentication methods consistent with NIST FIPS 140-2 requirements. General public access to system web pages does not require cryptographic authentication. Privileged users accessing systems use the public-key cryptographic functionality of Secure Shell (SSH) to encrypt the exchange of information (including the password) between the remote user and the server. Where Transport Layer Security (TLS, aka SSL) is used, cryptographic modules will be configured in accordance with FIPS 140-2.


### IA-8: Identification And Authentication (Non-Organizational Users)

> The information system uniquely identifies and authenticates non-organizational users (or processes acting on behalf of non-organizational users).

##### LINCS

All non-organization users must follow procedures for access privileges as described in AC-2. Any non-organizational user must receive written permission from a Department representative to access the LINCS. In addition, only temporary access of a specified duration is allowed for non-organizational users directly accessing the system. Once the time period is over or the task completed, the temporary user accounts are removed immediately.


### IA-8 (1): Acceptance Of Piv Credentials From Other Agencies

> The information system accepts and electronically verifies Personal Identity Verification (PIV) credentials from other federal agencies.

##### LINCS

LINCS does not utilize customer agency supplied PIV credentials.


### IA-8 (2): Acceptance Of Third-Party Credentials

> The information system accepts only FICAM-approved third-party credentials.

##### LINCS

LINCS does not utilize FICAM approved credentials.


### IA-8 (3): Use Of Ficam-Approved Products

> The organization employs only FICAM-approved information system components in [Assignment: organization-defined information systems] to accept third-party credentials.

##### LINCS

LINCS does not utilize FICAM approved products.


### IA-8 (4): Use Of Ficam-Issued Profiles

> The information system conforms to FICAM-issued profiles.

##### LINCS

CivicActions does not utilize FICAM approved products or profiles.


## IR: Incident Response

### IR-1: Incident Response Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  An incident response policy that addresses purpose, scope, roles, responsibilities,
> management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the incident response policy
> and associated incident response controls; and
>   b.  Reviews and updates the current:
>     1.  Incident response policy [Assignment: organization-defined frequency];
> and
>     2.  Incident response procedures [Assignment: organization-defined frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel an incident response planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in Incident Response (IR) Policy and Procedure that can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


##### LINCS

This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.
The LINCS Technology Project maintains an Incident Response Plan (IRP), consistent with Department of Education Directives and NIST 800-61, which addresses purpose, scope, roles, and responsibilities. The incident response procedures address any activity or occurrence that compromises the integrity of a system, denies access to or use of IT resources, and compromises the sensitivity of the information stored in, processed by or transmitted by a system.
Additionally, the IRP includes procedures to respond to waste, fraud, misuse, or abuse of any departmental IT system, damage or loss of software or data contained in any system, Use of unlicensed (pirated) software products, discovery of hardware or software vulnerabilities
The LINCS Incident Response Plan can be found in the CivicActions Github repository at <https://git.civicactions.net/lincs/compliance/blob/master/docs/security-irp.md>
Additional information is contained within the Department of Education, Handbook for Information Assurance Security Policy (Handbook OCIO-01) and the Department of Education, Handbook for Information Security Incident Response and Reporting Procedures (Handbook OCIO-14).


### IR-2: Incident Response Training

> The organization provides incident response training to information system users consistent with assigned roles and responsibilities:
>   a.  Within [Assignment: organization-defined time period] of assuming an incident
> response role or responsibility;
>   b.  When required by information system changes; and
>   c.  [Assignment: organization-defined frequency] thereafter.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident response training.


##### CivicActions

All CivicActions employees are required to participate in incident response training, as required by Incident Response Plan changes, and annually. The CivicActions Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>) is the basis for the training and the incident response workflow created by the Security team.  Upon a review of past incidents, the training is updated to ensure processes and workflows are updated.


##### LINCS

CivicActions Operations and users of the LINCS system with incident response responsibilities are required to participate in incident response training once the role is assumed within 10 days, as required by LINCS changes, and annually. The Incident Response Plan (<https://git.civicactions.net/lincs/compliance/blob/master/docs/security-irp.md>) is the basis for the training and the incident response workflow created by the Security team.  Upon a review of past incidents, the training is updated to ensure processes and workflows are updated.


### IR-4: Incident Handling

> The organization:
>   a.  Implements an incident handling capability for security incidents that includes
> preparation, detection and analysis, containment, eradication, and recovery;
>   b.  Coordinates incident handling activities with contingency planning activities;
> and
>   c.  Incorporates lessons learned from ongoing incident handling activities into
> incident response procedures, training, and testing, and implements the resulting changes accordingly.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident handling.


##### LINCS

The LINCS Technology Project’s Computer Security Officer (CSO) handles all incidents for the LINCS Technology Project. The CSO is prepared to report all incidents to The Department Computer Incident Response Capability (EDCIRC) and United States Computer Emergency Readiness Team (US-CERT) as necessary.
The LINCS Technology Project utilizes proven incident handling methodologies for security incidents that includes preparation, detection and analysis, containment, eradication, and recovery. The Department maintains a list of lessons learned from ongoing incident handling activities and uses those lessons to update the incident response procedures accordingly.
Preparation activities includes all CivicActions and LINCS internal users are trained if their role includes incident response. Detection monitoring tools providing notification to incident response personnel for analysis and action. Containment, eradication and recovery activities include AWS and LAMP-stack inherited fixes and LINCS system administrators adjusting IP port blocking security groups and SELinux policies.


#### a

##### CivicActions

CivicActions has implemented an Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>) that explains the process for incident handling, and discusses preparation, detection and analysis, containment, eradication, and recovery.
Preparation activities includes all CivicActions team members are trained in incident response. Detection and monitoring tools providing notification to incident response personnel for analysis and action.


#### b

##### CivicActions

CivicActions Operations and Security team leads are members of the CivicActions Contingency and Incident Response Plan teams which coordinates activities accordingly through the life of the incident event.


#### c

##### CivicActions

CivicActions Operations and Security conduct a post-incident analysis to assist in documenting lessons learned and suggesting changes to improve the incident response process. Tickets created in response to the incident event are reviewed upon completion by Engineering and Security teams. Changes to the Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>) require a team review session for approval.


### IR-5: Incident Monitoring

> The organization tracks and documents information system security incidents.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident monitoring.


##### CivicActions

CivicActions utilizes the JIRA ticketing tool for tracking and reporting of incident events from reporting to resolution and post-incident analysis. Initial reporting can come from continuous monitoring tools as well as client and public submissions made to support@civicactions.com. Jira processes the tickets for the public submissions and CivicActions' Support Team creates associated GitHub Issues. Internal incidents reported are processed within the GitHub Issue queue. Details of the handling procedures are included in the CivicActions Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan/#response-process>) Response Process.


##### LINCS

The LINCS Technology project utilizes network and host-based intrusion detection systems, monitoring the system and application logs for anomalous events.  Incidents are tracked using the same ticketing system that is used to track all system-related changes and events.


### IR-6: Incident Reporting

> The organization:
>   a.  Requires personnel to report suspected security incidents to the organizational
> incident response capability within [Assignment: organization-defined time period]; and
>   b.  Reports security incident information to [Assignment: organization-defined
> authorities].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident reporting.


##### LINCS

If an incident involves suspicious activity, CivicActions Operations will contact the LINCS System Owner who may then contact the LINCS CSO.
The LINCS Technology Project’s Computer Security Officer (CSO) handles all incidents for the LINCS Technology Project. The CSO is prepared to report all incidents to The Department Computer Incident Response Capability (EDCIRC) and United States Computer Emergency Readiness Team (US-CERT) as necessary.


#### a

##### CivicActions

CivicActions personnel, as soon as an incident event is detected and/or communicated, are required to report the incident event to CivicActions Security. Methods of detection and/or communication may include one or more of:
• Though continuous monitoring tools (StatusCake, OSSEC, others).
• As a result of application notifications where CivicActions Security receives notifications (AIDE, OpsGenie, others).
• Event logging described in AC-2
• Host based alerts from the cloud infrastructure or platform.


#### b

##### CivicActions

CivicActions personnel, as soon as the incident event is detected and/or communicated, are required to report the incident event to CivicActions Security.


### IR-7: Incident Response Assistance

> The organization provides an incident response support resource, integral to the organizational incident response capability that offers advice and assistance to users of the information system for the handling and reporting of security incidents.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident resonse assistance.


##### CivicActions

CivicActions HelpDesk team provides first response assistance to any users of the system. Response time for external reporting of incidents through e-mail is one business day. Internal users are able to request support thought the same process or initiate the incident response workflow.  Tickets created in the Jira (customer ticketing system) and GitLab (internal ticketing system) documents all details related to the incident to assist the incident response teams in handling the incident.


### IR-8: Incident Response Plan

> The organization:
>   a.  Develops an incident response plan that:
>     1.  Provides the organization with a roadmap for implementing its incident
> response capability;
>     2.  Describes the structure and organization of the incident response capability;
>     3.  Provides a high-level approach for how the incident response capability
> fits into the overall organization;
>     4.  Meets the unique requirements of the organization, which relate to mission,
> size, structure, and functions;
>     5.  Defines reportable incidents;
>     6.  Provides metrics for measuring the incident response capability within
> the organization;
>     7.  Defines the resources and management support needed to effectively maintain
> and mature an incident response capability; and
>     8.  Is reviewed and approved by [Assignment: organization-defined personnel
> or roles];
>   b.  Distributes copies of the incident response plan to [Assignment: organization-defined
> incident response personnel (identified by name and/or by role) and organizational elements];
>   c.  Reviews the incident response plan [Assignment: organization-defined frequency];
>   d.  Updates the incident response plan to address system/organizational changes
> or problems encountered during plan implementation, execution, or testing;
>   e.  Communicates incident response plan changes to [Assignment: organization-defined
> incident response personnel (identified by name and/or by role) and organizational elements]; and
>   f.  Protects the incident response plan from unauthorized disclosure and modification.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident response plan.


##### LINCS

The LINCS Incident Response Plan (<https://git.civicactions.net/lincs/compliance/blob/master/docs/security-irp.md>) includes a comprehensive incident response program, which details the implementation of procedures and tools required for incident handling. The incident response program details the roles and responsibilities of LINCS/CivicActions IR Team. The IR Team includes members from CivicActions Security and Operations teams.  Incident response plays a pivotal role in monitoring, detecting and handling security incidents of the entire information system. The IRP details categorization of incidents in accordance with NIST 800-61 and accordingly documents and reports incidents. The IRP is reviewed annually and updated as needed by ISSO, with the assistance of the incident response team.


#### a

##### CivicActions

Incident response plays a pivotal role in monitoring, detecting and handling security incidents of the entire information system. CivicActions has developed an Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>) that:
1. provides CivicActions with procedures and tools required for incident handling;
2. describes the structure and organization of the incident response capability;
3. provides a high-level approach for how the incident response capability fits into CivicActions and the systems it maintains;
4. meets the mission, size, structure, and functions of CivicActions;
5. defines reportable incidents;
6. provides metrics for measuring the incident response capability and details
  categorization of incidents in accordance with NIST 800-61;

7. defines the roles and responsibilities of CivicActions IR Team;
8. is reviewed annually and updated as needed by CivicActions Security, with the assistance of the Incident Response team.


#### b

##### CivicActions

The CivicActions Incident Response Plan is distributed to all CivicActions team
 members as part of the CivicActions Handbook
 (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>).
 The Incident Response team includes members from Security, Engineering, and Drupal
 Engineering teams.


#### c

##### CivicActions

CivicActions Security and the Incident Response team is responsible for reviewing the Incident Response Plan annually. The entire incident response team will review the plan and update it as necessary. Ultimately, the CISO has final say and will approve all updates to the plan.


#### d

##### CivicActions

CivicActions Security is responsible for managing the IR Plan, including annual reviews and updates. The IR Plan is updated to reflect any changes to processes, systems or applications. In addition, any concerns or difficulties encountered during IR Plan implementation, execution, or testing are addressed in an update to the IR Plan.


#### e

##### CivicActions

Modifications to the IR Plan are conducted by the IR team (CivicActions Security, Operations and Engineering teams) and communicated to the CivicActions team.


#### f

##### CivicActions

The IR Plan is available in the CivicActions Handbook and is maintained in the CivicActions Github repository. Github provides the configuration management capabilities for the IR Plan to be protected from unauthorized disclosure and modification.


## MA: Maintenance

### MA-1: System Maintenance Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A system maintenance policy that addresses purpose, scope, roles, responsibilities,
> management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the system maintenance
> policy and associated system maintenance controls; and
>   b.  Reviews and updates the current:
>     1.  System maintenance policy [Assignment: organization-defined frequency];
> and
>     2.  System maintenance procedures [Assignment: organization-defined frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a system maintenance policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in in the CivicActions Maintenance (MA) Policy and Procedure document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.


##### LINCS

System maintenance policy and procedures are formally documented in the LINCS SSP, which provides the roles and responsibilities as it pertains to software and systems maintennance and updates. The LINCS Technology Project ensures that maintenance controls are developed, disseminated, reviewed, and updated as necessary.
Physical and environmental protection is fully inherited from the AWS FedRAMP certified us-east cloud.
Additional information is contained within the Department of Education, Handbook for Information Assurance Security Policy (Handbook OCIO-01).
This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.


### MA-2: Controlled Maintenance

> The organization:
>   a.  Schedules, performs, documents, and reviews records of maintenance and repairs
> on information system components in accordance with manufacturer or vendor specifications and/or organizational requirements;
>   b.  Approves and monitors all maintenance activities, whether performed on site
> or remotely and whether the equipment is serviced on site or removed to another location;
>   c.  Requires that [Assignment: organization-defined personnel or roles] explicitly
> approve the removal of the information system or system components from organizational facilities for off-site maintenance or repairs;
>   d.  Sanitizes equipment to remove all information from associated media prior
> to removal from organizational facilities for off-site maintenance or repairs;
>   e.  Checks all potentially impacted security controls to verify that the controls
> are still functioning properly following maintenance or repair actions; and
>   f.  Includes [Assignment: organization-defined maintenance-related information]
> in organizational maintenance records.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: controlled maintenance.


##### LINCS

The LINCS Technology Project schedules, performs, and documents regular maintenance on the software components of all systems, including but not limited to:
• Hourly automated snapshot backups
• Daily disaster recovery remote backups
• Daily Intrusion Detection (OSSEC) / Data Integrity Assurance (AIDE)
• As needed HelpDesk support
• Twice-monthly OS updates/patches


### MA-4: Nonlocal Maintenance

> The organization:
>   a.  Approves and monitors nonlocal maintenance and diagnostic activities;
>   b.  Allows the use of nonlocal maintenance and diagnostic tools only as consistent
> with organizational policy and documented in the security plan for the information system;
>   c.  Employs strong authenticators in the establishment of nonlocal maintenance
> and diagnostic sessions;
>   d.  Maintains records for nonlocal maintenance and diagnostic activities; and
>   e.  Terminates session and network connections when nonlocal maintenance is
> completed.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: non-local maintenance.


#### a

##### CivicActions

System maintenance is done from remote sites as there is no direct access to the server instances in the AWS cloud; this is the government-approved method of doing business. Approval, QA, and monitoring is conducted by the team performing the specific maintenance.


#### b

##### CivicActions

Remote diagnostic tools, such as OSSEC, AIDE, fail2ban and OpenSCAP are used to verify the integrity of files, perform log analysis, monitor login attempts and check for root kits and other vulnerabilies.


#### c

##### CivicActions

All nonlocal maintenance requires the same authentication requirements to perform the maintenance activities as to access the system as defined in controls AC-3 and IA-2. SSH is used to secure all communications between the remote user and the components located in the AWS cloud.


#### d

##### CivicActions

CivicActions records for nonlocal maintenance is managed through JIRA tickets and the Git issue queue as well as normal system logs. CivicActions administrator activity to the system is also logged though the implementation of the AU-2 (Audit Events) and AU-3 (Content of Audit Records).


#### e

##### CivicActions

Any session for internal maintenance activities is terminated when the user completes their session, disconnects from the system, or logs out. In addition, sessions are terminated after 15 minutes of inactivity.


### MA-5: Maintenance Personnel

> The organization:
>   a.  Establishes a process for maintenance personnel authorization and maintains
> a list of authorized maintenance organizations or personnel;
>   b.  Ensures that non-escorted personnel performing maintenance on the information
> system have required access authorizations; and
>   c.  Designates organizational personnel with required access authorizations
> and technical competence to supervise the maintenance activities of personnel who do not possess the required access authorizations.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: maintenance personnel.


##### CivicActions

Maintenance on the system and applications can only be performed by personnel designated as having internal administrator privileges and responsibilities.  Access rights for the internal administrators are assigned and granted access to perform their specific job responsibilities. All physical maintenance requirements are inherited from AWS.


##### LINCS

The Department maintains a list of authorized contract (CivicActions) personnel who perform maintenance and repair activities on the LINCS Technology Project system components, and only these authorized personnel may perform the maintenance. All maintenance personnel have the required personnel security elements in place.


## MP: Media Protection

### MP-1: Media Protection Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A media protection policy that addresses purpose, scope, roles, responsibilities,
> management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the media protection policy
> and associated media protection controls; and
>   b.  Reviews and updates the current:
>     1.  Media protection policy [Assignment: organization-defined frequency];
> and
>     2.  Media protection procedures [Assignment: organization-defined frequency].

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for media protection controls as the system is entirely within the AWS Cloud boundary.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a media protection policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in CivicActions Media Protection (MP) Policy and Procedure document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.


##### LINCS

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.
Media protection policy and procedures are fully inherited from AWS Cloud.


### MP-2: Media Access

> The organization restricts access to [Assignment: organization-defined types of digital and/or non-digital media] to [Assignment: organization-defined personnel or roles].

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for media protection controls as the system is entirely within the AWS Cloud boundary.


### MP-6: Media Sanitization

> The organization:
>   a.  Sanitizes [Assignment: organization-defined information system media] prior
> to disposal, release out of organizational control, or release for reuse using [Assignment: organization-defined sanitization techniques and procedures] in accordance with applicable federal and organizational standards and policies; and
>   b.  Employs sanitization mechanisms with the strength and integrity commensurate
> with the security category or classification of the information.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for media protection controls as the system is entirely within the AWS Cloud boundary.


### MP-7: Media Use

> The organization [Selection: restricts; prohibits] the use of [Assignment: organization-defined types of information system media] on [Assignment: organization-defined information systems or system components] using [Assignment: organization-defined security safeguards].

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for media protection controls as the system is entirely within the AWS Cloud boundary.


## PE: Physical and Environmental Protection

### PE-1: Physical And Environmental Protection Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A physical and environmental protection policy that addresses purpose,
> scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the physical and environmental
> protection policy and associated physical and environmental protection controls; and
>   b.  Reviews and updates the current:
>     1.  Physical and environmental protection  policy [Assignment: organization-defined
> frequency]; and
>     2.  Physical and environmental protection procedures [Assignment: organization-defined
> frequency].

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-2: Physical Access Authorizations

> The organization:
>   a.  Develops, approves, and maintains a list of individuals with authorized
> access to the facility where the information system resides;
>   b.  Issues authorization credentials for facility access;
>   c.  Reviews the access list detailing authorized facility access by individuals
> [Assignment: organization-defined frequency]; and
>   d.  Removes individuals from the facility access list when access is no longer
> required.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-3: Physical Access Control

> The organization:
>   a.  Enforces physical access authorizations at [Assignment: organization-defined
> entry/exit points to the facility where the information system resides] by;
>     1.  Verifying individual access authorizations before granting access to the
> facility; and
>     2.  Controlling ingress/egress to the facility using [Selection (one or more):
> [Assignment: organization-defined physical access control systems/devices]; guards];
>   b.  Maintains physical access audit logs for [Assignment: organization-defined
> entry/exit points];
>   c.  Provides [Assignment: organization-defined security safeguards] to control
> access to areas within the facility officially designated as publicly accessible;
>   d.  Escorts visitors and monitors visitor activity [Assignment: organization-defined
> circumstances requiring visitor escorts and monitoring];
>   e.  Secures keys, combinations, and other physical access devices;
>   f.  Inventories [Assignment: organization-defined physical access devices] every
> [Assignment: organization-defined frequency]; and
>   g.  Changes combinations and keys [Assignment: organization-defined frequency]
> and/or when keys are lost, combinations are compromised, or individuals are transferred or terminated.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls in conjunction with their IaaS provider, AWS.


### PE-6: Monitoring Physical Access

> The organization:
>   a.  Monitors physical access to the facility where the information system resides
> to detect and respond to physical security incidents;
>   b.  Reviews physical access logs [Assignment: organization-defined frequency]
> and upon occurrence of [Assignment: organization-defined events or potential indications of events]; and
>   c.  Coordinates results of reviews and investigations with the organizational
> incident response capability.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-8: Visitor Access Records

> The organization:
>   a.  Maintains visitor access records to the facility where the information system
> resides for [Assignment: organization-defined time period]; and
>   b.  Reviews visitor access records [Assignment: organization-defined frequency].

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-12: Emergency Lighting

> The organization employs and maintains automatic emergency lighting for the information system that activates in the event of a power outage or disruption and that covers emergency exits and evacuation routes within the facility.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-13: Fire Protection

> The organization employs and maintains fire suppression and detection devices/systems for the information system that are supported by an independent energy source.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-14: Temperature And Humidity Controls

> The organization:
>   a.  Maintains temperature and humidity levels within the facility where the
> information system resides at [Assignment: organization-defined acceptable levels]; and
>   b.  Monitors temperature and humidity levels [Assignment: organization-defined
> frequency].

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-15: Water Damage Protection

> The organization protects the information system from damage resulting from water leakage by providing master shutoff or isolation valves that are accessible, working properly, and known to key personnel.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-16: Delivery And Removal

> The organization authorizes, monitors, and controls [Assignment: organization-defined types of information system components] entering and exiting the facility and maintains records of those items.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


## PL: Planning

### PL-1: Security Planning Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A security planning policy that addresses purpose, scope, roles, responsibilities,
> management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the security planning policy
> and associated security planning controls; and
>   b.  Reviews and updates the current:
>     1.  Security planning policy [Assignment: organization-defined frequency];
> and
>     2.  Security planning procedures [Assignment: organization-defined frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a system planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Planning (PL) Policy and Procedure document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.


##### LINCS

This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.
The LINCS Technology Project developed its security policy planning and procedures based on the Department of Education, Office of the Chief Information Officer, Handbook for Information Assurance Security Policy, Information Assurance Program (Handbook OCIO-01), guidance from NIST, the Office of Management and Budget and industry best practices. Security policies and procedures are formally documented within the LINCS SSP, which provides the roles and responsibilities as it pertains to security planning. It provides guidance on all aspects of security for the protection of LINCS information technology resources. It defines responsibilities for the implementation and oversight of the guidance contained herein. The plan was last updated in December, 2015.


### PL-2: System Security Plan

> The organization:
>   a.  Develops a security plan for the information system that:
>     1.  Is consistent with the organization�s enterprise architecture;
>     2.  Explicitly defines the authorization boundary for the system;
>     3.  Describes the operational context of the information system in terms of
> missions and business processes;
>     4.  Provides the security categorization of the information system including
> supporting rationale;
>     5.  Describes the operational environment for the information system and relationships
> with or connections to other information systems;
>     6.  Provides an overview of the security requirements for the system;
>     7.  Identifies any relevant overlays, if applicable;
>     8.  Describes the security controls in place or planned for meeting those
> requirements including a rationale for the tailoring decisions; and
>     9.  Is reviewed and approved by the authorizing official or designated representative
> prior to plan implementation;
>   b.  Distributes copies of the security plan and communicates subsequent changes
> to the plan to [Assignment: organization-defined personnel or roles];
>   c.  Reviews the security plan for the information system [Assignment: organization-defined
> frequency];
>   d.  Updates the plan to address changes to the information system/environment
> of operation or problems identified during plan implementation or security control assessments; and
>   e.  Protects the security plan from unauthorized disclosure and modification.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS system security plan.


##### LINCS

The System Security Plan (SSP) was developed and implemented for LINCS Technology Project system in accordance with the Department of Education, Office of the Chief Information Officer, Handbook for Information Assurance Security Policy, Information Assurance Program (Handbook OCIO-01), Department of Education Information Technology Security, Handbook for Information Technology Security, Certification and Accreditation Procedures (Handbook OCIO-05), NIST SP 800-18 and NIST SP 800-37. The SSP includes a description of the management, operational, and technical controls in place or planned for the application. The SSP is included as a key document in an application’s C&A package and is reviewed and approved by designated officials. The SSP identifies the system owner and responsible parties for managing system access and the overall security of the system. The Chief Information Security Officer reviews and approves the SSP.  The SSP will be reviewed at least annually and updated to account for any changes to the LINCS system and to address any changes in security controls.


#### a

##### CivicActions

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

##### CivicActions

The SSP is reviewed and approved by the authorizing official prior to plan implementation. A copy of the SSP is provided to authorized CivicActions and assessing personnel including the System Owner, Authorizing Official, Information System Security Officer, System/Network Administrator and CivicActions Operations. The SSP is maintained by CivicActions Security.


#### c

##### CivicActions

The SSP is reviewed at least annually by the System Owner and CivicActions Operations in collaboration with CivicActions Security.


#### d

##### CivicActions

CivicActions Operations in collaboration with CivicActions Security updates the system description and control descriptions within the SSP as needed to verify the SSP is an accurate description of the system.


#### e

##### CivicActions

The SSP is currently available to authorized users on GitLab. Per the Acceptable Use Policy, all entities granted access to CivicActions information assets are required to complete a non-disclosure agreement (NDA) to uphold information confidentiality. GitLab provides the configuration management capabilities for the SSP to be protected from unauthorized disclosure and modification.


### PL-4: Rules Of Behavior

> The organization:
>   a.  Establishes and makes readily available to individuals requiring access
> to the information system, the rules that describe their responsibilities and expected behavior with regard to information and information system usage;
>   b.  Receives a signed acknowledgment from such individuals, indicating that
> they have read, understand, and agree to abide by the rules of behavior, before authorizing access to information and the information system;
>   c.  Reviews and updates the rules of behavior [Assignment: organization-defined
> frequency]; and
>   d.  Requires individuals who have signed a previous version of the rules of
> behavior to read and re-sign when the rules of behavior are revised/updated.

##### LINCS

All users (privileged and program account users) requesting access to the LINCS Technology Project system are required to read the LINCS’ Rules of Behaviors, complete an account request form and sign both documents. Appendix B includes the Rules of Behavior, describing the user’s responsibilities and expected behavior when using the application and also includes the User Acknowledgement form. Account management procedures are described in detail in the SSP.


#### a

##### CivicActions

CivicActions maintains an Acceptable Use Policy that all CivicActions personnel are required to abide by when working with CivicActions operated systems. This information is available in the CivicActions Handbook under Security Policy here: <https://civicactions-handbook.readthedocs.io/en/latest/03-policies/security/#acceptable-use-policy>.


#### b

##### CivicActions

All CivicActions employees are required to read and sign the Security Policy <https://civicactions-handbook.readthedocs.io/en/latest/03-policies/security/> which includes the Acceptable Use Policy, prior to being authorized access to CivicActions operated systems. This is part of the onboarding Security Training process: <https://civicactions-handbook.readthedocs.io/en/latest/01-welcome-to-civicactions/training/security-training/>
If CivicActions staff fail to comply with CivicActions security awareness and training requirements, their access to CivicActions information systems may be terminated.


#### c

##### CivicActions

The CivicActions Acceptable Use Policy/Rules of Behavior are reviewed by CivicActions Security and Operations at least annually and is updated at least every three years.


#### d

##### CivicActions

CivicActions employees re-sign the revised/updated Acceptable Use Policy/Rules of Behavior policy document. The Director of Human Resources retains the signed acknowledgements.


## PS: Personnel Security

### PS-1: Personnel Security Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A personnel security policy that addresses purpose, scope, roles, responsibilities,
> management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the personnel security
> policy and associated personnel security controls; and
>   b.  Reviews and updates the current:
>     1.  Personnel security policy [Assignment: organization-defined frequency];
> and
>     2.  Personnel security procedures [Assignment: organization-defined frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a personnel security policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in CivicActions Personnel Security (PS) Policy document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.


##### LINCS

The LINCS Technology Project documents the security policy and procedures in addressing position categorization, personnel screening, personnel termination, personnel transfer, and access agreements within the LINCS SSP. The LINCS Technology Project adopts the Department of Education personnel security standards and determines position risks levels based on public trust responsibilities.
This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.


### PS-2: Position Risk Designation

> The organization:
>   a.  Assigns a risk designation to all organizational positions;
>   b.  Establishes screening criteria for individuals filling those positions; and
>   c.  Reviews and updates position risk designations [Assignment: organization-defined frequency].

##### LINCS

The LINCS Technology Project’s position sensitivity levels are assigned by the Department of Education and National Classification Center (NCC) as part of the position designation required by OPM under 5 CFR 731.106. Each Department position designation is documented on the Standard Position Description (SPD) and assigned a risk level (or sensitivity level) commensurate with the sensitivity of the information, the risk to that information and the system maintaining that information. The levels of risk still need to be designated by the Department for employee and contractor positions but since the LINCS Technology Project system does not have any sensitive data, a low risk scenario can be assumed.
• Employee risk levels and background investigations are: Low Risk= NACI, Moderate Risk= LBI, High Risk= BI.
• Contractor risk levels and background investigations are: Low Risk= NACI, Moderate Risk= NACC, High Risk= BI.
In order to ensure every employee is assigned to a position, which has been reviewed for sensitivity by the NCC, the SPD is a required data attribute of an employee’s HR record. Position risks designations are reviewed and revised when NCC or OPM publish changes to sensitivity levels.
This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog


#### a

##### CivicActions

Risk designations are assigned to all CivicActions positions. The CivicActions Director of Human Resources works in coordination with the CivicActions ISSO and the Chief Operating Officer to assign risk designations.


#### b

##### CivicActions

The CivicActions Director of Human Resources works in coordination with the CivicActions ISSO and the Chief Operating Officer to establish screening criteria for all CivicActions positions.


#### c

##### CivicActions

At least every three (3) years, the CivicActions Director of Human Resources reviews and revises position risk designations. If the Director of Human Resources determines that significant changes must be made to the position risk descriptions the Director of Human Resources works in coordination with the CivicActions ISSO and the Chief Operating Officer to implement changes as required.


### PS-3: Personnel Screening

> The organization:
>   a.  Screens individuals prior to authorizing access to the information system;
> and
>   b.  Rescreens individuals according to [Assignment: organization-defined conditions
> requiring rescreening and, where rescreening is so indicated, the frequency of such rescreening].

##### LINCS

Minimum background investigations are conducted, since all data is non-sensitive, for individuals requiring access to LINCS Technology Project information and information systems. The type of background investigation conducted for an individual is determined by the individual’s position risk categorization noted in control PS-2. The Department conducts periodic reinvestigations in accordance with OPM and NIST guidelines.
This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.


#### a

##### CivicActions

Prospective CivicActions employees undergo background checks commensurate with the individual’s job duties, the classification of the information they will access, and the risks associated with the role. At the discretion of the Chief Operating Officer these checks may also be conducted on contractors and / or third party users in cases where they will have access to application data that is not meant to be consumed by the public.  In these instances, the Chief Operating Officer will instruct the Director of Human Resources to conduct a background check before granting access to the information system.


#### b

##### CivicActions

Rescreening is conducted as required by the individual’s job duties, the classification of the information they will access, and the risks associated with the role. A basic background check is performed for all CivicActions employees.


### PS-4: Personnel Termination

> The organization, upon termination of individual employment:
>   a.  Disables information system access within [Assignment: organization-defined
> time period];
>   b.  Terminates/revokes any authenticators/credentials associated with the individual;
>   c.  Conducts exit interviews that include a discussion of [Assignment: organization-defined
> information security topics];
>   d.  Retrieves all security-related organizational information system-related
> property;
>   e.  Retains access to organizational information and information systems formerly
> controlled by terminated individual; and
>   f.  Notifies [Assignment: organization-defined personnel or roles] within [Assignment:
> organization-defined time period].

##### LINCS

The Department’s HR policy states that managers or designated officials are responsible for recovering and properly securing employee badges and returning it to the local physical security office. The Department executes termination procedures that remove personnel access privileges, computer accounts. When an employee is terminated, the employee’s manager or designated official completes a form requesting termination of access for the user. Local management and the security manager coordinate disabling or removing LINCS Technology Project privileged access with the system administrator. The employee’s manager or designated official is responsible for recovering and properly securing his/her ID badge and returning it to the local physical security office. The employee’s manager or designated official ensures that any information on the system that the employee was responsible for will be available to the appropriate personnel.
This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.


#### a

##### CivicActions

Information system access is terminated immediately upon the voluntary or involuntary departure of an employee. In the case of involuntary departure, in addition to immediate termination of system access, at no point is a departing employee allowed access to any part of the CivicActions infrastructure.
In the case of voluntary departure, employees are permitted access to the information system for the duration of their off boarding period. The departing employee’s manager is responsible for informing the Information Technology department when the employee off boarding period concludes. At this time system and facility access is terminated.


#### b

##### CivicActions

The terminated user’s accounts are disabled and all access associated with the individual is revoked.


#### c

##### CivicActions

The employee's manager or the Director of Human Resources conducts exit interviews with all employees who leave CivicActions voluntarily. There is a general discussion about the process of turning in any/all company issued devices, laptops, etc.


#### d

##### CivicActions

CivicActions employees provide their own equipment that must be hardened to security reqirements depending upon their role and duties. CivicActions supplies two factor authentication tokens that become the property of the employee.
Some employees may receive company-issued hardware for working on poarticular projects. These items are collected before the employee exits CivicActions.  In the case of an involuntary termination, the Director of Human Resources works to collect company issued devices and provides paperwork highlighting confidential protections for customers.


#### e

##### CivicActions

Access to CivicActions information and information systems is always shared, so that the termination of an individual will not prevent CivicActions from having access to needed resources.


#### f

##### CivicActions

When a person is terminated, a standard off-boarding process is used to notify management and IT and to track the process of disabling access to the information system/information system components. CivicActions IT Operations and Security is given at least a four hour notice to schedule the deactivation of access upon termination. Deactivation is a manual process that is tracked via a Trello card in order to meet the four hour turnaround time before termination.


### PS-5: Personnel Transfer

> The organization:
>   a.  Reviews and confirms ongoing operational need for current logical and physical
> access authorizations to information systems/facilities when individuals are reassigned or transferred to other positions within the organization;
>   b.  Initiates [Assignment: organization-defined transfer or reassignment actions]
> within [Assignment: organization-defined time period following the formal transfer action];
>   c.  Modifies access authorization as needed to correspond with any changes in
> operational need due to reassignment or transfer; and
>   d.  Notifies [Assignment: organization-defined personnel or roles] within [Assignment:
> organization-defined time period].

##### LINCS

When an employee is reassigned or transferred, the employee’s manager or designated official is required to request transfer of access (as appropriate) for the user.
In accordance with the Department’s HR policy, the employee’s manager or designated official is responsible for recovering and properly securing his/her ID badge and returning it to the local physical security office. The manager provides prompt notification to the LINCS Technology Project system/security administrator when an employee changes assignments and/or location. This includes taking prompt and appropriate action to change employee access profile and/or remove employee from the system; and ensure that users’ system access is cancelled when the need no longer exists.
This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.


#### a

##### CivicActions

When an employee, third party personnel and / or contractor is transferred to a new project or position within CivicActions, they may maintain access to the previous system they were working on in order to facilitate the process of maintenance and knowledge transfer. However, as part of the practices of account management (AC-02) and least privilege (AC-06), regular audits of privileged users are conducted and access privileges may be removed when no longer needed. Additionally, adherence to specific client SLAs may enhance the frequency of such audits or the timeliness of privilege removal during personnel transfer.


#### b

##### CivicActions

When an employee, third party personnel and / or contractor is transferred to a new position within CivicActions and there is a requirement for access change, such access changes are normally completed within five business days.


#### c

##### CivicActions

Access authorizations are modified as needed to coincide with changes in duties or operational need upon personnel transfer or reassignment.


#### d

##### CivicActions

CivicActions Operations is informed of transfers that require access authorization modifications within five business days by the Project Manager, System Owner or Director of Human Resources.


### PS-6: Access Agreements

> The organization:
>   a.  Develops and documents access agreements for organizational information
> systems;
>   b.  Reviews and updates the access agreements [Assignment: organization-defined
> frequency]; and
>   c.  Ensures that individuals requiring access to organizational information
> and information systems:
>     1.  Sign appropriate access agreements prior to being granted access; and
>     2.  Re-sign access agreements to maintain access to organizational information
> systems when access agreements have been updated or [Assignment: organization-defined frequency].

##### LINCS

The Department has implemented a formalized process for user account administration using the approved and signed Rules of Behavior and User Acknowledgement forms. All new users requesting access to the LINCS Technology Project system must complete these forms and the security manager will keep them on file and reviewed bi-annually.


#### a

##### CivicActions

CivicActions has developed and documented an Acceptable Use Policy that covers access and use of all CivicActiuons systems.


#### b

##### CivicActions

The Acceptable Use Policy is reviewed at least annually or when a significant change occurs. In the event that a major update is made to the Acceptable Use Policy, employees are required to read and sign the updated policy document and Human Resources stores the information.


#### c

##### CivicActions

All CivicActions team members are required to read and sign the Acceptable Use Policy (AUP) provided in the Security Policy document prior to gaining access to the any CivicActions system. The acknowledgment signature page is a separate document collected and recorded by the Director of Human Resources.


### PS-7: Third-Party Personnel Security

> The organization:
>   a.  Establishes personnel security requirements including security roles and
> responsibilities for third-party providers;
>   b.  Requires third-party providers to comply with personnel security policies
> and procedures established by the organization;
>   c.  Documents personnel security requirements;
>   d.  Requires third-party providers to notify [Assignment: organization-defined
> personnel or roles] of any personnel transfers or terminations of third-party personnel who possess organizational credentials and/or badges, or who have information system privileges within [Assignment: organization-defined time period]; and
>   e.  Monitors provider compliance.

##### LINCS

All contractor support personnel are required to meet the same personnel security policy requirements as Department personnel who have privileged access to the LINCS Technology Project system. Third party providers are required to review and sign the Rules of Behavior prior to being granted access to the system.


#### a

##### CivicActions

Third party personnel are required to following the same process and requirements as CivicActions employees.


#### b

##### CivicActions

Third party personnel are required to following the same process and requirements as CivicActions employees. CivicActions Operations or Security may require that a background check be conducted on contractors and / or third party users in cases where they will have access to application data that is not meant to be consumed by the public.


#### c

##### CivicActions

All personnel security requirements are documented and include things such as signing the Acceptable Use Policy (AUP) and taking security awareness training.


#### d

##### CivicActions

For personnel transfers and terminations of third-party personnel with access to the CivicActions systems, third parties must notify the CivicActions Operations an/or Director of Human Resources the same day. The same employee transfer and/or termination procedure(s) are folloed as if the third party personnel were CivicActions employees.


#### e

##### CivicActions

Compliance measures for assessing third-party personnel and/or contractors are determined on a case-by-case basis. CivicActions Security is responsible for coordinating with the managers of external systems to include appropriate and tailored compliance verification language in contracts as required.  Third-party personnel are continuously monitored to ensure compliance with personnel security requirements.


### PS-8: Personnel Sanctions

> The organization:
>   a.  Employs a formal sanctions process for individuals failing to comply with
> established information security policies and procedures; and
>   b.  Notifies [Assignment: organization-defined personnel or roles] within [Assignment:
> organization-defined time period] when a formal employee sanctions process is initiated, identifying the individual sanctioned and the reason for the sanction.

##### LINCS

The disciplinary sanctions for personnel failing to comply with establish IT security policies and procedures are included in the Department’s HR policy. If an employee violates the Department’s information security policies and procedures, the employee may be subject to disciplinary action at the discretion of management. Actions may range from verbal or written warning, removal of system access for a specific period of time, reassignment to other duties, or termination, depending on the severity of the violation. Disciplinary sanctions are reported to the OCIO.


#### a

##### CivicActions

The Director of Human Resources is responsible for determining and enforcing sanctions for failing to comply with established information security policies and procedures. Coaching may be considered prior to sanctions. Sanctions may include but are not limited to written warnings, reduction in system access, demotion, or termination.


#### b

##### CivicActions

When employee sanctions processes are initiated, the Director of Human Resources notifies the respective Project Manager(s) and CivicActions Security within five business days.


## RA: Risk Assessment

### RA-1: Risk Assessment Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A risk assessment policy that addresses purpose, scope, roles, responsibilities,
> management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the risk assessment policy
> and associated risk assessment controls; and
>   b.  Reviews and updates the current:
>     1.  Risk assessment policy [Assignment: organization-defined frequency]; and
>     2.  Risk assessment procedures [Assignment: organization-defined frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a risk assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Risk Assessment (RA) Policy and Procedure CivicActions that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.


##### LINCS

The Department follows the risk assessment policy and procedures formally documented within in the Department of Education Handbook for Information Technology Security Risk Assessment Procedures (Handbook OCIO-07). Furthermore, a Risk Assessment Plan was originally initiated to determine the extent of the potential threat and the risk associated with LINCS Technology Project throughout its System Development Life Cycle (SDLC). The LINCS Technology Project Risk Assessment defines the methodology approach to determine the likelihood risks, and identify potential mitigation options to reduce risks to the LINCS Technology Project system.
The LINCS Technology Project Risk Assessment will be conducted in accordance with the Department’s risk assessment policy and procedures. By doing so, the responsible parties associated with the LINCS Technology Project will be able to determine the risk, likelihood and impact that could result from exploiting vulnerabilities within the system.
This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.
Additional information is contained within the Department of Education Handbook for Information Technology Security Risk Assessment Procedures (Handbook OCIO-07).


### RA-2: Security Categorization

> The organization:
>   a.  Categorizes information and the information system in accordance with applicable
> federal laws, Executive Orders, directives, policies, regulations, standards, and guidance;
>   b.  Documents the security categorization results (including supporting rationale)
> in the security plan for the information system; and
>   c.  Ensures that the authorizing official or authorizing official designated
> representative reviews and approves the security categorization decision.

#### a

##### LINCS

In accordance with FIPS 199 requirement and guidelines provided in NIST SP800-60 Rev.1, the organization categorized the system as a Low system: Confidentiality (Low), Integrity (Low), Availability (Low).


#### b

##### LINCS

The security categorization was determined by evaluating the type of information that is stored, processed, and/or transmitted by the application and the potential impact levels associated with the confidentiality, integrity, and availability of that information. The application’s security categorization has been documented in this SSP.


#### c

##### LINCS

The security categorizations have been reviewed by the designated application POCs, were approved during the C&A effort. The formal security categorization document is available upon request. The system inventory for the LINCS Technology Project is revalidated semiannually.


### RA-3: Risk Assessment

> The organization:
>   a.  Conducts an assessment of risk, including the likelihood and magnitude of
> harm, from the unauthorized access, use, disclosure, disruption, modification, or destruction of the information system and the information it processes, stores, or transmits;
>   b.  Documents risk assessment results in [Selection: security plan; risk assessment
> report; [Assignment: organization-defined document]];
>   c.  Reviews risk assessment results [Assignment: organization-defined frequency];
>   d.  Disseminates risk assessment results to [Assignment: organization-defined
> personnel or roles]; and
>   e.  Updates the risk assessment [Assignment: organization-defined frequency]
> or whenever there are significant changes to the information system or environment of operation (including the identification of new threats and vulnerabilities), or other conditions that may impact the security state of the system.

#### a

##### LINCS

CivicActions/LINCS will perform risk assessments for the LINCS system based on SP 800-30 Rev. 1 Guide for Conducting Risk Assessments at least annually and as part of the change management activities for the LINCS system that warrant a new or updated risk assessment.


#### b

##### LINCS

The results of risk assessments will be compiled into a risk assessment report to be reviewed by CivicActions Security and relevant personnel, and also added to the GitLab system for the LINCS system.


#### c

##### LINCS

CivicActions/LINCS reviews risk assessment results at least annually.


#### d

##### LINCS

The Risk Assessment report will be disseminated to the appropriate personnel through the Project Manager and CivicActions Security.


#### e

##### LINCS

Risk assessments are conducted annually or whenever there are significant changes to the information system or environment of operation (including the identification of new threats and vulnerabilities), or other conditions that may impact the security state of the system, as defined in NIST Special Publication 800-37 Revision 1.
A significant change includes:
• Changing authentication or access control implementations;
• Changing storage implementations;
• Changing a COTS product to another product;
• Changing the backup mechanisms and process; and,
• Adding new interconnections to an outside service provide.


### RA-5: Vulnerability Scanning

> The organization:
>   a.  Scans for vulnerabilities in the information system and hosted applications
> [Assignment: organization-defined frequency and/or randomly in accordance with organization-defined process] and when new vulnerabilities potentially affecting the system/applications are identified and reported;
>   b.  Employs vulnerability scanning tools and techniques that facilitate interoperability
> among tools and automate parts of the vulnerability management process by using standards for:
>     1.  Enumerating platforms, software flaws, and improper configurations;
>     2.  Formatting checklists and test procedures; and
>     3.  Measuring vulnerability impact;
>   c.  Analyzes vulnerability scan reports and results from security control assessments;
>   d.  Remediates legitimate vulnerabilities [Assignment: organization-defined
> response times] in accordance with an organizational assessment of risk; and
>   e.  Shares information obtained from the vulnerability scanning process and
> security control assessments with [Assignment: organization-defined personnel or roles] to help eliminate similar vulnerabilities in other information systems (i.e., systemic weaknesses or deficiencies).

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: vulnerability scanning.


##### LINCS

The LINCS Technology Project uses vulnerability scanning software to document and determine risks to the system.  These scans are being run on a regular basis and the results of these scans are being used to inform changes to the system and verify that security controls are working correctly.  These scans are used to document the current state of the system, and to analyze security trends as changes are made over time.


#### a

##### CivicActions

CivicActions Operations uses vulnerability scanning software to document and determine risks to the system. Operating system and application vulnerability scans include:
• The CivicActions system environment employs the OpenSCAP scanner with the Red Hat STIG baseline to check for vulnerabilities.
• The CivicActions application environment is tested by the penetration tester OWASP ZAP, an open-source web application security scanner to report on needed updates based on known flaws.
CivicActions Operations has automated the process to perform the scans on a monthly basis. The resulting reports list vulnerabilities and ranks them by severity. These reports are stored on an audit server and are used to inform changes to the system and verify that security controls are working correctly.  These scans are used to document the current state of the system, and to analyze security trends as changes are made over time.


#### b

##### CivicActions

CivicActions uses the automated vulnerability scanning tools OpenSCAP and OWASP ZAP are interoperable with standard web browsers, the Open Source Ansible infrastructure provisioning system and other Open Source tools employed by CivicActions.


#### c

##### CivicActions

CivicActions Security reviews all vulnerabilities identified from automated scans and security assessments. Vulnerabilities found and deemed legitimate are assigned an impact rating and response time thought creation of an issue or ticket.  CivicActions Operations reviews current scans and compare with older scans to identify trends and to verify previous vulnerabilities have been mitigated.


#### d

##### CivicActions

Identified and reported vulnerabilities are assigned an impact rating and response time by CivicActions Security and must be remediated according to the following time requirements:
• High - Within 30 days of discovery (usually within 1 week))
• Moderate - Within 90 days of discovery (usually within 2 weeks)
• Low - Within 240 days of discovery


#### e

##### CivicActions

Results of the vulnerability scans and security assessments are shared with all appropriate CivicActions personnel supporting continuous monitoring requirements. CivicActions Security assigns each vulnerability an impact rating and response time though JIRA or the Git issue tool for tracking to the established remediation deadlines listed in RA-5(d).


## SA: System and Services Acquisition

### SA-1: System And Services Acquisition Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A system and services acquisition policy that addresses purpose, scope,
> roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the system and services
> acquisition policy and associated system and services acquisition controls; and
>   b.  Reviews and updates the current:
>     1.  System and services acquisition policy [Assignment: organization-defined
> frequency]; and
>     2.  System and services acquisition procedures [Assignment: organization-defined
> frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a system and services acquisition policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained the CivicActions System and Services Acquisition (SA) Policy document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.


##### LINCS

The LINCS Technology Project complies with the Department of Education Handbook for Software Management and Acquisition Policy and Federal Acquisition Regulation (FAR) policies and procedures. The Department of Education, Office of the Chief Information Officer, Handbook for Information Assurance Security Policy, Information Assurance Program (Handbook OCIO-01) states that security requirements will be included in information system acquisition contracts based on an assessment of risk in accordance with FISMA requirements. The LINCS Technology Project will identify new threats/vulnerabilities and technologies that may require updating of solicitation documents.
This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.


### SA-2: Allocation Of Resources

> The organization:
>   a.  Determines information security requirements for the information system
> or information system service in mission/business process planning;
>   b.  Determines, documents, and allocates the resources required to protect the
> information system or information system service as part of its capital planning and investment control process; and
>   c.  Establishes a discrete line item for information security in organizational
> programming and budgeting documentation.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: allocation of resources.


##### LINCS

The LINCS System Owner is responsible for leading the annual budgeting process and for tracking organizational spending. The System Owner coordinates with the CivicActions Project Manager and CivicActions Security on at least monthly basis to track security priorities and spending patterns and determine financial requirements. The System Owner also coordinates the approval process for interim increases to the security budget, if required. This data is used to support the development of the annual budget.
Security costs are included in Exhibit 53 in the Department's on-line electronic Capital Planning and Investment Control system (eCPIC) in order to provide adequate business case information for budget purposes. Security costs are represented across the life cycle in the business case (Exhibit 300) for major investments and (Exhibit 53) for non-major projects - LINCS is a non-major project. Security costs are summarized and listed as a line item on the Exhibit 53 in the budget submitted to Treasury.
Costs for providing security at the infrastructure level are contained in the business cases for infrastructure supporting computing platforms, desktop processing, the network environment, and web capability. Since the Exhibit 53 includes projections for multiple fiscal years, its intention is to identify and anticipate security resources required.


#### a

##### CivicActions

CivicActions Security in collaboration with the System Owner act and/or meet on a pre-determined basis to determine information system security requirements and to develop implementation budgets and plans.


#### b

##### CivicActions

CivicActions Security in collaboration with the System Owner determines, designates, documents, and allocates the resources required to protect the system as part of its capital planning and investment control processes.


#### c

##### CivicActions

The annual budget developed by the System Owner includes explicit budgetary line items for FISMA security requirements. Additional security-related expenditures that fall outside of explicit compliance requirements are addressed in sub-lines under the CivicActions Information Technology budget.


### SA-3: System Development Life Cycle

> The organization:
>   a.  Manages the information system using [Assignment: organization-defined system
> development life cycle] that incorporates information security considerations;
>   b.  Defines and documents information security roles and responsibilities throughout
> the system development life cycle;
>   c.  Identifies individuals having information security roles and responsibilities;
> and
>   d.  Integrates the organizational information security risk management process
> into system development life cycle activities.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: system development life cycle.


##### LINCS

The LINCS Technology Project draws from the Department of Education, Office of the Chief Information Officer, Handbook for Information Assurance Security Policy, Information Assurance Program (Handbook OCIO-01), Department of Education Lifecycle Management (LCM) Framework, NIST SP 800-64, the LINCS Enterprise Performance Life Cycle (EPLC) and Agile software development methodology to ensure security requirements are incorporated during each phase of the life cycle. This helps to ensure the development of secure systems and effective risk management.


#### a

##### CivicActions

The system and application(s) are managed by CivicActions using the Agile software development methodology, which provides a continuous System Development Life Cycle (SDLC) methodology. CivicActions Agile management continues to improve the software through ongoing planned code releases. The process is overseen by the Change Control Board (CCB) as described in CM-1. Each point release introduces code and configuration changes to the website through the following SDLC methodology:
• Code release planning: A code release ticket is created in the Change Request project of the CivicActions ticketing system which describes the overall goals of the code release. The code release ticket is linked to other tickets in the ticketing system which describe issues to be addressed by the planned code release. Those issues may include bug fixes and feature enhancements as well as upgrades to newer versions of the software packages that have been used to build the website.
• Sprints: The tickets covered by the planned code release are then implemented through a series of planned sprints, each of which typically lasts two weeks.  Each sprint begins with a sprint planning session at which the the CCB selects a list of tickets to be implemented. CivicActions Development holds daily coordination meetings throughout the sprint to share information and resolve any problems that may be blocking progress toward completion. At the end of the sprint, a retrospective is performed in which progress is reviewed to determine which issues have been resolved and which need further work.
• Development/unit testing: Work on each ticket is performed within a separate code branch within the CivicActions git repository, and tested using the Gitlab Runner continuous integration platform. Developers also write unit tests to prove their code behaves as expected and address security considerations such as information leakage, bounds checking, and input validation. Once work on a ticket is completed, the developer creates a merge request, and the changes are submitted to at least one other developer for review to ensure they meet functional requirements and address security considerations before the pull request is merged into the git repository's development branch for the planned code release.
• Integration testing: Once all work tickets have been completed, the code and configuration necessary to implement the changes is merged into the website's staging server, where it undergoes additional testing to ensure there are no conflicts between the work that has been done on individual tickets.
• User acceptance testing (UAT): The code release undergoes manual testing against a checklist of expected site behaviors and options each of the website's defined user roles to further verify that the functional changes work as expected and to identify any changes in user experience that need to be documented in release notes to be shared with the customer.
• Approval for deployment: After all the planned code release has passed all of the above tests, the code release is scheduled for deployment to production and presented to CivicActions' Change Control Board (CCB) for review and approval.
• Deployment to production: A full backup of the website is performed immediately prior to the deployment.
• Security scan: After the deployment to production, the website undergoes a security scan using the a web vulnerability scanner.
Security issues to be addressed in the planned code release may come from a variety of sources:
• Customer support requests received by the CivicActions Help Desk
• Security concerns, incidents, and site performance issues reported by users
• Security incident reports, including server log analysis and root cause analysis of those incidents performed by CivicActions Security and Operations
• Security notifications received by CivicActions Security from external security teams and other software vendors
• Vulnerabilities detected during security scans of the website performed by CivicActions Security
• Issues reported by CivicActions Security, Operations and Development
• Security issues reported through continuous monitoring


#### b

##### CivicActions

The CivicActions organization defines and documents information security roles and responsibilities throughout the SDLC. The following teams participate in this process:
• Customer Support: Files tickets when incidents are reported and shares incident reports with customers
• CivicActions Security: Receives security notifications from the Drupal security team and other software vendors; performs security scans; uses CivicActions JIRA ticketing system to request mitigation of all reported vulnerabilities
• CivicActions Development: Performs server log analysis when security incidents are reported; assists in root cause analysis
• Change Control Board: Meets weekly to review and approve upcoming planned code changes to the website, include security-related code releases.
• AWS Cloud: Monitors server and application events; proactively responds to security incidents, and reports incidents to CivicActions
• Users: Communicates customer security requirements and expectations, and alerts CivicActions' customer support team whenever it detects a security or site performance issue
Security responsibilities performed by these teams include the following:
• Perform configuration management during information system design, development, implementation, and operation;
• Implement only organization-approved changes;
• Document approved changes;
• Manage and control changes to the system;
• Fully test all changes, taking into account security considerations as well as other functional requirements;
• Track security flaws and flaw resolution; and
• Employ code analysis tools to examine software for common flaws and document the results of the analysis.


#### c

##### CivicActions

Each of the CivicActions teams described in SA-3(b) has a team leader who is responsible for defining roles and responsibilities of individual personnel members within that team. CivicActions uses role base management for access and authentication implementation and enforcement.


#### d

##### CivicActions

The CivicActions organization integrates the organizational information security risk management process into system development life cycle activities by requiring that the processes defined in SA-3(a) and (b) above are adhered to by all information system developers and associated security personnel.


### SA-4: Acquisition Process

> The organization includes the following requirements, descriptions, and criteria, explicitly or by reference, in the acquisition contract for the information system, system component, or information system service in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs:
>   a.  Security functional requirements;
>   b.  Security strength requirements;
>   c.  Security assurance requirements;
>   d.  Security-related documentation requirements;
>   e.  Requirements for protecting security-related documentation;
>   f.  Description of the information system development environment and environment
> in which the system is intended to operate; and
>   g.  Acceptance criteria.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: acquisition process.


##### CivicActions

CivicActions' System and Services Acquisition Policy affects all personnel with purchasing authorization, and applies to all purchases or deployments including infrastructure, software or hardware. The CivicActions System and Services Acquisition Policy contains the process for determining acceptance criteria for all system software and application services.
The Acquisition Security Policy includes an assessment that evaluates the product based on the vendor’s security practices, policies, and past performance. It also details the potential maintenance and end-of-life ramifications with regards to security.
CivicActions Security is responsible for determining the security documentation that must be included in information system or services acquisition contracts.
Configuration and design of the development and production environments are hosted in the CivicActions Git repository. All documentation are strictly controlled regarding transportation and storage in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs.


##### LINCS

The LINCS Technology Project follows the guidelines and procedures within the overarching Department of Education policy documents for all federal acquisition of information technology equipment, software and services, Federal Acquisition Regulations (FAR) Part 39, “Acquisition of Information Technology.”  Security requirements/specifications are included in information system acquisition contracts. The requirements in the information system acquisition contract permit updating security controls as new threat/vulnerabilities are identified and new technologies are implemented.
The LINCS System and Services Acquisition Policy contains the process for determining acceptance criteria for all LINCS system software and services.
The LINCS organization reviews and approves all acquisition contracts in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs.


### SA-4 (10): Use Of Approved Piv Products

> The organization employs only information technology products on the FIPS 201-approved products list for Personal Identity Verification (PIV) capability implemented within organizational information systems.

##### LINCS

CivicActions/LINCS and AWS describes this control as “not applicable”, as PIV credentials are not applicable to the LINCS system. Access and Authentication requirements for the LINCS system for internal CivicActions and customer are implemented under access management and enforcement (AC-2 and AC-3) and identification and authentication for all users (IA-2 and IA-8).
It is the responsibiility of LINCS for implementation of PIV capability for authentication as required.


### SA-5: Information System Documentation

> The organization:
>   a.  Obtains administrator documentation for the information system, system component,
> or information system service that describes:
>     1.  Secure configuration, installation, and operation of the system, component,
> or service;
>     2.  Effective use and maintenance of security functions/mechanisms; and
>     3.  Known vulnerabilities regarding configuration and use of administrative
> (i.e., privileged) functions;
>   b.  Obtains user documentation for the information system, system component,
> or information system service that describes:
>     1.  User-accessible security functions/mechanisms and how to effectively use
> those security functions/mechanisms;
>     2.  Methods for user interaction, which enables individuals to use the system,
> component, or service in a more secure manner; and
>     3.  User responsibilities in maintaining the security of the system, component,
> or service;
>   c.  Documents attempts to obtain information system, system component, or information
> system service documentation when such documentation is either unavailable or nonexistent and takes [Assignment: organization-defined actions] in response;
>   d.  Protects documentation as required, in accordance with the risk management
> strategy; and
>   e.  Distributes documentation to [Assignment: organization-defined personnel
> or roles].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: information system documentation.


##### LINCS

The Department maintains adequate documentation for the LINCS Technology Project system. The LINCS Technology Project system documentation is protected as required and made available to authorized personnel. Procedures for protecting system documentation include management in the private CivicActions Git repository and the publicly available documentation trees for Free and Open Source Software (FOSS). The documentation maintained for the LINCS Technology Project system includes:
  
• System Security Plan (SSP) – this document
• Configuration documentation
• Incident Response and Contingency Plans
• Rules of Behavior (Acceptable Use Policy)
• FOSS Reference Manuals (Drupal, Moodle, GNU/Linux, Apache, MySQL, PHP, Postfix, etc.)


#### a

##### CivicActions

Some application features are built on a custom basis and are not part of standard FOSS packages. Administrator documentation for those custom features is maintained in the CivicActions Git repository documentation system.


##### Drupal

Public documentation related to Drupal is maintained by the Drupal Association and is located at: <https://drupal.org/documentation>. This documentation contains administrator documentation for the information system that describes:
• secure configuration, installation, and operation of the system, component, or service;
• effective use and maintenance of security functions/mechanisms; and
• known vulnerabilities regarding configuration and use of administrative functions;


#### b

##### CivicActions

The publicly-available FOSS package documentation described in control SA-5(a) also includes user documentation for non-administrators as described in control AC-3. This includes documentation on how to create and manage user accounts as well as how to create, update and delete content.
CivicActions follows the user docuemntation standard practice to provide context-sensitive help as well as access to a HelpDesk in publicly facing applications.
CivicActions' Customer Support team, described in control SA-3(b), handles questions about how to use the system. Questions are submitted by sending an email to support@civicactions.com, which triggers creation of a ticket in CivicActions' customer support ticketing system.


##### Drupal

The public documentation at drupal.org contains user documentation for the information system that describes:
• user-accessible security functions/mechanisms and how to effectively use those
  security functions/mechanisms;

• methods for user interaction, which enables individuals to use the system,
  component, or service in a more secure manner; and

• user responsibilities in maintaining the security of the system, component, or service;


#### c

##### CivicActions

If the information needed to answer a question is not already included in the website's public-facing documentation, a ticket is created to determine whether the question is sufficiently general in nature to warrant adding the answer to the website's documentation.


##### Drupal

As a popular and well-used and maintained free and open source (FOSS) project, in the event that sought after documentation is not available on Drupal.org, it can usually be found in one of the many forums, mailing lists or StackExchange sites covering Drupal and its many contributed modules.


#### d

##### CivicActions

All administrator documentation is housed in a protected Git repository. User documentation is publicly available..


##### Drupal

The Drupal.org documentation is multi-sourced on github and private repositories.


#### e

##### CivicActions

As needed and approved by CivicActions Security, documentation is available to appropriate personnel by granting access to the private Git repository.


##### Drupal

As the Drupal.org documentation is publicly available, there is no need to provide distribution mechanisms.


### SA-8: Security Engineering Principles

> The organization applies information system security engineering principles in the specification, design, development, implementation, and modification of the information system.

##### CivicActions

Information system security engineering principles are applied in the specification, design, development, implementation, and modification of the application system.
Sound security policy, developing layered protections, and controls have been established as the foundation for design throughout the SDLC defined in control SA-3. Security requirements are incorporated into that SDLC, as described previously.
CivicActions uses a development-stage-production testing and management workflow as part of the CivicActions development model. Changes are first tested on a development environment, then moved to a staging environment for further testing. Once the chnages have been tested and approved, a backup is made of the production environment, and the changes are then deployed. More information regarding this model can be found in CM-3 and CM-4.The CivicActions organization ensures that all its developers are trained on how to build secure software, that security controls have been tailored to meet business and operational needs.


### SA-9: External Information System Services

> The organization:
>   a.  Requires that providers of external information system services comply with
> organizational information security requirements and employ [Assignment: organization-defined security controls] in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance;
>   b.  Defines and documents government oversight and user roles and responsibilities
> with regard  to external information system services; and
>   c.  Employs [Assignment: organization-defined processes, methods, and techniques]
> to monitor security control compliance by external service providers on an ongoing basis.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: external information system services.


##### CivicActions

CivicActions does not have any dedicated interconnections between information system components within the authorization boundary and external third-party vendor information systems for the purposes of storing, processing, or transmitting federal agency data.


##### LINCS

LINCS does not have any dedicated interconnections between information system components within the authorization boundary and external third-party vendor information systems for the purposes of storing, processing, or transmitting federal agency data.
LINCS is hosted on the AWS Cloud platform, which was approved under the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


## SC: System and Communications Protection

### SC-1: System And Communications Protection Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A system and communications protection policy that addresses purpose,
> scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the system and communications
> protection policy and associated system and communications protection controls; and
>   b.  Reviews and updates the current:
>     1.  System and communications protection policy [Assignment: organization-defined
> frequency]; and
>     2.  System and communications protection procedures [Assignment: organization-defined
> frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a system and communication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Communications Protection (SC) Policy CivicActions document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.


##### LINCS

System and communications protection policy and procedures are formally documented in the Department of Education, Handbook for Information Assurance Security Policy (Handbook OCIO-01) and the LINCS SSP. The Department reviews and updates the policy as necessary and has been continually updated since April 2008.
This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.


### SC-5: Denial Of Service Protection

> The information system protects against or limits the effects of the following types of denial of service attacks: [Assignment: organization-defined types of denial of service attacks or references to sources for such information] by employing [Assignment: organization-defined security safeguards].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: denial of service protection.


##### Drupal

Drupal has a manual ability to block IP addresses in cases where attacks bypass cloud protection. This is managed by CivicActions Operations.


##### LINCS

The LINCS Technology Project system is configured to reduce vulnerabilities in its operating system and applications to protect against Denial of Service (DoS) attacks.
The LINCS support staff ensures the system is protected against or limits the effect of DoS attacks as specified in the Department of Education, Handbook for Information Security Incident Response and Reporting Procedures (Handbook OCIO-14).


### SC-7: Boundary Protection

> The information system:
>   a.  Monitors and controls communications at the external boundary of the system
> and at key internal boundaries within the system;
>   b.  Implements subnetworks for publicly accessible system components that are
> [Selection: physically; logically] separated from internal organizational networks; and
>   c.  Connects to external networks or information systems only through managed
> interfaces consisting of boundary protection devices arranged in accordance with an organizational security architecture.

##### Drupal

Drupal, when deployed on SELinux in full enforcing mode, minimizes the number of services and computing nodes that are exposed to the Internet. Drupal employs both the AWS platform safeguards and the Drupal Watchdog module in monitoring and recording system events. All other computing nodes used in the system are isolated within AWS.


##### LINCS

The LINCS Technology Project system has monitored and controlled communications at the external boundary of the information system and at key internal boundaries within the system, where appropriate. The LINCS allocates publicly accessible information system components (e.g., public web servers) specific IP address and port combinations. Public access into the organization’s internal networks is prevented except as appropriately mediated.


#### a

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: boundary protection.


#### b

##### AWS

The authorization boundary is completely contained within a Virtual Private Cloud (VPC) created and managed by the AWS Infrastructure as a Service (IaaS). External connections must be explicitly configured via the AWS Security Groups (SG) mechanism.
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: boundary protection.


#### c

##### AWS

Internal organizational networks (e.g. CivicActions private networks) are physically separate from the AWS platform and are protected by managed boundary devices that include FIPS 140-2 validated encryption modules at all entry points.
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: boundary protection.


### SC-12: Cryptographic Key Establishment And Management

> The organization establishes and manages cryptographic keys for required cryptography employed within the information system in accordance with [Assignment: organization-defined requirements for key generation, distribution, storage, access, and destruction].

##### LINCS

Use of cryptographic key management for the LINCS system is not in use for at the time of implementation for authentication. CivicActions does not utilize customer agency supplied PIV credentials for access to customer instances of the LINCS. Access enforcement and authentication requirements for LINCS are described in AC-2 & IA-2. AWS platform does not utilize or manage cryptographic keys within the ACE boundary.


### SC-13: Cryptographic Protection

> The information system implements [Assignment: organization-defined cryptographic uses and type of cryptography required for each use] in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: cryptographic protection for data in motion (with SSH and HTTPS/SSL) and for data at rest (with Elastic Block Store (EBS) volumnes).


##### CivicActions

The information system implements:
• cryptographic modules through Secure Shell (SSH) to allow administrators to securely logon to the various system components
• HTTPS/SSL (TLS) for connection to web-based services
• TLS for connection to email services
* AES-256 (FIPS 140-2 validated) for data at rest (with Elastic Block Store (EBS) volumnes)


### SC-15: Collaborative Computing Devices

> The information system:
>   a.  Prohibits remote activation of collaborative computing devices with the
> following exceptions: [Assignment: organization-defined exceptions where remote activation is to be allowed]; and
>   b.  Provides an explicit indication of use to users physically present at the
> devices.

##### LINCS

This control is not applicable, as the LINCS system does not employ any collaborative computing devices.


### SC-20: Secure Name / Address Resolution Service (Authoritative Source)

> The information system:
>   a.  Provides additional data origin authentication and integrity verification
> artifacts along with the authoritative name resolution data the system returns in response to external name/address resolution queries; and
>   b.  Provides the means to indicate the security status of child zones and (if
> the child supports secure resolution services) to enable verification of a chain of trust among parent and child domains, when operating as part of a distributed, hierarchical namespace.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (authoritative source)


### SC-21: Secure Name / Address Resolution Service (Recursive Or Caching Resolver)

> The information system requests and performs data origin authentication and data integrity verification on the name/address resolution responses the system receives from authoritative sources.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (recursive or caching resolver)


### SC-22: Architecture And Provisioning For Name / Address Resolution Service

> The information systems that collectively provide name/address resolution service for an organization are fault-tolerant and implement internal/external role separation.

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: architecture and provisioning for name / address resolution service.


### SC-39: Process Isolation

> The information system maintains a separate execution domain for each executing process.

##### CivicActions

Process isolation is maintained on the Linux platform. Linux is the only operating system that is part of the boundary.


## SI: System and Information Integrity

### SI-1: System And Information Integrity Policy And Procedures

> The organization:
>   a.  Develops, documents, and disseminates to [Assignment: organization-defined
> personnel or roles]:
>     1.  A system and information integrity policy that addresses purpose, scope,
> roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
>     2.  Procedures to facilitate the implementation of the system and information
> integrity policy and associated system and information integrity controls; and
>   b.  Reviews and updates the current:
>     1.  System and information integrity policy [Assignment: organization-defined
> frequency]; and
>     2.  System and information integrity procedures [Assignment: organization-defined
> frequency].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a system and information integrity policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Information Integrity (SI) Policy document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.


##### LINCS

System and information integrity policy and procedures for the LINCS Technology Project system are formally documented in the LINCS SSP, which provides the roles and responsibilities as it pertains to physical and environmental protection systems. The LINCS Technology Project system support staff monitors the network on a daily basis and employs up-to-date patches to protect the integrity of the system.
Additional information is contained within the Department of Education, Handbook for Information Assurance Security Policy (Handbook OCIO-01.
This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.


### SI-2: Flaw Remediation

> The organization:
>   a.  Identifies, reports, and corrects information system flaws;
>   b.  Tests software and firmware updates related to flaw remediation for effectiveness
> and potential side effects before installation;
>   c.  Installs security-relevant software and firmware updates within [Assignment:
> organization-defined time period] of the release of the updates; and
>   d.  Incorporates flaw remediation into the organizational configuration management
> process.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  flaw remediation.


##### Drupal

Drupal contains built-in security status monitoring of the core application and contributed modules.


#### a

##### CivicActions

Identification of information system security flaws are detected as early as possible by the following methods:
• Vulnerability scans, as described in RA-5.
• Log analysis from monitoring described in SI-4.
• Service flaw notifications (CVEs, etc.) are received by CivicActions Security and passed on to CicvicActions Operations when relevant.
Any security issues found are ticketed through JIRA and/or the Git issue queue. CivicActions Operations prioritizes the high findings.  Changes made to correct the information system as a result of the system flaws are scheduled and coordinated through the CCB Change Request Process and appropriate approvals required from the CCB as implemented in CM-3.


#### b

##### CivicActions

CivicActions testing of the system as a result of security flaw remediation are done through a development environment though use of internal software and automated testing that ensures the system is working as intended. When a change is made by a developer, testing though a peer review is conducted as part of the Change Request process to ensure the correct analysis is completed. Then changed code is tested in an automatic test environment as described in Configuration Management Plan (CMP). Tracking of the testing is documented in JIRA and/or the Git issue queue.


#### c

##### CivicActions

CivicActions security-software updates are tested prior to place to production. The CivicActions Security framework for installation requires updates to be made within 30 days for high vulnerabilities, 90 days for moderate vulnerabilities, and 240 for low vulnerabilities. An issue ticket is created to track the any updates made to the system.


#### d

##### CivicActions

Flaw remediation is part of the CivicActions configuration management process.  Any security issues found are ticketed through JIRA or the Git issue queue. CivicActions Security prioritizes the high findings within the application. Changes made to correct the system as a result of the system flaws are scheduled and coordinated through the CCB Change Request Process and appropriate approvals required from the CCB Chair as implemented in CM-3.


### SI-2(2): SI-2(2)

> The organization:
>   a.  Identifies, reports, and corrects information system flaws;
>   b.  Tests software and firmware updates related to flaw remediation for effectiveness
> and potential side effects before installation;
>   c.  Installs security-relevant software and firmware updates within [Assignment:
> organization-defined time period] of the release of the updates; and
>   d.  Incorporates flaw remediation into the organizational configuration management
> process.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: automated flaw remediation status.


##### CivicActions

The OpenSCAP and OWASP ZAP security scanners are used to perform monthly vulnerability scans of all system components and assess web application interfaces to identify any performance or security issues/flaws. Vulnerabilities and findings identified are handled and remediated in accordance with the implementation of RA-5. Reports are generated to CivicActions Security and Operations for review, analysis, and remediation.


### SI-3: Malicious Code Protection

> The organization:
>   a.  Employs malicious code protection mechanisms at information system entry
> and exit points to detect and eradicate malicious code;
>   b.  Updates malicious code protection mechanisms whenever new releases are available
> in accordance with organizational configuration management policy and procedures;
>   c.  Configures malicious code protection mechanisms to:
>     1.  Perform periodic scans of the information system [Assignment: organization-defined
> frequency] and real-time scans of files from external sources at [Selection (one or more); endpoint; network entry/exit points] as the files are downloaded, opened, or executed in accordance with organizational security policy; and
>     2.  [Selection (one or more): block malicious code; quarantine malicious code;  send
> alert to administrator; [Assignment: organization-defined action]] in response to malicious code detection; and
>   d.  Addresses the receipt of false positives during malicious code detection
> and eradication and the resulting potential impact on the availability of the information system.

#### a

##### CivicActions

Virus scans are performed by ClamAV, a server-hosted tool protecting the application from Trojans, Viruses and other malicious cyber-threats. Real-time scans are conducted whenever files are uploaded from any external source and malicious code is blocked or quarantined when detected. All file-based traffic traversing the server is sanitized before being delivered. All input form text is validated and sanitized.


#### b

##### CivicActions

Anti-virus definitions and malicious code protection mechanisms are configured and updated automatically on a nightly basis.


#### c

##### CivicActions

CivicActions Operations receives information system security alerts, advisories and notifications in response to malicious code detection. These messages are sent to group email distribution lists to ensure all members of the team receive the proper information in a timely manner.


#### d

##### CivicActions

False positives during malicious code detection and eradication are dealt with on a case by case basis. Potential impacts on the availability of the information system are detailed in a false positive report depending on if the report is for the OS, database or web application.


### SI-4: Information System Monitoring

> The organization:
>   a.  Monitors the information system to detect:
>     1.  Attacks and indicators of potential attacks in accordance with [Assignment:
> organization-defined monitoring objectives]; and
>     2.  Unauthorized local, network, and remote connections;
>   b.  Identifies unauthorized use of the information system through [Assignment:
> organization-defined techniques and methods];
>   c.  Deploys monitoring devices:
>     1.  Strategically within the information system to collect organization-determined
> essential information; and
>     2.  At ad hoc locations within the system to track specific types of transactions
> of interest to the organization;
>   d.  Protects information obtained from intrusion-monitoring tools from unauthorized
> access, modification, and deletion;
>   e.  Heightens the level of information system monitoring activity whenever there
> is an indication of increased risk to organizational operations and assets, individuals, other organizations, or the Nation based on law enforcement information, intelligence information, or other credible sources of information;
>   f.  Obtains legal opinion with regard to information system monitoring activities
> in accordance with applicable federal laws, Executive Orders, directives, policies, or regulations; and
>   g.  Provides [Assignment: organization-defined information system monitoring
> information] to [Assignment: organization-defined personnel or roles] [Selection (one or more): as needed; [Assignment: organization-defined frequency]].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: information system monitoring.


#### a

##### CivicActions

CivicActions systems use a collection of monitoring systems, including:
• ClamAV - provides signature based malware detection/quarantine
• OSSEC host-based intrusion detection system (HIDS)
• AIDE Advanced Intrusion Detection Environment (IDS))
• fail2ban, an intrusion prevention system (IPS) framework
• SELinux - a Mandatory Access Control (MAC) IPS
• auditd - a secure system audit daemon
• CloudWatch - AWS monitoring and measurement system
• StatusCake - website monitoring tool
• OpsGenie - a slack/email/text/phone incident escalation tool


#### b

##### CivicActions

Logs from the systems described in SI-4(a) are sent to the CivicActions SIEM tool for analysis. These logs can identify unauthorized use of the information system.


#### c

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.
CivicActions leverages the AWS platform and a host-based intrusion detection system (HIDS) for monitoring strategically within the information system to collect organization-determined essential information and at ad hoc locations within the system; see inheritance below.


##### CivicActions

Monitoring and log collection occurs throughout the system.


#### d

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.


##### CivicActions

The Configuration Management process, remote log gathering and SELinux MAC protects information obtained from intrusion-monitoring tools from unauthorized access, modification, and deletion.


#### e

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.


##### CivicActions

In the event of a performance score lower than CivicActions standards, a notification is sent to CivicActions Security. CivicActions subscribes to security mailing lists in the event the monitoring activity is required based on law enforcement information, intelligence information, or other credible sources of information.


#### f

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.


##### CivicActions

Internal legal counsel is utilized as required when system notifications indicate such action based on user and/or malicious activity.  Legal counsel is engaged for any actions that may necessitate increased user monitoring, or evidence/forensic actions.


#### g

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.
AWS’s monitoring mechanisms provide notification including audit records, input from malicious code protection mechanisms, data from intrusion detection and prevention mechanisms, and boundary protection devices to the AWS Security Team on a daily basis.


##### CivicActions

System alerts generated by CivicActions internal monitors (StatusCake, OSSEC, ClamAV, others) are sent to the Incident Response team via OpsGenie.


### SI-5: Security Alerts, Advisories, And Directives

> The organization:
>   a.  Receives information system security alerts, advisories, and directives
> from [Assignment: organization-defined external organizations] on an ongoing basis;
>   b.  Generates internal security alerts, advisories, and directives as deemed
> necessary;
>   c.  Disseminates security alerts, advisories, and directives to: [Selection
> (one or more): [Assignment: organization-defined personnel or roles]; [Assignment: organization-defined elements within the organization]; [Assignment: organization-defined external organizations]]; and
>   d.  Implements security directives in accordance with established time frames,
> or notifies the issuing organization of the degree of noncompliance.

##### Drupal

CivicActions Security and Operations receive Drupal Security Advisories on a regular basis.


##### LINCS

LINCS Technology Project representatives and system administrators receive alerts from US-CERT on a regular basis. Support personnel take appropriate action in response to relevant areas of concern.


#### a

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.
The AWS Insight control panel provides direct access to the monitored systems.


##### CivicActions

CivicActions Security and Operations receive the following security alerts, advisories and directives on an ongoing basis:
• Mailing lists relevant to web application security
• US-CERT
• Technical Cyber Security Alerts
• Drupal Security Advisories


#### b

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.
The AWS host-based intrusion detection system (HIDS) monitors the events of the system boundary.


##### CivicActions

CivicActions utilizes StatusCake for front line monitoring for real-time system status and events of the application. StatusCake can feed to the OpsGenie incident escalation system.


#### c

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.


##### CivicActions

CivicActions Security disseminates security alerts, advisories, advisories, and directives to all CivicActions internal personnel and client personnel as directed.


#### d

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.


##### CivicActions

CivicActions Security is responsible for ensuring the dissemination and implementation of relevant security alerts and advisories.


### SI-7: Software, Firmware, And Information Integrity

> The organization employs integrity verification tools to detect unauthorized changes to [Assignment: organization-defined software, firmware, and information].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  software, firmware, and information integrity.


##### CivicActions

CivicActions employ the GitHub system to monitor source code and version control ensuring system integrity and prevents unauthorized changes.  The PHP-authenticator tool is perform a format check on source code prior to entering production. Per implementation of CM-3, any changes to the source code of the system requires the CCB Change Request process. A peer review as part of the Change Request process is conducted to ensure the requested change is verified prior to entering production.
CivicActions employs additional integrity checks on production systems as described in SI-4.


### SI-7 (1): Integrity Checks

> The information system performs an integrity check of [Assignment: organization-defined software, firmware, and information] [Selection (one or more): at startup; at [Assignment: organization-defined transitional states or security-relevant events]; [Assignment: organization-defined frequency]].

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  integrity checks.


##### CivicActions

The integrity check implementation of SI-7 is conducted though the GitHub system and verified monthly by redeploying the system codebase from GitHub.


### SI-7 (5): Automated Response To Integrity Violations

> The information system automatically [Selection (one or more): shuts the information system down; restarts the information system; implements [Assignment: organization-defined security safeguards]] when integrity violations are discovered.

##### CivicActions

The system maintains an audit log of all operations including integrity violations. When an integrity violation occurs, CivicActions Operations will be alerted via email with escalations to text and phone as needed.


### SI-7 (7): Integration Of Detection And Response

> The organization incorporates the detection of unauthorized [Assignment: organization-defined security-relevant changes to the information system] into the organizational incident response capability.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  integration of detection and response. AWS has deployed OSSEC HIDS to all AWS Enterprise hosts which continuously monitors and alerts for software changes as they occur throughout the AWS platform.


##### CivicActions

CivicActions incident response and configuration capabilities include the detection of unauthorized changes to the system though the IR Plan and CCB Change Request process and the implementation of IR-4 and IR-5. In the event of an unauthorized security change to the system, CivicActions support would roll back to and restore from the most recent authorized database set.


### SI-10: Information Input Validation

> The information system checks the validity of [Assignment: organization-defined information inputs].

##### Drupal

All Drupal form input text is subject to format verification and input validation.


### SI-11: Error Handling

> The information system:
>   a.  Generates error messages that provide information necessary for corrective
> actions without revealing information that could be exploited by adversaries; and
>   b.  Reveals error messages only to [Assignment: organization-defined personnel
> or roles].

#### a

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: error handling.


##### Drupal

Drupal system error logs do not contain passwords, personal information, encryption keys or other sensitive information.


##### LINCS

Drupal in production operation mode does not display application errors to the user but instead displays a predefined page indication that a request cannot be handled as requested and logs all errors to the watchdog.log file.


#### b

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: error handling.


##### Drupal

Drupal system error logs are only available to authenticated administrators and viewable within the administrative interface.


### SI-12: Information Handling And Retention

> The organization handles and retains information within the information system and information output from the system in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and operational requirements.

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: information output handling and retention.


##### CivicActions

The CivicActions organization retains all information, system-related information, incident-related information, and system output in accordance with customers’ requirements retention periods and other NIST guidance and standards, Federal policies, procedures, Federal laws and executive orders. Audit records are retained for 365 days.


##### LINCS

LINCS Technology Project representatives and systems administrators receive annual training from the Department regarding information assurance and information handling requirements. These personnel are required to operate the system and handle system data and output in accordance with legal requirements. Personnel training and system guidelines ensure that data and programs are handled appropriately.


# NIST SP 800-53 Revision 4 Privacy

## AP: AP

### AP-1: AP-1

##### Privacy

Under Title II of the Workforce Innovation and Opportunity Act (WIOA; PL 113-128),
Section 242, OCTAE carries out a program of national leadership activities to
enhance the quality and outcomes of adult education and literacy activities and
programs nationwide. OCTAE uses these funds to provide technical assistance and
professional development to programs and contribute to research and evaluations of
adult education programs and activities.


### AP-2: AP-2

##### Privacy

LINCS does not collect PII other than that covered by the "Roladex exception".
Anonymous access is possible, but courses and community participation require an
account for which these fields are required:

* Email address -  used for identification.

* First name, last name - used for addressing a logged in user.

Any additional information is entered by the user at will as part of coursework or
to enhance community participation in forums.


## AR: Accountability, Audit, and Risk Management

### AR-1: GOVERNANCE AND PRIVACY PROGRAM

> "The organization:
>    a.   Appoints a Senior Agency Official for Privacy (SAOP)/Chief Privacy Officer
>         (CPO) accountable for developing, implementing, and maintaining an organization-wide
>         governance and privacy program to ensure compliance with all applicable
> laws and
>         regulations regarding the collection, use, maintenance, sharing, and disposal
>         of personally identifiable information (PII) by programs and information
> systems;
>    b.   Monitors federal privacy laws and policy for changes that affect the privacy
>         program;
>    c.   Allocates [Assignment: organization-defined allocation of budget and staffing]
>         sufficient resources to implement and operate the organization-wide privacy
> program;
>    d.   Develops a strategic organizational privacy plan for implementing applicable
>         privacy controls, policies, and procedures;
>    e.   Develops, disseminates, and implements operational privacy policies and
>         procedures that govern the appropriate privacy and security controls for
> programs,
>         information systems, or technologies involving PII; and
>    f.   Updates privacy plan, policies, and procedures [Assignment: organization-defined
>         frequency, at least biennially]."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-2: PRIVACY IMPACT AND RISK ASSESSMENT

> "The organization:
>      a.   Documents and implements a privacy risk management process that assesses
> privacy risk to
>           individuals resulting from the collection, sharing, storing, transmitting,
> use, and disposal of
>           personally identifiable information (PII); and
>      b.   Conducts Privacy Impact Assessments (PIAs) for information systems,
> programs, or other
>           activities that pose a privacy risk in accordance with applicable law,
> OMB policy, or any
>           existing organizational policies and procedures."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-3: PRIVACY REQUIREMENTS FOR CONTRACTORS AND SERVICE PROVIDERS

> "The organization:
>      a.   Establishes privacy roles, responsibilities, and access requirements for contractors and service
>           providers; and
>      b.   Includes privacy requirements in contracts and other acquisition-related documents."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-4: PRIVACY MONITORING AND AUDITING

> "The organization monitors and audits privacy controls and internal privacy policy
>   [Assignment: organization-defined frequency] to ensure effective implementation."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-5: PRIVACY AWARENESS AND TRAINING

> "The organization:
>      a.   Develops, implements, and updates a comprehensive training and awareness
> strategy aimed at
>           ensuring that personnel understand privacy responsibilities and procedures;
>      b.   Administers basic privacy training [Assignment: organization-defined
> frequency, at least
>           annually] and targeted, role-based privacy training for personnel having
> responsibility for
>           personally identifiable information (PII) or for activities that involve
> PII [Assignment:
>           organization-defined frequency, at least annually]; and
>      c.   Ensures that personnel certify (manually or electronically) acceptance
> of responsibilities for
>           privacy requirements [Assignment: organization-defined frequency, at
> least annually]."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-6: PRIVACY REPORTING

> The organization develops, disseminates, and updates reports to the Office of
>      Management and Budget (OMB), Congress, and other oversight bodies, as appropriate,
> to
>      demonstrate accountability with specific statutory and regulatory privacy
> program mandates, and
>      to senior management and other personnel with responsibility for monitoring
> privacy program
>      progress and compliance."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-7: PRIVACY-ENHANCED SYSTEM DESIGN AND DEVELOPMENT

> Control:The organization designs information systems to support privacy by automating privacy controls.

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-8: ACCOUNTING OF DISCLOSURES

> "The organization:
>      a.   Keeps an accurate accounting of disclosures of information held in each
> system of records
>           under its control, including:
>           (1) Date, nature, and purpose of each disclosure of a record; and
>           (2) Name and address of the person or agency to which the disclosure
> was made;
>      b.   Retains the accounting of disclosures for the life of the record or
> five years after the
>           disclosure is made, whichever is longer; and
>      c.   Makes the accounting of disclosures available to the person named in
> the record upon request."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


## DI: Data Quality and Integrity

### DI-1: DATA QUALITY

> "The organization:
>      a.    Confirms to the greatest extent practicable upon collection or creation
> of personally
>            identifiable information (PII), the accuracy, relevance, timeliness,
> and completeness of that
>            information;
>      b.    Collects PII directly from the individual to the greatest extent practicable;
>      c.    Checks for, and corrects as necessary, any inaccurate or outdated PII
> used by its programs or
>            systems [Assignment: organization-defined frequency]; and
>      d.    Issues guidelines ensuring and maximizing the quality, utility, objectivity,
> and integrity of
>            disseminated information."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


### DI-2: DATA INTEGRITY AND DATA INTEGRITY BOARD

> "The organization:
>      a.    Documents processes to ensure the integrity of personally identifiable information (PII)
>            through existing security controls; and
> 
> 
>      b.    Establishes a Data Integrity Board when appropriate to oversee organizational Computer
>            Matching Agreements 123 and to ensure that those agreements comply with the computer
>            matching provisions of the Privacy Act."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


## DM: Data Minimization and Retention

### DM-1: MINIMIZATION OF PERSONALLY IDENTIFIABLE INFORMATION

> "The organization:
>      a.    Identifies the minimum personally identifiable information (PII) elements
> that are relevant
>            and necessary to accomplish the legally authorized purpose of collection;
>      b.    Limits the collection and retention of PII to the minimum elements
> identified for the purposes
>            described in the notice and for which the individual has provided consent;
> and
>      c.    Conducts an initial evaluation of PII holdings and establishes and
> follows a schedule for
>            regularly reviewing those holdings [Assignment: organization-defined
> frequency, at least
>            annually] to ensure that only PII identified in the notice is collected
> and retained, and that the
>            PII continues to be necessary to accomplish the legally authorized
> purpose."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. The data collected (email address, first
and last name) is demonstrably a minimum.


### DM-2: DATA RETENTION AND DISPOSAL

> "The organization:
>      a. Retains each collection of personally identifiable information (PII)
>         for [Assignment: organization-defined time period] to fulfill the purpose(s) identified in the notice or as
>         required by law;
>      b. Disposes of, destroys, erases, and/or anonymizes the PII, regardless
>         of the method of storage, in accordance with a NARA-approved record retention
>         schedule and in a manner that prevents loss, theft, misuse, or unauthorized access; and
>      c. Uses [Assignment: organization-defined techniques or methods] to ensure
>         secure deletion or destruction of PII (including originals, copies, and 
>         archived records)."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### DM-3: MINIMIZATION OF PII USED IN TESTING, TRAINING, AND RESEARCH

> "The organization:
>      a.    Develops policies and procedures that minimize the use of personally identifiable information
>            (PII) for testing, training, and research; and
>      b.    Implements controls to protect PII used for testing, training, and research."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


## IP: Individual Participation and Redress

### IP-1: CONSENT

> "The organization:
>      a.    Provides means, where feasible and appropriate, for individuals to
> authorize the collection,
>            use, maintaining, and sharing of personally identifiable information
> (PII) prior to its
>            collection;
>      b.    Provides appropriate means for individuals to understand the consequences
> of decisions to
>            approve or decline the authorization of the collection, use, dissemination,
> and retention of PII;
>      c.    Obtains consent, where feasible and appropriate, from individuals prior
> to any new uses or
>            disclosure of previously collected PII; and
>      d.    Ensures that individuals are aware of and, where feasible, consent
> to all uses of PII not
>            initially described in the public notice that was in effect at the
> time the organization collected
>            the PII."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


### IP-2: INDIVIDUAL ACCESS

> "The organization:
>      a.   Provides individuals the ability to have access to their personally identifiable information
>           (PII) maintained in its system(s) of records;
>      b.   Publishes rules and regulations governing how individuals may request access to records
>           maintained in a Privacy Act system of records;
>      c.   Publishes access procedures in System of Records Notices (SORNs); and
>      d.   Adheres to Privacy Act requirements and OMB policies and guidance for the proper
>           processing of Privacy Act requests."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


### IP-3: REDRESS

> "The organization: a.   Provides a process for individuals to have inaccurate personally identifiable information (PII) maintained by the organization corrected or amended, as appropriate; and b.   Establishes a process for disseminating corrections or amendments of the PII to other authorized users of the PII, such as external information-sharing partners and, where feasible and appropriate, notifies affected individuals that their information has been corrected or amended."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


### IP-4: COMPLAINT MANAGEMENT

> "The organization implements a process for receiving and responding to complaints,
>   concerns, or questions from individuals about the organizational privacy practices."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


## SE: Security

### SE-1: INVENTORY OF PERSONALLY IDENTIFIABLE INFORMATION

> "The organization:
>      a.   Establishes, maintains, and updates [Assignment: organization-defined
> frequency] an
>           inventory that contains a listing of all programs and information systems
> identified as
>           collecting, using, maintaining, or sharing personally identifiable information
> (PII); and
>      b.   Provides each update of the PII inventory to the CIO or information
> security official
>           [Assignment: organization-defined frequency] to support the establishment
> of information
>           security requirements for all new or modified information systems containing
> PII."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### SE-2: PRIVACY INCIDENT RESPONSE

> "The organization:
>      a.   Develops and implements a Privacy Incident Response Plan; and
>      b.   Provides an organized and effective response to privacy incidents in accordance with the
>           organizational Privacy Incident Response Plan."

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


## TR: Transparency

### TR-1: PRIVACY NOTICE

> "The organization:
>      a.    Provides effective notice to the public and to individuals regarding:
> (i) its activities that
>            impact privacy, including its collection, use, sharing, safeguarding,
> maintenance, and disposal
>            of personally identifiable information (PII); (ii) authority for collecting
> PII; (iii) the choices, if
>            any, individuals may have regarding how the organization uses PII and
> the consequences of
>            exercising or not exercising those choices; and (iv) the ability to
> access and have PII amended
>            or corrected if necessary;
>      b.    Describes: (i) the PII the organization collects and the purpose(s)
> for which it collects that
>            information; (ii) how the organization uses PII internally; (iii) whether
> the organization shares
>            PII with external entities, the categories of those entities, and the
> purposes for such sharing;
>            (iv) whether individuals have the ability to consent to specific uses
> or sharing of PII and how
>            to exercise any such consent; (v) how individuals may obtain access
> to PII; and (vi) how the
>            PII will be protected; and
>      c.    Revises its public notices to reflect changes in practice or policy
> that affect PII or changes in
>            its activities that impact privacy, before or as soon as practicable
> after the change."

##### Privacy

LINCS publishes a privacy policy in the footer of every  page. Further, upon login,
the user must accept a detailed Terms and Conditions of Use.


### TR-2: SYSTEM OF RECORDS NOTICES AND PRIVACY ACT STATEMENTS

> "The organization:
>      a.    Publishes System of Records Notices (SORNs) in the Federal Register,
> subject to required
>            oversight processes, for systems containing personally identifiable
> information (PII);
>      b.    Keeps SORNs current; and
>      c.    Includes Privacy Act Statements on its forms that collect PII, or on
> separate forms that can be
>            retained by individuals, to provide additional formal notice to individuals
> from whom the
>            information is being collected."

##### Privacy

LINCS does not collect or maintain PII and therefore does not publish a SORN.


### TR-3: DISSEMINATION OF PRIVACY PROGRAM INFORMATION

> "The organization:
>      a.    Ensures that the public has access to information about its privacy activities and is able to
>            communicate with its Senior Agency Official for Privacy (SAOP)/Chief Privacy Officer
>            (CPO); and
>      b.    Ensures that its privacy practices are publicly available through organizational websites or
>            otherwise."

##### Privacy

LINCS publishes a privacy policy in the footer of every page. Further, upon login,
the user must accept a detailed Terms and Conditions of Use.


## UL: Use Limitation

### UL-1: INTERNAL USE

> "The organization uses personally identifiable information (PII) internally only for the
>       authorized purpose(s) identified in the Privacy Act and/or in public notices."

##### Privacy

The information is collected on the LINCS Community is for identification and
authentication purposes, allowing individuals to:

* Identify themselves to the system

* Authenticate with the system to prove that they are the same person when they
return

* Enable emailed password reset

* Access control (e.g. updating notification settings, following a moderation of a
discussion, etc.)

* Carry out actions that impact that individual (e.g. joining a course or signing up
for a mailing list subscription)

* Publish information to make it available to others (e.g. forum posting, comment on
publications of learning resources, etc.)


### UL-2: INFORMATION SHARING WITH THIRD PARTIES

> "The organization:
>      a.   Shares personally identifiable information (PII) externally, only for
> the authorized purposes
>           identified in the Privacy Act and/or described in its notice(s) or for
> a purpose that is
>           compatible with those purposes;
>      b.   Where appropriate, enters into Memoranda of Understanding, Memoranda
> of Agreement,
>           Letters of Intent, Computer Matching Agreements, or similar agreements,
> with third parties
>           that specifically describe the PII covered and specifically enumerate
> the purposes for which
>           the PII may be used;
>      c.   Monitors, audits, and trains its staff on the authorized sharing of
> PII with third parties and on
>           the consequences of unauthorized use or sharing of PII; and
>      d.   Evaluates any proposed new instances of sharing PII with third parties
> to assess whether the
>           sharing is authorized and whether additional or new public notice is
> required."

##### Privacy

LINCS does not share any collected information with any third parties.



