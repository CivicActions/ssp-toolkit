# SECURITY ASSESSMENT AND AUTHORIZATION

## CA-01 SECURITY ASSESSMENT AND AUTHORIZATION POLICIES AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=CA-1>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a certification, accreditation, and security assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Security Assessment and Authorization Policy. This document can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.



#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel a certification, accreditation, and security assessment policy that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls.The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating the Security Assessment and Authorization Policy and Procedures annually. The Chief Operating Officer is responsible for approving Security Assessment and Authorization.  All procedures are consistent with requirements of FISMA, FedRAMP, ISO 27001, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## CA-02 SECURITY ASSESSMENTS

> Control description: <http://800-53.govready.com/control?id=CA-2>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

CivicActions will create internally or work with an independent Third Party Auditor to develop a security assessment plan (SAP) when required by FISMA and NIST. Risks identified during the security assessment are tracked in CivicActions' ticket tracking or software control repository system.



#### LINCS specific control or LINCS Responsibility

This will be completed in CY2018.

An independent Third Party Auditor will develop a security assessment plan (SAP) for the LINCS system in support of FISMA and NIST requirements selected by LINCS. Risks identified during the security assessment are tracked in the lincs.ed.gov Github repository. The scope of the assessment includes:

1. Security controls and control enhancements under assessment

2. Assessment procedures to be used to determine security control effectiveness

3. Assessment environment, assessment team, and assessment roles and responsibilities



### Part b)

#### CivicActions Responsibility

All controls assigned and documented in this System Security Plan (SSP) will be tested at least annually or when there is a major change to the system.



#### LINCS specific control or LINCS Responsibility

All controls as assigned by LINCS and documented in this System Security Plan (SSP) will be tested at least annually or when there is a major change to the LINCS system, or as directed by LINCS.



### Part c)

#### LINCS specific control or LINCS Responsibility

An independent Third Party Auditor of the LINCS System will create a Security Assessment Report (SAR) that will be provided to the internal authorizing official and the LINCS authorizing official.



### Part d)

#### LINCS specific control or LINCS Responsibility

CivicActions provides the results from the security control assessment package to the appropriate LINCS authorized official as required. The following security control assessment package includes the following:

* Security Control Matrix

* Privacy Impact Assessment

* E-Authentication

* Contingency Plan

* Configuration Management Plan

* Rules of Behavior

* Incident Response Plan



## CA-03 SYSTEM INTERCONNECTIONS

> Control description: <http://800-53.govready.com/control?id=CA-3>
> 
> 
> 
> Security control type: System Specific Control


#### CivicActions Responsibility

This control is not applicable. CivicActions systems do not have system interconnections. The only communication conducted to CivicActions systems is through the Internet.



## CA-05 PLAN OF ACTION AND MILESTONES

> Control description: <http://800-53.govready.com/control?id=CA-5>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions documents all deficiencies and vulnerabilities identified during the security certification and/or continuous monitoring phase (via security assessment, vulnerability scanning, risk assessment, etc.) within the Plan of Action and Milestones (POA&M).

The POA&M document provides a platform for CivicActions to monitor and track the deficiency and its mitigation strategy. POA&M items will include:

* The description of the deficiency,

* Dedicated point of contact for this deficiency.

* Cost of the mitigation strategy

* Associated risk and NIST control

* Recommended mitigation strategy

POA&Ms are tracked throughout the lifecycle of the system until its mitigation. All POA&Ms are reviewed on a monthly basis by CivicActions Information System Security Officer to ensure all mitigation strategies are continuing as documented.



## CA-06 SECURITY AUTHORIZATION

> Control description: <http://800-53.govready.com/control?id=CA-6>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The Authorizing Official (AO) for LINCS is LINCS' CIO. The AO will authorize the use of LINCS and this authorization will be reviewed and updated every three years or when there is a significant change to the LINCS system. The LINCS security package to be submitted to the AO for authorization include:

* System Security Plan

* LINCS Privacy Impact Assessment (Form)

* Contingency Plan

* Configuration Management Plan

* System Rules of Behavior

* Incident Response Plan

* Minimum Selected Security Controls and Implementation Statements.

* E-Authentication



## CA-07 CONTINUOUS MONITORING

> Control description: <http://800-53.govready.com/control?id=CA-7>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

CivicActions will implemented a continuous monitoring strategy that incorporates configuration management processes including the assessment of security impact analyses of all changes, ongoing security control assessments, and a reporting mechanism of basic information security and privacy effectiveness metrics to designated CivicActions teams.



### Part b)

#### CivicActions Responsibility

Quarterly review of the control assessments supporting the monitoring is conducted by the CivicActions ISSO.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: continuous monitoring for security events’ metrics for AWS monitoring tools.

CivicActions' continuous monitoring for security events metrics will occur in real-time using existing AWS monitoring tools tools.



### Part c)

#### CivicActions / Drupal control support

CivicActions works closely with the Drupal security community and reviews security announcements as part of the continuous monitoring strategy. Items found to require immediate remediation will be addressed.



#### LINCS specific control or LINCS Responsibility

CivicActions will implement an ongoing security control assessment of the LINCS system as part of the continuous monitoring strategy. Items to be found to be not implemented or planned will be documented as POA&M items for remediation.



### Part d)

#### CivicActions Responsibility

CivicActions conducts or oversees continuous system security monitoring.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: ongoing security status monitoring.



### Part e)

#### CivicActions Responsibility

The CivicActions Security Team reviews the results of the security scans and security assessments with associated JIRA and/or Github Issue tickets created to correlate and analyze security related information generated from the monitoring tools becoming POA&M items for tracking.



### Part f)

#### CivicActions Responsibility

POA&M items are tracked by the CivicActions Security team though Github Issue tickets with a Security categorization assigned.  Information included in the POA&M item include the severity, the due date, the weakness source identifier, and the plugin ID that identified the vulnerability.



### Part g)

#### CivicActions Responsibility

The security status of the system is reported up to the CivicActions Security team to be reviewed alongside other security issues relating to CivicActions.



## CA-09 INTERNAL SYSTEM CONNECTIONS

> Control description: <http://800-53.govready.com/control?id=CA-9>
> 
> 
> 
> Security control type: System Specific Control


#### CivicActions Responsibility

Not applicable: There are currently no internal systems that connect to CivicActions systems.



