# SYSTEM AND SERVICES ACQUISITION

## SA-01 SYSTEM AND SERVICES ACQUISITION POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=SA-1>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel a system and services acquisition policy that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls.The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating the System and Services Acquisition Policy and Procedures annually. The Chief Operating Officer is responsible for approving System and Services Acquisition.  All procedures are consistent with requirements of FISMA, FedRAMP, ISO 27001, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system.



#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a system and services acquisition policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained the CivicActions System and Services Acquisition (SA) Policy document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## SA-02 ALLOCATION OF RESOURCES

> Control description: <http://800-53.govready.com/control?id=SA-2>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

LINCS in collaboration with CivicActions determines, designates, documents, and allocates the resources required to protect the LINCS system as part of its capital planning and investment control processes. These individuals and groups act and/or meet on a pre-determined basis to determine information system security requirements and to develop implementation budgets and plans.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: allocation of physical resources.



### Part b)

#### LINCS specific control or LINCS Responsibility

The LINCS CFO is responsible for leading the annual budgeting process and for tracking organizational spending. The CFO coordinates with the CivicActions ISSO, the Chief Operating Officer and the Cloud Operations Manager on at least monthly basis to track security priorities and spending patterns and determine financial requirements. The CFO also coordinates the approval process for interim increases to the security budget, if required. This data is used to support the development of the annual budget.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: allocation of physical resources.



### Part c)

#### LINCS specific control or LINCS Responsibility

The annual budget developed by the CFO includes explicit budgetary line items for ISO 27001 and FISMA security requirements. Additional security-related expenditures that fall outside of explicit compliance requirements are addressed in sub-lines under the CivicActions Information Technology budget.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: allocation of physical resources.



## SA-03 SYSTEM DEVELOPMENT LIFE CYCLE

> Control description: <http://800-53.govready.com/control?id=SA-3>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

CivicActions manages the LINCS system, based on CivicActions' DKAN software, which is based on the open source Drupal platform. lincs.ed.gov is managed by CivicActions using the Agile software development methodology, which provides a continuous System Development Life Cycle (SDLC) methodology that is consistent with the LINCS Enterprise Performance Life Cycle (EPLC). CivicActions' Agile management of the website continues to improve the software through ongoing planned code releases. Each point release introduces code and configuration changes to the website through the following SDLC methodology:

* Code release planning: A code release ticket is created in the Change Request project of CivicActions' ticketing system which describes the overall goals of the code release. The code release ticket is linked to other tickets in CivicActions' Github ticketing system which describe issues to be addressed by the planned code release. Those issues may include bug fixes and feature enhancements as well as upgrades to newer versions of the Drupal software, the DKAN distribution, and the Drupal contributed modules that have been used to build the website.

Security issues to be addressed in the planned code release may come from a variety of sources:

* Customer support requests received by CivicActions' customer support team

* Security concerns, incidents, and site performance issues reported by LINCS

* Security incident reports, including server log analysis and root cause analysis of those incidents performed by CivicActions' Open Source Support Engineering team

* Security notifications received by CivicActions' security team from the Drupal security team and other software vendors

* Vulnerabilities detected during security scans of the website performed by CivicActions' security team

* Issues reported by CivicActions' Open Data Engineering and product engineering teams

* Security issues reported by AWS Cloud through its monitoring and ticketing system for lincs.ed.gov

* Sprints: The tickets covered by the planned code release are then implemented through a series of planned sprints, each of which typically lasts two weeks. Each sprint begins with a sprint planning session at which CivicActions developers select a list of tickets to be implemented. The developer team holds daily coordination meetings throughout the sprint to share information and resolve any problems that may be blocking progress toward completion. At the end of the sprint, a retrospective is performed in which progress is reviewed to determine which issues have been resolved and which need further work.

* Development/unit testing: Work on each ticket is performed within a separate code branch within CivicActions' git repository for lincs.ed.gov and tested using the CircleCI continuous integration platform. Developers also write unit tests to prove their code behaves as expected and address security considerations such as information leakage, bounds checking, and input validation. Once work on a ticket is completed, the developer creates a pull request, and the changes are submitted to at lease one other developer for review to ensure they meet functional requirements and address security considerations before the pull request is merged into git repository's development branch for the planned code release.

* Integration testing: Once all work tickets have been completed, the code and configuration necessary to implement the changes is merged into the website's staging server, where it undergoes additional testing to ensure there are no conflicts between the work that has been done on individual tickets.

* User acceptance testing (UAT): The code release undergoes manual testing against a checklist of expected site behaviors and options each of the website's defined user roles to further verify that the functional changes work as expected and to identify any changes in user experience that need to be documented in release notes to be shared with the customer.

