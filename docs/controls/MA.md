# MAINTENANCE

## MA-01 SYSTEM MAINTENANCE POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=MA-1>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel a system maintenance policy that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls.The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating the Maintenance Policy and Procedures annually. The Chief Operating Officer is responsible for approving Maintenance. All procedures are consistent with requirements of FISMA, FedRAMP, ISO 27001, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system.



#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a system maintenance policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in in the CivicActions Maintenance (MA) Policy and Procedure document that can be found in the CivicActions Github repository at <https://github.com/CivicActions/compliance-docs>.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## MA-02 CONTROLLED MAINTENANCE

> Control description: <http://800-53.govready.com/control?id=MA-2>
> 
> 
> 
> Security control type: Hybrid


#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  maintenance performed on the physical components in conjunction with their IaaS provider, AWS.



## MA-04 NON-LOCAL MAINTENANCE

> Control description: <http://800-53.govready.com/control?id=MA-4>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

CivicActions directly manages and controls all maintenance activities pertaining to the software components of the LINCS system, including DKAN, Drupal Core, and Drupal Modules. All maintenance is nonlocal to the LINCS system. Approval, QA, and monitoring is conducted by the team the specific maintenance is being performed.  Github tickets are assigned, QA, approved, and monitored by the DKAN Product Engineering team and DKAN team for the software components of the LINCS system before being ultimately approved by the Change Control Board.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: nonlocal maintenance.



### Part b)

#### LINCS specific control or LINCS Responsibility

CivicActions directly manages and controls all maintenance activities pertaining to the software components of the LINCS system, including DKAN, Drupal Core, and Drupal Modules. All maintenance is nonlocal to the LINCS system. Approval, QA, and monitoring is conducted by the team the specific maintenance is being performed. JIRA tickets are assigned, QA, approved, and monitored by the DKAN Product Engineering team and DKAN team for the software components of the LINCS system. For any nonlocal maintenance requires the same authentication requirements to perform the maintenance activities as to access the LINCS system as defined in controls AC-3 and IA-2.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  nonlocal maintenance.



### Part c)

#### LINCS specific control or LINCS Responsibility

All nonlocal maintenance requires the same authentication requirements to perform the maintenance activities as to access the LINCS system as defined in controls AC-3 and IA-2.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  nonlocal maintenance.



### Part d)

#### LINCS specific control or LINCS Responsibility

CivicActions records for nonlocal maintenance is conducted through the Github ticketing system tool as well as normal system logs. Github tickets are assigned, QA, approved, and monitored by the DKAN Product Engineering team and DKAN team for the software components of the LINCS system. Any CivicActions administrator activity to the LINCS system is also logged though the implementation of the AU-2 (Audit Events) and AU-3 (Content of Audit Records).



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  nonlocal maintenance 



### Part e)

#### LINCS specific control or LINCS Responsibility

Any session for internal LINCS maintenance activities are terminated when the user completes their session, disconnects from the LINCS system, or logs out form the LINCS system.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  nonlocal maintenance.



## MA-05 MAINTENANCE PERSONNEL

> Control description: <http://800-53.govready.com/control?id=MA-5>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

Non-local maintenance on the LINCS system and applications can only be performed by personnel designated as having LINCS internal administrator privileges and responsibilities.  Access rights for the LINCS internal administrators are assigned and granted access to perform their specific job responsibilities. All local maintenance requirements are inherited from AWS.



#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: maintenance personnel for the physical components in conjunction with their IaaS provider, AWS.



