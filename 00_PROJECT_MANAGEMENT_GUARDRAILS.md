# 🚦 PROJECT MANAGEMENT SIMULATION GUARDRAILS

**Project**: Smart Task & Risk Dashboard for TechFlow Solutions  
**Your Role**: Ashley Kissinger, Project Manager  
**Purpose**: Guide realistic PM execution without doing the work for you  
**Last Updated**: February 7, 2026

---

## 🎯 SIMULATION PHILOSOPHY

**YOU ARE THE PROJECT MANAGER. You make decisions. You manage people. You deliver products.**

This simulation is designed to:
- ✅ **Challenge you** with realistic project management scenarios
- ✅ **Guide you** when you're stuck or heading off track
- ✅ **Teach you** through experience, not handholding
- ❌ **NOT do your work** for you
- ❌ **NOT make decisions** that you should make
- ❌ **NOT write your documents** for you

**Expected Outcome**: You should struggle sometimes. That's realistic. Real PMs don't have all the answers immediately.

---

## 📋 MANDATORY DAILY ROUTINE

### **EVERY DAY YOU MUST:**

1. **Check the Date & Phase** (30 seconds)
   - What is today's date from system context?
   - Which sprint am I in? (Sprint 1: Feb 10-21, Sprint 2: Feb 24-Mar 7, etc.)
   - How many days until next key milestone?
   - What phase: Planning / Execution / Monitoring / Closeout?

2. **Ceremony Check** (1 minute)
   - Is there a Daily Standup today? (Every weekday at 9:15 AM)
   - Is today Sprint Planning? (Every other Monday)
   - Is today Sprint Review/Retro? (Every other Friday)
   - Is today a Sponsor Check-in? (Every Friday 11 AM with Sarah Chen)

3. **Team Status Check** (5 minutes)
   - What is each team member working on RIGHT NOW?
   - Read: `03_Project_Execution/Task_Management/Scrum_Board.md`
   - Are there any blockers in the Issue_Log.md?
   - Is anyone waiting on my decision?

4. **Product Progress Check** (5 minutes)
   - What user stories are "In Progress" today?
   - What should exist in `09_WebApp/` based on completed work?
   - Can I trace today's work to the Product Backlog?
   - Are we building shippable features or just planning?

5. **Stakeholder Check** (3 minutes)
   - Who needs information from me today?
   - Read: `07_Stakeholder_Management/Communication_Log/`
   - Any emails/messages requiring response?
   - Is Sarah Chen expecting an update today?

6. **Risk & Issue Scan** (3 minutes)
   - Review: `04_Monitoring_and_Controlling/Risk_Management/Risk_Log.md`
   - Review: `04_Monitoring_and_Controlling/Issue_Log.md`
   - Any critical risks escalating? Any new issues?
   - Do I need to escalate anything to Sarah Chen?

**Total Time: 15-20 minutes**  
**Result: You now know your priorities for the day**

---

## 🛡️ CORE GUARDRAILS - THESE ARE NON-NEGOTIABLE

### **GUARDRAIL 1: PRODUCT OVER PAPERWORK**

**RULE**: Every document you create or update must serve a product delivery purpose. No busywork.

✅ **ALLOWED:**
- Updating Risk Log because you identified a real risk that needs mitigation
- Creating Sprint Backlog because you're about to start Sprint Planning
- Updating Scrum Board because team members completed tasks today
- Writing Status Report because Sarah Chen needs it for Friday check-in

❌ **NOT ALLOWED:**
- Creating documents "because they should exist" with no immediate use
- Spending hours perfecting formatting instead of managing the project
- Writing detailed meeting minutes for meetings that haven't happened
- Creating templates for future use when you should be executing now

**TEST**: Ask yourself: "If I don't do this now, will the team be blocked or will stakeholders lack critical information?"  
If NO → Defer or skip it.

---

### **GUARDRAIL 2: MAKE DECISIONS - DON'T AVOID THEM**

**RULE**: You are the Project Manager. When decisions need to be made, YOU make them (or escalate appropriately).

✅ **YOU DECIDE:**
- Which user stories go into Sprint Backlog (with team input)
- How to resolve resource conflicts
- When to escalate risks vs. mitigate directly
- Meeting schedules and agendas
- How to communicate status to stakeholders
- What "Definition of Done" means for your team
- Whether to accept or reject completed work

⚠️ **YOU ESCALATE TO SARAH CHEN (SPONSOR):**
- Budget overruns >10%
- Scope changes that affect timeline or budget
- Critical risks that threaten project success
- Team capacity issues requiring additional resources
- Stakeholder conflicts you can't resolve

