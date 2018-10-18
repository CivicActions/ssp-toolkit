# PERSONNEL SECURITY

## PS-01 PERSONNEL SECURITY POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=PS-1>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel a personnel security policy that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls.The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating the Personnel Security Policy and Procedures annually. The Chief Operating Officer is responsible for approving Personnel Security.  All procedures are consistent with requirements of FISMA, FedRAMP, ISO 27001, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system.



#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a personnel security policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in CivicActions Personnel Security (PS) Policy document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## PS-02 POSITION CATEGORIZATION

> Control description: <http://800-53.govready.com/control?id=PS-2>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

Risk designations are assigned to all CivicActions positions. The CivicActions Director of Human Resources works in coordination with the CivicActions ISSO and the Chief Operating Officer to assign risk designations.



### Part b)

#### CivicActions Responsibility

The CivicActions Director of Human Resources works in coordination with the CivicActions ISSO and the Chief Operating Officer to establish screening criteria for all CivicActions positions.



### Part c)

#### CivicActions Responsibility

At least every three (3) years, the CivicActions Director of Human Resources reviews and revises position risk designations. If the Director of Human Resources determines that significant changes must be made to the position risk descriptions the Director of Human Resources works in coordination with the CivicActions ISSO and the Chief Operating Officer to implement changes as required.



## PS-03 PERSONNEL SCREENING

> Control description: <http://800-53.govready.com/control?id=PS-3>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

Prospective CivicActions employees undergo background checks commensurate with the individual’s job duties, the classification of the information they will access, and the risks associated with the role. At the discretion of the Chief Operating Officer these checks may also be conducted on contractors and / or third party users in cases where they will have access to application data that is not meant to be consumed by the public.  In these instances, the Chief Operating Officer will instruct the Director of Human Resources to conduct a background check before granting access to the information system.



### Part b)

#### CivicActions Responsibility

Rescreening is conducted as required by the individual’s job duties, the classification of the information they will access, and the risks associated with the role. A basic background check is performed for all CivicActions employees.



## PS-04 PERSONNEL TERMINATION

> Control description: <http://800-53.govready.com/control?id=PS-4>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

Information system access is terminated immediately upon the voluntary or involuntary departure of an employee. In the case of involuntary departure, in addition to immediate termination of system access, at no point is a departing employee allowed access to any part of the CivicActions infrastructure.

In the case of voluntary departure, employees are permitted access to the information system for the duration of their off boarding period. The departing employee’s manager is responsible for informing the Information Technology department when the employee off boarding period concludes. At this time system and facility access is terminated.



### Part b)

#### CivicActions Responsibility

The terminated user’s accounts are disabled and all access associated with the individual is revoked.



### Part c)

#### CivicActions Responsibility

The Director of Human Resources conducts exit interviews with all employees who leave CivicActions voluntarily. There is a general discussion about the process of turning in any/all company issued devices, laptops, etc.  All of these items are collected before the employee exits CivicActions.  In the case of an involuntary termination, the Director of Human Resources works to collect company issued devices and provides paperwork highlighting confidential protections for customers.



### Part d)

#### CivicActions Responsibility

CivicActions employees provide their own equipment that must be hardened to security reqirements depending upon their role and duties. CivicActions supplies two factor authentication tokens that become the property of the employee. Therefore, this control is not applicable.



### Part f)

#### CivicActions Responsibility

When a person is terminated, a standard process is used to notify management and IT and to track the process of disabling access to the information system/information system components. The CivicActions Help Desk is given at least a four hour notice to schedule the deactivation of access upon termination. Deactivation is a manual process that is tracked via a Trello card in order to meet the four hour turnaround time before termination.



## PS-05 PERSONNEL TRANSFER

> Control description: <http://800-53.govready.com/control?id=PS-5>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

When an employee, third party personnel and / or contractor is transferred to a new project or position within CivicActions, they may maintain access to the previous system they were working on in order to facilitate the process of maintenance and knowledge transfer. However, as part of the practices of account management (AC-02) and least privilege (AC-06), regular audits of privileged users are conducted and access privileges may be removed when no longer needed. Additionally, adherence to specific client SLAs may enhance the frequency of such audits or the timeliness of privilege removal during personnel transfer.



### Part b)

#### CivicActions Responsibility

When an employee, third party personnel and / or contractor is transferred to a new position within CivicActions and there is a requirement for access change, such access changes are normally completed within five business days.



### Part c)

#### CivicActions Responsibility

Access authorizations are modified as needed for the new employee duties based on transfer or reassignment.



### Part d)

#### CivicActions Responsibility

The CivicActions operations team is informed of transfers that require access authorization modifications within five business days by the Project Manager, Product Owner or Director of Human Resources.



