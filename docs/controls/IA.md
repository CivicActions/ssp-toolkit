# LINCS System Security Plan

# NIST SP 800-53 Revision 4

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

##### CivicActions

CivicActions system administrators employ a personal public-key pair for basic access and must originate from a whitelisted IP address. To access root (sudo) privileges an additional password is required.


##### Drupal

Drupal administrators and other roles with unrestricted access to user data are
required to use two factor authentication.


##### LINCS

The LINCS Technology Project employs multi-factor authentication for privileged
users.


### IA-2 (12): Acceptance Of Piv Credentials

> The information system accepts and electronically verifies Personal Identity Verification (PIV) credentials.

##### LINCS

The LINCS Technology Project system does not implement logical access control
systems (LACS) or physical access control systems (PACS). Therefore Personal
Identity Verification (PIV) credentials have not been issued for users.


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



