# Reusable Component Library System Security Plan

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


### IA-2: Identification And Authentication (Organizational Users)

> The information system uniquely identifies and authenticates organizational users (or processes acting on behalf of organizational users).

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: Identification and Authentication procedures for personnel who have rights to AWS platform.


##### CivicActions

Privileged users of the system are required to identify and authenticate in order to access any functions of the information system beyond viewing and downloading the publicly available website content that is available to all anonymous website visitors. Privileged users require the appropriate authorization described in AC-2.


##### Drupal

Drupal users authenticate using the standard login protocol prior to using application services. User roles are described in AC-3.
Privileged Drupal accounts can only be created by existing website users with the role of "administrator". Administrator users assign roles to each login account that govern the user's ability to create, publish, update or delete website content.


### IA-2 (1): Network Access To Privileged Accounts

> The information system implements multifactor authentication for network access to privileged accounts.

##### AWS

The AWS Management Console is configured to require two factor authentication. See artifact: AWS_IAM_MFA.png


##### CivicActions

CivicActions system administrators employ a personal public-key pair for basic access and must originate from a whitelisted IP address. The whitelist is maintained by an Ansible inventory file, the current complete list (includes dev sites and stardev) of users with whitelisted IPs is in artifact LINCS-inventory-whitelist.txt
To access root (sudo) privileges an additional password is required. The passwords are maintained in encrypted for in the Ansible inventory file. The mechanism to enable select users to use a password to obtain root access can be viewed in artifact: LINCS-caadmin-sudo.png


##### Drupal

Drupal administrators and other roles with unrestricted access to live content
and/or user accounts are required to use two factor authentication. See artifact
LINCS-COP-TFA.png


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


#### b

##### Drupal

Initial authenticator content (a unique email address – not previously used in any other account) is provided by the user. Internal initial password requirements set by CivicActions Operations and ongoing password refreshes by internal user follow the requirements set in the Identification and Authentication Policy.

#### c

##### Drupal

The system partially inherits this control from Drupal standard password strength mechanisms.

#### d

##### Drupal

The system partially inherits this control from Drupal standard password management.
All password creation/change/reset operations are recorded in the website's "Drupal watchdog" logs.


#### e

##### Drupal

Drupal requires users to change their password upon initial login, and the application website enforces this. User accounts are assigned a randomly-generated and unguessable default password that is not shared with anyone, including site Administrators. Once the user logs in and creates a new password, the default password erased from the website's database.


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



