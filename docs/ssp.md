
Table of Contents
=================

* [Reusable Component Library System Security Plan](#reusable-component-library-system-security-plan)
* [NIST SP 800-53 Revision 4](#nist-sp-800-53-revision-4)
   * [AC: Access Control](#ac-access-control)
   * [AU: Audit and Accountability](#au-audit-and-accountability)
   * [AT: Awareness and Training](#at-awareness-and-training)
   * [CM: Configuration Management](#cm-configuration-management)
   * [CP: Contingency Planning](#cp-contingency-planning)
   * [IA: Identification and Authentication](#ia-identification-and-authentication)
   * [IR: Incident Response](#ir-incident-response)
   * [MA: Maintenance](#ma-maintenance)
   * [MP: Media Protection](#mp-media-protection)
   * [PS: Personnel Security](#ps-personnel-security)
   * [PE: Physical and Environmental Protection](#pe-physical-and-environmental-protection)
   * [PL: Planning](#pl-planning)
   * [RA: Risk Assessment](#ra-risk-assessment)
   * [CA: Security Assessment and Authorization](#ca-security-assessment-and-authorization)
   * [SC: System and Communications Protection](#sc-system-and-communications-protection)
   * [SI: System and Information Integrity](#si-system-and-information-integrity)
   * [SA: System and Services Acquisition](#sa-system-and-services-acquisition)
* [NIST SP 800-53 Revision 4 Privacy](#nist-sp-800-53-revision-4-privacy)
   * [AP: Authority and Purpose](#ap-authority-and-purpose)
   * [AR: Accountability, Audit, and Risk Management](#ar-accountability-audit-and-risk-management)
   * [DI: Data Quality and Integrity](#di-data-quality-and-integrity)
   * [DM: Data Minimization and Retention](#dm-data-minimization-and-retention)
   * [IP: Individual Participation and Redress](#ip-individual-participation-and-redress)
   * [SE: Security](#se-security)
   * [TR: Transparency](#tr-transparency)
   * [UL: Use Limitation](#ul-use-limitation)

<!-- Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc) -->

# Reusable Component Library System Security Plan

# NIST SP 800-53 Revision 4

## AC: Access Control

### AC-1: Access Control Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel an access control policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Access Control (AC) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


### AC-2: Account Management

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS account management.


#### a

##### CivicActions

CivicActions Operations, in collaboration with CivicActions Security, will set
up privileged accounts accounts for the following roles:

• Developer - user level account that has access to application features and
sanitized databases

• System Administrator - user accounts that enjoy full system administrator
access


##### Drupal

Drupal provides user accounts for individuals who participate in visiting, contributing
to and administering the site with the following roles:

• Anonymous user – readers of the site who either do not have an account or
are not logged in.

• Authenticated user – All non-anonymous users inherit the "authenticated user
role."

• Administrator - This role has all permissions enabled by default.


#### b

##### CivicActions

CivicActions' Project Manager assigns the "admininstrator" role for the management of all accounts issued to internal admin roles supporting the information system. Account requests are initiated by the Project Manager by completing a ticket request and the CivicActions Operation Team manages the entire account creation process.


#### d

##### CivicActions

All accounts issued for application administrators and SSH are documented in CivicActions' ticketing system. Account request tickets contain details that explain the attributes for the account including authorized users of Drupal, system infrastructure, group and role membership, and access authorizations.


##### Drupal

Drupal has a sophisticated permissions and role-based access control built in. Each role within Drupal can only access the documents and controls for which their privilege allows.


#### e

##### CivicActions

All accounts issued for the admin management of Application or SSH access must be approved by the System Owner or Project Manager who must create an account request. The CivicActions Operations Team applies appropriate account permissions and settings based on the job role and function documented within the request ticket using processes defined by the CivicActions Security Team.


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


#### j

##### CivicActions

All privileged accounts are reviewed by CivicActions Operations every 180 days.


#### k

##### CivicActions

In accordance with standard security best practices and CivicActions policy, shared and reissued accounts for internal accounts of any kind are not created nor used for any purpose in any system.


### AC-3: Access Enforcement

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS account management.


##### Drupal

Access control in Drupal is enforced by authentication via unique username/password for every type of user except Anonymous user. The user’s privileges, permissions and access are provided on "least privilege" principle.
The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves. Drupal Administrators are the only user roles that can create new user accounts.


### AC-6: Least Privilege

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: application of least privilege.


##### CivicActions

CivicActions performs regular audits of privileged users as part of the practice of enforcing least privilege.


##### Drupal

CivicActions implements the policy of least privilege for all logical components of Drupal by allowing only authorized access for users, which are necessary to accomplish assigned tasks in accordance with business functions and organizational need.
At the application layer, Drupal is designed with a role based user access system, a least privileged approach based on assignment of privileges to roles. Drupal‘s permission systems enables control of what users can do and see on the site. CivicActions has defined a specific set of permissions for each of the user roles mentioned in control AC-5.
SSH access is provided on a least privilege basis and analyzed on an ongoing basis, at least quarterly. Findings related to these audits of accounts are reported and reviewed by the CivicActions Data team and evaluated to determine roles that need to be revoked.


### AC-6 (9): Auditing Use Of Privileged Functions

##### Drupal

CivicActions, at least quarterly, audits all team accounts based on the concept of least privilege. Each member of the developer team is assigned a role of which defines access needed to perform only the member’s job function.  The audit of accounts is reported and reviewed by the CivicActions Operations and evaluated to determine whether roles or membership within the developer team should be changed.


### AC-7: Unsuccessful Logon Attempts

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: unsuccessful logon attempts.


#### a

##### Drupal

Drupal can be configured to lock an account after a specified number of invalid login attempts within specified time period.


#### b

##### Drupal

Lock down following unsuccessful attempts is configurable by Drupal administrators to conform to defined requirements.  When a user exceeds the limit of invalid logon attempts, their account is automatically locked for a specfied time and requires administrator action to unlock the account before the lockout period expires.


### AC-14: Permitted Actions Without Identification Or Authentication

##### Drupal

The anonymous user role has the least access to the site of all roles. The website does not allow anonymous users to register an account for themselves.


### AC-17: Remote Access

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: remote access.


##### CivicActions

The CivicActions Access Control (AC) policy defines policy for remote usage restrictions.  The Project Manager or System Owner may additionally provision users according to their Access Control policies.


### AC-18: Wireless Access

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: wireless access.


##### CivicActions

This control is not applicable. The system does not provide wireless access points.


### AC-19: Access Control For Mobile Devices

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: mobile device restrictions.


##### CivicActions

This control is not applicable. The system does not maintain a facility in which mobile device access limitations are required.


### AC-20: Use Of External Information Systems

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: use of external information systems.


##### CivicActions

This control is not applicable. The system does not connect with external information systems.


## AU: Audit and Accountability

### AU-1: Audit And Accountability Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel an audit and accountability policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Audit and Accountability (AU) Policy.  This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


### AU-2: Audit Events

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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: disk space availability.


##### CivicActions

CivicActions ensures adequate storage capability requirements listed in AU-11 for all events from the application, database, and hosting environment.


### AU-5: Response To Audit Processing Failures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013: response to audit processing failures.
In the event of low storage or other system issues affecting audit, the AWS CloudWatch monitoring system will alert CivicActions Operations via real-time alert mechanism such as OpsGenie.


##### CivicActions

When notified (e.g., via CloudWatch) of an auditing failure, CivicActions Operations will review the causes and take corrective action.


### AU-6: Audit Review, Analysis, And Reporting

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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


### AU-9: Protection Of Audit Information

##### AWS

This system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


##### CivicActions

CivicActions ensures that audit logs are created, stored and maintained. Developers who have been assigned as members of the CivicActions Security Team are the only CivicActions personnel with logical permission to access and review audit logs.


### AU-11: Audit Record Retention

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.


##### CivicActions

CivicActions audits events from the application, database, and hosting environment, and retains these records for at least 180 days.


### AU-12: Audit Generation

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


## AT: Awareness and Training

### AT-1: Security Awareness And Training Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel awareness and training policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Awareness and Training (AT) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


### AT-2: Security Awareness Training

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


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

#### a

##### CivicActions

The CivicActions Information Security Office tracks all security awareness training within the organization and ensures that all employees have successfully completed training when required. The training records are stored and tracked in a spreadsheet maintained by the CivicActions Information Security Office.


#### b

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

Training records are tracked and maintained by the CivicActions Information Security Office. Records are maintained permanently.


## CM: Configuration Management

### CM-1: Configuration Management Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a configuration management policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Configuration Management (CM) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.
Configuration changes are overseen by the Change Control Board (CCB) consisting of the System Owner, Project Manager and CivicActions Development.


### CM-2: Baseline Configuration

##### AWS

Hardware Baselines
All hardware is maintained by AWS Cloud. The system therefore inherits hardware configuration aspects of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: baseline configuration.


##### CivicActions

A current baseline configuration is always available - stored as a tag in the Git repository - such that the site can be regenerated or rolled back should unauthorized or failing changes be applied.


##### Drupal

The baseline configuration is maintained in Git and described in the Configuration Management Plan, which describes the change workflow and software configuration. In the context of Security Configuration Management, the baseline configuration is a collection of formally approved configuration state(s) of one or more configuration items ("features") that compose the system. The baseline configuration is used to restore and serves as the basis against which the next change or set of changes to the system is made.
The features for the system are maintained in the website's source code, which is managed in git, a source code version control system. Once the source code is updated, git maintains the new version of staged code once committed in the git repository as the new baseline. All code prior to it being staged is documented, tested and approved by CivicActions Development, which is described in control SA-3. The production environment is configured to take database snapshots daily.


### CM-2 (1): Reviews And Updates

##### Drupal

CivicActions reviews and updates baseline configurations for the system at least annually, when requested by the System Owner or required by law, and as an integral part of information system component installations, upgrades and maintenance.
Review of the CM baselines for the system is conducted and approved by CivicActions Development. Any changes made to the production environment are approved prior to deployment by the CCB or agile scrum process. Changes that may require updates to the baseline configuration for the application include:
• Significant upgrades or changes to applications or database software
• Security assessment findings
• Changes in internal/external security requirements
• A new security threat, incident, or event


### CM-2 (2): Automation Support For Accuracy / Currency

##### Drupal

Drupal configuration settings use automated mechanisms to automate code deployment and baseline settings changes. The website's baseline configuration may be reapplied to the site at any time by manually retriggering a tagged code deployment.
The source code, which contains the site’s baseline configuration, is managed using git, a source code version control system. Git is used to track source code which allows administrators to easily deploy and roll back changes on production hosting environments.
The Features module is used to export configuration settings from the website's MySQL database and stores them as code so that the configuration settings can be managed within the git source code version control system.


### CM-2 (3): Retention Of Previous Configurations

##### Drupal

Previous baseline configurations are retained in git, which implements unlimited revision control. Each version of the codebase is given a unique tag when it is deployed to production. When new features are ready for deployment to production, the new code release is given a new tag. This makes it possible to roll back to a previous version of the baseline configuration if needed by redeploying the older release tag.


### CM-3: Configuration Change Control

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

##### CivicActions

CivicActions tests and validates changes to the system before implementing the changes in production. Changes are documented as code and comments in the git source code version control system. Any changes made to system are first captured in a separate development branch of git that is used to create a pull request, which is reviewed for quality and security control before being merged into the master branch of the repository.


### CM-4: Security Impact Analysis

##### CivicActions

Security impact analysis is conducted and documented within the Change Request (CR) process described in in CM-3(b). All proposed configuration-controlled changes to the application are tested first in a sandboxed development environment before being pushed to a staging environment to be tested by another developer and by the Engineering team prior to final approval from CCB to move changes to the production environment.


### CM-5: Access Restrictions For Change

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: physical and logical access restrictions to server instances. Development and staging environments are logged by default as part of the AWS Cloud system.


##### CivicActions

CivicActions restricts system logical access to only those internal personnel assigned to work on the application. Logical access is governed by the implementation described in AC-3 and the concept of least privilege requirements implemented by AC-6.
All access to server environments is via encrypted SSH session with public-key authentication, and all server access is logged.


### CM-5 (1): Automated Access Enforcement / Auditing

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: automated access enforcement / access.


##### Drupal

Access enforcement is monitored within Drupal, which records an entry in the Drupal watchdog log for every successful or failed login attempt to the system.  Each successful login or logout event is logged with an entry that includes the username of the account being used.
All access to server environments is via encrypted SSH sessions with public-key authentication, and all server access is logged.  Specific implementation of auditing events are captured in AU-2. The same access control procedures and need-to-know and accountability principles are enforced for all systems storing baseline configuration policies.


### CM-5 (5): Limit Production / Operational Privileges

#### a

##### Drupal

Configuration changes that do not entail software code changes can only be performed by CivicActions internal administrators with privileges implemented by access enforcement (AC-3) and least privilege (AC-6).


#### b

##### CivicActions

CivicActions internal administrators user access rights are reviewed at least quarterly by CivicActions Information Security, which is responsible for approving all user account assignments to CivicActions developers.


### CM-6: Configuration Settings

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: configuration settings.


##### Drupal

CivicActions configuration settings for Drupal are guided by the Drupal Security Coding Standards <https://www.drupal.org/docs/develop/security> for the security configuration management processes and tools.


#### b

##### CivicActions

CivicActions developers follow security best practices according to the guidelines set by CivicActions Information Security.


#### d

##### CivicActions

All changes to the configuration settings are logged in the Git source code version control system, which records the identity of the developer who committed each change. Version control is enforced, with previous tagged code releases kept for rollback purposes.


### CM-7: Least Functionality

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: least functionality.


### CM-8: Information System Component Inventory

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

##### AWS

Website content is backed up daily by the AWS Managed Cloud hosting system, which is configured to take daily database snapshots
The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: components inventory updates.


##### CivicActions

CivicActions stores all software code in a git source version control repository which is updated for all component installations, removals, and information system updates. This allows CivicActions to build an inventory of the system on demand.


### CM-10: Software Usage Restrictions

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013 for the following: software usage restrictions.


##### Drupal

Drupal is hosted on a LAMP platform (Linux, Apache, MySQL and PHP). These are all compatible with the Free Software Foundation's General Public License (GPL) version 2 or later and are freely available for use under copyright law.


### CM-11: User-Installed Software

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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a contingency planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in Contingency Planning (CP) Policy and Procedure that can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>. 


### CP-2: Contingency Plan

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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: contingency plan training.


##### CivicActions

The ISCP stipulates that all CivicActions system assigned roles in the Contingency Plan Team are trained in their duties within three months of first being assigned a role in the CP, and then annually thereafter or when changes are required. CivicActions uses the Contingency Plan as described in controls CP-1 and CP-2 as a basis for personnel contingency training.


### CP-4: Contingency Plan Testing

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: contingency plan testing.


##### CivicActions

Real world tests of the contingency plan will be held at least annually, with supplemental tests (checklist/table-top) as needed for specific scenarios. The ISCP Coordinator is responsible to facilitate annual testing exercises. The testing process for the ISCP includes review of the ISCP, exercise and identification of corrective actions and other improvements.


### CP-6: Alternate Storage Site

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: alternate storage site


### CP-6 (1): Separation From Primary Site

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: alternate storage site separation.


### CP-9: Information System Backup

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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: information system recovery and reconstitution.


##### CivicActions

The Contingency Plan documents the mechanisms with supporting procedures that allow all system components to be recovered and reconstituted to the system’s original state after a disruption or failure. This original state means that all system parameters (either default or organization-established) are reset, patches are reinstalled, system and security configuration settings are reestablished, system documentation and operating procedures are available, application and system software is reinstalled, information from the most recent backups is available and the system is fully tested.


## IA: Identification and Authentication

### IA-1: Identification And Authentication Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel an identification and authentication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained the CivicActions Identification and Authentication (IA) Policy. This document can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.


### IA-2: Identification And Authentication (Organizational Users)

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: Identification and Authentication procedures for personnel who have rights to AWS platform.


##### CivicActions

Privileged users of the system are required to identify and authenticate in order to access any functions of the information system beyond viewing and downloading the publicly available website content that is available to all anonymous website visitors. Privileged users require the appropriate authorization described in AC-2.


##### Drupal

Drupal users authenticate using the standard login protocol prior to using application services. User roles are described in AC-3.
Privileged Drupal accounts can only be created by existing website users with the role of "administrator". Administrator users assign roles to each login account that govern the user's ability to create, publish, update or delete website content.


### IA-2 (1): Network Access To Privileged Accounts

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

##### CivicActions

CivicActions systems do not support or allow device-to-device communications.


### IA-4: Identifier Management

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

##### Drupal

Feedback of authentication information is obscured during the authentication process into the Drupal application by displaying “dots” in the place of a password, as is standard for web-based applications. In transmission, passwords are encrypted using SSL via HTTPS.


### IA-7: Cryptographic Module Authentication

##### Drupal

All Drupal passwords are encrypted in storage, using the SHA-512 hashing algorithm with a salt. SHA-512 is an approved security function under FIPS PUB 140-2. The hash function is performed repeatedly to further obfuscate the password via key stretching. In transmission, passwords are encrypted using SSL via HTTPS.


#### j

##### CivicActions

CivicActions systems employ authentication methods consistent with NIST FIPS 140-2 requirements. General public access to system web pages does not require cryptographic authentication. Privileged users accessing systems use the public-key cryptographic functionality of Secure Shell (SSH) to encrypt the exchange of information (including the password) between the remote user and the server. Where Transport Layer Security (TLS, aka SSL) is used, cryptographic modules will be configured in accordance with FIPS 140-2.


## IR: Incident Response

### IR-1: Incident Response Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel an incident response planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in Incident Response (IR) Policy and Procedure that can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


### IR-2: Incident Response Training

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident response training.


##### CivicActions

All CivicActions employees are required to participate in incident response training, as required by Incident Response Plan changes, and annually. The CivicActions Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>) is the basis for the training and the incident response workflow created by the Security team.  Upon a review of past incidents, the training is updated to ensure processes and workflows are updated.


### IR-4: Incident Handling

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident handling.


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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident monitoring.


##### CivicActions

CivicActions utilizes the JIRA ticketing tool for tracking and reporting of incident events from reporting to resolution and post-incident analysis. Initial reporting can come from continuous monitoring tools as well as client and public submissions made to support@civicactions.com. Jira processes the tickets for the public submissions and CivicActions' Support Team creates associated GitHub Issues. Internal incidents reported are processed within the GitHub Issue queue. Details of the handling procedures are included in the CivicActions Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan/#response-process>) Response Process.


### IR-6: Incident Reporting

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident reporting.


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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident resonse assistance.


##### CivicActions

CivicActions HelpDesk team provides first response assistance to any users of the system. Response time for external reporting of incidents through e-mail is one business day. Internal users are able to request support thought the same process or initiate the incident response workflow.  Tickets created in the Jira (customer ticketing system) and GitLab (internal ticketing system) documents all details related to the incident to assist the incident response teams in handling the incident.


### IR-8: Incident Response Plan

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident response plan.


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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a system maintenance policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in in the CivicActions Maintenance (MA) Policy and Procedure document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.


### MA-2: Controlled Maintenance

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: controlled maintenance.


### MA-4: Nonlocal Maintenance

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

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: maintenance personnel.


##### CivicActions

Maintenance on the system and applications can only be performed by personnel designated as having internal administrator privileges and responsibilities.  Access rights for the internal administrators are assigned and granted access to perform their specific job responsibilities. All physical maintenance requirements are inherited from AWS.


## MP: Media Protection

### MP-1: Media Protection Policy And Procedures

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for media protection controls as the system is entirely within the AWS Cloud boundary.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a media protection policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in CivicActions Media Protection (MP) Policy and Procedure document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.


### MP-2: Media Access

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for media protection controls as the system is entirely within the AWS Cloud boundary.


### MP-6: Media Sanitization

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for media protection controls as the system is entirely within the AWS Cloud boundary.


### MP-7: Media Use

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for media protection controls as the system is entirely within the AWS Cloud boundary.


## PS: Personnel Security

### PS-1: Personnel Security Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a personnel security policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in CivicActions Personnel Security (PS) Policy document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.


### PS-2: Position Risk Designation

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

#### a

##### CivicActions

Prospective CivicActions employees undergo background checks commensurate with the individual’s job duties, the classification of the information they will access, and the risks associated with the role. At the discretion of the Chief Operating Officer these checks may also be conducted on contractors and / or third party users in cases where they will have access to application data that is not meant to be consumed by the public.  In these instances, the Chief Operating Officer will instruct the Director of Human Resources to conduct a background check before granting access to the information system.


#### b

##### CivicActions

Rescreening is conducted as required by the individual’s job duties, the classification of the information they will access, and the risks associated with the role. A basic background check is performed for all CivicActions employees.


### PS-4: Personnel Termination

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
Some employees may receive company-issued hardware for working on particular projects. These items are collected before the employee exits CivicActions. In the case of an involuntary termination, the Director of Human Resources works to collect company issued devices and provides paperwork highlighting confidential protections for customers.


#### e

##### CivicActions

Access to CivicActions information and information systems is always shared, so that the termination of an individual will not prevent CivicActions from having access to needed resources.


#### f

##### CivicActions

When a person is terminated, a standard off-boarding process is used to notify management and IT and to track the process of disabling access to the information system/information system components. CivicActions IT Operations and Security is given at least a four hour notice to schedule the deactivation of access upon termination. Deactivation is a manual process that is tracked via a Trello card in order to meet the four hour turnaround time before termination.


### PS-5: Personnel Transfer

#### a

##### CivicActions

When an employee, third party personnel and / or contractor is transferred to a new project or position within CivicActions, they may maintain access to the previous system they were working on in order to facilitate the process of maintenance and knowledge transfer. However, as part of the practices of account management (AC-2) and least privilege (AC-6), regular audits of privileged users are conducted and access privileges may be removed when no longer needed. Additionally, adherence to specific client SLAs may enhance the frequency of such audits or the timeliness of privilege removal during personnel transfer.


#### b

##### CivicActions

When an employee, third party personnel and / or contractor is transferred to a new position within CivicActions and there is a requirement for access change, such access changes are normally completed within five business days.


#### c

##### CivicActions

Access authorizations are modified as needed to coincide with changes in duties or
operational need upon personnel transfer or reassignment.


#### d

##### CivicActions

CivicActions Operations is informed of transfers that require access authorization modifications within five business days by the Project Manager, System Owner or Director of Human Resources.


### PS-8: Personnel Sanctions

#### a

##### CivicActions

CivicActions Security and/or the Director of Human Resources is responsible for determining and enforcing sanctions for failing to comply with established information security policies and procedures. Coaching may be considered prior to sanctions. Sanctions may include but are not limited to written warnings, reduction in system access, demotion, or termination.


#### b

##### CivicActions

When employee sanctions processes are initiated, the Director of Human Resources notifies the respective Project Manager(s) and CivicActions Security within five business days.


## PE: Physical and Environmental Protection

### PE-1: Physical And Environmental Protection Policy And Procedures

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-2: Physical Access Authorizations

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-3: Physical Access Control

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls in conjunction with their IaaS provider, AWS.


### PE-6: Monitoring Physical Access

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-8: Visitor Access Records

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-12: Emergency Lighting

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-13: Fire Protection

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-14: Temperature And Humidity Controls

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-15: Water Damage Protection

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


### PE-16: Delivery And Removal

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for all physical and environmental protection controls.


## PL: Planning

### PL-1: Security Planning Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a system planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Planning (PL) Policy and Procedure document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.


### PL-2: System Security Plan

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS system security plan.


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

#### a

##### CivicActions

CivicActions has created and made readily available to individuals requiring access to the information system the rules that describes their responsibilities and expected behavior with regard to information and information system usage. These rules, defined as the Acceptable Use Policy, are included in the CivicActions Security Policy accessible here : <https://civicactions-handbook.readthedocs.io/en/latest/03-policies/security/#acceptable-use-policy> which has also been uploaded to CSAM as 'Appendix J1 - System Rules of Behavior - Privileged User' (CivicActions Security Policy 20190226.docx).


#### b

##### CivicActions

CivicActions HR receives a signed acknowledgment from all employees, indicating that they have read, understand, and agree to abide by the rules of behavior, before authorizing access to information and the information system. The text of the electronically signed (via DocuSign) acknowledgement document has been uploaded to CSAM as artifact: 'CivicActions Security Policy Acknowledgement.docx'


#### c

##### CivicActions

CivicActions reviews the CivicActions Security Policy at least annually and updates is as required.


#### d

##### CivicActions

CivicActions requires individuals who have signed a previous version of the CivicActions Security Policy to read and re-sign when any part of it, including the Acceptable Use Policy/Rules of Behavior, are revised/updated.


## RA: Risk Assessment

### RA-1: Risk Assessment Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a risk assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Risk Assessment (RA) Policy and Procedure CivicActions that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.


### RA-5: Vulnerability Scanning

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: vulnerability scanning.


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


## CA: Security Assessment and Authorization

### CA-1: Security Assessment And Authorization Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a certification, accreditation, and security assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Security Assessment and Authorization Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.


### CA-2: Security Assessments

#### a

##### CivicActions

CivicActions will develop a security assessment plan (SAP) that describes the security controls and control enhancements under assessment, assessment procedures used to determine effectiveness, the assessment environment, the assessment team, and the assessment roles and responsibilities.


#### b

##### CivicActions

CivicActions will assess the security controls in their system and its environment of operation to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting established security requirements,
All controls assigned and documented in this System Security Plan (SSP) will be tested at least annually or when there is a major change to the system.


#### c

##### CivicActions

CivicActions will produce a security assessment report that documents the results of the assessment. The Security Assessment Report must contain the results of the assessment, and may also contain recommendations and suggestions for plans of actions and milestones (POA&Ms).


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

##### CivicActions

This control is not applicable. CivicActions systems do not have system interconnections. The only communication conducted to CivicActions systems is through the Internet.


### CA-5: Plan Of Action And Milestones

##### CivicActions

CivicActions documents all deficiencies and vulnerabilities identified during the security certification and/or continuous monitoring phase (via security assessment, vulnerability scanning, risk assessment, etc.) within the Plan of Action and Milestones (POA&M).
The POA&M document provides a platform for CivicActions to monitor and track the deficiency and its mitigation strategy. POA&M items will include:
• The description of the deficiency,
• Dedicated point of contact for this deficiency.
• Cost of the mitigation strategy
• Associated risk and NIST control
• Recommended mitigation strategy
POA&Ms are tracked throughout the lifecycle of the system until its mitigation. All POA&Ms are reviewed on a monthly basis by CivicActions Information System Security Officer to ensure all mitigation strategies are continuing as documented.


### CA-7: Continuous Monitoring

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

##### AWS

Not applicable: There are no internal systems that connect to the FedRAMP certified AWS cloud.


## SC: System and Communications Protection

### SC-1: System And Communications Protection Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a system and communication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Communications Protection (SC) Policy CivicActions document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.


### SC-5: Denial Of Service Protection

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: denial of service protection.


##### Drupal

Drupal has a manual ability to block IP addresses in cases where attacks bypass cloud protection. This is managed by CivicActions Operations.


### SC-7: Boundary Protection

##### Drupal

Drupal, when deployed on SELinux in full enforcing mode, minimizes the number of services and computing nodes that are exposed to the Internet. Drupal employs both the AWS platform safeguards and the Drupal Watchdog module in monitoring and recording system events. All other computing nodes used in the system are isolated within AWS.


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


### SC-13: Cryptographic Protection

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: cryptographic protection for data in motion (with SSH and HTTPS/SSL) and for data at rest (with Elastic Block Store (EBS) volumnes).


##### CivicActions

The information system implements:
• cryptographic modules through Secure Shell (SSH) to allow administrators to securely logon to the various system components
• HTTPS/SSL (TLS) for connection to web-based services
• TLS for connection to email services
* AES-256 (FIPS 140-2 validated) for data at rest (with Elastic Block Store (EBS) volumnes)


### SC-20: Secure Name / Address Resolution Service (Authoritative Source)

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (authoritative source)


### SC-21: Secure Name / Address Resolution Service (Recursive Or Caching Resolver)

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: secure name / address resolution service (recursive or caching resolver)


### SC-22: Architecture And Provisioning For Name / Address Resolution Service

##### AWS

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: architecture and provisioning for name / address resolution service.


### SC-39: Process Isolation

##### CivicActions

Process isolation is maintained on the Linux platform. Linux is the only operating system that is part of the boundary.


## SI: System and Information Integrity

### SI-1: System And Information Integrity Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a system and information integrity policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Information Integrity (SI) Policy document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.


### SI-2: Flaw Remediation

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


### SI-2(2): Flaw Remediation

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: automated flaw remediation status.


##### CivicActions

The OpenSCAP and OWASP ZAP security scanners are used to perform monthly vulnerability scans of all system components and assess web application interfaces to identify any performance or security issues/flaws. Vulnerabilities and findings identified are handled and remediated in accordance with the implementation of RA-5. Reports are generated to CivicActions Security and Operations for review, analysis, and remediation.


### SI-3: Malicious Code Protection

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

##### Drupal

CivicActions Security and Operations receive Drupal Security Advisories on a regular basis.


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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  software, firmware, and information integrity.


##### CivicActions

CivicActions employ the GitHub system to monitor source code and version control ensuring system integrity and prevents unauthorized changes.  The PHP-authenticator tool is perform a format check on source code prior to entering production. Per implementation of CM-3, any changes to the source code of the system requires the CCB Change Request process. A peer review as part of the Change Request process is conducted to ensure the requested change is verified prior to entering production.
CivicActions employs additional integrity checks on production systems as described in SI-4.


### SI-7 (1): Integrity Checks

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  integrity checks.


##### CivicActions

The integrity check implementation of SI-7 is conducted though the GitHub system and verified monthly by redeploying the system codebase from GitHub.


### SI-7 (5): Automated Response To Integrity Violations

##### CivicActions

The system maintains an audit log of all operations including integrity violations. When an integrity violation occurs, CivicActions Operations will be alerted via email with escalations to text and phone as needed.


### SI-7 (7): Integration Of Detection And Response

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  integration of detection and response. AWS has deployed OSSEC HIDS to all AWS Enterprise hosts which continuously monitors and alerts for software changes as they occur throughout the AWS platform.


##### CivicActions

CivicActions incident response and configuration capabilities include the detection of unauthorized changes to the system though the IR Plan and CCB Change Request process and the implementation of IR-4 and IR-5. In the event of an unauthorized security change to the system, CivicActions support would roll back to and restore from the most recent authorized database set.


### SI-10: Information Input Validation

##### Drupal

All Drupal form input text is subject to format verification and input validation.


### SI-11: Error Handling

#### a

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: error handling.


##### Drupal

Drupal system error logs do not contain passwords, personal information, encryption keys or other sensitive information.


#### b

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: error handling.


##### Drupal

Drupal system error logs are only available to authenticated administrators and viewable within the administrative interface.


### SI-12: Information Handling And Retention

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: information output handling and retention.


##### CivicActions

The CivicActions organization retains all information, system-related information, incident-related information, and system output in accordance with customers’ requirements retention periods and other NIST guidance and standards, Federal policies, procedures, Federal laws and executive orders. Audit records are retained for 365 days.


## SA: System and Services Acquisition

### SA-1: System And Services Acquisition Policy And Procedures

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.


##### CivicActions

CivicActions has developed, documented and disseminated to personnel a system and services acquisition policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained the CivicActions System and Services Acquisition (SA) Policy document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.


### SA-2: Allocation Of Resources

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: allocation of resources.


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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: system development life cycle.


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

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: acquisition process.


##### CivicActions

CivicActions' System and Services Acquisition Policy affects all personnel with purchasing authorization, and applies to all purchases or deployments including infrastructure, software or hardware. The CivicActions System and Services Acquisition Policy contains the process for determining acceptance criteria for all system software and application services.
The Acquisition Security Policy includes an assessment that evaluates the product based on the vendor’s security practices, policies, and past performance. It also details the potential maintenance and end-of-life ramifications with regards to security.
CivicActions Security is responsible for determining the security documentation that must be included in information system or services acquisition contracts.
Configuration and design of the development and production environments are hosted in the CivicActions Git repository. All documentation are strictly controlled regarding transportation and storage in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs.


### SA-5: Information System Documentation

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: information system documentation.


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

##### CivicActions

Information system security engineering principles are applied in the specification, design, development, implementation, and modification of the application system.
Sound security policy, developing layered protections, and controls have been established as the foundation for design throughout the SDLC defined in control SA-3. Security requirements are incorporated into that SDLC, as described previously.
CivicActions uses a development-stage-production testing and management workflow as part of the CivicActions development model. Changes are first tested on a development environment, then moved to a staging environment for further testing. Once the chnages have been tested and approved, a backup is made of the production environment, and the changes are then deployed. More information regarding this model can be found in CM-3 and CM-4.The CivicActions organization ensures that all its developers are trained on how to build secure software, that security controls have been tailored to meet business and operational needs.


### SA-9: External Information System Services

##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: external information system services.


##### CivicActions

CivicActions does not have any dedicated interconnections between information system components within the authorization boundary and external third-party vendor information systems for the purposes of storing, processing, or transmitting federal agency data.


# NIST SP 800-53 Revision 4 Privacy

## AP: Authority and Purpose

### AP-1: AUTHORITY TO COLLECT

##### Privacy

Under Title II of the Workforce Innovation and Opportunity Act (WIOA; PL 113-128),
Section 242, OCTAE carries out a program of national leadership activities to
enhance the quality and outcomes of adult education and literacy activities and
programs nationwide. OCTAE uses these funds to provide technical assistance and
professional development to programs and contribute to research and evaluations of
adult education programs and activities.


### AP-2: PURPOSE SPECIFICATION

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

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-2: PRIVACY IMPACT AND RISK ASSESSMENT

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-3: PRIVACY REQUIREMENTS FOR CONTRACTORS AND SERVICE PROVIDERS

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-4: PRIVACY MONITORING AND AUDITING

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-5: PRIVACY AWARENESS AND TRAINING

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-6: PRIVACY REPORTING

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-7: PRIVACY-ENHANCED SYSTEM DESIGN AND DEVELOPMENT

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### AR-8: ACCOUNTING OF DISCLOSURES

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


## DI: Data Quality and Integrity

### DI-1: DATA QUALITY

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


### DI-2: DATA INTEGRITY AND DATA INTEGRITY BOARD

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


## DM: Data Minimization and Retention

### DM-1: MINIMIZATION OF PERSONALLY IDENTIFIABLE INFORMATION

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. The data collected (email address, first
and last name) is demonstrably a minimum.


### DM-2: DATA RETENTION AND DISPOSAL

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### DM-3: MINIMIZATION OF PII USED IN TESTING, TRAINING, AND RESEARCH

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


## IP: Individual Participation and Redress

### IP-1: CONSENT

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


### IP-2: INDIVIDUAL ACCESS

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


### IP-3: REDRESS

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


### IP-4: COMPLAINT MANAGEMENT

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly. Users enter and have full access to
update or delete any information they input.


## SE: Security

### SE-1: INVENTORY OF PERSONALLY IDENTIFIABLE INFORMATION

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


### SE-2: PRIVACY INCIDENT RESPONSE

##### Privacy

LINCS does not collect or maintain PII and therefore does not directly address this
control though it may address it indirectly.


## TR: Transparency

### TR-1: PRIVACY NOTICE

##### Privacy

LINCS publishes a privacy policy in the footer of every  page. Further, upon login,
the user must accept a detailed Terms and Conditions of Use.


### TR-2: SYSTEM OF RECORDS NOTICES AND PRIVACY ACT STATEMENTS

##### Privacy

LINCS does not collect or maintain PII and therefore does not publish a SORN.


### TR-3: DISSEMINATION OF PRIVACY PROGRAM INFORMATION

##### Privacy

LINCS publishes a privacy policy in the footer of every page. Further, upon login,
the user must accept a detailed Terms and Conditions of Use.


## UL: Use Limitation

### UL-1: INTERNAL USE

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

##### Privacy

LINCS does not share any collected information with any third parties.



