# Access Control (AC) Standard (SOP)

*Reviewed and updated 2023-12-20*

----

**Table of Contents**
<!--TOC-->

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Standards](#standards)
  - [AC-01 Access Control Policy And Procedures](#ac-01-access-control-policy-and-procedures)
  - [AC-02 Account Management](#ac-02-account-management)
  - [AC-03 Access Enforcement](#ac-03-access-enforcement)
  - [AC-03(9) Controlled Release](#ac-039-controlled-release)
  - [AC-06 Least Privilege](#ac-06-least-privilege)
  - [AC-07 Unsuccessful Login Attempts](#ac-07-unsuccessful-login-attempts)
  - [AC-08 System Use Notification](#ac-08-system-use-notification)
  - [AC-14 Permitted Actions Without Identification Or Authentication](#ac-14-permitted-actions-without-identification-or-authentication)
  - [AC-17 Remote Access](#ac-17-remote-access)
  - [AC-18 Wireless Access](#ac-18-wireless-access)
  - [AC-19 Access Control For Mobile Devices](#ac-19-access-control-for-mobile-devices)
  - [AC-20 Use Of External Information Systems](#ac-20-use-of-external-information-systems)
  - [AC-22 Publicly Accessible Content](#ac-22-publicly-accessible-content)

<!--TOC-->

----

## Introduction

### Purpose

The Office of the Chief Information Officer (OCIO) Information Assurance Services (IAS) publication Information  Technology (IT) System Access Controls Standard of February 11, 2022 provides a comprehensive basis for  management across all systems in the Department. This document provides specific guidance as defined and implemented  by the Project.

### Scope

This system has been categorized as a FIPS-199 LOW system, and as such this document applies only to relevant  controls, policies, processes and procedures as defined within the system.

## Standards

### AC-01 Access Control Policy And Procedures

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

Access control policy and procedures are documented in the Project Full Name SSP. Access to Project operational information or system resources is limited to only authorized users, programs or processes. The Department enforces access control policies to protect the integrity of the Project Full Name. This Department reviews and updates this policy as necessary and it has been being updated, as necessary, since April 2008.


CivicActions has developed, documented and disseminated to personnel an access control policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Access Control (AC) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


### AC-02 Account Management

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS account management.


**a.**	SSH system accounts are provided to contractors on an as-needed basis.

Access privileges are used to ensure that only authorized personnel access certain areas of the Project system. User access is controlled by the completion and submission of Project system Rules of Behavior and New User Account Request forms by the user and management. These items are completed and submitted whenever a new user requires access or an existing user requires access changes. The system administrator, based on need-to-know, assigns the proper permissions. The employee’s manager approves the access rights before the initial account is created. Finally, the system administrator implements the access rights according to the New User Account Request form. The security staff and the support contractor review accounts periodically. Accounts no longer in use are removed from the system by the system administrator.

The Project has implemented user account procedures to disable inactive user accounts after 90-days of inactivity. The Project support staff monitors all user accounts to ensure this procedure is enforced. Section 6.3, Authentication Management, of the Project SSP illustrates the exact procedures the contractor support staff follows to ensure accounts are properly managed.
The Project system does not have guest or anonymous accounts.


Operations, in collaboration with the Security Office, will set up privileged accounts accounts for the following roles:
- Developer - user level account that has access to application features and sanitized databases
- System Administrator - user accounts that enjoy full system administrator (`sudo`) access


Ilias provides user accounts for individuals who participate in visiting, contributing to and administering the site with the following roles:
- Anonymous user – Readers of the site who either do not have an account or are not logged in.
- Guest – This role has limited visibility and read permissions
- User - Standard role for registered users. This role grants read access to most objects.
- Administrator - This role has all permissions enabled by default.


Drupal provides the following information system account types to support organizational mission/business functions:

- Anonymous user - readers of the site who either do not have an account or are not
  logged in.

- Authenticated user - All non-anonymous users inherit the "authenticated user role"
  that supports personal account management capabilities.

- Administrator - This role has all permissions enabled by default.


In this architecture, the baseline AWS Identity and Access Management (IAM) groups and roles are associated with access policies to align user accounts with personnel functions related to infrastructure/platform management (e.g. Billing, Amazon EC2/VPC/Amazon RDS systems administration, I.T. auditing, etc.)

**b.**	The system Owner has oversight over all permissions that the Project Manager and Operations Staff manages.


Drupal defines a default set of roles; Anonymous, Authenticated, and Administrator, as well as providing for the creation of additional organizational-defined roles identified by Project Full Name


The CivicActions Project Manager assigns the "administrator" role for the management of all accounts issued to internal admin roles supporting the information system.  Account requests are initiated by the Project Manager by completing a ticket request and the CivicActions Operation staff manages the account creation process.

**c.**	In accordance with Project Access Control Policy, Project group membership is determined according to the individual's position and role within the organization. A ticket request is used to request accounts and group membership. The request is authorized by the appropriate manager.

**d.**	Project user privileges vary depending on the type of user role assigned. Only users with the role of Administrator have the ability to create and modify user roles for other users.


Ilias' permissions and role-based access controls are built-in. Each role within Ilias can only access the pages and controls for which their privilege allows.

Drupal has a sophisticated permissions and role-based access control built-in. Each role within Drupal can only access the documents and controls for which their privilege allows.

All accounts issued for application administrators and SSH are documented in CivicActions' ticketing system. Account request tickets contain details that explain the attributes for the account including authorized users of Drupal, system infrastructure, group and role membership, and access authorizations.

**e.**	The System Owner approves, and CivicActions Operations set up the initial Administrator account for Project. Subsequent client access and related approvals are managed by CivicActions Operations in collaboration with the System Owner.


All accounts issued for the admin management of Application or SSH access must be approved by the System Owner or Project Manager who must create an account request. The CivicActions Operations staff applies appropriate account permissions and settings based on the job role and function documented within the request ticket using processes defined by the CivicActions' Security Office.
**f.**	CivicActions Operations staff is responsible for the following account management activities for both internal administrative users and customer accounts:

- Establishing account justification
- Activating accounts
- Modifying accounts
- Expiring accounts
- Disabling accounts
- Removing accounts

**g.**	Ilias monitors the usage of information accounts in a log on the server.

Drupal monitors the usage of information accounts in the Watchdog log.

In this architecture, AWS CloudTrail and Amazon S3 Bucket logging are enabled, which provide the audit trail capability for the organization to monitor the use of AWS Identity and Access Management (IAM) accounts. An Amazon S3 bucket centrally contains the CloudTrail audit logs. Amazon CloudWatch Alarm is configured to send an alert when any of the following happen:
  - an API call is made to create, update, or delete a Network ACL/Security Group
  - AWS account *root user* activity is detected
  - multiple API actions or login attempts fail
  - IAM Configuration changes are detected
  - new IAM access key was created
  - changes to the CloudTrail log configuration are detected


All CivicActions systems log the usage of information accounts.
**h.**	In accordance with the CivicActions Access Control (AC-01) Policy when an account is no longer required, the Project Manager notifies the Operations Team to immediately disable all access. Users upon reassignment, change in roles, termination, or leaving employment are initially removed from all roles and groups, effectively denying them all access to privileged accounts.

**i.**	Project governs their own administrative access. Users with
the Administrator roles are empowered to designate and approve
Administrators.


System accounts require access authorizations prior to accounts being created. The Project Manager must initiate an access request for an account to be created. CivicActions Operations staff reviews the request to ensure accuracy, including intended system usage and other attributes of the user access being requested.

**j.**	Administrators are empowered to and responsible for reviewing their own accounts and determining whether the accounts should still be authorized.


All privileged accounts are reviewed by CivicActions Operations staff every 180 days.

**k.**	In accordance with standard security best practices and CivicActions policy, shared and reissued accounts for internal accounts of any kind are not created nor used for any purpose in any system.

### AC-03 Access Enforcement

The Project Full Name ensures that assigned authorizations for controlling access to the system is enforced in accordance with the user definitions noted in Section 1.1.1 of the Project SSP. The technical support staff ensures that access to security functions and protected information is restricted to authorized personnel. Access will be controlled with access control list used on each instance. Members of one group cannot access resources defined for other groups unless explicitly permitted.


Access control in Ilias is enforced by authentication via Shibboleth single sing on (SSO) for every type of user except Anonymous user. The user’s privileges, permissions, and access are provided on the principle of least privilege.
The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves. Project Administrators, HR Managers, and Org Managers are the only roles that can create new user accounts.


Access control in Drupal is enforced by authentication via a unique username/password for every type of user except Anonymous user. The user’s privileges, permissions, and access are provided on the principle of least privilege.
The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves. Drupal Administrators are the only user roles that can create new user accounts.


In this architecture, AWS Identify and Access Management (IAM) and Amazon Amazon S3 enforce access to the AWS infrastructure and data in Amazon S3 buckets. The baseline IAM groups and roles are associated with access policies to align user accounts with personnel functions related to infrastructure/platform management (e.g. Billing, Amazon EC2/VPC/Amazon RDS systems administration, I.T. auditing, etc.) Login/API access is restricted to those users for whom the organization has authorized and created, or federated, IAM user accounts, and assigned the appropriate IAM group and/or role memberships. Amazon S3 buckets have specific access control policies assigned to restrict access to those IAM users who are assigned the appropriate IAM roles/groups.


### AC-03(9) Controlled Release

The Project information system does not release information outside of the established system boundary.


### AC-06 Least Privilege

SSH access is provided on a least privilege basis and analyzed on an ongoing basis, at least quarterly. Findings related to these audits of accounts are reported and reviewed by the Security Office and evaluated to determine roles that need to be revoked.

### AC-07 Unsuccessful Login Attempts

The Project system locks out users after three unsuccessful login attempts. The information system automatically locks the account permanently, unless an administrator unlocks the account before then, when the maximum number of unsuccessful attempts (3) is exceeded.


**a.**	Drupal can be configured to lock an account after a specified number of invalid login attempts within a specified time period. The default for Drupal is 5 failed login attempts within six hours.
**b.**	Lockdown following unsuccessful attempts is configurable by Drupal administrators to conform to defined requirements. When a user exceeds the limit of invalid login attempts, their account is automatically locked for a specified time and requires administrator action to unlock the account before the lockout period expires.
### AC-08 System Use Notification

A warning banner ensures that all persons attempting to gain access to the system know that the system and its information are “Authorized User Only” and that attempts to illegally log on to the system could lead to criminal prosecution. The warning message displayed notifies unauthorized users that they have accessed a U.S. Government computer system and continued, unauthorized use can be punishable by fines or imprisonment. Each device logged into will display a system use notification message before the log in window is displayed. The system use notification banner will remain on the screen until the user takes an explicit action to log on to the device. The following is the notification banner displayed on all system instances:

"You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions:

- The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.
- At any time, the USG may inspect and seize data stored on this IS.
- Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose.
- This IS includes security measures (e.g., authentication and access controls) to protect USG interests -- not for your personal benefit or privacy.
- Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."


System Use Notification is inherited from the Project.

### AC-14 Permitted Actions Without Identification Or Authentication

The Project Full Name allows the general public user to read the web pages, do searches on the resource database and to review online forum information without identification and authentication for the public web site. Program and Privilege users cannot access the Project system without identification or authentication.


The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves.

**a.**	The anonymous user role has the least access to the site of all roles. Drupal sites can be configured to allow actions identified by Project Full Name

### AC-17 Remote Access

The Project Full Name permits remote access for privileged functions to support operational needs. The technical staff documents, monitors, and controls all methods of remote access to the information system including remote access for privileged functions. Privileged user access is only permitted through the use of Secure Shell (SSH) where the user will authenticate to the device through this secure channel. Virtual Private Networking (VPN) is not enabled in any form within the Project accreditation boundary.


The CivicActions Access Control (AC) policy defines policy for remote usage restrictions. The Project Manager or System Owner may additionally provision users according to their Access Control policies.


### AC-18 Wireless Access

This control is not applicable. The system does not provide wireless access points.


### AC-19 Access Control For Mobile Devices

This control is not applicable. The system does not maintain a facility in which mobile device access limitations are required.


### AC-20 Use Of External Information Systems

This control is not applicable. The system does not connect with external information systems.


### AC-22 Publicly Accessible Content

**a.**	The Client Full Name grants certain Project support staff members the authority to post publicly accessible content. These individuals must complete Project system security training before being granted access to the Project and before they can post publicly accessible content within the Project Full Name. Furthermore, each authorized individual must follow the procedures delineated within the “Using Drupal” Instruction to ensure they are following a verifiable procedure throughout the entire process. This covers the Project Discussion Lists administration areas, Project Quarterly Reporting and training tools, and Drupal Content Management systems. Public content is only edited via the Drupal Content Management System. All other content is only viewable by Project system users and protected by hardened access controls.

**b.**	It is the Project responsibility to train authorized Project individuals ensuring publicly accessible information does not contain nonpublic information.

**c.**	Authorized Project individuals review the proposed content of information prior to posting onto the publicly accessible information system to ensure that nonpublic information is not included.

Project Users have been authorized for creation of publicly accessible content with publishing authority from an Administrator role. The publishing authority ensures the information being published does not contain nonpublic information.

**d.**	Authorized Project individuals review the content on the publicly accessible information system for nonpublic information at least every 365 days and removes such information.
