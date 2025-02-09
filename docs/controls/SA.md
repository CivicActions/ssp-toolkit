# Reusable OpenControl Components (SSP-Toolkit).

## SA: System and Services Acquisition

### SA-1: Policy and Procedures

```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] system and services acquisition policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the system and services acquisition policy and the associated system and services acquisition controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the system and services acquisition policy and procedures; and
 - c. Review and update the current system and services acquisition:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete


##### Contractor

CivicActions has developed, documented and disseminated to personnel a system and services acquisition policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained by the CivicActions System and Services Acquisition (SA) Policy document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs/>.





##### Project

The Project complies with the None. The Project will identify new threats/vulnerabilities and technologies that may require updating of solicitation documents.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.



### SA-2: Allocation of Resources

```text
 - a. Determine the high-level information security and privacy requirements for the system or system service in mission and business process planning;
 - b. Determine, document, and allocate the resources required to protect the system or system service as part of the organizational capital planning and investment control process; and
 - c. Establish a discrete line item for information security and privacy in organizational programming and budgeting documentation.

```
**Status:** complete


##### Project

The Project System Owner is responsible for leading the annual budgeting process and for tracking organizational spending. The System Owner coordinates with the CivicActions Project Manager and CivicActions Security on at least monthly basis to track security priorities and spending patterns and determine financial requirements. The System Owner also coordinates the approval process for interim increases to the security budget, if required. This data is used to support the development of the annual budget.

Security costs are included in Exhibit 53 in the Department's on-line electronic Capital Planning and Investment Control system (eCPIC) in order to provide adequate business case information for budget purposes. Security costs are represented across the life cycle in the business case (Exhibit 300) for major investments and (Exhibit 53) for non-major projects - Project is a non-major project. Security costs are summarized and listed as a line item on the Exhibit 53 in the budget submitted to Treasury.

Costs for providing security at the infrastructure level are contained in the business cases for infrastructure supporting computing platforms, desktop processing, the network environment, and web capability. Since the Exhibit 53 includes projections for multiple fiscal years, its intention is to identify and anticipate security resources required.



#### a

##### Contractor

CivicActions' Security Office, in collaboration with the System Owner, act and/or meet on a pre-determined basis to determine information system security requirements and to develop implementation budgets and plans.



#### b

##### Contractor

The CivicActions Security Office, in collaboration with the System Owner, determines, designates, documents, and allocates the resources required to protect the system as part of its capital planning and investment control processes.



#### c

##### Contractor

The annual budget developed by the System Owner includes explicit budgetary line items for FISMA security requirements. Additional security-related expenditures that fall outside of explicit compliance requirements are addressed in sub-lines under the CivicActions Information Technology budget.



### SA-3: System Development Life Cycle

```text
 - a. Acquire, develop, and manage the system using [Assignment: organization-defined system development life cycle] that incorporates information security and privacy considerations;
 - b. Define and document information security and privacy roles and responsibilities throughout the system development life cycle;
 - c. Identify individuals having information security and privacy roles and responsibilities; and
 - d. Integrate the organizational information security and privacy risk management process into system development life cycle activities.

