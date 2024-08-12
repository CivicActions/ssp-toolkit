# Identification And Authentication (IA) Standard (SOP)

*Reviewed and updated 2023-12-20*

----

**Table of Contents**
<!--TOC-->

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Standards](#standards)
  - [IA-01 Identification And Authentication Policy And Procedures](#ia-01-identification-and-authentication-policy-and-procedures)
  - [IA-02 Identification And Authentication (Organizational Users)](#ia-02-identification-and-authentication-organizational-users)
  - [IA-02(1) Network Access To Privileged Accounts](#ia-021-network-access-to-privileged-accounts)
  - [IA-02(12) Acceptance Of Piv Credentials](#ia-0212-acceptance-of-piv-credentials)
  - [IA-04 Identifier Management](#ia-04-identifier-management)
  - [IA-05 Authenticator Management](#ia-05-authenticator-management)
  - [IA-05(1) Password-Based Authentication](#ia-051-password-based-authentication)
  - [IA-05(11) Hardware Token-Based Authentication](#ia-0511-hardware-token-based-authentication)
  - [IA-06 Authenticator Feedback](#ia-06-authenticator-feedback)
  - [IA-07 Cryptographic Module Authentication](#ia-07-cryptographic-module-authentication)
  - [IA-08 Identification And Authentication (Non-Organizational Users)](#ia-08-identification-and-authentication-non-organizational-users)
  - [IA-08(1) Acceptance Of Piv Credentials From Other Agencies](#ia-081-acceptance-of-piv-credentials-from-other-agencies)
  - [IA-08(2) Acceptance Of Third-Party Credentials](#ia-082-acceptance-of-third-party-credentials)
  - [IA-08(3) Use Of Ficam-Approved Products](#ia-083-use-of-ficam-approved-products)
  - [IA-08(4) Use Of Ficam-Issued Profiles](#ia-084-use-of-ficam-issued-profiles)

<!--TOC-->

----

## Introduction

### Purpose

The Office of the Chief Information Officer (OCIO) Information Assurance Services (IAS) publication Information  Technology (IT) System Access Controls Standard of February 11, 2022 provides a comprehensive basis for  management across all systems in the Department. This document provides specific guidance as defined and implemented  by the Project.

### Scope

This system has been categorized as a FIPS-199 LOW system, and as such this document applies only to relevant  controls, policies, processes and procedures as defined within the system.

## Standards

### IA-01 Identification And Authentication Policy And Procedures

The Project system owners/managers manage user identifiers by: (i) uniquely identifying each user; (ii) verifying the identity of each user; (iii) receiving authorization to issue a user identifier from an appropriate official; (iv) ensuring that the user identifier is issued to the intended party; (v) disabling user identifier after a reasonable period of inactivity as documented in its security procedures; and (vi) archiving user identifiers. Project reviews and updates this policy as necessary.


CivicActions has developed, documented and disseminated to personnel an identification and authentication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained by the CivicActions Identification and Authentication (IA) Policy. This document can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs>.


### IA-02 Identification And Authentication (Organizational Users)

AWS built-in features of Identity and Access Management (IAM) provides the capability for uniquely identifying and authenticating users and processes acting on their behalf to both organizational and non-organizational users operating within the AWS account and infrastructure, providing privileges based on the credentials, group memberships, and access policies assigned to them. The customer organization, at its discretion, provides individual user accounts and privileges to both organizational non-organizational users in addition to organizational users.


### IA-02(1) Network Access To Privileged Accounts

The Project employs multi-factor authentication for privileged users.


Drupal administrators and other roles with unrestricted access to live content and/or user accounts are required to use two-factor authentication. See artifact None


CivicActions system administrators employ a personal public- key pair for basic access and must originate from a whitelisted IP address. The whitelist is maintained by an Ansible inventory file, the current complete list (includes dev sites) of users with whitelisted IPs is in artifact: None

To access root (sudo) privileges an additional password is required. The passwords are maintained in encrypted form in the Ansible inventory file. The mechanism to enable select users to use a password to obtain root access can be viewed in artifact: None


### IA-02(12) Acceptance Of Piv Credentials

The Project system allows users to access the system using Common Access Cards (CAC).


### IA-04 Identifier Management

**a.**	Upon account creation, the Ilias software assigns each user account a unique numerical user ID (UID). This UID is used internally by the system to track user actions such as content creation or editing. The numerical user IDs are never reused even if their user accounts are subsequently blocked or deleted.

Upon account creation, the Drupal software assigns each user account a unique numerical user ID (UID). This UID is used internally by the system to track user actions such as content creation or editing. The numerical user IDs are never reused even if their user accounts are subsequently blocked or deleted.


Access to the system is authorized by the System Owner or Project Manager for each role as described in AC-2.

**b.**	When Ilias user accounts are created, users' email addresses are verified by sending a single-use activation link to the user’s mailbox. The email recipient then uses the activation link to log in to the website and supply a password which must meet the system's password complexity requirements.

When Drupal user accounts are created, users' email addresses are verified by sending a single-use activation link to the user’s mailbox. The email recipient then uses the activation link to log in to the website and supply a password which must meet the system's password complexity requirements.


User accounts are assigned a unique identifier in the form of a unique username, password and email address based on the system for allocating user accounts described in AC-2.

In accordance with CivicActions Identification and Authentication (IA) Policy outlined at <https://github.com/CivicActions/compliance-docs>, CivicActions internal users are uniquely identified by the creation of an organizational account with a username based on each user's first and last names.

**c.**	Identifiers for CivicActions internal personnel include a username based on the individual's full first and last name and are reviewed for uniqueness by the admin group when it approves the creation of the user account.

Identifiers for CivicActions internal personnel include a username based on the individual's full first and last name and are reviewed for uniqueness by the admin group when it approves the creation of the user account.


User accounts are assigned a unique identifier in the form of a unique username, password and email address based on the system for allocating user accounts described in AC-2.

**d.**	Ilias user's unique identifier (the numeric user ID, or UID) is never reused.

Drupal user's unique identifier (the numeric user ID, or UID) is never reused.

Account usernames may not be re-used for at least two years.
**e.**	All user accounts are required to change their passwords every 90 days. The website will automatically block the accounts of users who fail to change their password within that time period, after which the account may only be unblocked by a website Administrator or CivicActions Operations staff.

### IA-05 Authenticator Management

**a.**	Authentication for Project internal personnel are created during the personnel assignment process where requests are made to the Project admin group for proper access levels. The Project admin group verifies the identity of the user. The website performs further verification by sending an email to the user's mailbox containing a single-use activation link which must be used to log in to the account for the first time and to create a password.


Refer to control AC-2 in this SSP for further details on account provisioning.
CivicActions will create and maintain an initial Ilias Administrator (highest level of Ilias Account). New Administrators are able to provide additional Administrator access at their own discretion and are ultimately responsible for managing their own Administrator and other user accounts that they create.


Refer to control AC-2 in this SSP for further details on account provisioning.
CivicActions will create and maintain an initial Drupal Administrator (highest level of Drupal Account). New Administrators are able to provide additional Administrator access at their own discretion and are ultimately responsible for managing their own Administrator and other user accounts that they create.

**b.**	Project admins in collaboration with CivicActions Operations are responsible for provisioning and de-provisioning end user accounts in compliance with the authentication requirements described herein.


Initial authenticator content (a unique email address – not previously used in any other account) is provided by the user. Internal initial password requirements set by CivicActions Operations and ongoing password refreshes by internal users follow the requirements set in the Identification and Authentication Policy.

Initial authenticator content (a unique email address – not previously used in any other account) is provided by the user. Internal initial password requirements set by CivicActions Operations and ongoing password refreshes by internal users follow the requirements set in the Identification and Authentication Policy.

**c.**	When entering a user account password upon initial login, all users must comply with the following password policies, which are enforced by the website's software configuration:

- Password must be at least 14 characters in length.
- Password must contain at least one digit.
- Password must contain at least one special character (not whitespace or an alphanumeric).
- Password must contain at least one uppercase character.
- Password must contain at least one lowercase character.


The system partially inherits this control from Ilias standard password strength mechanisms.

The system partially inherits this control from Drupal standard password strength mechanisms.
**d.**	Project is responsible for provisioning and de-provisioning end user accounts, which must comply with the strict password policies that are enforced by the website's software configuration, as described in IA-5(d).

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


The system partially inherits this control from Ilias standard password management.
All password creation/change/reset operations are recorded in the website's Ilias logs.


The system partially inherits this control from Drupal standard password management. All password creation/change/reset operations are recorded in the website's "Drupal Watchdog" logs.

**e.**	Ilias requires users to change their password upon initial login, and the application website enforces this. Each user account is assigned a default password that is randomly generated, not possible to guess, and not shared with anyone, including site administrators. When the user logs in and creates a new password, the default password is erased from the website database.

Drupal requires users to change their password upon initial login, and the application website enforces this. Each user account is assigned a default password that is randomly generated, not possible to guess, and not shared with anyone, including site administrators. When the user logs in and creates a new password, the default password is erased from the website database.

**f.**	Project authenticators follow these password lifetime restrictions:

- Maximum password age = 90
- Minimum password age = 1
- Password reuse restriction = 10

**g.**	Project enforces password lifetime restrictions. The password lifetime settings for internal accounts is as follows:

- Minimum restriction of zero (1) days and
- Maximum restriction of ninety (90) days before a password change is required.

**h.**	For all Ilias users, passwords are protected by the website's software, which only stores an encrypted string based on the password. This means that even if the website's database should be compromised, an attacker would still be unable to know users' actual passwords. Internal users receive training in security awareness and acceptable use and are instructed never to reveal their passwords to anyone.

For all Drupal users, passwords are protected by the website's software, which only stores an encrypted string based on the password. This means that even if the website's database should be compromised, an attacker would still be unable to know users' actual passwords. Internal users receive training in security awareness and acceptable use and are instructed never to reveal their passwords to anyone.

**i.**	Ilias users are required to take appropriate measures in the handling of passwords including:
- Not transmitting user names and passwords together in an unencrypted format
- Not permitting the sending of passwords in an unencrypted format via email
- Not listing passwords in tickets
- Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.


Drupal users are required to take appropriate measures in the handling of passwords including:

- Not transmitting user names and passwords together in an unencrypted format
- Not permitting the sending of passwords in an unencrypted format via email
- Not listing passwords in tickets
- Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.


CivicActions users are required to take appropriate measures in the handling of passwords including:

- Not transmitting user names and passwords together in an unencrypted format
- Not permitting the sending of passwords in an unencrypted format via email
- Not listing passwords in tickets
- Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.

**j.**	This control is not applicable due to the fact that group accounts are not created within the Ilias application per IA Policy.

This control is not applicable due to the fact that group accounts are not created within the Drupal application per IA Policy.
### IA-05(1) Password-Based Authentication

Project is responsible for provisioning and de-provisioning end user accounts, which must comply with the strict password policies that are enforced by the website's software configuration, as described in IA-5.


**a.**	Ilias supports the requirement for password-based authentication complexity. New users of Ilias are required to specify their password authentication as soon as they log in to the website for the first. The website requires all submitted passwords to comply with validation rules, as described above in IA-5(c).
Changing password lifetime, length, reuse or strength requirements requires a code setting change that therefore needs to be planned and approved by {'name': 'CivicActions, Inc', 'name_short': 'CivicActions', 'address': {'street': '3527 Mt Diablo Blvd, Unit 269', 'city': 'Lafayette', 'state': 'CA', 'zip': 94549, 'country': None}, 'phone': '510-408-7510', 'website': 'www.civicactions.com', 'compliance_docs_url': 'https://github.com/CivicActions/compliance-docs', 'email_support': 'support@civicactions.com', 'security_policy_url': 'https://github.com/CivicActions/security-policy'}' Change Control Board before being implemented.


Drupal supports the requirement for password-based authentication complexity. New users of Drupal are required to specify their password authentication as soon as they log in to the website for the first. The website requires all submitted passwords to comply with validation rules, as described above in IA-5(c).
Changing password lifetime, length, reuse or strength requirements requires a code setting change that therefore needs to be planned and approved by CivicActions Change Control Board before being implemented.


AWS built-in features of Identity and Access Management (IAM) provides minimum password complexity enforcement, but the characteristics to enforce must be manually configured by the customer. Refer to http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html

**b.**	When required to change passwords, Ilias users are required to change their authenticator password by changing at least one character. Enforcement of this control is implemented through the website's software configuration.

When required to change passwords, Drupal users are required to change their authenticator password by changing at least one character. Enforcement of this control is implemented through the website's software configuration.

**c.**	All Ilias passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.

All Drupal passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.


AWS built-in features of AWS Identity and Access Management (IAM) and the AWS Console store passwords on AWS systems in a cryptographically-protected format and only support TLS connectivity to the console web site to protect passwords in transit via encryption.

**d.**	The website requires all submitted passwords to comply with lifetime rules, as described above in IA-5(g).

The website requires all submitted passwords to comply with lifetime rules, as described above in IA-5(g).
**e.**	Password reuse is limited through software configuration.

Password reuse is limited through software configuration.
**f.**	When website users request a password reset, the website sends a temporary login link to the email address associated with their user account. After a user logs in via the temporary login link, the website requires the user to enter a new password before proceeding further.

When website users request a password reset, the website sends a temporary login link to the email address associated with their user account. After a user logs in via the temporary login link, the website requires the user to enter a new password before proceeding further.


AWS built-in features of AWS Identity and Access Management (IAM) provides the capability to require new password to be entered upon login. The customer organization, at its discretion, configures IAM to enforce that requirement.

### IA-05(11) Hardware Token-Based Authentication

Project does not support physical hardware token-based authentication. Therefore this control is Not Applicable.


AWS built-in features of AWS Identity and Access Management (IAM) provides the capability for Hardware MFA using Gemalto SafeNet IDProve 100 and 700 OTP Tokens which are compliant to OATH open standard (time based - 6 digits) Expected battery life is 3-5 years or approximately 15,000 - 20,000 clicks. These products are handheld devices that provide strong authentication by generating a unique password that is valid for only one attempt and for 30 seconds.

It is the customer organization's responsibility to implement Hardware MFA. Refer to http://aws.amazon.com/iam/details/mfa/ and http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html


### IA-06 Authenticator Feedback

Feedback of authentication information is obscured during the authentication process into the Ilias application by displaying “dots” in the place of a password, as is standard for web-based applications. In transmission, passwords are encrypted using SSL via HTTPS.

Feedback of authentication information is obscured during the authentication process into the Drupal application by displaying “dots” in the place of a password, as is standard for web-based applications. In transmission, passwords are encrypted using SSL via HTTPS.


In this architecture, All Amazon EC2 instances (bastion host, web/proxy servers, application servers) employ SSH for interactive login, and when a key passphrase is prompted for, the SSH prompting mechanism obscures the feedback by default.

AWS built-in features obscure keystroke feedback for password input during AWS console login with AWS Identity and Access Management (IAM) user credentials, and when the CloudFormation console prompts for an initial database password during Quick Start template deployment.


### IA-07 Cryptographic Module Authentication

All Ilias passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. SHA-512 is an approved security function under FIPS PUB 140-2. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.

All Drupal passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. SHA-512 is an approved security function under FIPS PUB 140-2. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.


AWS built-in features of AWS Identity and Access Management (IAM) authentication employs cryptographic modules that meet requirements as specified and assessed in the AWS FedRAMP authorization package.


**j.**	CivicActions systems employ authentication methods consistent with NIST FIPS 140-2 requirements. General public access to system web pages does not require cryptographic authentication. Privileged users accessing systems use the public-key cryptographic functionality of Secure Shell (SSH) to encrypt the exchange of information (including the password) between the remote user and the server. Where Transport Layer Security (TLS, aka SSL) is used, cryptographic modules will be configured in accordance with FIPS 140-2.

### IA-08 Identification And Authentication (Non-Organizational Users)

AWS built-in features of AWS Identity and Access Management (IAM) provide the capability for uniquely identifying and authenticating users and processes acting on their behalf to both organizational and non-organizational users, providing privileges based on the credentials, group memberships, and access policies assigned to them.

The customer organization at its discretion provides user accounts and privileges to both organizational non-organizational users in addition to organizational users.


### IA-08(1) Acceptance Of Piv Credentials From Other Agencies

Project allows the use of customer agency supplied Common Access Cards (CAC).


### IA-08(2) Acceptance Of Third-Party Credentials

Project does not utilize FICAM approved credentials.


### IA-08(3) Use Of Ficam-Approved Products

Project does not utilize FICAM approved products.


### IA-08(4) Use Of Ficam-Issued Profiles

CivicActions does not utilize FICAM approved products or profiles.
