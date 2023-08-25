# Reusable OpenControl Components (SSP-Toolkit).

## PL: Planning

### PL-1: Security Planning Policy And Procedures

```text
 - a. Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
   - 1. [Selection (one or more): organization-level, mission/business process-level, system-level] planning policy that:
     - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
     - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
   - 2. Procedures to facilitate the implementation of the planning policy and the associated planning controls;
 - b. Designate an [Assignment: organization-defined official] to manage the development, documentation, and dissemination of the planning policy and procedures; and
 - c. Review and update the current planning:
   - 1. Policy [Assignment: organization-defined frequency] and following [Assignment: organization-defined events]; and
   - 2. Procedures [Assignment: organization-defined frequency] and following [Assignment: organization-defined events].

```
**Status:** In Place


##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud Service Provider dated 1 May 2013.




##### Contractor

CivicActions has developed, documented and disseminated to personnel a system planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and procedures to facilitate the implementation of the policy and associated controls. This information is maintained in the CivicActions Planning (PL) Policy and Procedure document that can be found in the CivicActions GitHub repository at <https://github.com/CivicActions/compliance-docs/>.




##### Project

This is Agency common control. More data about implementation can be obtained from the Agency common control catalog.

The Project developed its security policy planning and procedures based on None, guidance from NIST, the Office of Management and Budget and industry best practices. Security policies and procedures are formally documented within the Project SSP, which provides the roles and responsibilities as it pertains to security planning. It provides guidance on all aspects of security for the protection of Project information technology resources. It defines responsibilities for the implementation and oversight of the guidance contained herein. The plan was last updated in December, 2015.


### PL-2: System Security Plan

```text
 - a. Develop security and privacy plans for the system that:
   - 1. Are consistent with the organization’s enterprise architecture;
   - 2. Explicitly define the constituent system components;
   - 3. Describe the operational context of the system in terms of mission and business processes;
   - 4. Identify the individuals that fulfill system roles and responsibilities;
   - 5. Identify the information types processed, stored, and transmitted by the system;
   - 6. Provide the security categorization of the system, including supporting rationale;
   - 7. Describe any specific threats to the system that are of concern to the organization;
   - 8. Provide the results of a privacy risk assessment for systems processing personally identifiable information;
   - 9. Describe the operational environment for the system and any dependencies on or connections to other systems or system components;
   - 10. Provide an overview of the security and privacy requirements for the system;
   - 11. Identify any relevant control baselines or overlays, if applicable;
   - 12. Describe the controls in place or planned for meeting the security and privacy requirements, including a rationale for any tailoring decisions;
   - 13. Include risk determinations for security and privacy architecture and design decisions;
   - 14. Include security- and privacy-related activities affecting the system that require planning and coordination with [Assignment: organization-defined individuals or groups]; and
   - 15. Are reviewed and approved by the authorizing official or designated representative prior to plan implementation.
 - b. Distribute copies of the plans and communicate subsequent changes to the plans to [Assignment: organization-defined personnel or roles];
 - c. Review the plans [Assignment: organization-defined frequency];
 - d. Update the plans to address changes to the system and environment of operation or problems identified during plan implementation or control assessments; and
 - e. Protect the plans from unauthorized disclosure and modification.

```
**Status:** In Place


##### AWS

The system partially inherits this control from the FedRAMP Provisional ATO granted to the AWS Cloud dated 1 May 2013 for the following: AWS system security plan.




##### Project

The System Security Plan (SSP) was developed and implemented for Project system in accordance with None, NIST SP 800-18 and NIST SP 800-37. The SSP includes a description of the management, operational, and technical controls in place or planned for the application. The SSP is included as a key document in an application’s C&A package and is reviewed and approved by designated officials. The SSP identifies the system owner and responsible parties for managing system access and the overall security of the system. The Chief Information Security Officer reviews and approves the SSP. The SSP will be reviewed at least annually and updated to account for any changes to the Project system and to address any changes in security controls.


#### a

##### Contractor

CivicActions has developed this system security plan (SSP) for the information system as part of compliance with NIST 800-53 and FIPS 199. The SSP defines the security categorization, system boundary, and security requirements and controls meeting the requirements of the NIST Risk Management Framework (RMF). Specifically the SSP:

1. Is consistent with the organization’s enterprise architecture
2. Explicitly defines the authorization boundary for the system
3. Describes the operational context of the information system in terms of missions and business processes
4. Provides the security categorization of the information system including supporting rationale
5. Describes the operational environment for the information system and relationships with or connections to other information systems
6. Provides an overview of the security requirements for the system
7. Identifies any relevant overlays, if applicable
8. Describes the security controls in place or planned for meeting those requirements including a rationale for the tailoring decisions
9. Is reviewed and approved by the authorizing official or designated representative prior to plan implementation


#### b

##### Contractor

The SSP is reviewed and approved by the authorizing official prior to plan implementation. A copy of the SSP is provided to authorized CivicActions and assessing personnel including the System Owner, Authorizing Official, Information System Security Officer, System/Network Administrator, and the CivicActions Operations staff. The SSP is maintained by the CivicActions Security Office.


#### c

##### Contractor

The SSP is reviewed at least annually by the System Owner and the CivicActions Operations staff in collaboration with the CivicActions Security Office.


#### d

##### Contractor

The CivicActions Operations staff in collaboration with the CivicActions Security Office updates the system description and control descriptions within the SSP as needed to verify the SSP is an accurate description of the system.


#### e

##### Contractor

The SSP is currently available to authorized users on GitLab. Per the Acceptable Use Policy, all entities granted access to CivicActions information assets are required to complete a non-disclosure agreement (NDA) to uphold information confidentiality. GitLab provides the configuration management capabilities for the SSP to be protected from unauthorized disclosure and modification.


### PL-4: Rules Of Behavior

```text
 - a. Establish and provide to individuals requiring access to the system, the rules that describe their responsibilities and expected behavior for information and system usage, security, and privacy;
 - b. Receive a documented acknowledgment from such individuals, indicating that they have read, understand, and agree to abide by the rules of behavior, before authorizing access to information and the system;
 - c. Review and update the rules of behavior [Assignment: organization-defined frequency]; and
 - d. Require individuals who have acknowledged a previous version of the rules of behavior to read and re-acknowledge [Selection (one or more): [Assignment: organization-defined frequency], when the rules are revised or updated].

```
**Status:** complete
#### a

##### Contractor

CivicActions has created and made readily available to individuals requiring access to the information system the rules that describe their responsibilities and expected behavior with regard to information and information system usage. These rules, defined as the Acceptable Use Policy, are included in the CivicActions Security Policy accessible here: <https://guidebook.civicactions.com/en/latest/company-policies/security/#acceptable-use-policy> which has also been uploaded to CSAM as ''Appendix J1 - System Rules of Behavior - Privileged User'' (CivicActions Security Policy 20190226.docx).'


#### a

##### Project

Project has created and made readily available to individuals requiring access to the information system the rules that describes their responsibilities and expected behavior with regard to information and information system usage. These rules are captured in ‘Appendix J2 - System Rules of Behavior - General User’ (ProjectSystemRoB2019-template.docx).

Project has reviewed and accepted as a superset alternative the CivicActions Acceptable Use Policy.


#### b

##### Contractor

CivicActions HR receives a signed acknowledgment from all employees, indicating that they have read, understand, and agree to abide by the rules of behavior, before authorizing access to information and the information system. The text of the electronically signed (via DocuSign) acknowledgment document has been uploaded to CSAM as artifact: ''CivicActions Security Policy Acknowledgement.docx''


#### b

##### Project

The Project System Owner receives a signed acknowledgment from such individuals that are not CivicActions employees, indicating that they have read, understand, and agree to abide by the rules of behavior, before authorizing access to information and the information system.


#### c

##### Contractor

CivicActions reviews the CivicActions Security Policy at least annually and updates as required.


#### c

##### Project

Project reviews the Rules of Behavior at least annually and updates it as required.


#### d

##### Contractor

CivicActions requires individuals who have signed a previous version of the CivicActions Security Policy to read and re-sign when any part of it, including the Acceptable Use Policy/Rules of Behavior, is revised/updated.


#### d

##### Project

Project requires individuals who have signed a previous version of the rules of behavior to read and re-sign when the Rules of Behavior are revised/updated.