```
**Status:** complete


##### Project

The Project draws from the None, NIST SP 800-64, and Agile software development methodology to ensure security requirements are incorporated during each phase of the life cycle. This helps to ensure the development of secure systems and effective risk management.



#### a

##### Contractor

The system and application(s) are managed by CivicActions using the Agile software development methodology, which provides a continuous System Development Life Cycle (SDLC) methodology. CivicActions Agile management continues to improve the software through ongoing planned code releases. The process is overseen by the Change Control Board (CCB) as described in CM-1. Each point release introduces code and configuration changes to the website through the following SDLC methodology:

- Code release planning: A code release ticket is created in the Change Request project of the
  CivicActions ticketing system which describes the overall goals of the code release.
  The code release ticket is linked to other tickets in the ticketing system which describe issues to
  be addressed by the planned code release. Those issues may include bug fixes and feature enhancements
  as well as upgrades to newer versions of the software packages that have been used to build the
  website.

- Sprints: The tickets covered by the planned code release are then implemented through a series of
  planned sprints, each of which typically lasts two weeks. Each sprint begins with a sprint planning
  session at which the CCB selects a list of tickets to be implemented. CivicActions
  Development holds daily coordination meetings throughout the sprint to share information and resolve
  any problems that may be blocking progress toward completion. At the end of the sprint, a
  retrospective is performed in which progress is reviewed to determine which issues have been
  resolved and which need further work.

- Development/unit testing: Work on each ticket is performed within a separate code branch within the
  CivicActions Git repository, and tested using the GitLab Runner continuous integration
  platform. Developers also write unit tests to prove their code behaves as expected and address security
  considerations such as information leakage, bounds checking, and input validation. Once work on a
  ticket is completed, the developer creates a merge request, and the changes are submitted to at least
  one other developer for review to ensure they meet functional requirements and address security
  considerations before the pull request is merged into the Git repository's development branch for the
  planned code release.

- Integration testing: Once all work tickets have been completed, the code and configuration necessary
  to implement the changes are merged into the website's staging server, where it undergoes additional
  testing to ensure there are no conflicts between the work that has been done on individual tickets.

- User acceptance testing (UAT): The code release undergoes manual testing against a checklist of
  expected site behaviors and options each of the website's defined user roles to further verify that
  the functional changes work as expected and to identify any changes in user experience that need to
  be documented in release notes to be shared with the customer.

- Approval for deployment: After all the planned code release has passed all of the above tests, the
  code release is scheduled for deployment to production and presented to CivicActions'
  Change
  Control Board (CCB) for review and approval.

- Deployment to production: A full backup of the website is performed immediately prior to the
  deployment.

- Security scan: After the deployment to production, the website undergoes a security scan using a web
  vulnerability scanner.

  Security issues to be addressed in the planned code release may come from a variety of sources:

- Customer support requests received by the CivicActions Help Desk
- Security concerns, incidents, and site performance issues reported by users
- Security incident reports, including server log analysis and root cause analysis of those incidents
  performed by the CivicActions Security Office and Operations staff

- Security notifications received by the CivicActions Security Office from external
  security teams and other software vendors

- Vulnerabilities detected during security scans of the website performed by the
  CivicActions Security Office

- Issues reported by the CivicActions Security Office, Operations staff and Development
- Security issues reported through continuous monitoring



#### b

##### Contractor

The CivicActions organization defines and documents information security roles and responsibilities throughout the SDLC. The following teams participate in this process:

- Customer Support: Files tickets when incidents are reported and shares incident reports with customers
- The CivicActions Security Office: Receives security notifications from the Drupal security
  team and other software vendors; performs security scans; uses CivicActions JIRA ticketing
  system to request mitigation of all reported vulnerabilities

- CivicActions Development: Performs server log analysis when security incidents are
  reported; assists in root cause analysis

- Change Control Board: Meets weekly to review and approve upcoming planned code changes to the website,
  include security-related code releases.

- AWS Cloud: Monitors server and application events; proactively respond to security incidents, and
  reports incidents to CivicActions

- Users: Communicates customer security requirements and expectations, and alerts the
  CivicActions customer support team whenever it detects a security or site performance
  issue


Security responsibilities performed by these teams include the following:

- Perform configuration management during information system design, development, implementation, and
  operation;

- Implement only organization-approved changes;
- Document approved changes;
- Manage and control changes to the system;
- Fully test all changes, taking into account security considerations as well as other functional
  requirements;

- Track security flaws and flaw resolution; and
- Employ code analysis tools to examine software for common flaws and document the results of the
  analysis.



#### c

##### Contractor

Each of the CivicActions teams described in SA-3(b) has a team leader who is responsible for defining the roles and responsibilities of individual personnel members within that team. CivicActions uses role-based management for access and authentication implementation and enforcement.



#### d

##### Contractor

The CivicActions organization integrates the organizational information security risk management process into system development life cycle activities by requiring that the processes defined in SA-3(a) and (b) above are adhered to by all information system developers and associated security personnel.



### SA-4: Acquisition Process

```text
Include the following requirements, descriptions, and criteria, explicitly or by reference, using [Selection (one or more): standardized contract language, [Assignment: organization-defined contract language]] in the acquisition contract for the system, system component, or system service:
 - a. Security and privacy functional requirements;
 - b. Strength of mechanism requirements;
 - c. Security and privacy assurance requirements;
 - d. Controls needed to satisfy the security and privacy requirements.
 - e. Security and privacy documentation requirements;
 - f. Requirements for protecting security and privacy documentation;
 - g. Description of the system development environment and environment in which the system is intended to operate;
 - h. Allocation of responsibility or identification of parties responsible for information security, privacy, and supply chain risk management; and
 - i. Acceptance criteria.

