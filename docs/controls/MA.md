# MAINTENANCE

## MA-01 SYSTEM MAINTENANCE POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=MA-1>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

System maintenance policy and procedures are formally documented in the LINCS SSP, which provides the roles and responsibilities as it pertains to software and systems maintennance and updates. The LINCS Technology Project ensures that maintenance controls are developed, disseminated, reviewed, and updated as necessary.

Physical and environmental protection is fully inherited from the AWS FedRAMP certified us-east cloud.

Additional information is contained within the Department of Education, Handbook for Information Assurance Security Policy (Handbook OCIO-01).

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.



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


#### LINCS specific control or LINCS Responsibility

The LINCS Technology Project schedules, performs, and documents regular maintenance on the software components of all systems, including but not limited to:

* Hourly automated snapshot backups

* Daily disaster recovery remote backups

* Daily Intrusion Detection (OSSEC) / Data Integrity Assurance (AIDE)

* As needed HelpDesk support

* Twice-monthly OS updates/patches



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: controlled maintenance.



## MA-04 NON-LOCAL MAINTENANCE

> Control description: <http://800-53.govready.com/control?id=MA-4>
> 
> 
> 
> Security control type: Hybrid


#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: non-local maintenance.



### Part a)

#### CivicActions Responsibility

System maintenance is done from remote sites as there is no direct access to the server instances in the AWS cloud; this is the government-approved method of doing business. Approval, QA, and monitoring is conducted by the team performing the specific maintenance.



### Part b)

#### CivicActions Responsibility

Remote diagnostic tools, such as OSSEC, AIDE, fail2ban and OpenSCAP are used to verify the integrity of files, perform log analysis, monitor login attempts and check for root kits and other vulnerabilies.



### Part c)

#### CivicActions Responsibility

All nonlocal maintenance requires the same authentication requirements to perform the maintenance activities as to access the system as defined in controls AC-3 and IA-2. SSH is used to secure all communications between the remote user and the components located in the AWS cloud.



### Part d)

#### CivicActions Responsibility

CivicActions records for nonlocal maintenance is managed through JIRA tickets and the Git issue queue as well as normal system logs. CivicActions administrator activity to the system is also logged though the implementation of the AU-2 (Audit Events) and AU-3 (Content of Audit Records).



### Part e)

#### CivicActions Responsibility

Any session for internal maintenance activities is terminated when the user completes their session, disconnects from the system, or logs out. In addition, sessions are terminated after 15 minutes of inactivity.



## MA-05 MAINTENANCE PERSONNEL

> Control description: <http://800-53.govready.com/control?id=MA-5>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The Department maintains a list of authorized contract (CivicActions) personnel who perform maintenance and repair activities on the LINCS Technology Project system components, and only these authorized personnel may perform the maintenance. All maintenance personnel have the required personnel security elements in place.



#### CivicActions Responsibility

Maintenance on the system and applications can only be performed by personnel designated as having internal administrator privileges and responsibilities.  Access rights for the internal administrators are assigned and granted access to perform their specific job responsibilities. All physical maintenance requirements are inherited from AWS.



#### Amazon Web Services (AWS) US-East/West control support

The system inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: maintenance personnel.



