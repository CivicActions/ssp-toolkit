# IDENTIFICATION AND AUTHENTICATION

## IA-01 IDENTIFICATION AND AUTHENTICATION POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=IA-1>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel an identification and authentication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained the CivicActions Identification and Authentication (IA) Policy. This document can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.



#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel an identification and authentication policy that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls.The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating Identification and Authentication Policy and Procedures annually. The Chief Operating Officer is responsible for approving Identification and Authentication. All procedures are consistent with requirements of FISMA, FedRAMP, ISO 27001, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## IA-02 IDENTIFICATION AND AUTHENTICATION (ORGANIZATIONAL USERS)

> Control description: <http://800-53.govready.com/control?id=IA-2>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

CivicActions users of the system are required to identify and authenticate in order to access any functions of the information system beyond viewing and downloading the publicly available website content that is available to all anonymous website visitors. Users who are assigned to CivicActions require the appropriate authorization described in AC-2. CivicActions users authenticate using the standard Drupal login protocol prior to using the LINCS services. LINCS user roles are described in AC-3.

To access the website as an authenticated user, front-end users of the application must first request and be given a login account with a unique username, password and email address. Login accounts can only be created by existing website users with the role of either Administrator or Site Manager. Users with those roles also assign roles to each login account that govern the user's ability to create, publish, update or delete website content such as blog entries, datasets and data resource files.



#### LINCS specific control or LINCS Responsibility

LINCS Access: Site Managers and End Users

* Site Manager access to web-accessible components of lincs.ed.gov is limited. Full access to web-accessible components is only available to CivicActions administrators.

* End Users, typically members of the public, have read-only access to view and download data resources published on lincs.ed.gov and do not need or receive user accounts. End users are also allowed to submit website feedback, but all submitted feedback is moderated by an LINCS Site Manager before it is published.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  Identification and Authentication procedures for CivicActions personnel who have rights to AWS platform.



## IA-02 (1) NETWORK ACCESS TO PRIVILEGED ACCOUNTS

> Control description: <http://800-53.govready.com/control?id=IA-2>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

Multifactor Authentication is a planned control for organization users of LINCS with privileged accounts.



## IA-02 (2) NETWORK ACCESS TO NON-PRIVILEGED ACCOUNTS

> Control description: <http://800-53.govready.com/control?id=IA-2>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

All accounts within LINCS’s PaaS provider (AWS ACE) and IaaS provider (AWS) are privileged accounts as described in FedRAMP Provisional ATO granted to the AWS Cloud dated 17 March 2016.



## IA-03 DEVICE IDENTIFICATION AND AUTHENTICATION

> Control description: <http://800-53.govready.com/control?id=IA-3>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions systems do not support or allow device-to-device communications.



## IA-04 IDENTIFIER MANAGEMENT

> Control description: <http://800-53.govready.com/control?id=IA-4>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Drupal specific control support

Upon account creation, the Drupal software assigns each user account a unique numerical user ID (uid). This uid is used internally by the system to track user actions such as content creation or editing. The numerical user IDs are never reused even if their user accounts are subsequently blocked or deleted.



#### LINCS specific control or LINCS Responsibility

LINCS/DKANusers are assigned a unique identifier in the form of a unique username, password and email address for the LINCS system based on the system for allocating user accounts described in AC-2. Each request must be based on a business need and is limited to only the access requirements for that individual to perform his/her identified role within LINCS. Requests for identifier assignment follows the process described in AC-2 and are authorized to perform actions according to the user account roles described in AC-3.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS identifier authorization to assign information system CivicActions identifiers.



### Part b)

#### Drupal specific control support

In accordance with CivicActions Identification and Authentication (IA) Policy <https://github.com/CivicActions/compliance-docs/blob/master/IA-Policy.md>, CivicActions internal users are uniquely identified by creation of an organizational account with a username based on each user's full first and last name.

When Drupal user accounts are created, users' email addresses are verified by sending a single-use activation link to the user’s mailbox. The email recipient then uses the activation link to log in to the website and supply a password which must meet the system's password complexity requirements.



#### LINCS specific control or LINCS Responsibility