* Approval for deployment: After all the planned code release has passed all of the above tests, the code release is scheduled for deployment to production and presented to CivicActions' Change Control Board (CCB) for review and approval.

* Deployment to production: A full backup of the website is performed immediately prior to the deployment.

* Security scan: After the deployment to production, the website undergoes a security scan using the a web vulnerability scanner.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: system development life cycle requirements.



### Part b)

#### LINCS specific control or LINCS Responsibility

The CivicActions organization defines and documents information security roles and responsibilities throughout the SDLC. The following teams participate in this process:

* Customer Support: Files tickets when incidents are reported and shares incident reports with customers

* Security: Receives security notifications from the Drupal security team and other software vendors; performs security scans of healthdata.org; uses CivicActions' Github ticketing system to request mitigation of all reported vulnerabilities

* Open Source Support Engineering: Performs server log analysis when security incidents are reported; assists in root cause analysis

* Open Data Platform Engineering: Provides programming support to fix security issues; deploys code changes to the production website

* DKAN Product Engineering: Oversees website software design and planning; employs code analysis tools to examine software for common flaws and fixes flaws when detected

* Change Control Board: Meets weekly to review and approve upcoming planned code changes to the website, include security-related code releases.

* AWS Cloud: Monitors server and application events; proactively responds to security incidents, and reports incidents to CivicActions

* LINCS: Communicates customer security requirements and expectations, and alerts CivicActions' customer support team whenever it detects a security or site performance issue

Security responsibilities performed by these teams include the following:

* Perform configuration management during information system design, development, implementation, and operation;

* Manage and control changes to the to the LINCS system;

* Implement only organization-approved changes;

* Document approved changes to the LINCS system;

* Fully test all changes to the LINCS, taking into account security considerations as well as other functional requirements;

* Track security flaws and flaw resolution; and

* Employ code analysis tools to examine software for common flaws and document the results of the analysis.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: system development life cycle requirements.



### Part c)

#### LINCS specific control or LINCS Responsibility

Each of the CivicActions teams described in SA-3(b) has a team leader who is responsible for defining roles and responsibilities of individual personnel members within that team. CivicActions uses role base management and access and authentication implementation and enforcement.



### Part d)

#### LINCS specific control or LINCS Responsibility

The CivicActions organization integrates the organizational information security risk management process into system development life cycle activities by requiring that the processes defined in SA-3(a) and (b) above are adhered to by all information system developers and associated security personnel.



## SA-04 ACQUISITIONS

> Control description: <http://800-53.govready.com/control?id=SA-4>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions' System and Services Acquisition Policy affects all personnel with purchasing authorization, and applies to all infrastructure purchases or deployments including software (e.g., SaaS, development tools, administration tools, hosting providers) or hardware (e.g., laptops, desktop computers, smartphones, tablets, servers, and external storage).



### Part a)

#### CivicActions Responsibility

The Acquisition security policy includes a list of questions to be reviewed in scoring each information system or service prior to acquisition. This assessment evaluates the product based on the vendor’s security practices, policies, and past performance. It also details the potential maintenance and end-of-life ramifications with regards to security. Questions asked include:

* Does the product meet any security standards set by independent laboratories, such as ISO/IEC?

* Does the product meet federal government security standards, such as FedRAMP or individual FIPS criteria?

* Does the product support encrypted connections for any online transactions required to use the product?

* Does the software store its data in a secure format?

Based on responses to the questions, the acquisition is given a security score which is then reviewed by CivicActions' Open Data Platform Engineering and Security teams prior to purchase.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: acquisitions of physical components making up the LINCS system.



### Part b)

#### CivicActions Responsibility

Answered in SA-4(a).



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: acquisitions of physical components making up the LINCS system.



### Part c)

#### LINCS specific control or LINCS Responsibility

LINCS requires all software and hardware products undergo a security risk assessment prior to purchase. This assessment evaluates the product based on the vendor’s security practices, policies, and past performance. It also details the potential maintenance and end-of-life ramifications with regards to security.



#### CivicActions Responsibility

CivicActions requires all software and hardware products undergo a security risk assessment prior to purchase. This assessment evaluates the product based on the vendor’s security practices, policies, and past performance. It also details the potential maintenance and end-of-life ramifications with regards to security.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: acquisitions of physical components making up the LINCS system.



### Part d)

#### LINCS specific control or LINCS Responsibility

The LINCS ISSO is responsible for determining the security documentation that must be included in information system or services acquisition contracts.  In determining these requirements the LINCS ISSO coordinates with the Development Operations Manager, Customer Support Engineering Manager, the Contracts Manager, and if necessary the Chief Operating Officer.