## PS-06 ACCESS AGREEMENTS

> Control description: <http://800-53.govready.com/control?id=PS-6>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

LINCS users are required to read and sign access agreements, including acknowledgement signature page for the Acceptable Use Policy (AUP), provided in the Rules of Behavior (RoB) document prior to gaining access to the LINCS. The acknowledgment signature page is a separate document provided within the referenced (RoB) document.



### Part b)

#### LINCS specific control or LINCS Responsibility

Access agreements, including the Acceptable Use Policy, are reviewed at least annually or when a significant change occurs. In the event that a major update is made to the Acceptable Use Policy, employees are required to read and sign the updated policy document and Human Resources stores the information.



### Part c)

#### LINCS specific control or LINCS Responsibility

Prior to gaining access to key systems, LINCS users are required to read and sign access agreements, including the Acceptable Use Policy.

Access agreements, including the Acceptable Use Policy, are reviewed at least annually. This review also takes place when a significant change occurs. In the event that a major update is made to the Acceptable Use Policy, employees are required to meet with the Director of Human Resources to review and sign the revised agreement.



## PS-07 THIRD-PARTY PERSONNEL SECURITY

> Control description: <http://800-53.govready.com/control?id=PS-7>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

Third party personnel are required to following the same process and requirements as LINCS employees. The Chief Operating Officer may also require that a background check be conducted on contractors and / or third party users in cases where they will have access to application data that is not meant to be consumed by the public. In these instances, the Chief Operating Officer will instruct the Director of Human Resources to conduct a background check before granting access to the information system.



#### CivicActions Responsibility

Third party personnel are required to following the same process and requirements as CivicActions employees. The Chief Operating Officer may also require that a background check be conducted on contractors and / or third party users in cases where they will have access to application data that is not meant to be consumed by the public. In these instances, the Chief Operating Officer will instruct the Director of Human Resources to conduct a background check before granting access to the information system.



### Part b)

#### LINCS specific control or LINCS Responsibility

LINCS HR reviews and updates the access agreements annually or whenever there is a significant change to the information system or information being processed; and whenever there is a change to the agreements’ verbiage.



#### CivicActions Responsibility

CivicActions HR reviews and updates the access agreements annually or whenever there is a significant change to the information system or information being processed; and whenever there is a change to the agreements’ verbiage.



### Part c)

#### LINCS specific control or LINCS Responsibility

All personnel security requirements are documented within the SSP and include things such as signing the Acceptable Use Policy (AUP) and taking security awareness training.



#### CivicActions Responsibility

All personnel security requirements are documented and include things such as signing the Acceptable Use Policy (AUP) and taking security awareness training.



### Part d)

#### LINCS specific control or LINCS Responsibility

For personnel transfers and terminations of employees with access to the LINCS systems, third parties must notify the LINCS Director of Human Resources the same day. The Director of Human Resources follows the same employee transfer and/or termination procedure(s) as if the Third Party Personnel were LINCS employees.



#### CivicActions Responsibility

For personnel transfers and terminations of third-party personnel with access to the CivicActions systems, third parties must notify the CivicActions Director of Human Resources the same day. The Director of Human Resources follows the same employee transfer and/or termination procedure(s) as if the Third Party Personnel were CivicActions employees.



### Part e)

#### LINCS specific control or LINCS Responsibility

Compliance measures for assessing third-party personnel and/or contractors are determined on a case-by-case basis. The LINCS ISSO is responsible for coordinating with the Cloud Operations Manager and the Contracts Manager to include appropriate and tailored compliance verification language in contracts as required.  Third-party personnel are continuously monitored to ensure compliance with personnel security requirements.



#### CivicActions Responsibility

Compliance measures for assessing third-party personnel and/or contractors are determined on a case-by-case basis. The CivicActions ISSO is responsible for coordinating with the Contracts Manager and managers of external systems to include appropriate and tailored compliance verification language in contracts as required. Third-party personnel are continuously monitored to ensure compliance with personnel security requirements.



## PS-08 PERSONNEL SANCTIONS

> Control description: <http://800-53.govready.com/control?id=PS-8>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

The Director of Human Resources is responsible for determining and enforcing sanctions for failing to comply with established information security policies and procedures. Coaching may be considered prior to sanctions. Sanctions may include but are not limited to written warnings, reduction in system access, demotion, or termination. Additional details regarding personnel sanctions can be found in the CivicActions 'Discipline Procedures,' an internal document that is available for review onsite or as required for audits and assessments.



### Part b)

#### CivicActions Responsibility

When employee sanctions processes are initiated, the Director of Human Resources notifies the respective supervisor/manager and physical security within five business days.



