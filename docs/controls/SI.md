# SYSTEM AND INFORMATION INTEGRITY

## SI-01 SYSTEM AND INFORMATION INTEGRITY POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=SI-1>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

System and information integrity policy and procedures for the LINCS Technology Project system are formally documented in the LINCS SSP, which provides the roles and responsibilities as it pertains to physical and environmental protection systems. The LINCS Technology Project system support staff monitors the network on a daily basis and employs up-to-date patches to protect the integrity of the system.

Additional information is contained within the Department of Education, Handbook for Information Assurance Security Policy (Handbook OCIO-01.

This is Agency common control.  More data about implementation can be obtained from the Agency common control catalog.



#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a system and information integrity policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Information Integrity (SI) Policy document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.



## SI-02 FLAW REMEDIATION

> Control description: <http://800-53.govready.com/control?id=SI-2>
> 
> 
> 
> Security control type: Hybrid


#### Drupal specific control support

Drupal contains built-in security status monitoring of the core application and contributed modules.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  flaw remediation.



### Part a)

#### CivicActions Responsibility

Identification of information system security flaws are detected as early as possible by the following methods:

* The CivicActions system environment employs the OpenSCAP scsnner with the DISA STIB baseline to check for vulnerabilities. CivicActions Operations has automated the process to perform the scans on a monthly basis. A report created from the OpenSCAP scanner lists vulnerabilities and ranks them per severity.

* The CivicActions applicate environment is tested by the penetration tester OWASP ZAP, an open-source web application security scanner to report on needed updates based on known flaws. CivicActions Operations has automated the process to perform the scans on a monthly basis. A report created from the OWASP ZAP scanner lists vulnerabilities and ranks them per severity.

* Service flaw notifications (CVEs, etc.) are received by CivicActions Security and passed on to CicvicActions Operations when relevant.

Any security issues found are ticketed through JIRA and/or the Git issue queue. CivicActions Operations prioritizes the high findings.  Changes made to correct the information system as a result of the system flaws are scheduled and coordinated through the CCB Change Request Process and appropriate approvals required from the CCB as implemented in CM-3.



### Part b)

#### CivicActions Responsibility

CivicActions testing of the system as a result of security flaw remediation are done through a development environment though use of internal software and automated testing that ensures the system is working as intended. When a change is made by a developer, testing though a peer review is conducted as part of the Change Request process to ensure the correct analysis is completed. Then changed code is tested in an automatic test environment as described in Configuration Management Plan (CMP). Tracking of the testing is documented in JIRA and/or the Git issue queue.



### Part c)

#### CivicActions Responsibility

CivicActions security-software updates are tested prior to place to production. The CivicActions Security framework for installation requires updates to be made within 30 days for high vulnerabilities, 90 days for moderate vulnerabilities, and 240 for low vulnerabilities. An issue ticket is created to track the any updates made to the system.



### Part d)

#### CivicActions Responsibility

Flaw remediation is part of the CivicActions configuration management process.  Any security issues found are ticketed through JIRA or the Git issue queue. CivicActions Security prioritizes the high findings within the application. Changes made to correct the system as a result of the system flaws are scheduled and coordinated through the CCB Change Request Process and appropriate approvals required from the CCB Chair as implemented in CM-3.



## SI-02(2) AUTOMATED FLAW REMEDIATION STATUS

> Control description: <http://800-53.govready.com/control?id=SI-2>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

The OpenSCAP and OWASP ZAP security scanners are used to perform monthly vulnerability scans of all system components and assess web application interfaces to identify any performance or security issues/flaws. Vulnerabilities and findings identified are handled and remediated in accordance with the implementation of RA-5. Reports are generated to CivicActions Security and Operations for review, analysis, and remediation.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: automated flaw remediation status.



## SI-03 MALICIOUS CODE PROTECTION

> Control description: <http://800-53.govready.com/control?id=SI-3>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

Virus scans are performed by ClamAV, a server-hosted tool protecting the application from Trojans, Viruses and other malicious cyber-threats. Real-time scans are conducted whenever files are uploaded from any external source and malicious code is blocked or quarantined when detected. All file-based traffic traversing the server is sanitized before being delivered. All input form text is validated and sanitized.



### Part b)

#### CivicActions Responsibility

Anti-virus definitions and malicious code protection mechanisms are configured and updated automatically on a nightly basis.



### Part c)

#### CivicActions Responsibility

CivicActions Operations receives information system security alerts, advisories and notifications in response to malicious code detection. These messages are sent to group email distribution lists to ensure all members of the team receive the proper information in a timely manner.



### Part d)

#### CivicActions Responsibility

False positives during malicious code detection and eradication are dealt with on a case by case basis. Potential impacts on the availability of the information system are detailed in a false positive report depending on if the report is for the OS, database or web application.



## SI-04 INFORMATION SYSTEM MONITORING

> Control description: <http://800-53.govready.com/control?id=SI-4>
> 
> 
> 
> Security control type: Hybrid


#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: information system monitoring.



### Part a)

#### CivicActions Responsibility

CivicActions systems use a collection of monitoring systems, including:

* ClamAV - provides signature based malware detection/quarantine

* OSSEC host-based intrusion detection system (HIDS)

* AIDE Advanced Intrusion Detection Environment (IDS))

