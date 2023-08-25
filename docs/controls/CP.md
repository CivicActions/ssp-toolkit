# Reusable OpenControl Components (SSP-Toolkit).

## CP: Contingency Planning

### CP-1: Contingency Planning Policy And Procedures

```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] contingency planning policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the contingency planning policy and the associated contingency planning controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the contingency planning policy and procedures; and
 - c. Review and update the current contingency planning:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete


##### Contractor

CivicActions has developed, documented and disseminated to personnel a contingency planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in Contingency Planning (CP) Policy and Procedure that can be found in the CivicActions Compliance Docs GitHub repository at <https://github.com/CivicActions/compliance-docs>.




##### Project

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

The Project and has developed a contingency planning policy consistent with NIST 800-34. Contingency planning procedures are formally documented within the Project Contingency Plan, which provides the roles and responsibilities as it pertains to contingency planning. The Project reviews and updates the policy as necessary and the policy was last updated in July 2012.


### CP-2: Contingency Plan

```text
 - a. Develop a contingency plan for the system that:
   - 1. Identifies essential mission and business functions and associated contingency requirements;
   - 2. Provides recovery objectives, restoration priorities, and metrics;
   - 3. Addresses contingency roles, responsibilities, assigned individuals with contact information;
   - 4. Addresses maintaining essential mission and business functions despite a system disruption, compromise, or failure;
   - 5. Addresses eventual, full system restoration without deterioration of the controls originally planned and implemented;
   - 6. Addresses the sharing of contingency information; and
   - 7. Is reviewed and approved by [Assignment: organization-defined personnel or roles];
 - b. Distribute copies of the contingency plan to [Assignment: organization-defined key contingency personnel (identified by name and/or by role) and organizational elements];
 - c. Coordinate contingency planning activities with incident handling activities;
 - d. Review the contingency plan for the system [Assignment: organization-defined frequency];
 - e. Update the contingency plan to address changes to the organization, system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing;
 - f. Communicate contingency plan changes to [Assignment: organization-defined key contingency personnel (identified by name and/or by role) and organizational elements];
 - g. Incorporate lessons learned from contingency plan testing, training, or actual contingency activities into contingency testing and training; and
 - h. Protect the contingency plan from unauthorized disclosure and modification.