Users assigned to system requiring access to the lincs.ed.gov system require authorization by the employee’s manager with LINCS’s admin group completing the the creation of the account.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  selection of individual accounts identifiers for CivicActions admins within the AWS platform.



### Part c)

#### Drupal specific control support

Identifiers for CivicActions internal personnel include a username based on the individual's full first and last name and are reviewed for uniqueness by the LINCS admin group when it approves creation of the user account.



#### LINCS specific control or LINCS Responsibility

Once the initial Site Manager accounts are created for LINCS, they subsequently are responsible for assigning accounts and privileges to other customer users in their organization.

Identifiers for devices that access the system use the same username, email address and password protocol as the identifiers provided to human users of the system and undergo the same process of review by the LINCS admin group. The LINCS admin group is responsible for assigning a unique username that identifies the device as well as an email address that can be used for account verification.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  assignment of identifiers for CivicActions admins within the AWS platform.



### Part d)

#### CivicActions Responsibility

CivicActions internal users' usernames may not be re-used for at least two years.



#### Drupal specific control support

Drupal users unique identifier (the numeric user id, or uid) is never reused.



### Part e)

#### LINCS specific control or LINCS Responsibility

All user accounts are required to change their passwords every 90 days. The website will automatically block the accounts of users who fail to change their password within that time period, after which the account may only be unblocked by a website Administrator or Site Manager.



## IA-05 AUTHENTICATOR MANAGEMENT

> Control description: <http://800-53.govready.com/control?id=IA-5>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Drupal specific control support

Refer to control AC-2 in this SSP for further details on account provisioning.

CivicActions will create and maintain an initial Drupal Administrator (highest level of Drupal Account). New Administrators are able to provide additional Administrator access at their own discretion, and are ultimately responsible for managing their own Administrator and other user accounts that they create.



#### LINCS specific control or LINCS Responsibility

Authentication for LINCS internal personnel are created during the personnel assignment process where requests are made to the LINCS admin group for proper access levels.  The LINCS admin group verifies the identity of the user. The website performs further verification by sending an email to the user's mailbox containing a single-use activation link which must be used to log in to the account for the first time and to create a password.

Prior to issuing initial Drupal Site Manager (highest level of Client User Account) system credentials (user ID and initial password),  the CivicActions Implementation staff verifies the user’s request for access, typically during the initial kick-off call when all stakeholders are present. New Site Managers are able to provide additional Site Manager access at their own discretion, and are ultimately responsible for managing their own Site Manager and other user accounts that they create.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: identity verification of the CivicActions admins.



### Part b)

#### Drupal specific control support

Internal initial password requirements set by CivicActions admins and ongoing password refreshes by internal user follow the requirements set in the Identification and Authentication Policy.



#### LINCS specific control or LINCS Responsibility

Initial authenticator content (a unique email address – not previously used in any other account) is provided by the customer. CivicActions Implementation staff use that email address to provide the new user with Admin access. Before the Admin has access, they are required to create their own passwords; however, the passwords Admins choose must conform to the password criteria defined:

* Enforce password history = 24

* Minimum password length = 15



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  internal authentication for CivicActions admins.

Customer Requirement

LINCS customers are responsible for provisioning and de-provisioning end user accounts in compliance with the authentication requirements described above (i.e., password strengths).



### Part c)

#### Drupal specific control support

The system partially inherits this control from Drupal standard password strength mechanisms.



#### LINCS specific control or LINCS Responsibility

When entering a user account password upon initial login to lincs.ed.gov, all users must comply with the following strict password policies, which are enforced by the website's software configuration:

* Password must contain at least one punctuation (not whitespace or an alphanumeric) character.

* Password must contain at least one uppercase character.

* Password must contain at least one lowercase character.

* Password must be at least 15 characters in length.

* Password must contain at least one digit.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  sufficient strength of authentication.



### Part d)

#### Drupal specific control support

The system partially inherits this control from Drupal standard password management.

All password changes/resets are recorded in the website's "Drupal watchdog" logs.



#### LINCS specific control or LINCS Responsibility

LINCS Site Managers have the ability to add additional Site Managers to their account. The Site Manager needs only a unique email address to do so. All password requirements are set at the account level, and will apply to all user accounts. Password requirements are not editable for Site Managers.

