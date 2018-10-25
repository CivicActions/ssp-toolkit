# CONTINGENCY PLANNING

## CP-01 CONTINGENCY PLANNING POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=CP-1>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel a contingency planning policy that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls. The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating the Contingency Planning Policy and Procedures annually. The Chief Operating Officer is responsible for approving Contingency Planning.  All procedures are consistent with requirements of FISMA, FedRAMP, ISO 27001, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system.



#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel a contingency planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in Contingency Planning (CP) Policy and Procedure that  can be found in the CivicActions Github repository at <https://github.com/NuCivic/healthdata/wiki/contingency-plan> also: <https://github.com/NuCivic/healthdata/wiki/contingency-plan-word>



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Providers dated 1 May 2013.



## CP-02 CONTINGENCY PLAN

> Control description: <http://800-53.govready.com/control?id=CP-2>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  contingency plan.



### Part b)

#### LINCS specific control or LINCS Responsibility

An Information System Contingency Plan (ISCP) (<https://github.com/NuCivic/healthdata/wiki/contingency-plan>) has been developed and is maintained for the LINCS system. The CivicActions ISSO details the following elements that are critical for a successful recovery and resumption of operations in the event of a contingency scenario:

1. Essential missions, business functions and associated contingency requirements

2. Recovery objectives, restoration priorities, and metrics

3. Roles and responsibilities are identified in Section 2.3 of the CP and includes the ISCP Director (ISCPD), ISCP Coordinator (ISCPC), CivicActions ISCP Coordinator (GD_CPC), CivicActions System Administrator, AWS CP Coordinator (AWS_CPC), and Information System Security Officer (ISSO).

4. Maintaining essential missions and business functions despite an information system disruption, compromise, or failure

5. Full information system restoration without deterioration of the security safeguards originally planned and implemented

6. The ISCP is reviewed and approved by ISCP Director (ISCPD), ISCP Coordinator (ISCPC), CivicActions ISCP Coordinator (GD_CPC)and system owner annually.



#### LINCS specific control or LINCS Responsibility

ISCP Coordinator (ISCPC) distributes the CP plan to all members who have roles in Contingency Planning and Incident Response team. Direction by the System Owner will updated who is required to receive a copy of the contingency plan.



### Part c)

#### CivicActions Responsibility

The Information System Contingency Plan (ISCP) is closely integrated with the Incident Response Plan (IRP). Coordination is the responsibility of the ISCP Director and IRP Director.



### Part d)

#### CivicActions Responsibility

The ISCP Director and CivicActions Security Team are responsible to review the ISCP annually and when a change to the system occurs.



### Part e)

#### CivicActions Responsibility

The CivicActions and ISCP Director are required to update the ISCP to address changes to the organization, information system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing.



### Part f)

#### CivicActions Responsibility

The ISCP requires that changes to the plan be communicated to those on the Contingency Plan Contact List (Appendix A).



### Part g)

#### CivicActions Responsibility

The ISCP is available on CivicActions Github repository.  This repository provides the configuration management capabilities for the ISCP to be protected from unauthorized disclosure and modification.



## CP-03 CONTINGENCY TRAINING

> Control description: <http://800-53.govready.com/control?id=CP-3>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

The ISCP stipulates that all CivicActions system assigned roles in the Contingency Plan Team are trained in their duties within three months of first being assigned a role in the CP, and then annually thereafter or when changes are required. CivicActions uses the Contingency Plan as described in controls CP-1 and CP-2 as a basis for personnel contingency training.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: contingency plan training.



## CP-04 CONTINGENCY PLAN TESTING

> Control description: <http://800-53.govready.com/control?id=CP-4>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

Real world tests of the contingency plan will be held at least annually, with supplemental tests (checklist/table-top) as needed for specific scenarios. The ISCP Coordinator is responsible to facilitate annual testing exercises. The testing process for the CP includes review of the CP exercise and identification of corrective actions and other improvements.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: contingency plan testing.



## CP-06 ALTERNATE STORAGE SITE

> Control description: <http://800-53.govready.com/control?id=CP-6>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  alternate storage site in conjunction with their IaaS provider, AWS.



## CP-06 (1) SEPARATION FROM PRIMARY SITE

> Control description: <http://800-53.govready.com/control?id=CP-6>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: alternate storage site separation from primary site in conjunction with their IaaS provider, AWS.



## CP-09 INFORMATION SYSTEM BACKUP

> Control description: <http://800-53.govready.com/control?id=CP-9>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

CivicActions conducts system user-level information backup in accordance with requirements (at a minimum, incremental backups must be conducted at least weekly and full backups must be conducted at least monthly).



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: user level backup requirements.

AWS functionally makes full backups completed daily and incremental backups in real time.  In addition, transactional logging is conducted by AWS in real time.



### Part b)

#### CivicActions Responsibility

System level information for the application is replicated and backed up in the same way as user-level information – see Part (a) above.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: system level backup requirements.



### Part c)

#### CivicActions Responsibility

System documentation is backed up from the Git repository on a daily basis with a minimum two-week retention period and off-site storage.



### Part d)

#### CivicActions Responsibility

CivicActions employees must authenticate prior to being granted access to the Github repository. Roles and responsibilities within Github determine the proper level of access for the documentation being accessed. The folder structure of Github protects though permissions and ownership prohibiting users from accessing unauthorized documentation.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: protection of the confidentiality, integrity, and availability of backup information at storage locations in conjunction with AWS.



## CP-10 INFORMATION SYSTEM RECOVERY AND RECONSTITUTION

> Control description: <http://800-53.govready.com/control?id=CP-10>
> 
> 
> 
> Security control type: Inherited (Cloud Service Provider)


#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: information system recovery and reconstitution.



