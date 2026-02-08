# Project Charter: Smart Task & Risk Dashboard

## Document Control

| Item | Details |
|------|--------|
| **Project Name** | Smart Task & Risk Dashboard |
| **Project Code** | STRD-2026-001 |
| **Project Manager** | Ashley Kissinger |
| **Project Sponsor** | Sarah Chen, VP of Delivery Operations |
| **Charter Date** | February 7, 2026 |
| **Authorized By** | Sarah Chen |
| **Version** | 1.0 - Approved |

---

## Executive Summary

TechFlow Solutions requires a unified Smart Task & Risk Dashboard to consolidate project tracking, resource management, and risk monitoring into a single, real-time visual interface. This dashboard will replace the current fragmented approach (Excel, Jira, email) that has contributed to a 23% increase in deadline overruns and multiple unescalated critical risks.

The project has an allocated budget of $85,000, a timeline of 12 weeks (February 10 - May 1, 2026), and will be delivered using Agile/Scrum methodology with 2-week sprints.

---

## Project Purpose and Justification

### Business Case
TechFlow PMs currently spend 6-8 hours per week manually consolidating data for status reports. This inefficiency, combined with lack of real-time visibility, has resulted in:
- $150K in penalty fees from missed milestones (2025)
- Client NPS score of 52 (target: 75+)
- Resource double-booking incidents affecting project delivery
- Critical risks becoming issues due to delayed escalation

### Strategic Alignment
This project directly supports TechFlow's 2026 strategic pillars:
- **Operational Excellence**: 40% reduction in PM administrative overhead
- **Client Centricity**: Real-time transparency enabling trust and satisfaction
- **Growth Enablement**: Scalable infrastructure supporting 25 concurrent projects
- **PMO Maturity**: Standardized processes advancing from Level 2 to Level 3

A major $2M annual enterprise client contract requires real-time project visibility as a prerequisite, making this dashboard critical for business development.

---

## Project Objectives

### Primary Objectives
1. **Consolidation**: Create a single source of truth for tasks, resources, and risks
2. **Automation**: Auto-sync Jira task data within 15 minutes of updates
3. **Visibility**: Provide real-time dashboard access to 12 PMs and 5 executives
4. **Proactivity**: Implement risk scoring algorithm to flag high-priority risks
5. **Efficiency**: Reduce PM reporting time from 7 hours/week to 4 hours/week

### Success Metrics
| Metric | Baseline | Target | Measurement |
|--------|----------|--------|-------------|
| PM Admin Time | 7 hrs/week | 4 hrs/week | Time tracking survey |
| Deadline Overruns | 23% | ≤17% | Project completion data |
| Risk Escalation | 2 missed/Q | 0 missed/Q | Risk log analysis |
| Client NPS | 52 | 75+ | Quarterly client survey |
| Dashboard Adoption | 0% | 100% | Login analytics |
| Executive Reporting Lag | 3-5 days | Real-time | System timestamp |

---

## High-Level Scope

### In Scope

#### Core Features
- **Task Management Dashboard**
  - Real-time task list with status, priority, assignee, deadline
  - Visual progress indicators (completion %, overdue flags)
  - Filtering by project, assignee, status, priority
  - Integration with Jira API for automated task sync

- **Resource Allocation View**
  - Team member utilization rates across projects
  - Conflict detection for double-bookings
  - Capacity planning visualization
  - Skill-based resource matching

- **Risk Management Module**
  - Risk register with probability, impact, status
  - Automated risk scoring algorithm (P×I matrix)
  - Risk trend analysis and aging indicators
  - Escalation alerts for high-priority risks

- **Executive Dashboard**
  - Portfolio health overview (all projects)
  - Key metrics: on-time delivery rate, budget variance, risk exposure
  - Project status summaries (RAG: Red/Amber/Green)
  - Drill-down capability into individual projects

- **Automated Notifications**
  - Daily email digest: overdue tasks, high risks, resource conflicts
  - Threshold alerts: project red status, critical risks identified
  - Weekly portfolio summary for senior leadership

#### Technical Scope
- Web-based responsive dashboard (desktop, tablet, mobile)
- Backend API for data management (Python Flask or Java Spring)
- Jira API integration for task synchronization
- PostgreSQL database for dashboard data storage
- User authentication via existing Active Directory/SSO
- Role-based access control (PM, Executive, Read-only)

### Out of Scope