The LINCS ISSO ensures all components of the LINCS system system boundary are properly documented to meet the CivicActions Acquisition Security Policy. Prior to testing and deployment to production.



#### CivicActions Responsibility

The CivicActions ISSO is responsible for determining the security documentation that must be included in information system or services acquisition contracts. In determining these requirements the CivicActions ISSO coordinates with the Development Operations Manager, Customer Support Engineering Manager, the Contracts Manager, and if necessary the Chief Operating Officer.



### Part e)

#### CivicActions Responsibility

The CivicActions ISSO is responsible for determining the requirements for protecting security-related documentation that is included in CivicActions acquisition contracts. This determination is based on an assessment of risk and in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards for requirements for protecting security-related documentation.  In determining these requirements the CivicActions ISSO coordinates with the Development Operations Manager, Customer Support Engineering Manager, the Contracts Manager, and if necessary the Chief Operating Officer.

The CivicActions System and Services Acquisition Policy is only accessible to authorized roles via the Github repository tool.  Access to Github is role based and maintained through the access management and enforcement controls (AC-2 and AC-3).



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: acquisitions of physical components making up the LINCS system.



### Part f)

#### CivicActions Responsibility

Configuration and design of the development and production environments are hosted in the CivicActions Github service and Git repository service. All documentation are strictly controlled regarding transportation and storage in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: description of the AWS environ running the LINCS system.



### Part g)

#### LINCS specific control or LINCS Responsibility

The LINCS System and Services Acquisition Policy contains the process for determining acceptance criteria for all LINCS system software and services.

The LINCS organization includes the use of Common Criteria (ISO/IEC 15408) evaluated products in all acquisition contracts in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs.



#### CivicActions Responsibility

The CivicActions Acquisition Security Policy contains the process for determining acceptance criteria for all system software and application services.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: acceptance criteria for AWS and the system components representing the LINCS system.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: acquisitions of physical components making up the LINCS system.



## SA-04 (10) USE OF APPROVED PIV PRODUCTS

> Control description: <http://800-53.govready.com/control?id=SA-4>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

CivicActions/LINCS and AWS describes this control as “not applicable”, as PIV credentials are not applicable to the LINCS system. Access and Authentication requirements for the LINCS system for internal CivicActions and customer are implemented under access management and enforcement (AC-2 and AC-3) and identification and authentication for all users (IA-2 and IA-8).

It is the responsibiility of LINCS for implementation of PIV capability for authentication as required.



## SA-05 INFORMATION SYSTEM DOCUMENTATION

> Control description: <http://800-53.govready.com/control?id=SA-5>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

The LINCS system is configured based on the DKAN distribution of Drupal. Administrator documentation for the Drupal application framework and contributed modules are located at http://drupal.org/documentation. The Drupal documentation repository is maintained by the Drupal Documentation Team: http://drupal.org/contribute/documentation. Public documentation related to DKAN is maintained by CivicActions and is located at: http://docs.getdkan.com. CivicActions also maintains additional documentation in a "DKAN Guide" that is updated with each new point release of DKAN, which happens roughly every three months. The latest point release is DKAN 7.x-1.15, so the current guide is named  "DKAN 7.x-1.15 Guide." Administrator documentation for DKAN is included In the DKAN Guide.

Some features of lincs.ed.gov were built on a custom basis and are not part of standard DKAN. Administrator documentation for those custom features is maintained in CivicActions' Github documentation system in a Github page named "LINCS Custom Development."

Since DKAN is an open source project, all DKAN standard documentation is available to unauthenticated and authenticated users. Administrator documentation for custom features that were built specifically for lincs.ed.gov is only shared with CivicActions personnel.

CivicActions' Open Data Platform Engineering team maintains documentation for developers in Github explaining how to create copies of the lincs.ed.gov website for testing purposes. This documentation includes instructions to sanitize the website's database when creating test copies of the website. (For example, email addresses and user passwords are obfuscated.)



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: administrator documentation to the platform where the LINCS system resides.



### Part b)

#### LINCS specific control or LINCS Responsibility

The publicly-available Drupal and DKAN documentation described in control SA-5(a) also includes user documentation for non-administrators, including for the roles of Content Creator, Editor, Site Manager, Workflow Contributor, Workflow Moderator and Workflow Supervisor as described in control AC-3. This includes documentation on how to create and manage user accounts as well as how to create, update and delete datasets, resources, blog entries and other content on the website.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: user documentation to the platform where the LINCS system resides.



### Part c)

#### LINCS specific control or LINCS Responsibility

