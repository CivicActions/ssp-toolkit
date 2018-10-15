# CONFIGURATION MANAGEMENT

## CM-01 CONFIGURATION MANAGEMENT POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=CM-1>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a configuration management policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Configuration Management (CM) Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.



#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel a configuration management policy  that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls.The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating the Configuration Management Policy and Procedures annually. All procedures are consistent with requirements of FISMA, FedRAMP, ISO 27001, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system. The DKAN SSP Configuration Management Plan can be found in the CivicActions HealthData GitHub repository wiki at <https://github.com/NuCivic/healthdata/wiki/configuration-management-plan>.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## CM-02 BASELINE CONFIGURATION

> Control description: <http://800-53.govready.com/control?id=CM-2>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The application software component of lincs.ed.gov consists of (1) the DKAN distribution of the Drupal web application platform, with (2) additional software features that were developed expressly for lincs.ed.gov based on specifications provided by LINCS.

Baseline configuration for the website's standard DKAN features is stored in the website's codebase and managed using the Features module for Drupal (<https://www.drupal.org/project/features>). Site administrators can view the list of features by visiting the site's features management page at https://www.lincs.ed.gov/admin/structure/features. Most of the configuration for additional features that were developed specifically for lincs.ed.gov is also managed using the Drupal Features module.

The Features module makes it possible to override configuration for individual features without modifying the codebase. It stores those overridden features in the website's MySQL database. The features management page referenced above shows which components of each feature are based on the default configuration stored in code, and shows which components have been overridden in the database. Most components of lincs.ed.gov are based on the default configuration stored in code, but there are approximately a dozen components that have overrides stored in the database.

CivicActions maintains documentation describing each custom feature for lincs.ed.gov that is not standard DKAN, as well as documentation describing feature components that have overrides stored in the database.



#### LINCS specific control or LINCS Responsibility

The baseline configuration is described in Section 3.2 of the Configuration Management Plan, which describes the approved configuration of the LINCS system including all of its hardware, software, and firmware components and the physical and logical locations of each. In the context of Security Configuration Management, the baseline configuration is a collection of formally approved configuration state(s) of one or more configuration items ("features") that compose the LINCS system. The baseline configuration is used by LINCS to restore and serves as the basis against which the next change or set of changes to the LINCS is made.

The features for the LINCS system are maintained in the website's source code, which is managed in git, a source code version control system. Once the source code is updated, git maintains the new version of staged code once committed in the git repository as the new baseline. All code prior to it being staged is documented, tested and approved by CivicActions' DKAN Engineering team, which is described in control SA-3. The LINCS production environment is configured to take database snapshots daily.



#### Amazon Web Services (AWS) US-East/West control support

The system therefore inherits server configuration aspects of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: baseline configuration for IaaS components.

Hardware Baselines

All hardware is maintained by AWS Cloud. The system therefore inherits hardware configuration aspects of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: baseline configuration.

Server Configuration

AWS maintains the baseline software configuration for the server components required to run the Drupal platform upon which the system is built.



## CM-02 (1) REVIEWS AND UPDATES

> Control description: <http://800-53.govready.com/control?id=CM-2>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

CivicActions reviews and updates baseline configurations for lincs.ed.gov at least annually, as an integral part of information system component installations, upgrades and maintenance.



### Part b)

#### LINCS specific control or LINCS Responsibility

Review of the CM baselines for the LINCS system is conducted and approved by the DKAN Engineering team. Any changes made to the production environment are approved prior to deployment by the LINCS CCB. Changes that may require updates to the baseline configuration for the lincs.ed.gov application include:

* Significant upgrades or changes to applications or database software

* Security assessment findings

* Changes in internal/external security requirements

* A new security threat, incident, or event



### Part c)

#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## CM-02 (2) AUTOMATION SUPPORT FOR ACCURACY / CURRENCY

> Control description: <http://800-53.govready.com/control?id=CM-2>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

LINCS configuration settings use automated mechanisms to automate code deployment and baseline settings changes. The website's baseline configuration may be reapplied to the site at any time by manually retriggering a code deployment using the AWS dashboard.

The source code, which contains the site’s baseline configuration, is managed using git, a source code version control system. Git is used to track source code which allows administrators to easily deploy and roll back changes on production hosting environments.

The Features module (described above under "Application Configuration") is used to export configuration settings from the website's MySQL database and stores them as code so that the configuration settings can be managed within the git source code version control system.



## CM-02 (3) RETENTION OF PREVIOUS CONFIGURATIONS

> Control description: <http://800-53.govready.com/control?id=CM-2>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

Previous baseline configurations are retained in git, which implements unlimited revision control. Each version of the codebase is given a unique tag when it is deployed to production. When new features are ready for deployment to production, the new code release is given a new tag. This makes it possible to roll back to a previous version of the baseline configuration if needed by redeploying the older release tag.



## CM-03 CONFIGURATION CHANGE CONTROL

> Control description: <http://800-53.govready.com/control?id=CM-3>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

In accordance with the Configuration Management Plan and control SA-3, CivicActions releases changes to the baseline configuration of the application through planned point releases, which bundle multiple new features, and feature changes into a single planned code releases. Point releases occur roughly every two months. Since they bundle multiple new features into a single release, Examples of the types of changes that may be introduced through a code release include the following, ordered by increasing level of possible security risk:

1. Minor application code changes

2. New software releases for Drupal core, contributed Drupal modules, or other software components that are supplied by outside open source vendors

3. Significant software enhancement

4. Major application modification



### Part b)

#### CivicActions Responsibility

In accordance with the Configuration Management Plan, CivicActions performs security impact analysis of all planned code releases. Level of impact is assessed by the Engineering team before the planned code release is presented to the Change Control Board (CCB) for final approval. Significant software enhancements and major application modifications require approval from the Tech Lead of the Engineering team. Once a code release is considered ready for deployment, a CCB Review is done before scheduling deployment of the code release to production, in accordance with the Agile-based System Development Life Cycle methodology described



### Part c)

#### CivicActions Responsibility

Configuration changes follow the CivicActions CCB process. The changes themselves are documented clearly within a Change Request (CR) ticket in the CivicActions (JIRA or Git) ticketing system. The CR ticket has an approval step built into the ticketing workflow that is required before the implementation phase. The CCB is responsible for reviewing the change and either approving (all members of the CCB must come to a consensus) or rejecting the proposal. These workflow changes are captured within an audit log in the ticket, and are available to anyone viewing the ticket.



### Part d)

#### CivicActions Responsibility

See part b). Configuration changes are captured within tickets in the CivicActions ticketing system. Each CR follows a specific workflow within the ticketing system that follows our process:

1. Open

2. In testing

3. In peer review

4. Waiting for approval

5. Approved OR Rejected

6. Successful OR Unsuccessful

All CRs must be approved before they are applied to the information system.



### Part e)

#### CivicActions Responsibility

All changes are logged and retained for a minimum of three years in the ticketing system. The Change Request (CR) tickets contain a detailed record of the steps taken to implement the change, as well as dates of approval and implementation.



### Part f)

#### CivicActions Responsibility

All changes are logged and retained for a minimum of three years in the ticketing system. The Change Request (CR) tickets contain a detailed record of the steps taken to implement the change, as well as dates of approval and implementation.



### Part g)

#### CivicActions Responsibility

The CivicActions Change Control Board meets weekly, or when operational or security imperatives require, to address requested changes to the application.



#### LINCS specific control or LINCS Responsibility

The Change Control Board (CCB) is a group containing two individuals (at a minimum) that have the collective responsibility and authority to review and approve proposed change to the LINCS system. The LINCS OCIO Policy for Information Systems Security and Privacy Handbook requires that the configuration management process include the system CA (Certification Authority) or a representative from that system as a member of the CCB. The LINCS CCB shall meet regularly at a time and place set by the LINCS CCB Chair.  In addition, the LINCS CCB Chair may convene the LINCS CCB in an emergency session to address time-critical topics as deemed necessary.



## CM-03 (2) TEST / VALIDATE / DOCUMENT CHANGES

> Control description: <http://800-53.govready.com/control?id=CM-3>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions tests and validates changes to the system before implementing the changes in production. Changes are documented as comments in the git source code version control system. Any changes made to LINCS are first captured in a separate development branch of git that is used to create a pull request, which is reviewed for quality control before being merged into the master branch of the repository.



#### Amazon Web Services (AWS) US-East/West control support

Before deployment to production, the code in the master branch of the repository is deployed to a staging server hosted by AWS where it the code changes are reviewed again. After all code changes have been reviewed and tested on the staging server, the code release is presented to the CCB for approval before the code is tagged for release and deployed to the production server.



## CM-04 SECURITY IMPACT ANALYSIS