❌ **Explicitly Excluded**:
- Financial/budget tracking functionality (handled by existing ERP)
- Time tracking or timesheets (use existing TimeHub system)
- Document management/file storage (use SharePoint)
- Client-facing portal (internal use only for Phase 1)
- Gantt chart or Microsoft Project integration
- Mobile native apps (responsive web only)
- Multi-language support (English only)
- Custom reporting builder (predefined reports only)
- Integration with non-Jira systems (e.g., Asana, Trello)
- AI/ML predictive analytics (Phase 2 possibility)

### Assumptions
- Jira API access and credentials will be provided by IT Security by Feb 12
- All 12 PMs have modern browsers (Chrome, Firefox, Safari, Edge)
- Existing Active Directory can be used for authentication
- Team members will be available for user acceptance testing in Weeks 9-10
- Current Jira data structure is standardized across projects
- Hosting infrastructure (AWS or on-prem) will be provisioned by IT Ops

### Constraints
- **Budget**: $85,000 (includes development, testing, deployment)
- **Timeline**: 12 weeks (February 10 - May 1, 2026) - hard deadline for client proposal
- **Resources**: 1 PM (Ashley Kissinger), 2 Developers (Jordan Martinez, Jamie Park), 1 Designer (Sam Kim), 1 QA (Riley Thompson)
- **Technology**: Must use existing TechFlow tech stack (Python or Java, PostgreSQL)
- **Security**: Must comply with TechFlow data security policies and SOC 2 requirements
- **Integration**: Limited to Jira API only (no other tool integrations in Phase 1)

---

## Key Deliverables

### Phase 1: Planning & Design (Weeks 1-2)
- ✅ Project charter and kickoff meeting
- ✅ Requirements documentation (business, functional, technical)
- ✅ Technical architecture design document
- ✅ UI/UX wireframes and mockups
- ✅ Sprint 1 backlog and sprint plan

### Phase 2: Development (Weeks 3-8)
- ✅ Task management dashboard (Sprints 2-3)
- ✅ Resource allocation view (Sprint 3-4)
- ✅ Risk management module (Sprint 4-5)
- ✅ Executive dashboard (Sprint 5-6)
- ✅ Jira API integration (Sprint 6)
- ✅ Automated notifications (Sprint 7)
- ✅ User authentication and RBAC (Sprint 7)

### Phase 3: Testing & Deployment (Weeks 9-12)
- ✅ UAT with 4 pilot PMs (Week 9)
- ✅ Bug fixes and refinements (Week 10)
- ✅ Security and performance testing (Week 10)
- ✅ User training and documentation (Week 11)
- ✅ Production deployment (Week 12)
- ✅ Post-launch support plan

### Documentation Deliverables
- User guide for PMs and executives
- Technical documentation for IT support
- API integration guide
- Troubleshooting runbook
- Training slide deck and video tutorials

---

## Stakeholders

### Primary Stakeholders

| Name | Role | Interest | Influence |
|------|------|----------|----------|
| Sarah Chen | VP Delivery Ops (Sponsor) | High | High |
| Ashley Kissinger | Project Manager | High | High |
| Michael Rodriguez | PMO Director | High | High |
| David Park | CTO | Medium | High |
| Lisa Wong | Director, Client Services | Medium | Medium |

### User Groups
- **Project Managers (12)**: Primary users - daily dashboard interaction
- **Executive Team (5)**: Secondary users - weekly portfolio review
- **Resource Managers (3)**: Tertiary users - capacity planning
- **IT Operations (2)**: Support team - deployment and maintenance

### Extended Stakeholders
- Development Team (Jordan Martinez, Jamie Park)
- Design Team (Sam Kim)
- QA Team (Riley Thompson)
- IT Security (Maya Patel - API access, security review)
- Enterprise Client Prospect (Dr. Amanda Foster, CIO - awaiting demo)

---

## Approach and Methodology

### Agile/Scrum Framework

**Sprint Duration**: 2 weeks  
**Total Sprints**: 6 sprints (12 weeks)  
**Sprint Schedule**: Monday start, Friday review/retro

**Sprint Ceremonies**:
- Sprint Planning: Mondays, 9:00 AM - 11:00 AM
- Daily Standup: Every day, 9:15 AM - 9:30 AM
- Sprint Review: Fridays, 2:00 PM - 3:00 PM
- Sprint Retrospective: Fridays, 3:00 PM - 4:00 PM
- Backlog Grooming: Wednesdays, 10:00 AM - 11:00 AM