Disabling the access of Site Managers to lincs.ed.gov is the responsibility of LINCS.

LINCS is responsible for provisioning and de-provisioning end user accounts, which must comply with the strict password policies that are enforced by the website's software configuration, as described above

In accordance with lincs.ed.gov site configuration, the following implementation administrative procedures exist for initial authenticator distribution, for lost/compromised/damaged authenticators, and for revoking authenticators.

* Initial authenticator distribution:  Users receive a one-time login link by email upon creating of their user account. They use that link to log in and then must enter a password themselves which complies with the password complexity requirements described in IA-4(b).

* Lost/compromised/damaged authenticators:  Users who have forgotten their password may request a new password by submitting their username or email address. The website responds by emailing a one-time login link to the user's email address. After using the link to log in, the user is required to enter a new password.

* Revoking authenticators: Users who have not changed their password in the last 90 days are automatically blocked. Administrators and Site Managers may block any user account if they believe there is a reason to do so.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  administrative procedures for initial authenticator distribution, for lost/compromised or damaged authenticators, and for revoking authenticators for CivicActions admin users of AWS.



### Part e)

#### Drupal specific control support

CivicActions/Drupal requires users to change their password upon initial login, and the application website enforces this. User accounts are assigned a randomly-generated and unguessable default password that is not shared with anyone, including site Administrators. Once the user logs in and creates a new password, the default password erased from the website's database.



#### LINCS specific control or LINCS Responsibility

CivicActions application password re-use requirements are configurable in accordance with LINCS own security requirements. However, changing the password age requirement requires a code setting change that therefore needs to be planned and approved by CivicActions' Change Control Board before being implemented.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  changing default content of authenticators prior to information system installation for CivicActions admin users of AWS.



### Part f)

#### LINCS specific control or LINCS Responsibility

LINCS DKAN users follow the following requirements:

* Maximum password age = 90

* Minimum password age = 1



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  establishing minimum and maximum lifetime restrictions and reuse conditions for authenticators.



### Part g)

#### LINCS specific control or LINCS Responsibility

CivicActions internal users for LINCS uses Group Policy to enforce password lifetime restrictions.  The password lifetime settings for internal accounts is as follows:

* Minimum restriction of zero (0) days and

* Maximum restriction of ninety (90) days before a password change is required.

The LINCS application has no interaction with Active Directory; all password requirements are managed within the application itself.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: changing/refreshing authenticator requirements.



### Part h)

#### Drupal specific control support

For all Drupal users, passwords are protected by the website's software, which only stores an encrypted string based on the password. This means that even if the website's database should be compromised, an attacker would still be unable to know users' actual passwords. Internal users receive training in security awareness and acceptable use and are instructed never to reveal their passwords to anyone.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  protecting authenticator content from unauthorized disclosure and modification.



### Part i)

#### Drupal specific control support

CivicActions internal users are required to take appropriate measures in the handling of passwords including:

* Not transmitting user names and passwords together in an unencrypted format

* Not permitting the sending of passwords in an unencrypted format via email

* Not listing passwords in tickets

* Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.



#### LINCS specific control or LINCS Responsibility

LINCS internal users are required to take appropriate measures in the handling of passwords including:

* Not transmitting user names and passwords together in an unencrypted format

* Not permitting the sending of passwords in an unencrypted format via email

* Not listing passwords in tickets

* Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  security safeguards to protect authenticators under CivicActions admin possession.



### Part j)

#### Drupal specific control support

This control is not applicable due to the fact that group accounts are not created within the Drupal application per IA Policy.



## IA-05 (1) PASSWORD-BASED AUTHENTICATION

> Control description: <http://800-53.govready.com/control?id=IA-5>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Drupal specific control support

Drupal supports the requirement for password based authentication complexity. New users of Drupal are required to specify their password authentication as soon as they log in to the website for the first.  The website requires all submitted passwords to comply with validation rules, as described above in IA-5(c).



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: password complexity requirements for CivicActions admin users of the platform.

Customer Requirement

LINCS customers are responsible for provisioning and de-provisioning end user accounts, which must comply with the strict password policies that are enforced by the website's software configuration, as described above.



### Part b)

#### Drupal specific control support