* fail2ban, an intrusion prevention system (IPS) framework

* SELinux - a Mandatory Access Control (MAC) IPS

* auditd - a secure system audit daemon

* CloudWatch - AWS monitoring and measurement system

* StatusCake - website monitoring tool

* OpsGenie - a slack/email/text/phone incident escalation tool



### Part b)

#### CivicActions Responsibility

Logs from the systems described in SI-4(a) are sent to the CivicActions SIEM tool for analysis. These logs can identify unauthorized use of the information system.



### Part c)

#### CivicActions Responsibility

Monitoring and log collection occurs throughout the system.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.

CivicActions leverages the AWS platform and a host-based intrusion detection system (HIDS) for monitoring strategically within the information system to collect organization-determined essential information and at ad hoc locations within the system; see inheritance below.



### Part d)

#### CivicActions Responsibility

The Configuration Management process, remote log gathering and SELinux MAC protects information obtained from intrusion-monitoring tools from unauthorized access, modification, and deletion.



#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.



### Part e)

#### CivicActions Responsibility

In the event of a performance score lower than CivicActions standards, a notification is sent to CivicActions Security. CivicActions subscribes to security mailing lists in the event the monitoring activity is required based on law enforcement information, intelligence information, or other credible sources of information.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.



### Part f)

#### CivicActions Responsibility

Internal legal counsel is utilized as required when system notifications indicate such action based on user and/or malicious activity.  Legal counsel is engaged for any actions that may necessitate increased user monitoring, or evidence/forensic actions.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.



### Part g)

#### CivicActions Responsibility

System alerts generated by CivicActions internal monitors (StatusCake, OSSEC, ClamAV, others) are sent to the Incident Response team via OpsGenie.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  information system monitoring.

AWS’s monitoring mechanisms provide notification including audit records, input from malicious code protection mechanisms, data from intrusion detection and prevention mechanisms, and boundary protection devices to the AWS Security Team on a daily basis.



## SI-05 SECURITY ALERTS, ADVISORIES, AND DIRECTIVES

> Control description: <http://800-53.govready.com/control?id=SI-5>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

LINCS Technology Project representatives and system administrators receive alerts from US-CERT on a regular basis. Support personnel take appropriate action in response to relevant areas of concern.



#### Drupal specific control support

CivicActions Security and Operations receive Drupal Security Advisories on a regular basis.



### Part a)

#### CivicActions Responsibility

CivicActions Security and Operations receive the following security alerts, advisories and directives on an ongoing basis:

* Mailing lists relevant to web application security

* US-CERT

* Technical Cyber Security Alerts

* Drupal Security Advisories



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.

The AWS Insight control panel provides direct access to the monitored systems.



### Part b)

#### CivicActions Responsibility

CivicActions utilizes StatusCake for front line monitoring for real-time system status and events of the application. StatusCake can feed to the OpsGenie incident escalation system.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.

The AWS host-based intrusion detection system (HIDS) monitors the events of the system boundary.



### Part c)

#### CivicActions Responsibility

CivicActions Security disseminates security alerts, advisories, advisories, and directives to all CivicActions internal personnel and client personnel as directed.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.



### Part d)

#### CivicActions Responsibility

CivicActions Security is responsible for ensuring the dissemination and implementation of relevant security alerts and advisories.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  AWS security alerts, advisories, and directives.



## SI-07 SOFTWARE, FIRMWARE, AND INFORMATION INTEGRITY

> Control description: <http://800-53.govready.com/control?id=SI-7>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions employ the GitHub system to monitor source code and version control ensuring system integrity and prevents unauthorized changes.  The PHP-authenticator tool is perform a format check on source code prior to entering production. Per implementation of CM-3, any changes to the source code of the system requires the CCB Change Request process. A peer review as part of the Change Request process is conducted to ensure the requested change is verified prior to entering production.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  software, firmware, and information integrity.



## SI-07 (1) INTEGRITY CHECKS

> Control description: <http://800-53.govready.com/control?id=SI-7>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

The integrity check implementation of SI-7 is conducted though the GitHub system and verified monthly by redeploying the system codebase from GitHub.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  integrity checks.



## SI-07 (7) INTEGRATION OF DETECTION AND RESPONSE

> Control description: <http://800-53.govready.com/control?id=SI-7>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

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

All Drupal form input text is subject to format verification and input validation.



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



## SI-12 INFORMATION HANDLING AND RETENTION

> Control description: <http://800-53.govready.com/control?id=SI-12>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

LINCS Technology Project representatives and systems administrators receive annual training from the Department regarding information assurance and information handling requirements. These personnel are required to operate the system and handle system data and output in accordance with legal requirements. Personnel training and system guidelines ensure that data and programs are handled appropriately.



#### CivicActions Responsibility

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



