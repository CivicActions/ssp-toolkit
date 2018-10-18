# RISK ASSESSMENT

## RA-01 RISK ASSESSMENT POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=RA-1>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel a risk assessment policy that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls.The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating the Risk Assessment Policy and Procedures annually. The Chief Operating Officer is responsible for approving Risk Assessment.  All procedures are consistent with requirements of FISMA, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system.



#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a risk assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Risk Assessment (RA) Policy and Procedure CivicActions that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs/>.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## RA-02 SECURITY CATEGORIZATION

> Control description: <http://800-53.govready.com/control?id=RA-2>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

In accordance with FIPS 199 requirement and guidelines provided in NIST SP800-60 Rev.1, the organization categorized the system as a Low system: Confidentiality (Low), Integrity (Low), Availability (Low). This categorization was accepted by the Authorizing Official.



### Part b)

#### LINCS specific control or LINCS Responsibility

The outcome of the security categorization and related information types are reflected in section 2 (Information System Categorization) of the lincs.ed.gov System Security Plan (SSP).



### Part c)

#### LINCS specific control or LINCS Responsibility

The CivicActions organization ensures the FIPS 199 security categorization decision is reviewed and approved by the LINCS Authorizing Official when considering authorizing the CivicActions LINCS system.



## RA-03 RISK ASSESSMENT

> Control description: <http://800-53.govready.com/control?id=RA-3>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

This was completed in CY2016.



### Part a)

#### LINCS specific control or LINCS Responsibility

CivicActions will perform risk assessments for the LINCS system based on SP 800-30 Rev. 1 Guide for Conducting Risk Assessments at least annually and part of the change management activities for the LINCS system that warrant a new or updated risk assessment. The results of risk assessments will be compiled into a risk assessment report to be reviewed by CivicActions Management and relevant personnel, and also added to the GitHub system for the LINCS system.



### Part b)

#### LINCS specific control or LINCS Responsibility

CivicActions will perform risk assessments for the LINCS system based on SP 800-30 Rev. 1 Guide for Conducting Risk Assessments at least annually, or whenever changes to the LINCS system warrant a new or updated risk assessment. The results of risk assessments will be compiled into a risk assessment report to be reviewed by CivicActions Management and relevant personnel.



### Part c)

#### LINCS specific control or LINCS Responsibility

CivicActions will perform risk assessments for the LINCS system based on SP 800-30 Rev. 1 Guide for Conducting Risk Assessments at least annually, or whenever changes to the LINCS system warrant a new or updated risk assessment. The results of risk assessments will be compiled into a risk assessment report.



### Part d)

#### LINCS specific control or LINCS Responsibility

The Risk Assessment report will be disseminated to the appropriate personnel through the CivicActions Security team at least annually.



### Part e)

#### LINCS specific control or LINCS Responsibility

Risk assessments are conducted annually or whenever there are significant changes to the information system or environment of operation (including the identification of new threats and vulnerabilities), or other conditions that may impact the security state of the system, as defined in NIST Special Publication 800-37 Revision 1, Appendix F.

A significant change includes:

* Changing authentication or access control implementations;

* Changing storage implementations;

* Changing a COTS product to another product;

* Changing the backup mechanisms and process; and,

* Adding new interconnections to an outside service provide.



## RA-05 VULNERABILITY SCANNING

> Control description: <http://800-53.govready.com/control?id=RA-5>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

In addition to the fully inherited IaaS and PaaS scanning conducted by AWS ACE as reported to FedRAMP, the CivicActions Security team uses the OWASP ZAP application scanning tool to scan the LINCS application for vulnerabilities on a monthly basis.  All vulnerability findings are documented for remediation though the CivicActions Security team by creating a GitHub issue and assigning the ticket to the appropriate CivicActions team. Vulnerability assessments will be archived and be tracked on a quarterly Plan of Action & Milestones (POA&M) and submitted to LINCS personnel responsible for the LINCS system.



#### Amazon Web Services (AWS) US-East/West control support

The system fully inherits this control to fully cover the AWS managed cloud from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  vulnerability scanning for operating system/infrastructure and database servers. AWS monthly scan results can be monitored via FedRAMP to verify the control’s implementation was adequate such as OS-level scans.



### Part b)

#### LINCS specific control or LINCS Responsibility

CivicActions uses the automated vulnerability scanning tool OWASP ZAP to scan the LINCS system application. ZAP updates the list of known vulnerabilities automatically and describes the risk of each vulnerability.



#### Amazon Web Services (AWS) US-East/West control support

The system fully inherits this control to fully cover this control for the AWS managed cloud from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  vulnerability scanning for operating system/infrastructure and database servers. AWS monthly scan results can be monitored via FedRAMP to verify the control’s implementation was adequate such as OS-level scans.



### Part c)

#### CivicActions Responsibility

CivicActions Security team reviews all vulnerabilities identified from automated scans and security assessments.  Vulnerabilities found and deemed legitimate are assigned an impact rating and response time thought creation of an issue or ticket. The CivicActions Security team reviews current scans and compare with older scans to identify trends and to verify previous vulnerabilities have been mitigated.



#### Amazon Web Services (AWS) US-East/West control support

The system fully inherits this control to fully cover this control for the AWS managed cloud from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  vulnerability scanning for operating system/infrastructure and database servers. AWS monthly scan results can be monitored via FedRAMP to verify the control’s implementation was adequate such as OS-level scans.



### Part d)

#### CivicActions Responsibility

CivicActions identified and reported vulnerabilities are assigned by the CivicActions Security team an impact rating and response time and must be remediated according to the following time requirements.

* High - Within 30 days of discovery

* Moderate - Within 90 days of discovery

* Low - Within 240 days of discovery



#### Amazon Web Services (AWS) US-East/West control support

The system fully inherits this control to fully cover this control for the AWS managed cloud from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  vulnerability scanning for operating system/infrastructure and database servers. AWS monthly scan results can be monitored via FedRAMP to verify the control’s implementation was adequate such as OS-level scans.



### Part e)

#### LINCS specific control or LINCS Responsibility

Results of the vulnerability scans and security assessments are shared with all appropriate CivicActions personnel and appropriate LINCS personnel supporting continuous monitoring requirements. CivicActions Security team assigns each vulnerability an impact rating and response time though the GitHub issue tool for tracking to the established remediation deadlines listed in RA-5(d).



#### Amazon Web Services (AWS) US-East/West control support

The system fully inherits this control to fully cover this control for the AWS managed cloud from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  vulnerability scanning for operating system/infrastructure and database servers. AWS monthly scan results can be monitored via FedRAMP to verify the control’s implementation was adequate such as OS-level scans.

Results of vulnerability scans and security assesments and related continuous montioring of AWS is available to LINCS through FedRAMP.



