# ACCESS CONTROL

## AC-01 ACCESS CONTROL POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=AC-1>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel an access control policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Access Control (AC) Policy.  This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.



#### LINCS specific control or LINCS Responsibility

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

Access control policy and procedures are documented in the LINCS SSP. Access to LINCS Technology Project operational information or system resources is limited to only authorized users, programs or processes. The Department enforces access control policies to protect the integrity of the LINCS Technology Project system. This Department reviews and updates this policy as necessary and it has been being updated, as necessary, since April 2008.

Additional information is contained within the Department of Education, OCIO-01, Handbook for Information Assurance Cybersecurity Policy.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## AC-02 ACCOUNT MANAGEMENT

> Control description: <http://800-53.govready.com/control?id=AC-2>
> 
> 
> 
> Security control type: Partially Inheritable


#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS account management.



### Part a)

#### Drupal specific control support

Drupal provides user accounts for individuals who participate in visiting, contributing to and administering the site with the following roles:

* Anonymous user – readers of the site who either do not have an account or are not logged in.

* Authenticated user – All non-anonymous users inherit the "authenticated user role."

* Administrator - This role has all permissions enabled by default.



#### LINCS specific control or LINCS Responsibility

SSH system accounts are provided to contractors on an as-needed basis.

Access privileges are used to ensure that only authorized personnel access certain areas of the LINCS Technology Project system. User access is controlled by the completion and submission of LINCS Technology Project System Rules of Behavior and New User Account Request forms by the user and management. These items are completed and submitted whenever a new user requires access or an existing user requires access changes. The system administrator, based on need-to-know, assigns the proper permissions. The employee’s manager approves the access rights before the initial account is created. Finally, the system administrator implements the access rights according to the New User Account Request form. The security staff and the support contractor review accounts periodically. Accounts no longer in use are removed from the system by the system administrator.

The LINCS Technology Project has implemented user account procedures to disable inactive user accounts after 90-days of inactivity. The LINCS support staff monitors all user accounts to ensure this procedure is enforced. Section 6.3, Authentication Management, of the LINCS SSP illustrates the exact procedures the contractor support staff follows to ensure accounts are properly managed.

The LINCS Technology Project system does not have guest or anonymous accounts.



### Part b)

#### Drupal specific control support

CivicActions' Project Manager assigns the "admininstrator" role for the management of all accounts issued to internal admin roles supporting the information system. Account requests are initiated by the Project Manager by completing a ticket request and the CivicActions Operation Team manages the entire account creation process.



#### LINCS specific control or LINCS Responsibility

The Project Owner has oversight over all permissions that the Project Manager and Operations Staff manages.



### Part c)

#### LINCS specific control or LINCS Responsibility

In accordance with LINCS Access Control Policy, LINCS group membership is determined according to the individual's position and role within the organization. A ticket request is used to request accounts and group membership. The request is authorized by the appropriate manager.



### Part d)

#### Drupal specific control support

All accounts issued for Drupal administrators and SSH are documented in CivicActions' ticketing system. Account request tickets contain details that explain the attributes for the account including authorized users of Drupal, system infrastructure, group and role membership, and access authorizations.



#### LINCS specific control or LINCS Responsibility

LINCS user privileges vary depending on the type of user role assigned. Only users with the role of Site Manager have the ability to create and modify user roles for other users.



### Part e)

#### Drupal specific control support

All accounts issued for the admin management of Drupal or SSH access must be approved by the Project Owner or Project Manager who must create an account request. The CivicActions Operations Team applies appropriate account permissions and settings based on the job role and function documented within the request ticket using processes defined by the CivicActions Security Team.



#### LINCS specific control or LINCS Responsibility

CivicActions sets up the initial Site Manager account for LINCS; however, any subsequent client access and related approvals are managed by LINCS.



### Part f)

#### Drupal specific control support

The CivicActions Operations Team is responsible for the following account management activities for both internal administrative users and customer accounts:

* Establishing account justification

* Activating accounts

* Modifying accounts

* Expiring accounts

* Disabling accounts

* Removing accounts



### Part h)

#### Drupal specific control support

In accordance with the CivicActions Access Control (AC) Policy when a CivicActions employee's account is no longer required, the employee’s manager notifies the Security Team to immediately disable all access. Users upon reassignment, change in roles, termination, or leaving employment are initially removed from all groups, effectively denying them all access to LINCS privileged accounts.



### Part i)

#### Drupal specific control support

CivicActions Drupal administration accounts require access authorizations prior to accounts being created. Employee managers must initiate an access request for an account to be created. The CivicActions Operations Team reviews the request to ensure accuracy, including intended system usage and other attributes of the user access being requested.



#### LINCS specific control or LINCS Responsibility

