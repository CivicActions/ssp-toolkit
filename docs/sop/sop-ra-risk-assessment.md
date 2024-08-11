# Risk Assessment (RA) Standard (SOP)

*Reviewed and updated 2023-12-20*

----

**Table of Contents**
<!--TOC-->

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Standards](#standards)
  - [RA-01 Risk Assessment Policy And Procedures](#ra-01-risk-assessment-policy-and-procedures)
  - [RA-02 Security Categorization](#ra-02-security-categorization)
  - [RA-03 Risk Assessment](#ra-03-risk-assessment)
  - [RA-05 Vulnerability Scanning](#ra-05-vulnerability-scanning)

<!--TOC-->

----

## Introduction

### Purpose

The Office of the Chief Information Officer (OCIO) Information Assurance Services (IAS) publication Information  Technology (IT) System Access Controls Standard of February 11, 2022 provides a comprehensive basis for  management across all systems in the Department. This document provides specific guidance as defined and implemented  by the Project.

### Scope

This system has been categorized as a FIPS-199 LOW system, and as such this document applies only to relevant  controls, policies, processes and procedures as defined within the system.

## Standards

### RA-01 Risk Assessment Policy And Procedures

The Client follows the risk assessment policy and procedures formally documented within None. Furthermore, a Risk Assessment Plan was originally initiated to determine the extent of the potential threat and the risk associated with Project throughout its System Development Life Cycle (SDLC). The Project Risk Assessment defines the methodology approach to determine the likelihood risks, and identify potential mitigation options to reduce risks to the Project system.

The Project Risk Assessment will be conducted in accordance with the Department’s risk assessment policy and procedures. By doing so, the responsible parties associated with the Project will be able to determine the risk, likelihood and impact that could result from exploiting vulnerabilities within the system.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.


The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


CivicActions has developed, documented and disseminated to personnel a risk assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Risk Assessment (RA) Policy and Procedure that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs/>.


### RA-02 Security Categorization

**a.**	In accordance with FIPS 199 requirement and guidelines provided in NIST SP800-60 Rev.1, the organization categorized the system as a Low system: Confidentiality (Low), Integrity (Low), Availability (Low).

**b.**	The security categorization was determined by evaluating the type of information that is stored, processed, and/or transmitted by the application and the potential impact levels associated with the confidentiality, integrity, and availability of that information. The application’s security categorization has been documented in this SSP.

**c.**	The security categorizations have been reviewed by the designated application POCs, were approved during the C&A effort. The formal security categorization document is available upon request. The system inventory for the Project Project is revalidated semiannually.

### RA-03 Risk Assessment

**a.**	CivicActions/Project will perform risk assessments for the Project system based on SP 800-30 Rev. 1 Guide for Conducting Risk Assessments at least annually and as part of the change management activities for the Project system that warrant a new or updated risk assessment.

**b.**	The results of risk assessments will be compiled into a risk assessment report to be reviewed by CivicActions Security and relevant personnel, and also added to the GitLab system for the Project system.

**c.**	CivicActions/Project reviews risk assessment
results at least annually.

**d.**	The Risk Assessment report will be disseminated to the appropriate
personnel through the Project Manager and CivicActions
Security.

**e.**	Risk assessments are conducted annually or whenever there are significant changes to the information system or environment of operation (including the identification of new threats and vulnerabilities), or other conditions that may impact the security state of the system, as defined in NIST Special Publication 800-37 Revision 1.
A significant change includes:

- Changing authentication or access control implementations;
- Changing storage implementations;
- Changing a COTS product to another product;
- Changing the backup mechanisms and process; and,
- Adding new interconnections to an outside service provide.

### RA-05 Vulnerability Scanning

The Project uses vulnerability scanning software to document and determine risks to the system. These scans are run monthly and the results of these scans are being used to inform changes to the system and verify that security controls are working correctly. These scans are used to document the current state of the system, and to analyze security trends as changes are made over time.


The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: vulnerability scanning.


**a.**	CivicActions Operations uses vulnerability scanning software to document and determine risks to the system. Operating system and application vulnerability scans include:

- The CivicActions system environment employs the OpenSCAP scanner with the Red Hat STIG baseline to check for vulnerabilities.
- The CivicActions application environment is tested by the penetration tester OWASP ZAP, an open-source web application security scanner to report on needed updates based on known flaws.

CivicActions Operations has automated the process to perform the scans on a monthly basis. The resulting reports list vulnerabilities and rank them by severity. These reports are stored in Amazon S3 buckets and are used to inform changes to the system and verify that security controls are working correctly. These scans are used to document the current state of the system, and to analyze security trends as changes are made over time.

**b.**	CivicActions employs the automated vulnerability scanning tools OpenSCAP and OWASP ZAP which are interoperable with standard web browsers, the Open Source Ansible infrastructure provisioning system and other Open Source tools.

**c.**	The CivicActions Security Office reviews all vulnerabilities identified from automated scans and security assessments. "False positive" findings are documented and may be tailored out. Vulnerabilities found and deemed legitimate are assigned an impact rating and response time thought creation of an issue or ticket. The CivicActions Operations staff reviews current scans and compare with older scans to identify trends and to verify previous vulnerabilities have been mitigated.

**d.**	Identified and reported vulnerabilities are assigned an impact rating and response time by CivicActions' Security and must be remediated according to the following time requirements:

- Critical - Within 15 days of discovery (usually within 1 week))
- High - Within 30 days of discovery (usually within 1 week))
- Moderate - Within 90 days of discovery (usually within 2 weeks)
- Low - Within 180 days of discovery

**e.**	Results of the vulnerability scans and security assessments are shared with all appropriate CivicActions personnel supporting continuous monitoring requirements. CivicActions Security assigns each vulnerability an impact rating and response time through JIRA or the Git issue tool for tracking to the established remediation deadlines listed in RA-5(d).