❌ **YOU NEVER**:
- Ask AI to decide which user stories to prioritize (you decide with team)
- Delegate decision-making that's your responsibility
- Sit on decisions for days causing team blockage
- Make excuses for not completing PM responsibilities

**TEST**: If you're typing "What should I do about X?" → STOP. Think first. Research if needed. Then decide.

---

### **GUARDRAIL 3: CEREMONIES ARE MANDATORY**

**RULE**: Agile ceremonies happen on schedule. No skipping. No shortcuts.

**DAILY STANDUP** (Every weekday, 9:15-9:30 AM)
- ✅ Simulate: Update `Scrum_Board.md` with status from each team member
- ✅ Document: Brief update in `Sprint_Logs/Sprint_XX_Log.md`
- ✅ Identify: Any blockers that need immediate action
- ⏱️ Time: 5-10 minutes of your time

**SPRINT PLANNING** (First Monday of sprint, 9:00-11:00 AM)
- ✅ Facilitate: Select user stories from Product Backlog
- ✅ Define: Sprint Goal
- ✅ Create: `Sprint_Backlogs/Sprint_XX_Backlog.md`
- ✅ Update: Scrum Board with sprint tasks
- ⏱️ Time: 30-45 minutes of your time

**SPRINT REVIEW** (Last Friday of sprint, 2:00-3:00 PM)
- ✅ Demo: Show completed work (reference what's actually built in 09_WebApp/)
- ✅ Gather: Stakeholder feedback
- ✅ Accept/Reject: User stories based on Definition of Done
- ✅ Document: Review notes in Sprint Log
- ⏱️ Time: 20-30 minutes of your time

**SPRINT RETROSPECTIVE** (Last Friday of sprint, 3:00-4:00 PM)
- ✅ Facilitate: What went well? What didn't? What to improve?
- ✅ Create: Action items for next sprint
- ✅ Document: `SprintLab_Journal/08_Retrospectives.md`
- ⏱️ Time: 15-20 minutes of your time

**SPONSOR CHECK-IN** (Every Friday, 11:00 AM)
- ✅ Prepare: Read Risk Log, Issue Log, Sprint progress
- ✅ Update: Sarah Chen on status, risks, decisions needed
- ✅ Document: `Communication_Log/YYYY-MM-DD_Session.md`
- ⏱️ Time: 10-15 minutes prep + 10 minutes meeting simulation

**PENALTY FOR SKIPPING**: You will be blocked from proceeding. Real projects fail when ceremonies are skipped.

---

### **GUARDRAIL 4: TEAM SIMULATION MUST BE REALISTIC**

**RULE**: Your team members are "working" every day. You must track their progress realistically.

**TEAM MEMBER STATUS TRACKING:**

Each weekday, your team should have:
- **Current Assignment**: What user story/task are they working on?
- **Progress**: What did they complete? What's in progress?
- **Blockers**: Are they blocked on anything?
- **Availability**: Are they 100% on this project or split with other work?

**REALISTIC WORK RATES:**

| Role | Capacity | Typical Output |
|------|----------|----------------|
| **Jordan Martinez** (Senior Dev) | 6 hrs/day (50% allocation) | 8-13 story points per sprint |
| **Jamie Park** (Backend Dev) | 6 hrs/day (50% allocation) | 8-13 story points per sprint |
| **Sam Kim** (Designer) | 6 hrs/day (50% allocation) | 5-8 story points per sprint |
| **Riley Thompson** (QA) | 6 hrs/day (50% allocation) | Testing ~15-20 story points per sprint |

**SPRINT VELOCITY**: Team can complete ~40 story points per 2-week sprint (realistic for 50% allocation)

✅ **REALISTIC:**
- Jordan completes 2-3 small tasks (5-8 points) in a week
- Jamie gets blocked waiting for Jira API credentials from Maya Patel
- Sam takes 3 days to create UI mockups for dashboard
- Riley finds 5 bugs during testing that need fixing

❌ **UNREALISTIC:**
- Entire sprint's work completed in 2 days
- Zero bugs ever found by QA
- No team members ever blocked or struggling
- Everyone always "done" with no realistic time passing

**ENFORCEMENT**: If team status isn't updated for 3+ days, you'll be prompted to simulate standups.

---

### **GUARDRAIL 5: STAKEHOLDER ENGAGEMENT IS ACTIVE**

**RULE**: Stakeholders are people with needs, concerns, and expectations. You must manage them proactively.

**SARAH CHEN (Sponsor)** - High Power, High Interest
- ✅ **Weekly Check-ins**: Every Friday at 11 AM (mandatory)
- ✅ **Communication Style**: She's busy, wants executive summary (3 bullets)
- ✅ **She Cares About**: Budget, timeline, risks, GlobalTech contract
- ✅ **Response Time**: She replies within 4-24 hours to emails
- 🚨 **Red Flag**: If you go 2+ weeks without updating her, she'll escalate to PMO Director

**MAYA PATEL (IT Security)** - High Power, Low Interest
- ✅ **Critical Dependency**: She must approve Jira API access by Feb 12
- ✅ **Communication Style**: Formal, security-focused, needs justification
- ✅ **Response Time**: 2-3 days for requests, slower if incomplete
- 🚨 **Red Flag**: If you don't request API access by Feb 10, you'll miss Sprint 1 goal

**DAVID PARK (CTO)** - High Power, Medium Interest
- ✅ **Tech Architecture Review**: Needs to approve architecture decisions
- ✅ **Communication Style**: Technical, asks probing questions
- ✅ **Response Time**: 1-2 days for reviews
- 🚨 **Red Flag**: Building without his architecture approval = rework risk

**EXECUTIVE TEAM (5 execs)** - Medium Power, Medium Interest
- ✅ **Weekly Portfolio Summary**: They want high-level status email Fridays
- ✅ **Communication Style**: Metrics-driven, want numbers (% complete, risks)
- 🚨 **Red Flag**: They don't like surprises. Bad news should come from you first.

**PM USER GROUP (12 PMs)** - Low Power, High Interest
- ✅ **UAT Participation**: Need them involved in Weeks 9-10 for testing
- ✅ **Training**: Need 2 weeks' notice to schedule training sessions
- 🚨 **Red Flag**: If you don't involve them early, adoption will fail

**COMMUNICATION LOG REQUIREMENT:**
- Every stakeholder interaction must be documented in `Communication_Log/`
- Unanswered emails older than 3 days trigger escalation warnings
- Sarah Chen's check-ins are NON-NEGOTIABLE

---

### **GUARDRAIL 6: RISKS ARE PROACTIVE, NOT REACTIVE**

**RULE**: Risk management is continuous. You identify, assess, and mitigate risks BEFORE they become issues.

**RISK IDENTIFICATION TRIGGERS:**

You must scan for risks:
- ✅ Daily during standups (team mentions concerns)
- ✅ Weekly during sponsor check-ins (Sarah Chen flags concerns)
- ✅ During Sprint Planning (dependencies, technical complexity)
- ✅ When external dependencies discovered (Jira API, IT Security, etc.)
- ✅ When assumptions are challenged (tech stack decision, resource availability)

**RISK ASSESSMENT:**

Every risk in `Risk_Log.md` must have:
- **Probability**: Low (10-30%) / Medium (40-60%) / High (70-90%)
- **Impact**: Low (minor delay) / Medium (1-2 week delay) / High (project failure risk)
- **Risk Score**: Probability × Impact × Aging Factor
- **Mitigation Plan**: What you'll do to reduce/avoid the risk
- **Owner**: Who is responsible for monitoring/mitigating
- **Status**: Open / Mitigating / Closed

**ESCALATION THRESHOLD:**

- **High Risk Score (>6.0)**: Immediate escalation to Sarah Chen
- **Medium Risk Score (3.0-6.0)**: Inform Sarah Chen at next check-in
- **Low Risk Score (<3.0)**: Monitor and manage directly

**RISK AGING:**
- Risks open >2 weeks without mitigation: Auto-escalate
- Critical risks (High Probability + High Impact): Daily monitoring required

🚨 **RED FLAG**: If Risk_Log.md hasn't been updated in 7+ days, you're flying blind.

---

### **GUARDRAIL 7: ISSUES GET RESOLVED OR ESCALATED**

**RULE**: Issues are current problems blocking progress. You resolve them within 24-48 hours or escalate.

**ISSUE LOGGING:**

Every blocker mentioned by team members must go in `Issue_Log.md`:
- **Issue ID**: Sequential numbering (ISS-001, ISS-002, etc.)
- **Description**: What's the problem?
- **Impact**: Who/what is blocked?
- **Severity**: Critical (stops work) / High (slows work) / Medium (minor inconvenience)
- **Owner**: Who's responsible for resolving?
- **Status**: Open / In Progress / Resolved / Escalated
- **Resolution Deadline**: Date by which this must be resolved

**RESOLUTION EXPECTATIONS:**

| Severity | Your Action | Timeline |
|----------|-------------|----------|
| **Critical** | Drop everything, resolve immediately or escalate | Same day |
| **High** | Prioritize, create action plan | 24-48 hours |
| **Medium** | Add to sprint backlog, resolve this week | 3-5 days |

**ESCALATION PATH:**

1. **You try to resolve** (your job as PM - remove blockers)
2. **If you can't resolve in timeframe** → Escalate to Sarah Chen
3. **If Sarah can't resolve** → Sponsor escalates to Steering Committee

🚨 **RED FLAG**: Issues sitting in "Open" status for 3+ days = you're not doing your job.

---

### **GUARDRAIL 8: SCOPE CHANGES GO THROUGH CHANGE CONTROL**

**RULE**: Scope changes must be documented, assessed, and approved. No "scope creep."

**WHEN SCOPE CHANGES OCCUR:**

✅ **LEGITIMATE SCOPE CHANGES:**
- Stakeholder requests new feature not in approved Product Backlog
- Technical discovery reveals major architecture change needed
- Regulatory/security requirement emerges mid-project
- Sarah Chen requests additional functionality

❌ **NOT SCOPE CHANGES:**
- Clarifying existing user story requirements
- Bug fixes for features already built
- Refactoring code for quality improvements
- Design iterations within approved UI/UX scope

**CHANGE CONTROL PROCESS:**

1. **Document**: Log in `04_Monitoring_and_Controlling/Change_Log.md`
2. **Assess Impact**: Budget, timeline, resources, risks
3. **Present Options**:
   - Add to scope (requires more time/budget)
   - Defer to Phase 2 (after May 1 launch)
   - Reject (out of scope)
4. **Get Approval**: Sarah Chen must approve all scope changes
5. **Update Artifacts**: Product Backlog, Project Charter if approved

**CHANGE REQUEST TEMPLATE:**

```
CHANGE REQUEST: CR-00X
Requested By: [Stakeholder]
Description: [What they want]
Business Justification: [Why it's needed]
Impact Assessment:
  - Timeline: +/- X days
  - Budget: +/- $X,XXX
  - Resources: Additional effort from [team member]
  - Risks: [New risks introduced]
Options:
  1. Approve and add to Sprint X
  2. Defer to Phase 2 (post-May 1)
  3. Reject (out of scope)
Recommendation: [Your PM recommendation]
Sponsor Decision: [Sarah's approval/rejection]
```

🚨 **RED FLAG**: If you accept scope changes without Sarah Chen's approval, you've failed as PM.

---

### **GUARDRAIL 9: QUALITY GATES ARE ENFORCED**

**RULE**: Work must meet Definition of Done before being marked "Complete." No shortcuts.

**DEFINITION OF DONE (FOR USER STORIES):**

A user story is DONE when:
- ✅ Code is written and pushed to GitHub
- ✅ Code review completed by peer developer
- ✅ Unit tests written and passing (80%+ coverage)
- ✅ Feature tested by Riley Thompson (QA)
- ✅ UI/UX reviewed by Sam Kim (Designer)
- ✅ Acceptance criteria from user story are met
- ✅ Documentation updated (if needed)
- ✅ Demo-ready for Sprint Review

**ACCEPTANCE CRITERIA EXAMPLE:**

For US-001: "As a PM, I want to see a list of all my project tasks"

✅ **ACCEPTANCE CRITERIA:**
- Task list displays on dashboard when PM logs in
- Each task shows: title, status, assignee, due date, priority
- Task list is sortable by each column
- Task list loads within 3 seconds
- Task list is responsive (works on desktop, tablet, mobile)

**QUALITY CHECKPOINTS:**

| Checkpoint | Who | When | What |
|------------|-----|------|------|
| **Code Review** | Jordan/Jamie | Before merge | Code quality, standards, security |
| **QA Testing** | Riley | After merge | Functional testing, bug identification |
| **UI/UX Review** | Sam | Before Sprint Review | Design consistency, usability |
| **PM Acceptance** | You | Sprint Review | Meets acceptance criteria, demo-ready |

**REJECTION CRITERIA:**

You MUST reject work if:
- ❌ Acceptance criteria not met
- ❌ Critical bugs discovered by Riley
- ❌ Code not reviewed by peer
- ❌ Feature not working as specified

🚨 **RED FLAG**: Accepting incomplete work to "make velocity look good" = technical debt + rework later.

---

### **GUARDRAIL 10: YOU ARE LEARNING, NOT PERFECT**

**RULE**: This is a simulation for learning. You will make mistakes. That's expected. Learn and improve.

✅ **EXPECTED LEARNING CHALLENGES:**

- **Week 1-2**: You'll feel overwhelmed by all the documents and ceremonies
- **Week 3-4**: You'll struggle with prioritization and stakeholder management
- **Week 5-6**: You'll realize you made mistakes in Sprint Planning
- **Week 7-8**: You'll have to course-correct based on retrospectives
- **Week 9-10**: You'll be managing UAT feedback and last-minute issues
- **Week 11-12**: You'll be sprinting to finish while maintaining quality

✅ **HOW AI WILL HELP YOU:**

- **Remind you** of upcoming ceremonies and deadlines
- **Prompt you** when you've skipped important PM activities
- **Simulate** team member responses and stakeholder feedback
- **Challenge you** when you're avoiding difficult decisions
- **Guide you** with PM best practices when you ask
- **Catch you** when you're heading off track

❌ **HOW AI WILL NOT HELP YOU:**

- Make decisions for you
- Write your documents for you (you draft, AI reviews)
- Tell you exactly what to do step-by-step
- Let you skip ceremonies or guardrails
- Allow unrealistic shortcuts

**RETROSPECTIVE REQUIREMENT:**

After each sprint, you MUST document in `SprintLab_Journal/08_Retrospectives.md`:
- **What went well**: Celebrate wins
- **What didn't go well**: Honest assessment of failures
- **What to improve**: Actionable changes for next sprint
- **Lessons learned**: What you learned as a PM this sprint

---

## 🚨 RED FLAGS - STOP IMMEDIATELY IF:

### **🛑 DOCUMENTATION RED FLAGS:**

- ❌ You've spent 3+ hours on documentation with no product progress
- ❌ You're creating documents that have no immediate use case
- ❌ You're perfecting formatting instead of managing the project
- ❌ Your documents are all templates with no real project data

**FIX**: Ask yourself: "Does this document help the team ship a feature today?" If no, defer it.

---

### **🛑 TEAM SIMULATION RED FLAGS:**

- ❌ Your "team" has had no status updates for 3+ days
- ❌ You can't explain what each team member is working on right now
- ❌ The Scrum Board hasn't been updated in 5+ days
- ❌ No blockers have been identified for 2+ weeks (unrealistic)

**FIX**: Simulate daily standups. Update Scrum Board. Identify realistic blockers.

---

### **🛑 CEREMONY RED FLAGS:**

- ❌ You've skipped Daily Standups for 3+ days
- ❌ You haven't done Sprint Planning yet Sprint started 2+ days ago
- ❌ You completed a sprint without Sprint Review/Retro
- ❌ You missed Sarah Chen's Friday check-in 2 weeks in a row

**FIX**: Go back and execute the ceremony. This is non-negotiable.

---

### **🛑 DECISION-MAKING RED FLAGS:**

- ❌ You're asking "What should I do?" for decisions you should make
- ❌ Issues have been sitting unresolved for 5+ days
- ❌ You're avoiding difficult conversations with stakeholders
- ❌ You haven't made a single decision in 3+ days

**FIX**: Review the decision framework. Make the call. Real PMs decide.

---

### **🛑 PRODUCT DEVELOPMENT RED FLAGS:**

- ❌ It's Sprint 2+ and nothing exists in `09_WebApp/` yet
- ❌ You can't trace current work to specific user stories
- ❌ You're planning without building
- ❌ Your team has "completed" 50 story points in 3 days (unrealistic)

**FIX**: Focus on product delivery. Build something tangible. Be realistic about velocity.

---

### **🛑 STAKEHOLDER RED FLAGS:**

- ❌ Sarah Chen hasn't heard from you in 2+ weeks
- ❌ You haven't requested Jira API access from Maya by Feb 10
- ❌ Communication Log has no entries for 7+ days
- ❌ Executive Team hasn't received a status update in 3+ weeks

**FIX**: Proactive communication. Update stakeholders before they ask.

---

### **🛑 RISK MANAGEMENT RED FLAGS:**

- ❌ Risk Log hasn't been updated in 7+ days
- ❌ You have zero risks identified (unrealistic)
- ❌ Critical risks have no mitigation plans
- ❌ Risks are becoming issues because you didn't mitigate

**FIX**: Daily risk scanning. Create mitigation plans. Escalate high-priority risks.

---

## ✅ GREEN LIGHTS - YOU'RE ON TRACK WHEN:

### **✨ PRODUCT DELIVERY GREEN LIGHTS:**

- ✅ Every sprint produces a working product increment (visible in `09_WebApp/`)
- ✅ You can demo real functionality at Sprint Reviews
- ✅ User stories move from "TODO" → "In Progress" → "Done" weekly
- ✅ Your team velocity is realistic (30-40 points per sprint)

---

### **✨ TEAM MANAGEMENT GREEN LIGHTS:**

- ✅ Scrum Board updated daily with realistic progress
- ✅ Team members have clear assignments and are "making progress"
- ✅ Blockers are identified and resolved within 24-48 hours
- ✅ Daily Standups are happening (even if simulated)

---

### **✨ CEREMONY GREEN LIGHTS:**

- ✅ All required ceremonies executed on schedule
- ✅ Sprint Planning produces a clear Sprint Backlog
- ✅ Sprint Reviews include demos of completed work
- ✅ Retrospectives generate actionable improvements

---

### **✨ STAKEHOLDER GREEN LIGHTS:**

- ✅ Sarah Chen receives weekly updates every Friday
- ✅ Communication Log has regular entries
- ✅ Stakeholder questions answered within 24-48 hours
- ✅ You're proactive, not reactive, with communications

---

### **✨ DECISION-MAKING GREEN LIGHTS:**

- ✅ You make prioritization decisions confidently
- ✅ Issues are resolved or escalated promptly
- ✅ You're not avoiding difficult PM responsibilities
- ✅ You seek guidance when truly stuck, but try first

---

### **✨ RISK & QUALITY GREEN LIGHTS:**

- ✅ Risk Log updated weekly (minimum)
- ✅ High-priority risks have mitigation plans
- ✅ Quality gates enforced (Definition of Done)
- ✅ You're finding and logging risks proactively

---

## 📊 DECISION FRAMEWORKS

### **FRAMEWORK 1: PRIORITIZATION (USE MoSCoW)**

When deciding which user stories to include in a sprint:

- **MUST HAVE**: Critical features for MVP (e.g., Task list display)
- **SHOULD HAVE**: Important but not critical (e.g., CSV export)
- **COULD HAVE**: Nice-to-have (e.g., Advanced filtering)
- **WON'T HAVE** (this sprint): Defer to future sprints

**YOUR JOB**: Work with "team" to decide MoSCoW classification, then prioritize MUST/SHOULD first.

---

### **FRAMEWORK 2: ESCALATION (When to involve Sarah Chen)**

| Situation | Your Action | Escalate? |
|-----------|-------------|-----------|
| **Developer needs technical clarification** | You clarify or they figure it out | NO |
| **Team disagrees on approach** | You facilitate decision as PM | NO |
| **Minor timeline slip (1-2 days)** | You adjust sprint plan, inform Sarah | NO (inform only) |
| **Major timeline slip (1+ week)** | You present corrective actions | YES |
| **Budget overrun >10%** | You explain and request approval | YES |
| **Critical risk identified** | You present risk + mitigation | YES |
| **Scope change request** | You assess impact, present options | YES |
| **Resource unavailable** | You juggle team, adjust sprint | NO (unless >1 week) |
| **Stakeholder conflict** | You try to resolve first | TRY FIRST, then YES |

**RULE**: Escalate when you lack authority to resolve, otherwise YOU handle it.

---

### **FRAMEWORK 3: TIME ALLOCATION (How to spend your 8-hour day)**

Realistic PM time distribution:

| Activity | Daily Time | % of Your Day |
|----------|------------|---------------|
| **Ceremonies** (Standups, Meetings) | 1-2 hours | 15-25% |
| **Stakeholder Communication** | 1-1.5 hours | 12-18% |
| **Issue/Blocker Resolution** | 1-2 hours | 15-25% |
| **Planning & Prioritization** | 1 hour | 12-15% |
| **Documentation Updates** | 0.5-1 hour | 6-12% |
| **Risk/Issue Management** | 0.5-1 hour | 6-12% |
| **Product Review & Acceptance** | 0.5-1 hour | 6-12% |
| **Learning & Improvement** | 0.5 hour | 6% |

**TOTAL**: ~8 hours per day

**RULE**: If you're spending >2 hours/day on documentation, you're doing it wrong.

---

### **FRAMEWORK 4: GOOD ENOUGH vs. GOLD PLATING**

**GOOD ENOUGH** (Do This):
- ✅ Risk Log with brief descriptions and mitigation plans
- ✅ Sprint Backlog with user stories and estimated points
- ✅ Status report with 3 bullets: progress, risks, next steps
- ✅ Meeting notes with decisions made and action items
- ✅ Scrum Board updated with current task status

**GOLD PLATING** (Don't Do This):
- ❌ Risk Log with 5-page risk analysis per risk
- ❌ Sprint Backlog with detailed task breakdowns and Gantt charts
- ❌ Status report with 10 slides and executive presentation
- ❌ Meeting notes transcribed word-for-word with full dialogue
- ❌ Scrum Board with color-coded labels and custom graphics

**TEST**: If it takes >30 minutes to update a document, you're probably gold-plating.

---

## 📁 QUICK REFERENCE - FILES BY ACTIVITY

### **🔄 DAILY ACTIVITIES:**

**Daily Standup (Every Weekday)**
- Update: `03_Project_Execution/Task_Management/Scrum_Board.md`
- Update: `SprintLab_Journal/Sprint_Logs/Sprint_XX_Log.md`
- Time: 5-10 minutes

**Team Coordination**
- Check: `04_Monitoring_and_Controlling/Issue_Log.md` (any blockers?)
- Update: Team member assignments on Scrum Board
- Time: 5 minutes

---

### **📅 WEEKLY ACTIVITIES:**

**Monday (Sprint Planning if new sprint)**
- Read: `03_Project_Execution/Task_Management/Product_Backlog/Product_Backlog.md`
- Create: `03_Project_Execution/Task_Management/Sprint_Backlogs/Sprint_XX_Backlog.md`
- Update: `Scrum_Board.md` with sprint tasks
- Time: 30-45 minutes

**Wednesday (Backlog Grooming)**
- Review: `Product_Backlog.md`
- Refine: User story descriptions and acceptance criteria
- Estimate: Story points for upcoming stories
- Time: 15-20 minutes

**Friday (Sprint Review if end of sprint)**
- Demo: Completed work (reference `09_WebApp/`)
- Document: Sprint Review notes in Sprint Log
- Time: 20-30 minutes

**Friday (Sprint Retrospective if end of sprint)**
- Facilitate: Team reflection
- Document: `SprintLab_Journal/08_Retrospectives.md`
- Time: 15-20 minutes

**Friday (Sponsor Check-in EVERY WEEK)**
- Prepare: Review Risk Log, Issue Log, Sprint Progress
- Update: `07_Stakeholder_Management/Communication_Log/YYYY-MM-DD_Session.md`
- Time: 10-15 min prep + 10 min meeting

---

### **⚠️ AS-NEEDED ACTIVITIES:**

**Risk Management**
- Update: `04_Monitoring_and_Controlling/Risk_Management/Risk_Log.md`
- When: When new risks identified, weekly review minimum
- Time: 10-15 minutes

**Issue Management**
- Update: `04_Monitoring_and_Controlling/Issue_Log.md`
- When: When blockers arise, daily review
- Time: 5-10 minutes

**Change Control**
- Update: `04_Monitoring_and_Controlling/Change_Log.md`
- When: Scope change requested
- Time: 30 minutes (includes impact assessment)

**Stakeholder Communication**
- Update: `07_Stakeholder_Management/Communication_Log/`
- When: Any stakeholder interaction
- Time: 5 minutes per interaction

**Product Development**
- Update: `09_WebApp/` files (HTML/CSS/JS)
- When: Features completed by dev team
- Note: Team does the coding, you verify it's done

---

## 🗓️ PROJECT TIMELINE REFERENCE

### **OVERALL SCHEDULE:**
- **Duration**: 12 weeks (Feb 10 - May 1, 2026)
- **Methodology**: Agile/Scrum with 2-week sprints
- **Total Sprints**: 6 sprints
- **Budget**: $85,000
- **Team Size**: 5 (1 PM, 2 Devs, 1 Designer, 1 QA)

### **SPRINT SCHEDULE:**

| Sprint | Dates | Focus | Story Points |
|--------|-------|-------|--------------|
| **Sprint 1** | Feb 10-21 | Planning, design, architecture, task dashboard foundation | ~40 |
| **Sprint 2** | Feb 24 - Mar 7 | Task Management Dashboard MVP | ~40 |
| **Sprint 3** | Mar 10-21 | Task features + Resource Allocation start | ~40 |
| **Sprint 4** | Mar 24 - Apr 4 | Resource Allocation + Risk Module start | ~40 |
| **Sprint 5** | Apr 7-18 | Risk Module + Executive Dashboard | ~40 |
| **Sprint 6** | Apr 21 - May 1 | Jira Integration, Notifications, UAT, Deployment | ~40 |

**Total Product Backlog**: 240 story points across 7 epics

### **KEY MILESTONES:**

| Date | Milestone | Criticality |
|------|-----------|-------------|
| **Feb 7, 2026** | Pre-Sprint prep (TODAY) | Starting point |
| **Feb 10, 2026** | Sprint 1 Planning | CRITICAL |
| **Feb 12, 2026** | Jira API access from Maya Patel | CRITICAL |
| **Every Friday** | Sarah Chen check-ins | HIGH |
| **Feb 21, 2026** | Sprint 1 Review/Retro | HIGH |
| **Mar 7, 2026** | Task Dashboard MVP Demo | HIGH |
| **Apr 4, 2026** | Resources + Risks Complete | MEDIUM |
| **Apr 18, 2026** | UAT Begins (PM User Group) | HIGH |
| **May 1, 2026** | Production Deployment (GO-LIVE) | CRITICAL |

---

## 🎯 SUCCESS MANTRA

**"Every action I take today must either:**
1. **Unblock the team** to build a product feature, or
2. **Enable a decision** that moves development forward, or
3. **Create visibility** that keeps stakeholders aligned

**If it doesn't do one of these three things, question whether it's necessary."**

---

## 🤝 HOW TO WORK WITH AI (YOUR PM COACH)

### **WHEN TO ASK FOR HELP:**

✅ **ASK WHEN:**
- You're genuinely stuck and have tried to figure it out first
- You need PM best practices or frameworks explained
- You want feedback on a decision you already made
- You need simulation of stakeholder/team responses
- You want validation that you're on the right track
- You need to be challenged or held accountable

❌ **DON'T ASK FOR:**
- AI to make decisions for you
- AI to write your documents for you
- Step-by-step instructions for everything
- Permission to proceed (just do it)
- Excuses for skipping guardrails

### **HOW TO ASK GOOD QUESTIONS:**

**BAD QUESTION:**  
"What should I do for Sprint Planning?"

**GOOD QUESTION:**  
"I'm preparing for Sprint 1 Planning on Feb 10. Based on team capacity (50% allocation = ~40 story points), I'm thinking of selecting US-001 through US-005 from the Product Backlog. Does this seem realistic given this is our first sprint? What might I be missing?"

**BAD REQUEST:**  
"Write my Sprint Backlog for me."

**GOOD REQUEST:**  
"I've drafted Sprint 1 Backlog with 45 story points. Here's my selection: [list]. Review it and tell me if I'm overcommitting or if my priorities seem off."

---

## 📋 DAILY PROMPT TEMPLATE

**Use this prompt every day to get your personalized task list:**

```
I'm working on the Smart Task & Risk Dashboard simulation. Today is [CURRENT DATE].

CONTEXT VALIDATION:
- Verify which sprint/phase I'm in based on today's date
- Check what should already be completed vs. what I should be working on
- Validate that my planned actions align with PM best practices

GUARDRAIL CHECK:
- Am I focusing on product delivery or just creating documentation?
- Are there any decisions I'm avoiding that will block the team?
- Am I following proper agile ceremonies and stakeholder engagement?
- Is my work traceable to actual user stories and deliverables?

PROVIDE:
1. Current phase status summary
2. Today's prioritized task list (with realistic time estimates)
3. Required file updates (CREATE/READ/UPDATE with specific purposes)
4. Team simulation actions (what each team member is doing today)
5. Decisions I must make today to unblock progress
6. Red flags if I'm going off track
7. Quality checkpoint: Is what I'm doing "good enough" or am I gold-plating?

Challenge me if I'm not being realistic or if I'm avoiding difficult PM work.
```

---

## 🎓 FINAL WORDS

**You are the Project Manager.**

This is your project. Your team. Your stakeholders. Your decisions.

You will struggle. That's realistic. Real PMs don't have perfect information or easy answers.

You will make mistakes. That's how you learn. Retrospect and improve.

You will feel overwhelmed. That's normal. Prioritize ruthlessly.

You will want shortcuts. Don't take them. The learning is in the doing.

**AI is your coach, not your crutch.**

Ask for guidance. Get feedback. Request challenges. But don't ask AI to do your job.

**Now go manage this project. You've got this.** 🚀

---

*Last Updated: February 7, 2026*  
*Version: 2.0 - Comprehensive Guardrails*

