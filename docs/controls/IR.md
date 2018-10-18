# INCIDENT RESPONSE

## IR-01 INCIDENT RESPONSE POLICY AND PROCEDURES

> Control description: <http://800-53.govready.com/control?id=IR-1>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

The Department of Education developed, documented and disseminated to personnel an incident response policy that addresses purpose, scope, roles, responsibilities, management committment, coordination among organizational entities, and compliance, and developed, documented and disseminated to personnel procedures to facilitate the implementation of the policy and associated controls.The policy is stated in the Office of the Secretary Information Security Policy dated July 17, 2013 and the procedures are defined in the Office of the Secretary Procedures Handbook for Information Security, Version 1.1 dated July 30, 2014. These documents will be reviewed periodically. These policies and procedures are applicable to the LINCS personnel using the lincs.ed.gov information system.

The CivicActions ISSO is responsible for reviewing and updating the Incident Response Plan Policy and Procedures annually. The Chief Operating Officer is responsible for approving Incident Response Plan.  All procedures are consistent with requirements of FISMA, FedRAMP, ISO 27001, applicable executive orders, directives, policies, regulations, standards, and guidance. These policies and procedures are applicable to the CivicActions staff administering the lincs.ed.gov information system.

The DKAN Incident Response (IR) Policy and Procedures can be found in the CivicActions Github repository at <https://github.com/NuCivic/healthdata/wiki/incident-response-plan>.



#### CivicActions Responsibility

CivicActions has developed, documented and disseminated to personnel an incident response policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Incident Response (IR) Policy and Procedure that can be found in the CivicActions Handbook Github repository at <https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan/>



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.



## IR-02 INCIDENT RESPONSE TRAINING

> Control description: <http://800-53.govready.com/control?id=IR-2>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

All CivicActions employees with incident response responsibilities are required to participate in incident response training once the role is assumed within 10 days, as required by LINCS changes, and annually. The CivicActions Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>) is the basis for the training and the incident response workflow created by the Security team.  Upon a review of past incidents, the training is updated to ensure processes and workflows are updated.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident response training.



### Part a)

#### LINCS specific control or LINCS Responsibility

All CivicActions users of the LINCS system with incident response responsibilities are required to participate in incident response training once the role is assumed within 10 days, as required by LINCS changes, and annually. The Incident Response Plan (<https://github.com/NuCivic/healthdata/wiki/incident-response-plan>) is the basis for the training and the incident response workflow created by the Security team. Upon a review of past incidents, the training is updated to ensure processes and workflows are updated.



## IR-04 INCIDENT HANDLING

> Control description: <http://800-53.govready.com/control?id=IR-4>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

The Incident Response Plan (<https://github.com/NuCivic/healthdata/wiki/incident-response-plan>) explains the process for incident handling, and discusses preparation, detection and analysis, containment, eradication, and recovery.

Preparation activities includes all CivicActions and LINCS internal users are trained if their role includes incident response. Detection monitoring tools providing notification to incident response personnel for analysis and action. Containment, eradication and recovery activities include AWS inherited fixes and LINCS system administrators blocking IP address at the source of the incident and clearing caches.



#### CivicActions Responsibility

The Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>) explains the process for incident handling, and discusses preparation, detection and analysis, containment, eradication, and recovery.

Preparation activities includes all CivicActions internal users are trained if their role includes incident response. Detection monitoring tools providing notification to incident response personnel for analysis and action.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident handling.



### Part b)

#### CivicActions Responsibility

The CivicActions Engineering team leads are members of the CivicActions Contingency and Incident Response Plan teams and coordinates activities accordingly through the life of the incident event.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident handling.



### Part c)

#### CivicActions Responsibility

The CivicActions Engineering and Security teams conduct a post-incident analysis to assist in documenting lessons learned and suggesting changes to improve the incident response process. Tickets created in response to the incident event are reviewed upon completion by Engineering and Security teams. Updates considered requiring changes to the Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>) through the team review session for approval.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: incident handling.



## IR-05 INCIDENT MONITORING

> Control description: <http://800-53.govready.com/control?id=IR-5>
> 
> 
> 
> Security control type: Hybrid


#### CivicActions Responsibility

CivicActions utilizes the JIRA ticketing tool for tracking and reporting of incident events from reporting to resolution and post-incident analysis. Initial reporting can come from continuous monitoring tools as well as client and public submissions made to support@civicactions.com. Jira processes the tickets for the public submissions and CivicActions' Support Team creates associated GitHub Issues. Internal incidents reported are processed within the GitHub Issue queue. Details of the handling procedures are included in the CivicActions Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>), section 5.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  incident monitoring of infrastructure and platform.



## IR-06 INCIDENT REPORTING

> Control description: <http://800-53.govready.com/control?id=IR-6>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### CivicActions Responsibility

CivicActions internal personnel, as soon as the incident event is detected and/or communicated, are required to report the incident event to the CivicActions Security team. Methods of detection and/or communication may include one or more of:

* Though continuous monitoring tools (StatusCake, OWASP ZAP, others).

* As a result of application notifications where the CivicActions Security team receives notifications

* Event logging described in AC-2

* Host based alerts from the cloud infrastructure or platform.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  incident reporting.



### Part b)

#### CivicActions Responsibility

CivicActions internal personnel, as soon as the incident event is detected and/or communicated, are required to report the incident event to the CivicActions Security team.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  incident reporting.



## IR-07 INCIDENT RESPONSE ASSISTANCE

> Control description: <http://800-53.govready.com/control?id=IR-7>
> 
> 
> 
> Security control type: Hybrid


#### LINCS specific control or LINCS Responsibility

CivicActions Customer Support team provides first response assistance to any external users of the LINCS system. Response time for external reporting of incidents through e-mail is one business day. Internal users are able to request support thought the same process or initiate the incident response workflow.  Tickets created in the Jira (customer ticketing system) and Github (internal ticketing system) documents all details related to the incident to assist the incident response teams in handling the incident.



## IR-08 INCIDENT RESPONSE PLAN

> Control description: <http://800-53.govready.com/control?id=IR-8>
> 
> 
> 
> Security control type: Hybrid


### Part a)

#### LINCS specific control or LINCS Responsibility

DKAN/LINCS Incident Response Plan (<https://github.com/NuCivic/healthdata/wiki/incident-response-plan>), includes a comprehensive incident response program, which details the implementation of procedures and tools required for incident handling. The incident response program details the roles and responsibilities of CivicActions IR Team. The IR Team includes members from Security, Engineering, and Drupal Engineering teams.  Incident response plays a pivotal role in monitoring, detecting and handling security incidents of the entire information system. The IRP details categorization of incidents in accordance with NIST 800-61 and accordingly documents and reports incidents. The IRP is reviewed annually and updated as needed by ISSO, with the assistance of the incident response team.



#### CivicActions Responsibility

CivicActions Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>), includes a comprehensive incident response program, which details the implementation of procedures and tools required for incident handling. The incident response program details the roles and responsibilities of CivicActions IR Team. The IR Team includes members from Security, Engineering, and Drupal Engineering teams.  Incident response plays a pivotal role in monitoring, detecting and handling security incidents of the entire information system. The IRP details categorization of incidents in accordance with NIST 800-61 and accordingly documents and reports incidents. The IRP is reviewed annually and updated as needed by ISSO, with the assistance of the incident response team.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  incident response plan.



### Part b)

#### LINCS specific control or LINCS Responsibility

The DKAN/LINCS Incident Response Plan (<https://github.com/NuCivic/healthdata/wiki/incident-response-plan>) is stored in the CivicActions Github repository. CivicActions personnel who are a part of the incident response team will have access to the plan in order to review any updates made to the IR Plan, including CivicActions Security, DKAN Engineering, and Engineering teams.



#### CivicActions Responsibility

The CivicActions Incident Response Plan

 (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>)

 is stored in the CivicActions Github repository. CivicActions personnel who are a

 part of the incident response team will have access to the plan in order to review

 any updates made to the IR Plan, including CivicActions Security, DKAN Engineering,

 and Engineering teams.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  incident response plan.



### Part c)

#### LINCS specific control or LINCS Responsibility

The LINCS ISSO and the CivicActions IR team is responsible for reviewing the Incident Response Plan (<https://github.com/NuCivic/healthdata/wiki/incident-response-plan>) annually.  The entire incident response team will sit down and review the plan and update it as necessary. Ultimately, the ISSO has final say and will approve all updates to the plan team.



#### CivicActions Responsibility

The CivicActions CISO and IR team is responsible for reviewing the Incident Response Plan (<https://civicactions-handbook.readthedocs.io/en/latest/09-security/incident-response-plan>) annually.  The entire incident response team will sit down and review the plan and update it as necessary. Ultimately, the CISO has final say and will approve all updates to the plan team.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  incident response plan.



### Part d)

#### CivicActions Responsibility

The CivicActions Security team is responsible for managing the IR Plan, including annual reviews and updates. The IR Plan is updated to reflect any changes to the application system. In addition, any concerns or difficulties encountered during IR Plan implementation, execution, or testing are addressed in an update to the IR Plan.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  incident response plan.



### Part e)

#### LINCS specific control or LINCS Responsibility

Modifications to the IR Plan are conducted by the IR team (CivicActions Security, DKAN Engineering, and Engineering teams) and communicated to the IR team and LINCS designated personnel, including the System Owner and ISSO.



#### CivicActions Responsibility

Modifications to the IR Plan are conducted by the IR team (CivicActions Security, Operations and Engineering teams) and communicated to the IR team and designated personnel, including the System Owner and ISSO.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  incident response plan.



### Part f)

#### CivicActions Responsibility

The IR Plan is available in the CivicActions Github repository. Github provides the configuration management capabilities for the IR Plan to be protected from unauthorized disclosure and modification.



#### Amazon Web Services (AWS) US-East/West control support

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following:  incident response plan.