When required to change passwords, Drupal users are required to change their authenticator password by changing at least one character. Enforcement of this control is implemented through the website's software configuration.



#### LINCS specific control or LINCS Responsibility

LINCS: All password requirements are set at the application level, and will apply to all website user accounts. Password requirements are not editable by Site Managers.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: password complexity requirements for CivicActions admin users of the platform.



### Part c)

#### Drupal specific control support

All Drupal passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: enforcement for minimum and maximum lifetime restrictions.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: storing and transmitting only cryptographically-protected passwords.



### Part d)

#### Drupal specific control support

The website requires all submitted passwords to comply with lifetime rules, as described above in IA-5(g).



#### LINCS specific control or LINCS Responsibility

LINCS: Password age requirements are configurable at the application level. The minimum age is set to 1 day, and the maximum age can be set to whatever LINCS requires to meet its own security requirements. However, changing the password age requirement requires a code setting change that therefore needs to be planned and approved by CivicActions' Change Control Board before being implemented.



### Part e)

#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: prohibiting password reuse.



### Part f)

#### Drupal specific control support

When website users request a password reset, the website sends a temporary login link to the email address associated with their user account. After a user logs in via the temporary login link, the website requires the user to enter a new password before proceeding further.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: use of temporary password for system logons.



## IA-05 (11) HARDWARE TOKEN-BASED AUTHENTICATION

> Control description: <http://800-53.govready.com/control?id=IA-5>
> 
> 
> 
> Security control type: System Specific Control


#### LINCS specific control or LINCS Responsibility

LINCS DKAN does not support physical hardware token-based authentication. Therefore this control is Not Applicable.



## IA-05(1) PASSWORD-BASED AUTHENTICATION

> Control description: <http://800-53.govready.com/control?id=IA-5>
> 
> 
> 
> Security control type: Hybrid


### Part e)

#### LINCS specific control or LINCS Responsibility

This will be completed in CY2018.

This control is planned but not yet fully implemented. The system does enforces password minimum and maximum lifetime, and prohibits reuse of the 6 previous passwords, but does not prohibit reuse of the 24 previous passwords. Enforcement of the 24 previous password restriction will be implemented by the end of 2016.



## IA-06 AUTHENTICATOR FEEDBACK

> Control description: <http://800-53.govready.com/control?id=IA-6>
> 
> 
> 
> Security control type: System Specific Control


#### Drupal specific control support

Feedback of authentication information is obscured during the authentication process into the Drupal application by displaying “dots” in the place of a password, as is standard for web-based applications. In transmission, passwords are encrypted using SSL via HTTPS.



## IA-07 CRYPTOGRAPHIC MODULE AUTHENTICATION

> Control description: <http://800-53.govready.com/control?id=IA-7>
> 
> 
> 
> Security control type: System Specific Control


#### Drupal specific control support

All Drupal passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. SHA-512 is an approved security function under FIPS PUB 140-2. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.



## IA-08 IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS)

> Control description: <http://800-53.govready.com/control?id=IA-8>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

LINCS is a publically accessible solution that allows government organizations to share open data resources with the general public. Non-organizational users have read-only access to the open data resources which are shared on lincs.ed.gov as documented in control AC-14.



## IA-08 (1) ACCEPTANCE OF PIV CREDENTIALS FROM OTHER AGENCIES

> Control description: <http://800-53.govready.com/control?id=IA-8>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

CivicActions does not utilize customer agency supplied PIV credentials for access to customer instances of Drupal.



## IA-08 (2) ACCEPTANCE OF THIRD-PARTY CREDENTIALS

> Control description: <http://800-53.govready.com/control?id=IA-8>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

CivicActions does not utilize customer agency supplied PIV credentials for access to customer instances of Drupal.



## IA-08 (3) USE OF FICAM-APPROVED PRODUCTS

> Control description: <http://800-53.govready.com/control?id=IA-8>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

CivicActions does not utilize customer agency supplied PIV credentials for access to customer instances of Drupal.



## IA-08 (4) USE OF FICAM-ISSUED PROFILES

> Control description: <http://800-53.govready.com/control?id=IA-8>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

CivicActions does not utilize customer agency supplied PIV credentials for access to customer instances of Drupal.