> Control description: <http://800-53.govready.com/control?id=CM-4>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

Security impact analysis is conducted and documented within the Change Request (CR) process described in in CM-3(b). All proposed configuration-controlled changes to the application are tested first in a sandboxed development environment before being pushed to a staging environment to be tested by another developer and by the Engineering team prior to final approval from CCB to move changes to the production environment.



## CM-05 ACCESS RESTRICTIONS FOR CHANGE

> Control description: <http://800-53.govready.com/control?id=CM-5>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions restricts system logical access to only those internal personnel assigned to work on the application. Logical access is governed by the implementation described in AC-3 and the concept of least privilege requirements implemented by AC-6.

All access to server environments is via encrypted SSH session with public-key authentication, and all server access is logged.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: physical access restrictions with changes to LINCS. Development and staging environments is logged by default as part of the AWS Managed Cloud system.



## CM-05 (1) AUTOMATED ACCESS ENFORCEMENT / AUDITING

> Control description: <http://800-53.govready.com/control?id=CM-5>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

LINCS access enforcement is monitored within Drupal, which records an entry in the Drupal watchdog log for every successful or failed login attempt to the system. Each successful login or logout event is logged with an entry that includes the username of the account being used.

All access to server environments is via encrypted SSH sessions with public-key authentication, and all server access is logged. Specific implementation of auditing events are captured in AU-2. The same access control procedures and need-to-know and accountability principles are enforced for all systems storing baseline configuration policies.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: automated access enforcement / access.



## CM-05 (5) LIMIT PRODUCTION / OPERATIONAL PRIVILEGES

> Control description: <http://800-53.govready.com/control?id=CM-5>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Drupal specific control support

Configuration changes that do not entail software code changes can only be performed by CivicActions internal administrators with privileges implemented by access enforcement (AC-3) and least privilege (AC-6).



#### Amazon Web Services (AWS) US-East/West control support

CivicActions personnel cannot modify hardware or firmware components because they have no physical access to the servers. Software changes can only be performed by CivicActions developers with Senior Developer or Team Leader roles as defined by AWS.



### Part b)

#### CivicActions Responsibility

CivicActions internal administrators user access rights are reviewed at least quarterly by the CivicActions Information Security group, which is responsible for approving all user account assignments to CivicActions developers.



## CM-06 CONFIGURATION SETTINGS

> Control description: <http://800-53.govready.com/control?id=CM-6>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Drupal specific control support

CivicActions configuration settings for Drupal are guided by the Drupal Security Coding Standards <https://www.drupal.org/docs/develop/security> for the security configuration management processes and tools.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: configuration settings for the system software components for the security configuration management processes and tools.



### Part b)

#### CivicActions Responsibility

CivicActions developers follow security best practices according to the guidelines set by CivicActions Information Security.



#### LINCS specific control or LINCS Responsibility

Configuration settings are implemented, monitored, and controlled in accordance with the organizational Configuration Management Plan, section 2, for the security configuration management processes and tools.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.



### Part c)

#### LINCS specific control or LINCS Responsibility

Currently, deviations do not exist for established configuration settings. In the event this changes, the following notes the process that will take place.

The CivicActions CCB, identifies, approves, and documents exceptions to mandatory configuration settings for individual components within its cloud offering only when operationally necessary.  All variances identified during the monthly and annual system testing scans that must be accepted for operational purposes are tracked.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  explicit operational requirements for AWS managed components.



### Part d)

#### CivicActions Responsibility

All changes to the configuration settings are logged in the Git source code version control system, which records the identity of the developer who committed each change. Version control is enforced, with previous tagged code releases kept for rollback purposes.



## CM-07 LEAST FUNCTIONALITY

> Control description: <http://800-53.govready.com/control?id=CM-7>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Amazon Web Services (AWS) US-East/West control support

Access from the internet to the application running on AWS Managed Cloud is permitted only on port 80 TCP (HTTP) and port 443 TCP (HTTPS) for Drupal, and on port 22 TCP (SSH) for the underlying web server. AWS has access to all open ports on all other computing nodes within AWS Managed Cloud to monitor internal-facing services.



### Part b)

#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  least functionality.



## CM-08 INFORMATION SYSTEM COMPONENT INVENTORY

> Control description: <http://800-53.govready.com/control?id=CM-8>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

Application software

The software inventory for the lincs.ed.gov application is maintained in the codebase stored CivicActions' git source code version control system. It consists of the following components:

* The Drupal open source web content management system