```
**Status:** partial


##### Contractor

The CivicActions System and Services Acquisition Policy affects all personnel with purchasing authorization and applies to all purchases or deployments including infrastructure, software or hardware. The CivicActions System and Services Acquisition Policy contains the process for determining acceptance criteria for all system software and application services.

The Acquisition Security Policy includes an assessment that evaluates the product based on the vendor’s security practices, policies, and past performance. It also details the potential maintenance and end-of-life ramifications with regards to security.

The CivicActions Security Office is responsible for determining the security documentation that must be included in the information system or services acquisition contracts.

Configuration and design of the development and production environments are hosted in the CivicActions Git repository. All documentation is strictly controlled regarding transportation and storage in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs.





##### Project

The Project follows the guidelines and procedures within the overarching None. The requirements in the information system acquisition contract permit updating security controls as new threat/vulnerabilities are identified and new technologies are implemented.

The Project System and Services Acquisition Policy contains the process for determining acceptance criteria for all Project system software and services.

The Project organization reviews and approves all acquisition contracts in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs.



### SA-4 (10): Use of Approved PIV Products

```text
Employ only information technology products on the FIPS 201-approved products list for Personal Identity Verification (PIV) capability implemented within organizational systems.

```
**Status:** None


##### Project

CivicActions/Project and AWS describes this control as “not applicable”, as PIV credentials are not applicable to the Project system. Access and Authentication requirements for the Project system for internal CivicActions and customer are implemented under access management and enforcement (AC-2 and AC-3) and identification and authentication for all users (IA-2 and IA-8).

It is the responsibility of CivicActions for implementation of PIV capability for authentication as required.



### SA-5: System Documentation

```text
 - a. Obtain or develop administrator documentation for the system, system component, or system service that describes:
   - 1. Secure configuration, installation, and operation of the system, component, or service;
   - 2. Effective use and maintenance of security and privacy functions and mechanisms; and
   - 3. Known vulnerabilities regarding configuration and use of administrative or privileged functions;
 - b. Obtain or develop user documentation for the system, system component, or system service that describes:
   - 1. User-accessible security and privacy functions and mechanisms and how to effectively use those functions and mechanisms;
   - 2. Methods for user interaction, which enables individuals to use the system, component, or service in a more secure manner and protect individual privacy; and
   - 3. User responsibilities in maintaining the security of the system, component, or service and privacy of individuals;
 - c. Document attempts to obtain system, system component, or system service documentation when such documentation is either unavailable or nonexistent and take [Assignment: organization-defined actions] in response; and
 - d. Distribute documentation to [Assignment: organization-defined personnel or roles].