LINCS governs their own administrative access. The designated government contracting official responsible for approving the purchase of CivicActions' services, or authorized representative, is empowered to designate and approve Site Managers. It is left to the discretion of the designated government contracting official or authorized representative to determine if a Site Manager is considered to have a valid reason for accessing the CC application.



### Part j)

#### Drupal specific control support

All privileged accounts are reviewed by the CivicActions Operations Team every 180 days.



#### LINCS specific control or LINCS Responsibility

Site Managers are empowered to and responsible for reviewing their own accounts and determining whether the accounts should still be authorized.



### Part k)

#### Drupal specific control support

In accordance with standard security best practices and CivicActions policy, shared and reissued accounts for internal accounts of any kind are not created nor used for any purpose in any system.



## AC-03 ACCESS ENFORCEMENT

> Control description: <http://800-53.govready.com/control?id=AC-3>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

Access control in Drupal is enforced by authentication via unique username/password for every type of user except Anonymous user. The user’s privileges, permissions and access are provided on "least privilege" principle.

The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves. Administrators and Site Managers are the only user roles that can create new user accounts.



#### LINCS specific control or LINCS Responsibility

The LINCS Technology Project ensures that assigned authorizations for controlling access to the system is enforced in accordance with the user definitions noted in Section 1.1.1 of the LINCS SSP. The technical support staff ensures that access to security functions and protected information is restricted to authorized personnel. Access will be controlled with access control list used on each instance. Members of one group cannot access resources defined for other groups unless explicitly permitted.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS account management.



## AC-06 LEAST PRIVILEGE

> Control description: <http://800-53.govready.com/control?id=AC-6>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions performs regular audits of privileged users as part of the practice of enforcing least privilege.



#### Drupal specific control support

CivicActions implements the policy of least privilege for all logical components of Drupal by allowing only authorized access for users, which are necessary to accomplish assigned tasks in accordance with business functions and organizational need.

At the application layer, Drupal is designed with a role based user access system, a least privileged approach based on assignment of privileges to roles. Drupal‘s permission systems enables control of what users can do and see on the site. In consultation with LINCS, CivicActions has defined a specific set of permissions for each of the user roles mentioned in control AC-5.

SSH access is provided on a least privilege basis and analyzed on an ongoing basis, at least quarterly. Findings related to these audits of accounts are reported and reviewed by the CivicActions Data team and evaluated to determine roles that need to be revoked.



#### LINCS specific control or LINCS Responsibility

Drupal privileged access roles are designated by LINCS which is responsible for determining who will have administrator privileges and the ability to create other user accounts, including user accounts with the role of "administrator".



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: application of least privilege.



## AC-06 (9) AUDITING USE OF PRIVILEGED FUNCTIONS

> Control description: <http://800-53.govready.com/control?id=AC-6>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

CivicActions, at least quarterly, audits all team accounts based on the concept of least privilege. Each member of the developer team is assigned a role of which defines access needed to perform only the member’s job function.  The audit of accounts is reported and reviewed by the LINCS admin group and evaluated to determine whether roles or membership within the developer team should be changed. 



## AC-07 UNSUCCESSFUL LOGIN ATTEMPTS

> Control description: <http://800-53.govready.com/control?id=AC-7>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The LINCS Technology Project system locks out users after three unsuccessful login attempts. The information system automatically locks the account permanently, unless an administrator unlocks the account before then, when the maximum number of unsuccessful attempts (3) is exceeded.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: unsuccessful logon attempts.



### Part a)

#### Drupal specific control support

Drupal can be configured to lock an account after a specified number of invalid login attempts within specified time period.



### Part b)

#### Drupal specific control support

Lock down following unsuccessful attempts is configurable by Drupal administrators to conform to defined requirements.  When a user exceeds the limit of invalid logon attempts, their account is automatically locked for a specfied time and requires administrator action to unlock the account before the lockout period expires.



## AC-08 SYSTEM USE NOTIFICATION

> Control description: <http://800-53.govready.com/control?id=AC-8>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

A warning banner ensures that all persons attempting to gain access to the system know that the system and its information are “Authorized User Only” and that attempts to illegally log on to the system could lead to criminal prosecution. The warning message displayed notifies unauthorized users that they have accessed a U.S. Government computer system and continued, unauthorized use can be punishable by fines or imprisonment. Each device logged into will display a system use notification message before the log in window is displayed. The system use notification banner will remain on the screen until the user takes an explicit action to log on to the device. The following is the notification banner displayed on all Department instances:

