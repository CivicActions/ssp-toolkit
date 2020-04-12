# Project Security Incident Response Procedures

## Contents
<!--TOC-->

- [Overview](#overview)
- [Response process](#response-process)
  - [Initiate](#initiate)
  - [Assess](#assess)
  - [Remediate](#remediate)
  - [Retrospect](#retrospect)
- [Incident Severities](#incident-severities)
  - [1 - High Severity](#1---high-severity)
  - [2 - Medium Severity](#2---medium-severity)
  - [3 - Low Severity](#3---low-severity)

<!--TOC-->

----

## Overview

This document outlines the CivicActions Incident Response Team's process for responding to Project security incidents and other system disruptions. It outlines roles and responsibilities during and after incidents, and it outlines the steps for resolution.

- For incident responders, see the [IRP checklist](security-irp-checklist.md). It is a short, actionable companion to this guide.*

At a high level, incident response follows this process:

[Initiate](#initiate):

- The _incident reporter_ (a Client or CivicActions team member) notices and reports a Project related incident to the CivicActions Incident Response Team:
  1. Slack: [#None](None) using `@channel`
  1. Email: TheProject@example.com
  1. [CivicActions/Project contacts](None)
- The first responder on the Incident Response Team, which could be the reporter if the reporter is on the team, assumes the **Incident Commander (IC)** role.

[Assess](#assess):

- The IC forms a team of _responders_ to determine whether the event is a security incident. _Note that some apparent outages can be triggered by [external dependencies as listed in the contingency plan](contingency-plan.md#external-dependencies)._

  - If the incident is confirmed:
    - The team [assesses the severity](#incident-severities).
    - The IC creates an initial situation report, called a _sitrep_, in a [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident).
    - The IC assesses whether to activate the [contingency plan](contingency-plan.md) for disaster recovery.
  - If the incident is determined to be a false alarm, the IC follows the notification procedure for false alarms.

[Remediate](#remediate):

- If suspicious activity is suspected or other unanswered questions exist:
  - Make [CPM snapshots](https://cpm.project.com/) of relevant volumes.
  - Preserve logs.
  - Take screen captures of anomalous activity that can be used in post-remediation forensic analysis. _Do this before making any changes._
- The responders work to contain and remediate the issue. Timelines vary based on the assessed severity.
- The IC coordinates, communicates, and tracks incident investigation and remediation.
- If appropriate, the IC coordinates with the Product Owner (PO) to notify affected customers.

[Retrospect](#retrospective):

- The responding team holds a retrospective to analyze the incident, capture follow-ups and lessons learned, and write a formal report.

During this process, the team communicates in the following places:

- **JIRA ticket**: Situation updates, investigation notes, and other relevant information gets captured in the [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident) created to track this event.
- **Slack**: Real-time communication happens in the Slack channel [#None](None).
- **Other**: If needed, the team may use Zoom, Google Hangouts, and/or Google Docs to share information not appropriate for Slack (PII, etc.).

For full details, read on.

## Response process

### Initiate

An incident begins when someone becomes aware of a potential incident. We define "incident" broadly, following [_NIST SP 800-61: Computer Security Incident Handling Guide_](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf), as "a violation or imminent threat of violation of computer security policies, acceptable use policies, or standard security practices". This is a deliberately broad definition, designed to encompass any scenario that might threaten the security of Project. For more, see: [What is an incident?](http://civicactions-handbook.readthedocs.io/en/latest/09-security/incidents/#what-is-an-incident)

When a person (the _reporter_) notices what appears to be a Project-related incident, they should check the Slack channel [#None](None) to see if this may be expected behavior (e.g., expected system downtime during a maintenance window), and if necessary, alert the on-call system administrators by email TheProject@example.com. If there is no acknowledgment from the Incident Response Team within 10 minutes, the reporter should escalate the issue by contacting the None directly until receiving acknowledgment of the report.

The first participant on the CivicActions Incident Response Team is the _reporter_, who is also the initial _Incident Commander_ (IC). The IC does the following:

- Carries out the next steps in the incident response process.
- Focuses on coordination, not necessarily investigation.
- Ensures that the incident response process is followed.
- Supports the reporter if the reporter already started the process, or starts the process.
- Remains IC throughout the process, or hands off IC duties later in the process.

#### Communications during the Initiate phase

Note that at this point the event status is "investigating". The issue has not been confirmed yet, so it should be called an "event". When it has been confirmed, it becomes an "incident".

To help with reporting, copy the following template into Slack or an email to create the issue:

``` markdown
[Short description of the event and its impact]

- **Status**: investigating
- **Severity**: unknown
- **Reporter**: [name of the person who reported the issue]
- **IC**: [your name]
- **Responders**: [names of other responders]

[Any extra details about the issue can go here.]
```

The IC is responsible for keeping this issue updated as investigation and remediation progresses. _Responders_ should add comments to the make notes on the issue.

- The IC may use Zoom, Google Hangouts, and/or Google Docs so that responders can share sensitive information not suitable for sharing in a [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident) or Slack.

### Assess

The next step is to assess the event. We need to answer two questions:

- Is this an incident? Did the thing we suspect happen actually happen?
- If so, how severe is it? This determines the response.
- Could the event have been triggered by an [external dependency](contingency-plan.md#external-dependencies)?

To answer these questions, the IC should form an Incident Response Team using Slack Direct Messages. The Incident Response Team should work to confirm the event and assess its impact.

If the event is determined to be a false alarm, the IC should update the ticket, set the status to "false alarm", and close the ticket.

If the event is confirmed as an incident, the team should assess its impact and determine an initial severity using the incident severity guide below. Note that severity can change over the lifespan of an incident, and it is acceptable for the team to assess the initial severity quickly.

If a security incident is suspected, the IC ensures that the system state is captured with disk snapshots, screen captures, and any other mechanisms relevant to the system to support post-remediation forensic analysis.

After this has been done, the IC should update the ticket and note the following:

- **Status**: confirmed
- **Severity**: [High/Med/Low]
- **Responders**: [update to include names of new/changed responders]

The IC should assess whether the [contingency plan](contingency-plan.md) should be activated.

The IC should write an initial situation report, called a _sitrep_, in a [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident), summarizing the incident details, identifying the IC, and linking to the issue. Here is an example sitrep:

``` markdown
Subject: [sitrep] The chickens are escaping

Severity: low
IC: Farmer Jane
Responders: Spot the Dog, Farmer Dave

We've confirmed reports of escaped chickens. Looks like a fox may have tunneled into the run. Dave is working to fix the fence. Spot is tracking the fox.
```

This sitrep should be posted in:

- 
- Slack channel [#None](None) (include link to [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident))

#### Communications during the Assess phase

Updates and real time chat should continue using Slack, Zoom, or Google Hangouts.

### Remediate

Remediation is about resolving the issues caused by the incident. Remediation will be situation-specific. Here are a few guidelines:

- If suspicious activity is suspected or other unanswered questions exist, create database dumps, take disk snapshots of relevant volumes, get screen captures of anomalous activity _before making changes_ to support post-remediation forensic analysis.

- The IC's responsibility is coordination, communication, and information collection. The remediation team will be focused on resolving the issue, so the IC must track what happened, how the incident is being remediated, and who is part of those efforts. Ideally the notes that the second IC makes should be sufficient for an outside investigator to independently follow the work of the Incident Response Team and validate the team's work.

- The team will develop a list of informational leads from the incident — actionable information about any security breaches, stolen data, etc. The IC should track these leads, maintaining information about the investigations and their outcomes. These can be tracked as checklists in the [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident).

- Similarly, the team will develop a list of remediation steps. The IC is responsible for tracking them, making sure they are assigned and followed, and verifying them when they are completed. Remediation efforts may be tracked with the issue details. The IC should distinguish between immediate concerns, which need to be completed before the incident is considered resolved, and long-term improvements/hardening, which can be deferred to the Retrospective.

- The Incident Response Team should aim to adopt a containment strategy. If machines are compromised, avoid destroying volumes or shutting down systems if possible, both of which can hamper forensics. Creating [CPM snapshots](https://cpm.project.com/) of relevant volumes is helpful at this stage.

   - For AWS instances, leave the instance running and reconfigure the Security Group for the instance to drop all ingress and egress traffic except from specific IPs (like yours) until forensics can be performed.

- Remediation may require service disruption. If it does, the team should proceed in a different way depending on the [severity](#incident-severities):

   - High-severity: Take action immediately, even if this causes disruption. A notification about the disruption should be sent out as soon as possible, but the team needs no permission to take action at this level.

   - Medium-severity: Notify the Project leads of the planned action, and help them assess the relative risk of disruption versus security. If the leads are unavailable on Slack, contact them using the phone numbers in their Slack profiles. The team should reach a collaborative decision on action, with a bias towards disruption. If they cannot be reached within an hour, the team may take action without them.

   - Low-severity: Notify the leads as described above. Do not take action until a mutually-agreed course of action has been determined.

- Remediation takes time. If the issue progresses for more than 3 hours without being resolved, the IC should plan for a long remediation. This means:

   - Determine whether remediation efforts will occur during business hours only or be continuous. This depends on the severity of the issue, and whether breaches are ongoing.

   - For a continuous response, the IC should plan shifts. This allows responders to take breaks and insures continuous coverage. Shifts should be no longer than 3 hours. Also, the IC duties should rotate in shifts no longer than 3 hours.

When the incident is no longer active -- for example, the breach has been contained, the issue has been fixed, etc. -- the IC should close out the incident. There might be longer term remediation required, and possibly more investigation, but when the incident is no longer active, these activities can proceed at the regular pace of business.

To close out an incident, the IC should:

- Set the status of the incident to **Ready for QA**.
- Send a final sitrep to stakeholders.
- Thank everyone involved for their service.

#### Communications during the Remediate phase

- Updates and real time chat should continue as above (updates on the [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident), chat in Slack or Google Hangouts).
- The IC should continue to post updated sitreps on a regular basis (the section on severities, below, suggests time intervals for each level). These sitreps should be shared in Slack, in the [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident), and with all stakeholders identified during the process (e.g. clients).

### Retrospect

The final step in handling a security incident is identifying what we can learn from it. The IC (or one of the ICs if there were multiple, or a designated other party) should lead a retrospective and develop an incident report.

The report should contain:

- a timeline of the incident
- details about how the incident progressed
- information about the vulnerabilities that led to the incident, or _cause analysis_

The _cause analysis_ is an important part of this report; the team should use tools such as [Infinite Hows](https://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/) or [Five Whys](https://en.wikipedia.org/wiki/5_Whys) to try to dig into causes, how future incidents could be prevented, how responses could be better in the future, etc.

The report should also contain some basic response metrics:

- Discovery method (how did we become aware of the issue?)
- Time to discovery (how long did it take from when the incident started until we became aware of it?)
- Time to containment (how long did it take from when we became aware until the issue was contained?)
- Threat actions (which specific actions -- e.g. phishing, password attacks, etc) -- were taken by the actor)?

This report should be posted as a final comment on the [JIRA Incident ticket](https://project.atlassian.net/issues/?jql=issuetype=Incident), which can then be closed.

## Incident Severities

_Note that Project has no High Value Assets (HVAs) or Sensitive Personally Identifiable Information (SPII). As such, Project incidents are generally expected to fall into the_ **Low Severity** _bucket._

Severity ratings drive the actions of the Incident Response Team. Below are the severities ratings we use, some examples of incidents that might fall into that bucket, and some guidelines for ICs and Incident Response Teams about how to treat each class of incident.

Note the severities may (and often will) change during the lifecycle of the incident. That's normal.

### 1 - High Severity

High-severity incidents successfully compromise the confidentiality/integrity of -Sensitive* Personally Identifiable Information (SPII), impact the availability of services for a large number of customers, or have significant financial impact. Examples include:

- Confirmed breach of SPII
- Successful root-level compromise of production systems
- Denial of Service attacks resulting in severe outages

Guidelines for addressing High-sev issues:

- Work will likely be 24/7 (e.g. work until the issue is contained).
- Responders are empowered to take any step needed to contain the issue, up to and including complete service degradation.
- Sitreps should be sent every hour, or more.

### 2 - Medium Severity

Medium-severity incidents represent attempts (possibly un- or not-yet-successful) at breaching PII, or those with limited availability/financial impact. Examples include:

- Suspected SPII breach
- Targeted (but as-of-yet unsuccessful) attempts to compromise production systems
- Spam/phishing attacks targeting CivicActions or Project staff
- DoS attacks resulting in limited service degradation

Guidelines for addressing Medium-sev issues:

- Response should be business-hours.
- Responders should attempt to consult stakeholders before causing downtime, but may proceed without them if they can't be contacted in a reasonable time-frame.
- Sitreps should be sent approximately twice a day.

### 3 - Low Severity

Low-sev incidents don't affect SPII, and have no availability or financial impact. Examples include:

- Attempted compromise of non-important systems (staging/testing instances, etc.)
- Incidents involving specific employees
- DoS attacks with no noticeable customer impact

Guidelines for addressing Low-sev issues:

- Response should be business-hours.
- Responders should avoid service degradation unless stakeholders agree.
- Sitreps should be sent approximately daily.