```
**Status:** complete
#### a

##### Contractor

CivicActions has developed a contingency plan for that addresses:
1. Essential missions, business functions, and associated contingency requirements
2. Recovery objectives, restoration priorities, and metrics
3. Roles and responsibilities are identified in the CP and include the ISCP Director, Incident Commander (IC), CivicActions Coordinator, and CivicActions Information System Security Officer (ISSO).
4. Maintaining essential missions and business functions despite an information system disruption, compromise, or failure
5. Full information system restoration without deterioration of the security safeguards originally planned and implemented
6. The ISCP is reviewed and approved by ISCP Director, Incident Commander (IC), CivicActions ISSO and the System Owner annually.


#### b

##### Contractor

The CivicActions Information System Contingency Plan (ISCP) has been distributed to all CivicActions team members. The ISCP can be found in the CivicActions Handbook at <https://guidebook.civicactions.com/en/latest/common-practices-tools/security/contingency-plan/>.


#### b

##### Project

The Project Information System Contingency Plan (ISCP) has been distributed to all members who have roles in Contingency Planning and Incident Response Team. Direction by the System Owner will update who is required to receive a copy of the contingency plan. The ISCP can be found in the Project GitHub wiki at <https://guidebook.civicactions.com/en/latest/common-practices-tools/security/contingency-plan/>.


#### c

##### Contractor

The Information System Contingency Plan (ISCP) is closely integrated with the Incident Response Plan (IRP). Coordination is the responsibility of the ISCP Director and CivicActions Operations staff.


#### d

##### Contractor

The ISCP Director and CivicActions' Security Office are responsible to review the ISCP annually and when a change to the system occurs.


#### e

##### Contractor

CivicActions Operations staff and ISCP Director are required to update the ISCP to address changes to the organization, information system, or environment of operation and problems encountered during contingency plan implementation, execution, or testing.


#### f

##### Contractor

The ISCP requires that changes to the plan be communicated to those on the Incident Response/Contingency Plan Contact List.


#### g

##### Contractor

The ISCP is available on CivicActions GitHub repository. This repository provides the configuration management capabilities for the ISCP to be protected from unauthorized disclosure and modification.


### CP-3: Contingency Training

```text
 - a. Provide contingency training to system users consistent with assigned roles and responsibilities:
   - 1. Within [Assignment: organization-defined time period] of assuming a contingency role or responsibility;
   - 2. When required by system changes; and
   - 3. [Assignment: organization-defined frequency] thereafter; and
 - b. Review and update contingency training content [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** complete


##### Contractor

The ISCP stipulates that all CivicActions system assigned roles in the Contingency Plan Team are trained in their duties within three months of first being assigned a role in the CP, and then annually thereafter or when changes are required. CivicActions uses the Contingency Plan as described in controls CP-1 and CP-2 as a basis for personnel contingency training.


### CP-4: Contingency Plan Testing

```text
 - a. Test the contingency plan for the system [Assignment: organization-defined frequency] using  the following tests to determine the effectiveness of the plan and the readiness to execute the plan: [Assignment: organization-defined tests].
 - b. Review the contingency plan test results; and
 - c. Initiate corrective actions, if needed.

```
**Status:** complete


##### Contractor

Real-world tests of the contingency plan will be held at least annually, with supplemental tests (checklist/table-top) as needed for specific scenarios. The ISCP Coordinator is responsible to facilitate annual testing exercises. The testing process for the ISCP includes a review of the ISCP, exercise, and identification of corrective actions and other improvements.


### CP-9: Information System Backup

```text
 - a. Conduct backups of user-level information contained in [Assignment: organization-defined system components]
                  [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives];
 - b. Conduct backups of system-level information contained in the system [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives];
 - c. Conduct backups of system documentation, including security- and privacy-related documentation [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives]; and
 - d. Protect the confidentiality, integrity, and availability of backup information.

```
**Status:** partial
#### a

##### AWS

In this architecture, user data is limited to that which is stored in the Amazon RDS database. Amazon RDS is fully backed up by a daily snapshot as well as through transaction logging conducted by AWS as part of this managed service. Full database recovery from snapshot or point-in-time can be initiated from the Amazon RDS console/API.


#### a

##### Contractor

CivicActions conducts system user-level information backup in accordance with requirements (at a minimum, incremental backups must be conducted at least weekly and full backups must be conducted at least monthly).


#### b

##### AWS

AWS built-in features automatically backs up system-level information limited to infrastructure CONFIGURATION information within the AWS account. While individual running Amazon EC2 instances and attached EBS volumes are NOT backed up, they can be reconstituted from Amazon Machine Images (AMIs) provided by AWS (which are backed up by AWS) and user data scripts included in CloudFormation templates. Once deployed, the CloudFormation template contents are backed up by AWS R488within the CloudFormation service. These AWS backups of AWS services are transparent to the customer as part of AWS backend processes.


#### b

##### Contractor

System-level information for the application is replicated and backed up in the same way as user-level information as defined in CP-9(a).


#### c

##### AWS

AWS built-in features back up online administrator and developer documentation, limited to that which is published at https://aws.amazon.com/documentation.


#### c

##### Contractor

System documentation is backed up from the GitHub repository on a daily basis with a minimum two-week retention period and off-site storage.


#### d

##### AWS

AWS built-in features protect the confidentiality, integrity, and availability of information that AWS services back up. This information includes the service configuration information within an account, AWS online administrator and developer documentation, and AWS CloudFormation stacks for templates once deployed into an account. R612


#### d

##### Contractor

CivicActions employees must authenticate prior to being granted access to the GitHub repository. Roles and responsibilities within GitHub determine the proper level of access for the documentation being accessed. The folder structure of GitHub protects though permissions and ownership prohibiting users from accessing unauthorized documentation.


### CP-10: Information System Recovery And Reconstitution

```text
Provide for the recovery and reconstitution of the system to a known state within [Assignment: organization-defined time period consistent with recovery time and recovery point objectives] after a disruption, compromise, or failure.

```
**Status:** complete


##### Contractor

The Contingency Plan documents the mechanisms with supporting procedures that allow all system components to be recovered and reconstituted to the system’s original state after a disruption or failure. This original state means that all system parameters (either default or organization- established) are reset, patches are reinstalled, system and security configuration settings are reestablished, system documentation and operating procedures are available, application and system software is reinstalled, information from the most recent backups is available and the system is fully tested.