```
**Status:** complete


##### Project

Client maintains adequate documentation for the Project system. The Project system documentation is protected as required and made available to authorized personnel. Procedures for protecting system documentation include management in the private CivicActions Git repository and the publicly available documentation trees for Free and Open Source Software (FOSS). The documentation maintained for the Project system includes:

- System Security Plan (SSP) – this document
- Configuration documentation
- Incident Response and Contingency Plans
- Rules of Behavior (Acceptable Use Policy)
- FOSS Reference Manuals (Drupal, GNU/Linux, Apache, MySQL, PHP, Postfix,
  etc.)



#### a

##### AWS

In this architecture, documentation of the infrastructure configuration in the form of AWS CloudFormation templates in JSON or YAML format, architecture diagrams, deployment user guide and security controls implementation details is included.

AWS built-in features include online documentation for management of the infrastructure at <https://aws.amazon.com/documentation/>





##### Contractor

Some application features are built on a custom basis and are not part of standard FOSS packages. Administrator documentation for those custom features is maintained in the CivicActions Git repository documentation system.





##### Ilias

Public documentation related to Ilias is maintained by the Ilias Association and is located at <https://Ilias.de/documentation>. This documentation contains administrator documentation for the information system that describes:
- secure configuration, installation, and operation of the system, component, or service;
- effective use and maintenance of security functions/mechanisms; and
- known vulnerabilities regarding configuration and use of administrative functions;



#### b

##### AWS

AWS built-in features include online documentation of AWS services at <https://aws.amazon.com/documentation/>

1. AWS built-in features include online documentation for AWS account users at
   <https://aws.amazon.com/documentation/> such as user Guides, API reference guides, CLI
   reference guides and developer reference guides to provide information on how to
   effectively use security functions.

2. AWS built-in features include online documentation for AWS account users within the
   infrastructure at <https://aws.amazon.com/documentation/> such as user Guides, API
   reference guides, CLI reference guides and developer reference guides to provide
   information on how to access AWS services and components in a more secure manner.

3. AWS built-in features include online documentation for AWS account users at
   <https://aws.amazon.com/security/security-resources/> that provides information
   related to security responsibilities of customers using AWS services.





##### Contractor

The publicly-available FOSS package documentation described in control SA-5(a) also includes user documentation for non-administrators as described in control AC-3. This includes documentation on how to create and manage user accounts as well as how to create, update and delete content.

CivicActions follows the user documentation standard practice to provide context-sensitive help as well as access to a Help Desk in publicly facing applications.

The CivicActions Customer Support team, described in control SA-3(b), handles questions about how to use the system. Questions are submitted by sending an email to support@civicactions.com, which triggers the creation of a ticket in the CivicActions customer support ticketing system.





##### Ilias

The public documentation at Ilias.de contains user documentation for the information system that describes:
- user-accessible security functions/mechanisms and how to effectively use those
  security functions/mechanisms;
- methods for user interaction, which enables individuals to use the system,
  component, or service in a more secure manner; and
- user responsibilities in maintaining the security of the system, component, or service;



#### c

##### Contractor

If the information needed to answer a question is not already included in the website's public-facing documentation, a ticket is created to determine whether the question is sufficiently general in nature to warrant adding the answer to the website's documentation.





##### Ilias

As a popular and well-used and maintained free and open source (FOSS) project, in the event that sought after documentation is not available on Ilias.de, it can usually be found in one of the many forums, mailing lists or Stack Exchange sites covering Ilias and its many contributed modules.


#### d

##### AWS

AWS built-in features include online documentation that is protected by AWS from unauthorized modification or deletion within AWS system.





##### Contractor

All administrator documentation is housed in a protected Git repository. User documentation is publicly available.





##### Ilias

The Ilias.de documentation is multi-sourced on GitHub and private repositories.


#### e

##### AWS

AWS built-in features include online documentation located at <https://aws.amazon.com/documentation/> that is publicly available.





##### Contractor

As needed and approved by the CivicActions Security Office, documentation is available to appropriate personnel by granting access to the private Git repository.





##### Ilias

As the Ilias.de documentation is publicly available, there is no need to provide distribution mechanisms.


### SA-8: Security and Privacy Engineering Principles

```text
Apply the following systems security and privacy engineering principles in the specification, design, development, implementation, and modification of the system and system components: [Assignment: organization-defined systems security and privacy engineering principles].

```
**Status:** incomplete
### SA-8 (33): Minimization

```text
Implement the privacy principle of minimization using [Assignment: organization-defined processes].

```
**Status:** incomplete
### SA-9: External System Services

```text
 - a. Require that providers of external system services comply with organizational security and privacy requirements and employ the following controls: [Assignment: organization-defined controls];
 - b. Define and document organizational oversight and user roles and responsibilities with regard to external system services; and
 - c. Employ the following processes, methods, and techniques to monitor control compliance by external service providers on an ongoing basis: [Assignment: organization-defined processes, methods, and techniques].

```
**Status:** complete


##### Contractor

CivicActions does not have any dedicated interconnections between information system components within the authorization boundary and external third-party vendor information systems for the purposes of storing, processing or transmitting federal agency data.





##### Project

Project does not have any dedicated interconnections between information system components within the authorization boundary and external third-party vendor information systems for the purposes of storing, processing, or transmitting federal agency data.

Project is hosted on the AWS Cloud platform, which was approved under the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013.