**Team Velocity**: 
- Estimated: 40 story points per sprint
- Will be calibrated after Sprint 1

### Technical Approach

**Architecture**: 3-tier web application
- **Frontend**: React.js with responsive design
- **Backend**: Python Flask REST API (or Java Spring Boot - TBD in Sprint 1)
- **Database**: PostgreSQL 14+
- **Integration**: Jira REST API v3
- **Hosting**: AWS (EC2, RDS) or on-premises (TBD with IT Ops)

**Development Standards**:
- Git/GitHub for version control
- Trunk-based development with feature branches
- Code reviews required before merge
- Unit test coverage ≥80%
- Automated CI/CD pipeline (GitHub Actions)

**Automation Elements**:
- Automated Jira task sync (Python script, runs every 15 min)
- Risk scoring algorithm (Python: probability × impact + aging factor)
- Email notification service (Python with SendGrid API)
- Database backup automation (daily incremental, weekly full)
- Health check monitoring scripts

---

## High-Level Milestones

| Milestone | Target Date | Success Criteria |
|-----------|-------------|------------------|
| Project Kickoff | Feb 10, 2026 | Charter approved, team aligned |
| Sprint 1 Complete | Feb 21, 2026 | Requirements finalized, architecture approved |
| Task Dashboard MVP | Mar 7, 2026 | Core task view functional with Jira sync |
| Resource & Risk Modules | Mar 21, 2026 | All core modules integrated |
| Executive Dashboard | Apr 4, 2026 | Portfolio view complete |
| UAT Complete | Apr 18, 2026 | All critical bugs resolved, user acceptance |
| Production Deployment | May 1, 2026 | Dashboard live, all PMs trained |
| 30-Day Post-Launch Review | May 30, 2026 | Success metrics validated |

---

## Budget Summary

| Category | Estimated Cost | Notes |
|----------|---------------|-------|
| Personnel (50% allocation) | $62,000 | 4 team members × 12 weeks |
| AWS Infrastructure | $8,000 | EC2, RDS, data transfer |
| Third-party APIs | $2,000 | SendGrid, monitoring tools |
| Training & Documentation | $5,000 | Video production, training sessions |
| Testing Tools | $3,000 | Load testing, security scanning |
| Contingency (15%) | $5,000 | Risk buffer |
| **Total** | **$85,000** | |

---

## Risks and Dependencies

### High-Level Risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Jira API changes or downtime | Medium | High | Version lock API, build retry logic |
| Resource availability (developers) | Medium | High | Cross-train team, prioritize core features |
| Scope creep from stakeholders | High | Medium | Strict change control, backlog prioritization |
| Security vulnerability discovered | Low | High | Security review in Sprint 7, penetration testing |
| UAT reveals major usability issues | Medium | Medium | Early design validation, weekly demos |

### Key Dependencies

- **IT Security**: Jira API credentials by Feb 12
- **IT Operations**: Hosting infrastructure by Mar 1
- **PMO**: Access to 4 PMs for UAT in Week 9
- **External**: Jira API availability and stability
- **Team**: Developers available without interruption from client projects

---

## Approval and Authorization

This charter authorizes Ashley Kissinger to proceed with the Smart Task & Risk Dashboard project within the defined scope, budget, and timeline. The Project Manager has authority to:

- Allocate assigned resources (Jordan Martinez, Jamie Park, Sam Kim, Riley Thompson)
- Make day-to-day project decisions within scope
- Approve minor changes that don't affect budget, timeline, or scope
- Escalate issues and major change requests to Project Sponsor

**Signature Required for Baseline Changes**:
- Scope changes: Sponsor approval required
- Budget variance >10%: Sponsor + Finance approval
- Timeline extension: Sponsor approval (impacts client proposal)

---

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Project Sponsor** | Sarah Chen | __________ | Feb 7, 2026 |
| **Project Manager** | Ashley Kissinger | __________ | Feb 7, 2026 |
| **PMO Director** | Michael Rodriguez | __________ | Feb 7, 2026 |

---

*Approved and authorized to proceed.*  
*Project officially begins: February 10, 2026*

---

## Notes

- First sprint planning meeting scheduled for Feb 10, 9:00 AM (Conference Room B)
- Access to Jira test environment provided for development
- Weekly sponsor check-ins: Fridays 11:00 AM
- Project Slack channel: #smart-dashboard-project
- Sharepoint folder: /Projects/STRD-2026-001/