* The DKAN distribution of Drupal

* Drupal add-on modules, themes and libraries available from the Drupal.org website which extend Drupal core

* Custom code written for lincs.ed.gov by CivicActions' developers

The inventory is reviewed monthly by CivicActions' DKAN Product Engineering and Open Data Platform Engineering teams. In accordance with the LINCS Configuration Management Plan, section 3.



#### Amazon Web Services (AWS) US-East/West control support

Platform Software

lincs.ed.gov is hosted on the AWS platform. The system therefore inherits the platform software components of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system component inventory.



#### Drupal specific control support

CivicActions stores all software code for the lincs.ed.gov application in a git source version control repository. Website content is backed up daily by the AWS Managed Cloud hosting system, which is configured to take daily database snapshots. This allows CivicActions to build an inventory of the LINCS system on demand.



## CM-08 (1) UPDATES DURING INSTALLATIONS / REMOVALS

> Control description: <http://800-53.govready.com/control?id=CM-8>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions stores all software code in a git source version control repository. This allows CivicActions to build an inventory of the system on demand.



#### Amazon Web Services (AWS) US-East/West control support

Website content is backed up daily by the AWS Managed Cloud hosting system, which is configured to take daily database snapshots

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: hardware components inventory updates.



## CM-09 CONFIGURATION MANAGEMENT PLAN

> Control description: <http://800-53.govready.com/control?id=CM-9>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The LINCS Configuration Management Plan addresses roles, responsibilities, and configuration management processes and procedures. It defines the configuration items for the information system and when in the system development life cycle the configuration items are placed under configuration management (section 3.1.1); and establishes the means for identifying configuration items throughout the system development life cycle (section 3.1.2) and a process for managing the configuration of the configuration items (section 4). This document can be found in the CivicActions HealthData GitHub repository at <https://github.com/NuCivic/healthdata/wiki/configuration-management-plan>.



## CM-10 SOFTWARE USAGE RESTRICTIONS

> Control description: <http://800-53.govready.com/control?id=CM-10>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

The LINCS system is built using CivicActions' DKAN distribution of Drupal which is licensed under the Free Software Foundation's General Public License (GPL), version 2 or later.



#### Amazon Web Services (AWS) US-East/West control support

lincs.ed.gov is hosted on a LAMP platform (Linux, Apache, MySQL and PHP) that is managed by AWS. The system therefore inherits the platform software components of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  software usage restrictions (CM-10).



### Part b)

#### LINCS specific control or LINCS Responsibility

The LINCS Configuration Management Plan, section 3.2.1., notes the software, function, and version for the software components of the LINCS system. DKAN, Drupal core, and all third-party Drupal modules are licensed under the Free Software Foundation's General Public License (GPL), version 2 or later.



#### Amazon Web Services (AWS) US-East/West control support

The system therefore inherits the platform software components of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  software usage restrictions (CM-10).



### Part c)

#### LINCS specific control or LINCS Responsibility

Not Applicable. Peer-to-peer and file sharing are not included in the authorization boundary.



## CM-11 USER-INSTALLED SOFTWARE

> Control description: <http://800-53.govready.com/control?id=CM-11>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

All software installed in the LINCS system environment must be first approved via the CCB resulting in a Change Request (CR) being initiated and executed. No government-furnished equipment (GFE) is within the authorization boundary for the system. Software installation on the computing nodes within the authorization boundary is restricted to administrators. All CivicActions internal administrators are informed of this during their initial training and as part of the rules of behavior document.



#### Amazon Web Services (AWS) US-East/West control support

lincs.ed.gov is hosted on the AWS platform. The system therefore inherits the platform software components of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  Governing installation of software by users



### Part b)

#### CivicActions Responsibility

CivicActions enforces software installation policies through required acknowledgement and sign-off on acceptable use policy by CivicActions personnel. CivicActions' Engineering team is responsible for enforcing compliance with the acceptable use policy.



#### Amazon Web Services (AWS) US-East/West control support

lincs.ed.gov is hosted on the AWS platform. The system therefore inherits the platform software components of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  Enforcing software installation policies.



### Part c)

#### CivicActions Responsibility

CivicActions monitors policy compliance continuously via the code release planning and quality control systems built into the System Development Life Cycle described in control SA-3.



#### Amazon Web Services (AWS) US-East/West control support

lincs.ed.gov is hosted on the AWS platform. The system therefore inherits the platform software components of this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  Monitoring compliance.



