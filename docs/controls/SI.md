# SYSTEM AND INFORMATION INTEGRITY

## SI-01 SYSTEM AND INFORMATION INTEGRITY POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=SI-1>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a system and information integrity policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Information Integrity (SI) Policy document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.



#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel a system and information integrity policy that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls.The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating the System and Information Integrity Policy and Procedures annually. The Chief Operating Officer is responsible for approving System and Information Integrity. All procedures are consistent with requirements of FISMA, FedRAMP, ISO 27001, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## SI-02 FLAW REMEDIATION

> Control description: <http://800-53.govready.com/control?id=SI-2>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

Identification of LINCS security flaws are detected as early as possible by the following methods:

* The CivicActions LINCS system environment uses the OWASP ZAP open-source web application security scanner to report on needed updates based on known flaws. The CivicActions Open Data Team performs the scans on a monthly basis. A report created from the OWASP ZAP scanner lists vulnerabilities and ranks them per severity.

* Service flaw notifications are received by the CivicActions Open Data team.

Any security issues found are ticketed through the Github ticketing tool. The CivicActions Open Data team prioritizes the high findings within Drupal. Changes made to correct the LINCS system as a result of the system flaws are scheduled and coordinated through the CCB Change Request Process and appropriate approvals required from the CCB as implemented in CM-3.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  flaw remediation.



### Part b)

#### Drupal specific control support

CivicActions testing of the system as a result of security flaw remediation are done through a development environment though use of internal software and automated testing that ensures the system is working as intended. When a change is made by a developer, testing though a peer review is conducted as part of the Change Request process to ensure the correct analysis is completed. Tracking of the testing is documented in the Github ticketing tool.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  flaw remediation.



### Part c)

#### Drupal specific control support

CivicActions security-software updates are tested prior to place to production.  The CivicActions Security team framework for installation requires updates to be made within 30 days for high vulnerabilities, 90 days for moderate vulnerabilities, and 240 for low vulnerabilities.  An issue ticket is created to track the any updates made to the system.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  flaw remediation.



### Part d)

#### Drupal specific control support

Flaw remediation is part of the CivicActions configuration management process.  Any security issues found are ticketed through the Github ticketing tool. The CivicActions Security team prioritizes the high findings within the Drupal application. Changes made to correct the system as a result of the system flaws are scheduled and coordinated through the CCB Change Request Process and appropriate approvals required from the CCB Chair as implemented in CM-3.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: flaw remediation.



## SI-02(2) AUTOMATED FLAW REMEDIATION STATUS

> Control description: <http://800-53.govready.com/control?id=SI-2>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The OWASP ZAP open-source web application security scanner is used to perform monthly vulnerability scans of all LINCS system components and assess web application interfaces to identify any performance or security issues/flaws. Vulnerabilities and findings identified are handled and remediated in accordance with the implementation of RA-5. Reports are generated to the CivicActions Open Data team for review, analysis, and remediation.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: automated flaw remediation status.



## SI-03 MALICIOUS CODE PROTECTION

> Control description: <http://800-53.govready.com/control?id=SI-3>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Drupal specific control support

Virus scans are performed by ClamAV is a server-hosted tool protecting the application from Trojans, Viruses and other malicious cyber-threats. Real-time scans are conducted whenever files are uploaded from any external source and malicious code is blocked or quarantined when detected. All traffic traversing the server is sanitized before being delivered.



### Part b)

#### Drupal specific control support

Anti-virus definitions and malicious code protection mechanisms are configured and updated automatically.



### Part c)

#### Drupal specific control support

The Cloud Operations Team receives information system security alerts, advisories and notifications in response to malicious code detection. These messages are sent to group email distribution lists to ensure all members of the team receive the proper information in a timely manner.



### Part d)

#### Drupal specific control support

False positives during malicious code detection and eradication are dealt with on a case by case basis. Potential impacts on the availability of the information system are detailed in a false positive report depending on if the report is for the OS, database or web application.



## SI-04 INFORMATION SYSTEM MONITORING

> Control description: <http://800-53.govready.com/control?id=SI-4>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.

AWS host-based intrusion detection system (HIDS) monitors the AWS boundary and unauthorized local, network, and remote connections to the LINCS system; see inheritance below.



### Part b)

#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.

The AWS host-based intrusion detection system (HIDS) monitors the perimeter of the AWS boundary and events of the system boundary. Logs from the HIDS are forwarded to the AWS SIEM tool.



### Part c)

#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.

CivicActions leverages the AWS platform and a host-based intrusion detection system (HIDS) for monitoring strategically within the information system to collect organization-determined essential information and at ad hoc locations within the system; see inheritance below.



### Part d)

#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.



### Part e)

#### CivicActions Responsibility

In the event of a performance score lower than CivicActions standards, a notification is sent to the CivicActions Open Source Support Engineering team. CivicActions subscribes to security mailing lists in the event the monitoring activity is required based on law enforcement information, intelligence information, or other credible sources of information.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.



