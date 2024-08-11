# Personnel Security (PS) Standard (SOP)

*Reviewed and updated 2023-12-20*

----

**Table of Contents**
<!--TOC-->

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Standards](#standards)
  - [PS-01 Personnel Security Policy And Procedures](#ps-01-personnel-security-policy-and-procedures)
  - [PS-02 Position Risk Designation](#ps-02-position-risk-designation)
  - [PS-03 Personnel Screening](#ps-03-personnel-screening)
  - [PS-04 Personnel Termination](#ps-04-personnel-termination)
  - [PS-05 Personnel Transfer](#ps-05-personnel-transfer)
  - [PS-06 Access Agreements](#ps-06-access-agreements)
  - [PS-07 Third-Party Personnel Security](#ps-07-third-party-personnel-security)
  - [PS-08 Personnel Sanctions](#ps-08-personnel-sanctions)

<!--TOC-->

----

## Introduction

### Purpose

The Office of the Chief Information Officer (OCIO) Information Assurance Services (IAS) publication Information  Technology (IT) System Access Controls Standard of February 11, 2022 provides a comprehensive basis for  management across all systems in the Department. This document provides specific guidance as defined and implemented  by the Project.

### Scope

This system has been categorized as a FIPS-199 LOW system, and as such this document applies only to relevant  controls, policies, processes and procedures as defined within the system.

## Standards

### PS-01 Personnel Security Policy And Procedures

The Project documents the security policy and procedures in addressing position categorization, personnel screening, personnel termination, personnel transfer, and access agreements within the Project SSP. Project adopts the Client personnel security standards and determines position risks levels based on public trust responsibilities.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.


The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.


CivicActions has developed, documented and disseminated to personnel a personnel security policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in CivicActions Personnel Security (PS) Policy document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs>.


### PS-02 Position Risk Designation

Project position sensitivity levels are assigned by the Client Full Name. Each position designation is documented on the Standard Position Description (SPD) and assigned a risk level (or sensitivity level) commensurate with the sensitivity of the information, the risk to that information and the system maintaining that information. The levels of risk still need to be designated by Client for employee and contractor positions but since Project system does not have any sensitive data, a low risk scenario can be assumed.

- Employee risk levels and background investigations are: Low Risk= NACI, Moderate Risk= LBI, High Risk= BI.
- Contractor risk levels and background investigations are: Low Risk= NACI, Moderate Risk= NACC, High Risk= BI.

In order to ensure every employee is assigned to a position, which has been reviewed for sensitivity by the NCC, the SPD is a required data attribute of an employee’s HR record. Position risks designations are reviewed and revised when NCC or OPM publish changes to sensitivity levels.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog


**a.**	Risk designations are assigned to all CivicActions positions. The CivicActions Office of Human Resources works in coordination with the CivicActions Security Office to assign risk designations.

**b.**	The CivicActions Office of Human Resources works in coordination with the CivicActions Security Office to establish screening criteria for all CivicActions positions.

**c.**	At least every three (3) years, the CivicActions Office of Human Resources reviews and revises position risk designations. If the Office of Human Resources determines that significant changes must be made to the position risk descriptions the Office of Human Resources works in coordination with the CivicActions Security Office to implement changes as required.

### PS-03 Personnel Screening

Minimum background investigations are conducted, since all data is non-sensitive, for individuals requiring access to Project information and information systems. The type of background investigation conducted for an individual is determined by the individual’s position risk categorization noted in control PS-2. Client conducts periodic reinvestigations in accordance with OPM and NIST guidelines.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.


**a.**	Prospective CivicActions employees undergo background checks commensurate with the individual’s job duties, the classification of the information they will access, and the risks associated with the role. At the discretion of the CivicActions Security Office, these checks may also be conducted on contractors and/or third party users in cases where they will have access to application data that is not meant to be consumed by the public. In these instances, the Security Office will instruct the Office of Human Resources to conduct a background check before granting access to the information system.

**b.**	Rescreening is conducted as required by the individual’s job duties, the classification of the information they will access, and the risks associated with the role. A basic background check is performed for all CivicActions employees.

### PS-04 Personnel Termination

Client Full Name HR policy states that managers or designated officials are responsible for recovering and properly securing employee badges and returning it to the local physical security office. The Client executes termination procedures that remove personnel access privileges, computer accounts. When an employee is terminated, the employee’s manager or designated official completes a form requesting termination of access for the user. Local management and the security manager coordinate disabling or removing Project privileged access with the system administrator. The employee’s manager or designated official is responsible for recovering and properly securing his/her ID badge and returning it to the local physical security office. The employee’s manager or designated official ensures that any information on the system that the employee was responsible for will be available to the appropriate personnel.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.


**a.**	Information system access is terminated immediately upon the voluntary or involuntary departure of an employee. In the case of involuntary departure, in addition to immediate termination of system access, at no point is a departing employee allowed access to any part of the CivicActions infrastructure.
In the case of voluntary departure, employees are permitted access to the information system for the duration of their offboarding period. The departing employee’s manager is responsible for informing the Information Technology department when the employee offboarding period concludes. At this time system and facility, access is terminated.

**b.**	The terminated user’s accounts are disabled and all access associated with the individual is revoked.

**c.**	The employee's manager or the Office of Human Resources conducts exit interviews with all employees who leave CivicActions voluntarily. There is a general discussion about the process of turning in any/all company-issued devices, laptops, etc.

**d.**	CivicActions employees provide their own equipment that must be hardened to security requirements depending upon their roles and duties. CivicActions supplies two-factor authentication tokens that become the property of the employee.
Some employees may receive company-issued hardware for working on particular projects. These items are collected before the employee exits CivicActions. In the case of an involuntary termination, the Office of Human Resources works to collect company-issued devices and provides paperwork highlighting confidential protections for customers.

**e.**	Access to CivicActions information and information systems is always shared so that the termination of an individual will not prevent CivicActions from having access to needed resources.

**f.**	When a person is terminated, a standard off-boarding process is used to notify management and CivicActions' Operations staff, and to track the process of disabling access to the information system/information system components. The CivicActions Operations staff and Security Office are given at least four hours notice to schedule the deactivation of access upon termination. Deactivation is a manual process that is tracked via a Trello card in order to meet the four hour turnaround time before termination.

### PS-05 Personnel Transfer

When an employee is reassigned or transferred, the employee’s manager or designated official is required to request transfer of access (as appropriate) for the user.

In accordance with the Client Full Name HR policy, the employee’s manager or designated official is responsible for recovering and properly securing his/her ID badge and returning it to the local physical security office. The manager provides prompt notification to the Project system/security administrator when an employee changes assignments and/or location. This includes taking prompt and appropriate action to change employee access profile and/or remove employee from the system; and ensure that users’ system access is cancelled when the need no longer exists.

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.


**a.**	When an employee, third party personnel and/or contractor is transferred to a new project or position within CivicActions, they may maintain access to the previous system they were working on in order to facilitate the process of maintenance and knowledge transfer. However, as part of the practices of account management (AC-2) and least privilege (AC-6), regular audits of privileged users are conducted and access privileges may be removed when no longer needed. Additionally, adherence to specific client SLAs may enhance the frequency of such audits or the timeliness of privilege removal during personnel transfer.

**b.**	When an employee, third party personnel and/or contractor is transferred to a new position within CivicActions and there is a requirement for access change, such access changes are normally completed within five business days.

**c.**	Access authorizations are modified as needed to coincide with changes in duties or operational needs upon personnel transfer or reassignment.

**d.**	CivicActions Operations staff is informed of transfers that require access authorization modifications within five business days by the Project Manager, System Owner or Office of Human Resources.

### PS-06 Access Agreements

**a.**	All users of the Project system must read and accept access agreements upon every login.

**b.**	The Access Agreements are reviewed at least annually or when a significant change occurs.

**c.**	All individuals requiring access to the Project system are required to sign the Access Agreements before login is granted. When the Access Agreements are updated, the individual will be required to sign the new copy before regaining access.

### PS-07 Third-Party Personnel Security

**a.**	Personnel security requirements including security roles and responsibilities that apply to primary contracting organizations flow down to their subcontractors.

**b.**	Personnel security policies and procedures that apply to primary contracting organizations flow down to their subcontractors.

**c.**	All personnel security requirements are documented in PS-1 and other related Personnel Security controls.

**d.**	For personnel transfers and terminations of third-party personnel, the procedures defined in employee termination (PS-4) and employee transfer (PS-5) flow down to subcontractors.

**e.**	Compliance measures for assessing third-party personnel and/or contractors are determined on a case-by-case basis. Third-party personnel are monitored to ensure compliance with personnel security requirements.

### PS-08 Personnel Sanctions

The disciplinary sanctions for personnel failing to comply with establish IT security policies and procedures are included in Client Full Name HR policy. If an employee violates the Client information security policies and procedures, the employee may be subject to disciplinary action at the discretion of management. Actions may range from verbal or written warning, removal of system access for a specific period of time, reassignment to other duties, or termination, depending on the severity of the violation. Disciplinary sanctions are reported to the OCIO.


**a.**	The CivicActions Security Office and/or the Office of Human Resources is responsible for determining and enforcing sanctions for failing to comply with established information security policies and procedures. Coaching may be considered prior to sanctions. Sanctions may include but are not limited to written warnings, reduction in system access, demotion, or termination.

**b.**	When employee sanctions processes are initiated, the Office of Human Resources notifies the respective Project Manager(s) and CivicActions' Security Office within five business days.
