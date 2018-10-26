# IDENTIFICATION AND AUTHENTICATION

## IA-01 IDENTIFICATION AND AUTHENTICATION POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=IA-1>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The LINCS Technology Project complies with identification and authentication policies contained within the Department of Education, Handbook for Information Assurance Security Policy (Handbook OCIO-01).

The LINCS system owners/managers manage user identifiers by: (i) uniquely identifying each user; (ii) verifying the identity of each user; (iii) receiving authorization to issue a user identifier from an appropriate official; (iv) ensuring that the user identifier is issued to the intended party; (v) disabling user identifier after a reasonable period of inactivity as documented in its security procedures; and (vi) archiving user identifiers. The Department reviews and updates this policy as necessary.



#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel an identification and authentication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained the CivicActions Identification and Authentication (IA) Policy. This document can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.



## IA-02 IDENTIFICATION AND AUTHENTICATION (ORGANIZATIONAL USERS)

> Control description: <http://800-53.govready.com/control?id=IA-2>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The LINCS Technology Project system uniquely identifies and authenticates all privileged and program users. This is accomplished through the use of unique user identification and a secret user password. All user IDs are maintained in a database by the system administrator and no identical IDs may be issued.

Password requirements are listed under security control IA-5.



#### CivicActions Responsibility

Privileged users of the system are required to identify and authenticate in order to access any functions of the information system beyond viewing and downloading the publicly available website content that is available to all anonymous website visitors. Privileged users require the appropriate authorization described in AC-2.



#### Drupal specific control support

Drupal users authenticate using the standard login protocol prior to using application services. User roles are described in AC-3.

Privileged Drupal accounts can only be created by existing website users with the role of "administrator". Administrator users assign roles to each login account that govern the user's ability to create, publish, update or delete website content.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: Identification and Authentication procedures for personnel who have rights to AWS platform.



## IA-02 (1) NETWORK ACCESS TO PRIVILEGED ACCOUNTS

> Control description: <http://800-53.govready.com/control?id=IA-2>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The LINCS Technology Project system does not process sensitive information, thus it does not employ multifactor authentication.

Access to system services - SSH for GNU/Linux instances, RDP for Windows - is managed by a set of firewall rules on the systems. The network firewall is configured to only allow users to connect to these services from a configured and audited IP addres.



## IA-02 (12) ACCEPTANCE OF PIV CREDENTIALS

> Control description: <http://800-53.govready.com/control?id=IA-2>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The LINCS Technology Project system does not implement logical access control systems (LACS) or physical access control systems (PACS). Therefore Personal Identity Verification (PIV) credentials have not been issued for users.



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


#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: identifier management.



### Part a)

#### CivicActions Responsibility

Access to the system is authorized by the Product Owner or Project Manager for each role as described in AC-2.



#### Drupal specific control support

Upon account creation, the Drupal software assigns each user account a unique numerical user ID (uid). This uid is used internally by the system to track user actions such as content creation or editing. The numerical user IDs are never reused even if their user accounts are subsequently blocked or deleted.



### Part b)

#### CivicActions Responsibility

User accounts are assigned a unique identifier in the form of a unique username, password and email address based on the system for allocating user accounts described in AC-2.

In accordance with CivicActions Identification and Authentication (IA) Policy <https://github.com/CivicActions/compliance-docs/blob/master/IA-Policy.md>, CivicActions internal users are uniquely identified by creation of an organizational account with a username based on each user's first and last names.



#### Drupal specific control support

When Drupal user accounts are created, users' email addresses are verified by sending a single-use activation link to the user’s mailbox. The email recipient then uses the activation link to log in to the website and supply a password which must meet the system's password complexity requirements.



### Part c)

#### CivicActions Responsibility

User accounts are assigned a unique identifier in the form of a unique username, password and email address based on the system for allocating user accounts described in AC-2.



#### Drupal specific control support

Identifiers for CivicActions internal personnel include a username based on the individual's full first and last name and are reviewed for uniqueness by the LINCS admin group when it approves creation of the user account.



### Part d)

#### CivicActions Responsibility

Account usernames may not be re-used for at least two years.



#### Drupal specific control support

Drupal users unique identifier (the numeric user id, or uid) is never reused.



### Part e)

#### CivicActions Responsibility