CivicActions' Customer Support team, described in control SA-3(b), handles all questions from LINCS about how to use lincs.ed.gov. Questions are submitted by sending an email to support@civicactions.com, which triggers creation of a ticket in CivicActions' customer support ticketing system. If the information needed to answer a question is not already included in the website's documentation, the ticket is reviewed to determine whether the question is sufficiently general in nature to warrant adding the answer to the website's documentation.



### Part d)

#### CivicActions Responsibility

All administrator documentation is housed on Github. User documentation is posted in Github.



### Part e)

#### CivicActions Responsibility

As needed and approved by the CivicActions Security team, documentation is available to appropriate personnel by granting access to the private github repository.



## SA-08 SECURITY ENGINEERING PRINCIPLES

> Control description: <http://800-53.govready.com/control?id=SA-8>
> 
> 
> 
> Security control type: System Specific Control


#### CivicActions Responsibility

Information system security engineering principles are applied in the specification, design, development, implementation, and modification of the application system.

Sound security policy, developing layered protections, and controls have been established as the foundation for design throughout the SDLC defined in control SA-3. Security requirements are incorporated into that SDLC, as described previously.

CivicActions uses a development-stage-production testing and management workflow as part of the CivicActions development model. Changes are first tested on a development environment, then moved to a staging environment for further testing. Once the client approves the changes, a backup is made of the production environment, and the changes are then deployed. More information regarding this model can be found in CM-3 and CM-4.The CivicActions organization ensures that all its developers are trained on how to build secure software, that security controls have been tailored to meet business and operational needs.



## SA-09 EXTERNAL INFORMATION SYSTEM SERVICES

> Control description: <http://800-53.govready.com/control?id=SA-9>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

This is a planned control.

