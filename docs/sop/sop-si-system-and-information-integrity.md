# System And Information Integrity (SI) Standard (SOP)

*Reviewed and updated 2023-12-20*

----

**Table of Contents**
<!--TOC-->

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Standards](#standards)
  - [SI-01 System And Information Integrity Policy And Procedures](#si-01-system-and-information-integrity-policy-and-procedures)
  - [SI-02 Flaw Remediation](#si-02-flaw-remediation)
  - [SI-03 Malicious Code Protection](#si-03-malicious-code-protection)
  - [SI-04 Information System Monitoring](#si-04-information-system-monitoring)
  - [SI-05 Security Alerts, Advisories, And Directives](#si-05-security-alerts-advisories-and-directives)
  - [SI-12 Information Handling And Retention](#si-12-information-handling-and-retention)
  - [SI-12 Information Output Handling And Retention](#si-12-information-output-handling-and-retention)

<!--TOC-->

----

## Introduction

### Purpose

The Office of the Chief Information Officer (OCIO) Information Assurance Services (IAS) publication Information  Technology (IT) System Access Controls Standard of February 11, 2022 provides a comprehensive basis for  management across all systems in the Department. This document provides specific guidance as defined and implemented  by the Project.

### Scope

This system has been categorized as a FIPS-199 LOW system, and as such this document applies only to relevant  controls, policies, processes and procedures as defined within the system.

## Standards

### SI-01 System And Information Integrity Policy And Procedures

System and information integrity policy and procedures for the Project system are formally documented in the Project SSP, which provides the roles and responsibilities as it pertains to physical and environmental protection systems. The Project system support staff monitors the network on a daily basis and employs up-to-date patches to protect the integrity of the system.

Additional information is contained within the None.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.


CivicActions has developed, documented and disseminated to personnel a system and information integrity policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions System and Information Integrity (SI) Policy document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs/>.


### SI-02 Flaw Remediation

Ilias contains built-in security status monitoring of the core application and contributed modules.

**a.**	Identification of information system security flaws are detected as early as possible by the following methods:

- Vulnerability scans, as described in RA-5.
- Log analysis from monitoring described in SI-4.
- Service flaw notifications (CVEs, etc.) are received by the
  CivicActions Security Office and passed on to
  CivicActions Operations staff when relevant.

Any security issues found are ticketed through JIRA and/or the Git issue queue. CivicActions Operations staff prioritizes high findings. Changes made to correct the information system as a result of the system flaws are scheduled and coordinated through the CCB Change Request Process and appropriate approvals required from the CCB as implemented in CM-3.

**b.**	CivicActions testing of the system as a result of security flaw remediation is done through a development environment through the use of internal software and automated testing that ensures the system is working as intended. When a change is made by a developer, testing though a peer review is conducted as part of the Change Request process to ensure the correct analysis is completed. Then the changed code is tested in an automatic test environment as described in the Configuration Management Plan (CMP). Tracking of the testing is documented in JIRA and/or the Git issue queue.

**c.**	CivicActions security-software updates are tested prior to implementation on production. The CivicActions Security framework for installation requires updates to be made within 30 days for high vulnerabilities, 90 days for moderate vulnerabilities, and 240 for low vulnerabilities. An issue ticket is created to track any updates made to the system.

**d.**	Flaw remediation is part of the CivicActions configuration management process. Any security issues found are ticketed through JIRA or the Git issue queue. The CivicActions Security Office prioritizes the high findings within the application. Changes made to correct the system as a result of the system flaws are scheduled and coordinated through the CCB Change Request Process and appropriate approvals required from the CCB Chair as implemented in CM-3.

### SI-03 Malicious Code Protection

**a.**	Virus scans are performed by ClamAV, a server-hosted tool protecting the application from Trojans, Viruses and other malicious cyber-threats. Real-time scans are conducted whenever files are uploaded from any external source and malicious code is blocked or quarantined when detected. All file-based traffic traversing the server is sanitized before being delivered. All input form text is validated and sanitized.

**b.**	Anti-virus definitions and malicious code protection mechanisms are configured and updated automatically on a nightly basis.

**c.**	CivicActions Operations staff receives information system security alerts, advisories, and notifications in response to malicious code detection. These messages are sent to group email distribution lists to ensure all members of the team receive the proper information in a timely manner.

**d.**	False positives during malicious code detection and eradication are dealt with on a case by case basis. Potential impacts on the availability of the information system are detailed in a false positive report depending on if the report is for the OS, database or web application.

### SI-04 Information System Monitoring

**a.**	CivicActions systems use a collection of monitoring systems, including:

- ClamAV - provides signature-based malware detection/quarantine
- OSSEC host-based intrusion detection system (HIDS)
- AIDE Advanced Intrusion Detection Environment (IDS))
- fail2ban, an intrusion prevention system (IPS) framework
- SELinux - a Mandatory Access Control (MAC) IPS
- auditd - a secure system audit daemon
- CloudWatch - AWS monitoring and measurement system
- StatusCake - website monitoring tool
- OpsGenie - a slack/email/text/phone incident escalation tool

**b.**	Logs from the systems described in SI-4(a) are sent to the CivicActions SIEM tool for analysis. These logs can identify unauthorized use of the information system.

**c.**	Monitoring and log collection occur throughout the system.
**d.**	The Configuration Management process, remote log gathering, and SELinux MAC protects information obtained from intrusion-monitoring tools from unauthorized access, modification, and deletion.

**e.**	In the event of a performance score lower than CivicActions standards, a notification is sent to the CivicActions Security Office. CivicActions subscribes to security mailing lists in the event the monitoring activity is required based on law enforcement information, intelligence information, or other credible sources of information.

**f.**	Internal legal counsel is utilized as required when system notifications indicate such action based on user and/or malicious activity. Legal counsel is engaged for any actions that may necessitate increased user monitoring or evidence/forensic actions.

**g.**	System alerts generated by CivicActions internal monitors (StatusCake, OSSEC, ClamAV, others) are sent to the Incident Response team via OpsGenie.

### SI-05 Security Alerts, Advisories, And Directives

Project representatives and system administrators receive alerts from US-CERT on a regular basis. Support personnel take appropriate action in response to relevant areas of concern.


CivicActions Security and Operations receive Ilias Security Advisories on a regular basis.

**a.**	The CivicActions Security Office and Operations staff receive the following security alerts, advisories, and directives on an ongoing basis:

- Mailing lists relevant to web application security
- US-CERT
- Technical Cyber Security Alerts
- Drupal Security Advisories

**b.**	CivicActions utilizes StatusCake for front line monitoring for real time system status and events of the application. StatusCake can feed to the OpsGenie incident escalation system.

**c.**	The CivicActions Security Office disseminates security alerts, advisories, and directives to all CivicActions internal personnel and client personnel as directed.

**d.**	The CivicActions Security Office is responsible for ensuring the dissemination and implementation of relevant security alerts and advisories.

### SI-12 Information Handling And Retention

Project representatives and systems administrators receive annual training from Client regarding information assurance and information handling requirements. These personnel are required to operate the system and handle system data and output in accordance with legal requirements. Personnel training and system guidelines ensure that data and programs are handled appropriately.


### SI-12 Information Output Handling And Retention

The CivicActions organization retains all information, system-related information, incident-related information, and system output in accordance with customers’ requirements retention periods and other NIST guidance and standards, Federal policies, procedures, federal laws, and executive orders. Audit records are retained for 365 days.