All user accounts are required to change their passwords every 90 days. The website will automatically block the accounts of users who fail to change their password within that time period, after which the account may only be unblocked by a website Administrator or CivicActions Operations.



## IA-05 AUTHENTICATOR MANAGEMENT

> Control description: <http://800-53.govready.com/control?id=IA-5>
> 
> 
> 
> Security control type: Hybrid


#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: authenticator management.



### Part a)

#### LINCS specific control or LINCS Responsibility

Authentication for LINCS internal personnel are created during the personnel assignment process where requests are made to the LINCS admin group for proper access levels. The LINCS admin group verifies the identity of the user. The website performs further verification by sending an email to the user's mailbox containing a single-use activation link which must be used to log in to the account for the first time and to create a password.



#### Drupal specific control support

Refer to control AC-2 in this SSP for further details on account provisioning.

CivicActions will create and maintain an initial Drupal Administrator (highest level of Drupal Account). New Administrators are able to provide additional Administrator access at their own discretion, and are ultimately responsible for managing their own Administrator and other user accounts that they create.



### Part b)

#### LINCS specific control or LINCS Responsibility

LINCS admins in collaboration with CivicActions Operations are responsible for provisioning and de-provisioning end user accounts in compliance with the authentication requirements described herein.



#### Drupal specific control support

Initial authenticator content (a unique email address – not previously used in any other account) is provided by the user. Internal initial password requirements set by CivicActions Operations and ongoing password refreshes by internal user follow the requirements set in the Identification and Authentication Policy.



### Part c)

#### LINCS specific control or LINCS Responsibility

When entering a user account password upon initial login to lincs.ed.gov, all users must comply with the following password policies, which are enforced by the website's software configuration:

* Password must be at least 14 characters in length.

* Password must contain at least one digit.

* Password must contain at least one special character (not whitespace or an alphanumeric).

* Password must contain at least one uppercase character.

* Password must contain at least one lowercase character.



#### Drupal specific control support

The system partially inherits this control from Drupal standard password strength mechanisms.



### Part d)

#### LINCS specific control or LINCS Responsibility

LINCS is responsible for provisioning and de-provisioning end user accounts, which must comply with the strict password policies that are enforced by the website's software configuration, as described in IA-5(d).

In accordance with LINCS site configuration, the following administrative procedures exist for initial authenticator distribution, for lost/compromised/damaged authenticators, and for revoking authenticators.

* Initial authenticator distribution: Users receive a one-time login link by email upon creating of their user account. They use that link to log in and then must enter a password themselves which complies with the password complexity requirements described in IA-4(b).

* Lost/compromised/damaged authenticators: Users who have forgotten their password may request a new password by submitting their username or email address. The website responds by emailing a one-time login link to the user's email address. After using the link to log in, the user is required to enter a new password.

* Revoking authenticators: Users who have not changed their password in the last 90 days are automatically blocked. Administrators and Site Managers may block any user account if they believe there is a reason to do so.



#### Drupal specific control support

The system partially inherits this control from Drupal standard password management.

All password creation/change/reset operations are recorded in the website's "Drupal watchdog" logs.



### Part e)

#### Drupal specific control support

Drupal requires users to change their password upon initial login, and the application website enforces this. User accounts are assigned a randomly-generated and unguessable default password that is not shared with anyone, including site Administrators. Once the user logs in and creates a new password, the default password erased from the website's database.



### Part f)

#### LINCS specific control or LINCS Responsibility

LINCS authenticators follow these password lifetime restrictions:

* Maximum password age = 90

* Minimum password age = 1

* Password reuse restriction = 10



### Part g)

#### LINCS specific control or LINCS Responsibility

LINCS enforces password lifetime restrictions.  The password lifetime settings for internal accounts is as follows:

* Minimum restriction of zero (1) days and

* Maximum restriction of ninety (90) days before a password change is required.



### Part h)

#### Drupal specific control support

For all Drupal users, passwords are protected by the website's software, which only stores an encrypted string based on the password. This means that even if the website's database should be compromised, an attacker would still be unable to know users' actual passwords. Internal users receive training in security awareness and acceptable use and are instructed never to reveal their passwords to anyone.



### Part i)

#### CivicActions Responsibility

CivicActions users are required to take appropriate measures in the handling of passwords including:

* Not transmitting user names and passwords together in an unencrypted format

* Not permitting the sending of passwords in an unencrypted format via email

* Not listing passwords in tickets

* Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.



#### Drupal specific control support

Drupal users are required to take appropriate measures in the handling of passwords including:

* Not transmitting user names and passwords together in an unencrypted format

* Not permitting the sending of passwords in an unencrypted format via email

* Not listing passwords in tickets

* Not writing down or storing passwords in a readable form in any physical or logical location where they may be discoverable by unauthorized persons.



### Part j)

#### CivicActions Responsibility

This control is not applicable due to the fact that group accounts are not created within CivicActions Operations per IA Policy.



#### Drupal specific control support

This control is not applicable due to the fact that group accounts are not created within the Drupal application per IA Policy.



## IA-05 (1) PASSWORD-BASED AUTHENTICATION

> Control description: <http://800-53.govready.com/control?id=IA-5>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

LINCS is responsible for provisioning and de-provisioning end user accounts, which must comply with the strict password policies that are enforced by the website's software configuration, as described in IA-5.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: password based authentication.



### Part a)

#### Drupal specific control support

Drupal supports the requirement for password based authentication complexity. New users of Drupal are required to specify their password authentication as soon as they log in to the website for the first.  The website requires all submitted passwords to comply with validation rules, as described above in IA-5(c).

Changing password lifetime, length, reuse or strength requirements requires a code setting change that therefore needs to be planned and approved by CivicActions' Change Control Board before being implemented.



### Part b)

#### Drupal specific control support

When required to change passwords, Drupal users are required to change their authenticator password by changing at least one character. Enforcement of this control is implemented through the website's software configuration.



### Part c)

#### Drupal specific control support

All Drupal passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.



### Part d)

#### Drupal specific control support

The website requires all submitted passwords to comply with lifetime rules, as described above in IA-5(g).



### Part e)

#### Drupal specific control support

Password reuse is limited through software configuration.



### Part f)

#### Drupal specific control support

When website users request a password reset, the website sends a temporary login link to the email address associated with their user account. After a user logs in via the temporary login link, the website requires the user to enter a new password before proceeding further.



## IA-05 (11) HARDWARE TOKEN-BASED AUTHENTICATION

> Control description: <http://800-53.govready.com/control?id=IA-5>
> 
> 
> 
> Security control type: System Specific Control


#### LINCS specific control or LINCS Responsibility

LINCS does not support physical hardware token-based authentication.  Therefore this control is Not Applicable.



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



### Part j)

#### CivicActions Responsibility

CivicActions systems employ authentication methods consistent with NIST FIPS 140-2 requirements. General public access to system web pages does not require cryptographic authentication. Privileged users accessing systems use the public-key cryptographic functionality of Secure Shell (SSH) to encrypt the exchange of information (including the password) between the remote user and the server. Where Transport Layer Security (TLS, aka SSL) is used, cryptographic modules will be configured in accordance with FIPS 140-2.



## IA-08 IDENTIFICATION AND AUTHENTICATION (NON-ORGANIZATIONAL USERS)

> Control description: <http://800-53.govready.com/control?id=IA-8>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

All non-organization users must follow procedures for access privileges as described in AC-2. Any non-organizational user must receive written permission from a Department representative to access the LINCS. In addition, only temporary access of a specified duration is allowed for non-organizational users directly accessing the system. Once the time period is over or the task completed, the temporary user accounts are removed immediately.



## IA-08 (1) ACCEPTANCE OF PIV CREDENTIALS FROM OTHER AGENCIES

> Control description: <http://800-53.govready.com/control?id=IA-8>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

LINCS does not utilize customer agency supplied PIV credentials.



## IA-08 (2) ACCEPTANCE OF THIRD-PARTY CREDENTIALS

> Control description: <http://800-53.govready.com/control?id=IA-8>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

LINCS does not utilize FICAM approved credentials.



## IA-08 (3) USE OF FICAM-APPROVED PRODUCTS

> Control description: <http://800-53.govready.com/control?id=IA-8>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

LINCS does not utilize FICAM approved products.



## IA-08 (4) USE OF FICAM-ISSUED PROFILES

> Control description: <http://800-53.govready.com/control?id=IA-8>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

CivicActions does not utilize FICAM approved products or profiles.