"You are accessing a U.S. Federal Government computer system intended to be solely accessed by individual users expressly authorized to access the system by the U.S. Department of Education. Usage may be monitored, recorded, and/or subject to audit. For security purposes and in order to ensure that the system remains available to all expressly authorized users, the U.S. Department of Education monitors the system to identify unauthorized users. Anyone using this system expressly consents to such monitoring and recording. Unauthorized use of this information system is prohibited and subject to criminal and civil penalties. Except as expressly authorized by the U.S. Department of Education, unauthorized attempts to access, obtain, upload, modify, change, and/or delete information on this system are strictly prohibited and are subject to criminal prosecution under 18 U.S.C § 1030, and other applicable statutes, which may result in fines and imprisonment. For purposes of this system, unauthorized access includes, but is not limited to:

* Any access by an employee or agent of a commercial entity, or other third party, who is not the individual user, for purposes of commercial advantage or private financial gain (regardless of whether the commercial entity or third party is providing a service to an authorized user of the system); and

* Any access in furtherance of any criminal or tortious act in violation of the Constitution or laws of the United States or any State.

If system monitoring reveals information indicating possible criminal activity, such evidence may be provided to law enforcement personnel."



## AC-14 PERMITTED ACTIONS WITHOUT IDENTIFICATION OR AUTHENTICATION

> Control description: <http://800-53.govready.com/control?id=AC-14>
> 
> 
> 
> Security control type: System Specific Control


#### LINCS specific control or LINCS Responsibility

The Department of Education allows the general public user to read the web pages, do searches on the resource database and to review online forum information without identification and authentication for the public web site. Program and Privilege users cannot access LINCS Technology Project system without identification or authentication.



## AC-17 REMOTE ACCESS

> Control description: <http://800-53.govready.com/control?id=AC-17>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### Drupal specific control support

The CivicActions Access Control (AC) policy defines policy for remote usage restrictions.  The Project Manager or Project Owner may additionally provision users according to their Access Control policies.



#### LINCS specific control or LINCS Responsibility

The LINCS Technology Project permits remote access for privileged functions to support operational needs. The technical staff documents, monitors, and controls all methods of remote access to the information system including remote access for privileged functions. Privileged user access is only permitted through the use of Secure Shell (SSH) or the Remote Desktop Protocol (RDP) where the user will authenticate to the device through this secure channel. Virtual Private Networking (VPN) is not enabled in any form within the LINCS accreditation boundary.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: remote access.



## AC-18 WIRELESS ACCESS

> Control description: <http://800-53.govready.com/control?id=AC-18>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: wireless access.



## AC-19 ACCESS CONTROL FOR MOBILE DEVICES

> Control description: <http://800-53.govready.com/control?id=AC-19>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### LINCS specific control or LINCS Responsibility

This control is not applicable. LINCS does not maintain a facility in which mobile device access limitations are required.



#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: mobile device restrictions.



## AC-20 USE OF EXTERNAL INFORMATION SYSTEMS

> Control description: <http://800-53.govready.com/control?id=AC-20>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### LINCS specific control or LINCS Responsibility

This control is not applicable. LINCS does not connect with external information systems.



#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: use of external information systems.



## AC-22 PUBLICLY ACCESSIBLE CONTENT

> Control description: <http://800-53.govready.com/control?id=AC-22>
> 
> 
> 
> Security control type: System Specific Control


### Part a)

#### LINCS specific control or LINCS Responsibility

The Department of Education grants certain LINCS support staff members the authority to post publicly accessible content. These individuals must complete LINCS system security training before being granted access to the LINCS and before they can post publicly accessible content within the LINCS. Furthermore, each authorized individual must follow the procedures delineated within the “Using Drupal” Instruction to ensure they are following a verifiable procedure throughout the entire process. This covers the LINCS Discussion Lists administration areas, Wiki.lincs.ed.gov, LINCS Quarterly Reporting and training tools, and Drupal Content Management systems. Public content is only edited via the Drupal Content Management System. All other content is only viewable by LINCS system users and protected by hardened access controls.



### Part b)

#### LINCS specific control or LINCS Responsibility

It is the LINCS responsibility to train authorized LINCS individuals ensuring publicly accessible information does not contain nonpublic information.



### Part c)

#### LINCS specific control or LINCS Responsibility

It is the LINCS responsibility for LINCS authorized individuals to review the proposed content of information prior to posting onto the publicly accessible information system to ensure that nonpublic information is not included.

LINCS users with the Content Creator role have been authorized by LINCS personnel for creation of publicly accessible content with publishing authority from an Administrator or Site Manager role. The publishing authority ensures the information being published does not contain nonpublic information.  LINCS publishes automated and system-related content where the administrator has the approving authority.



### Part d)

#### LINCS specific control or LINCS Responsibility

It is the LINCS responsibility for LINCS to review the content on the publicly accessible information system for nonpublic information at least every 365 days and removes such information.