CivicActions employs Jenkins (https://jenkins.io/), an open source "task runner" software system, to run scripts that perform common automated site maintenance tasks on lincs.ed.gov. These tasks include:

* Re-running the DKAN Data Harvester

* Rebuilding the website's data.json feed

* Checking the site periodically to perform uptime monitoring and to automatically restore the site to normal functioning if it detects a service interruption.

Jenkins is installed on a website created by CivicActions that is currently hosted on the Linode web hosting platform (www.linode.com). Linode is not FedRAMP certified. We plan to move the Jenkins website onto a FedRAMP-certified hosting platform by the end of 2016.

CivicActions does not currently have any other dedicated interconnections between information system components within the authorization boundary and external third-party vendor information systems for the purposes of storing, processing, or transmitting federal customer data. If additional external information system services are required in the future, CivicActions shall employ appropriate security controls in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.

LINCS is hosted on the AWS Cloud platform, which was approved under the FedRAMP Provisional ATO granted to the AWS Cloud dated 17 March 2016. As such, AWS is already a FedRAMP-approved CSP and currently meets the FedRAMP requirements.



## SA-10 DEVELOPER CONFIGURATION MANAGEMENT

> Control description: <http://800-53.govready.com/control?id=SA-10>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

CivicActions performs configuration management during information system design, development, implementation, and operation in accordance with CM-9.  Developers and System Administrators working on the LINCS system are required to work within the bounds of CivicActions' configuration management process. This defines the process for moving any change from lower (i.e. development and test) environments to higher ones (i.e. production).



### Part b)

#### CivicActions Responsibility

CivicActions uses a version control system to track all changes made to the source code, Drupal application, and Drupal modules. Using a development-stage-production testing and management workflow as part of the CivicActions development model. Configuration changes are first tested on a development environment, then moved to a staging environment for further testing and client approval. Once the client approves the changes, a backup is made of the production environment, and the changes are then deployed. This application receives the LINCS’s source code from the code repository stored in GitHub, a web storage collaboration site.



### Part c)

#### CivicActions Responsibility

All changes must begin with a Github ticket initiating the CCB process for review, analysis, and approval by the CCB.



### Part d)

#### CivicActions Responsibility

All changes to the LINCS system are documented in Github and conducted in accordance with the Configuration Management Policy.



### Part e)

#### CivicActions Responsibility

When security flaws and flaw resolution are addressed, the CivicActions Security Team reports, assigns, and tracks each issues through the issue ticketing tool within Github.

More information regarding this model can be found in CM-3 and CM-4.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: developer configuration management for physical components of the LINCS system.



## SA-10 (1) SOFTWARE / FIRMWARE INTEGRITY VERIFICATION

> Control description: <http://800-53.govready.com/control?id=SA-10>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

In accordance with the LINCS/DKAN Configuration Management Plan (<https://github.com/NuCivic/healthdata/wiki/configuration-management-plan>), integrity verification tools are employed on the LINCS system to detect unauthorized changes. The first line of monitoring is that CivicActions developers use the git source code version control system to manage all source code running on lincs.ed.gov.  The git repository is hosted by AWS Cloud as part of its PaaS hosting service. CivicActions maintains its own separate clone of the git repository which mirrors the AWS repository and is hosted on GitHub. All code objects, branches and git commits are check-summed before they are stored and can then be referred to by that checksum. This prevents anyone from to changing the contents of any file or directory without Git detecting the unauthorized change. This functionality is built into Git at the lowest levels and is integral to its philosophy.

As initiated by the CM process, any changes to the website's code submitted by a developer must be peer reviewed by another member from the Open Data Platform Engineering or the DKAN Product Engineering team. All changes in source code are required to submit the source code through the PHP Authenticator to verify it is formatted correctly.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: developer firmware integrity verification of the physical components of the LINCS system.



## SA-11 DEVELOPER SECURITY TESTING AND EVALUATION

> Control description: <http://800-53.govready.com/control?id=SA-11>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

Development testing efforts follow a structured methodology as defined within the Security Assessment Plan (SAP). The SAP is outlined within the Software Release Process document on the CivicActions Wiki. All activities that impact the system, including all developer security testing activities, are recorded in GitHub throughout the phases of the system development lifecycle. In accordance with the LINCS/DKAN Configuration Management Plan (<https://github.com/NuCivic/healthdata/wiki/configuration-management-plan>), section 4, a security impact of change is conducted during the request for change.

All tickets are peer-reviewed and changes are tested in a lower environment before deployment to production. At all stages the CivicActions Open Data Platform Engineering, DKAN Product Engineering and Open Source Support Engineering teams validate that ticket-specific QA procedures have been satisfied and conduct testing to ensure that required changes were implemented securely and in such a manner as to preserve the confidentiality, integrity and availability of system resources and data, through the process described in control SA-3.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS security assessment plan.



### Part b)

#### LINCS specific control or LINCS Responsibility

As described in CM-2, CM-4, and SA-3, CivicActions manages the LINCS system development life cycle (SDLC) methodology that includes developer information security considerations including:

* Unit, integration, system, and regression testing/evaluation with enough depth and coverage to determine if the required security controls are implemented correctly, operating as intended, enforcing the desired security policy, and meeting established security requirements

In addition to the testing/evaluation perform in the security assessment plan described in SA-11(a), an application vulnerability scanner and Drupal system monitoring tools are used to identify software flaws. System weaknesses and deficiencies identified by security testing are remediated and addressed through CivicActions' Github issue ticketing system.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS security assessment plan.



### Part c)

#### LINCS specific control or LINCS Responsibility

Development testing efforts follow a structured methodology as defined within the Security Assessment Plan (SAP) and/or the CivicActions SDLC defined in SA-3.



### Part d)

#### LINCS specific control or LINCS Responsibility

The steps in flaw remediation for CivicActions, including developers, follow the Configuration Change Control described in the LINCS/DKAN Configuration Management Plan (<https://github.com/NuCivic/healthdata/wiki/configuration-management-plan>), section 3.3 and implementation of SI-10. The LINCS team develops, tests, validates, and documents proposed changes prior to implementation to assess the impact to the security and privacy risk posture of the system.  Approval for any change as a result of the identifying flaws to the LINCS system will be processed by CivicActions Security, Open Data Platform Engineering, DKAN Product Engineering, and the Open source support engineering teams. All change requests are organized into code release tickets in Github, which are approved and reviewed by the Change Control Board (CCB) prior to deployment to production.



### Part e)

#### LINCS specific control or LINCS Responsibility

Flaws identified by the CivicActions Security team are logged in Github issues, reviewed by the Open Data Platform Engineering and DKAN Product Engineering teams, and submitted for resolution. CivicActions security personnel may also identify flaws during security testing and thus will initiate a Github ticket to begin remediation efforts.



## SA-11 (1) STATIC CODE ANALYSIS

> Control description: <http://800-53.govready.com/control?id=SA-11>
> 
> 
> 
> Security control type: System Specific Control


#### CivicActions Responsibility

The CivicActions team develops, tests, validates, and documents proposed changes prior to implementation to assess the impact to the security and privacy risk posture of the system.  Approval for any change as a result of the identifying flaws to the system will be processed by CivicActions Security, Open Data Platform Engineering, DKAN Product Engineering, and the Open source support engineering teams.

CivicActions developed in-house code requires a peer review of any change to the source code. All change requests are organized into code release tickets in Github, which are approved and reviewed by the Change Control Board (CCB) prior to deployment to production.