### Part f)

#### CivicActions Responsibility

Internal legal counsel is utilized as required when system notifications indicate such action based on user and/or malicious activity.  Legal counsel is engaged for any actions that may necessitate increased user monitoring, or evidence/forensic actions.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.



### Part g)

#### LINCS specific control or LINCS Responsibility

LINCS system alerts generated by CivicActions internal monitors (AWS Insight, StatusCake, OWASP ZAP, and Drupal ClamAV) are sent to the Incident Response team.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.

AWS’s monitoring mechanisms provide notification including audit records, input from malicious code protection mechanisms, data from intrusion detection and prevention mechanisms, and boundary protection devices to the AWS Security Team on a daily basis.



## SI-05 SECURITY ALERTS, ADVISORIES, AND DIRECTIVES

> Control description: <http://800-53.govready.com/control?id=SI-5>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Drupal specific control support

CivicActions / Drupal engineering and operations teams receive the following security alerts, advisories and directives on an ongoing basis:

* Mailing lists relevant to Drupal and web application security

* US-CERT

* Technical Cyber Security Alerts

* Drupal Security Advisories



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.

The AWS Insight control panel provides direct access to the monitored systems.



### Part b)

#### Drupal specific control support

CivicActions utilizes StatusCake for front line monitoring for real-time system status and events of the application.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.

The AWS host-based intrusion detection system (HIDS) monitors the events of the system boundary.



### Part c)

#### Drupal specific control support

CivicActions Security team disseminates security alerts, advisories, advisories, and directives to all CivicActions internal personnel and client personnel as directed.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.



### Part d)

#### Drupal specific control support

CivicActions Security team is responsible for ensuring the dissemination and implementation of relevant security alerts and advisories.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.



## SI-07 SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY

> Control description: <http://800-53.govready.com/control?id=SI-7>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

CivicActions employ the GitHub system to monitor source code, Drupal, and Drupal Modules version control ensuring system integrity and prevents unauthorized changes. The PHP-authenticator tool is perform a format check on source code prior to entering production. Per implementation of CM-3, any changes to the source code of the system requires the CCB Change Request process. A peer review as part of the Change Request process is conducted to ensure the requested change is verified prior to entering production.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  software, firmware, and information integrity.



## SI-07 (1) INTEGRITY CHECKS

> Control description: <http://800-53.govready.com/control?id=SI-7>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

The integrity check implementation of SI-7 is conducted though the GitHub system and verified monthly by redeploying the system codebase from GitHub.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  integrity checks.



## SI-07 (7) INTEGRATION OF DETECTION AND RESPONSE

> Control description: <http://800-53.govready.com/control?id=SI-7>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

CivicActions incident response and configuration capabilities include the detection of unauthorized changes to the system though the IR Plan and CCB Change Request process and the implementation of IR-4 and IR-5. In the event of an unauthorized security change to the system, CivicActions support would roll back to and restore from the most recent authorized database set.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  integration of detection and response. AWS has deployed OSSEC HIDS to all AWS Enterprise hosts which continuously monitors and alerts for software changes as they occur throughout the AWS platform.



## SI-07(5) AUTOMATED RESPONSE TO INTEGRITY VIOLATIONS

> Control description: <http://800-53.govready.com/control?id=SI-7>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The LINCS system does not shut down in the event of an integrity violation is discovered. If an integrity violation is found, CivicActions conducts frequent backups of the LINCS system to support rollback of the LINCS system.



## SI-10 INFORMATION INPUT VALIDATION

> Control description: <http://800-53.govready.com/control?id=SI-10>
> 
> 
> 
> Security control type: System Specific Control


#### Drupal specific control support

The linked data component and information submitted via web forms of the system are the only component vulnerable to code insertion attacks, and has been hardened to prevent them. Third party scans of the system verify the linked data component is not susceptible to cross-site scripting attacks. Information submitted are checked from the execution of the inputs and will disable any script entered in the text.



#### Amazon Web Services (AWS) US-East/West control support

None.



## SI-11 ERROR HANDLING

> Control description: <http://800-53.govready.com/control?id=SI-11>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Drupal specific control support

Drupal system error logs do not contain passwords, personal information, encryption keys or other sensitive information.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  error handling.



### Part b)

#### Drupal specific control support

Drupal system error logs are only available to authenticated administrators and viewable within the administrative interface.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  error handling.



## SI-12 INFORMATION OUTPUT HANDLING AND RETENTION

> Control description: <http://800-53.govready.com/control?id=SI-12>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

The CivicActions organization retains all information, system-related information, incident-related information, and system output in accordance with customers’ requirements retention periods and other NIST guidance and standards, Federal policies, procedures, Federal laws and executive orders. Audit records are retained for 365 days.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information output handling and retention.



## SI-16 MEMORY PROTECTION

> Control description: <http://800-53.govready.com/control?id=SI-16>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  data execution prevention an address space layout randomization]to protect its memory from unauthorized code execution.



