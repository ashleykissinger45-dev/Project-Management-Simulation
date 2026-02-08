# Product Backlog: Smart Task & Risk Dashboard

## Document Control

| Item | Details |
|------|---------|
| **Project Name** | Smart Task & Risk Dashboard |
| **Product Owner** | Sarah Chen (Sponsor) / Ashley Kissinger (PM) |
| **Created Date** | February 7, 2026 |
| **Last Updated** | February 7, 2026 |
| **Version** | 1.0 |

---

## Backlog Overview

This product backlog contains all user stories, epics, and technical tasks for the Smart Task & Risk Dashboard. Items are prioritized based on business value, dependencies, and the Agile release plan (6 sprints, 12 weeks).

**Sprint Schedule:**
- Sprint 1 (Planning): Feb 10-21
- Sprints 2-7 (Development): Feb 24 - Apr 18
- Sprint 8 (UAT & Deploy): Apr 21 - May 1

---

## Epics

### Epic 1: Task Management Dashboard
**Goal**: Enable PMs to view and manage project tasks in a centralized dashboard  
**Business Value**: Eliminate 4 hours/week of manual Excel consolidation  
**Story Points**: ~55 points  
**Target Sprints**: 2-3

### Epic 2: Resource Allocation & Utilization
**Goal**: Provide visibility into team member allocation across projects  
**Business Value**: Prevent resource double-booking conflicts  
**Story Points**: ~34 points  
**Target Sprints**: 3-4

### Epic 3: Risk Management Module
**Goal**: Track and score project risks with automated escalation  
**Business Value**: Eliminate unescalated critical risks  
**Story Points**: ~42 points  
**Target Sprints**: 4-5

### Epic 4: Executive Dashboard & Portfolio View
**Goal**: Give leadership real-time visibility into all projects  
**Business Value**: Replace 3-5 day reporting lag with real-time data  
**Story Points**: ~28 points  
**Target Sprints**: 5-6

### Epic 5: Jira Integration & Automation
**Goal**: Auto-sync task data from Jira every 15 minutes  
**Business Value**: Ensure data accuracy and save manual entry time  
**Story Points**: ~21 points  
**Target Sprints**: 6

### Epic 6: Notifications & Alerts
**Goal**: Automate email notifications for overdue tasks and high risks  
**Business Value**: Proactive issue management  
**Story Points**: ~18 points  
**Target Sprints**: 7

### Epic 7: User Authentication & Security
**Goal**: Secure dashboard with Active Directory SSO and role-based access  
**Business Value**: Compliance with security policies  
**Story Points**: ~13 points  
**Target Sprints**: 7

---

## Product Backlog Items

### High Priority (Sprint 1-3)

| ID | User Story / Task | Epic | Story Points | Assigned To | Status | Sprint | Dependencies |
|----|-------------------|------|--------------|-------------|--------|--------|--------------|
| US-001 | As a PM, I want to see a list of all my project tasks so that I can track what needs to be done | Epic 1 | 5 | | Not Started | 2 | None |
| US-002 | As a PM, I want to filter tasks by status (Not Started, In Progress, Complete, Overdue) so that I can focus on specific work | Epic 1 | 3 | | Not Started | 2 | US-001 |
| US-003 | As a PM, I want to see task priority levels visually (High/Medium/Low) so that I can quickly identify critical work | Epic 1 | 2 | | Not Started | 2 | US-001 |
| US-004 | As a PM, I want to see who is assigned to each task so that I know who to follow up with | Epic 1 | 2 | | Not Started | 2 | US-001 |
| US-005 | As a PM, I want to see task due dates and overdue indicators so that I can manage deadlines proactively | Epic 1 | 3 | | Not Started | 2 | US-001 |
| US-006 | As a PM, I want to filter tasks by project so that I can view one project at a time | Epic 1 | 2 | | Not Started | 3 | US-001 |
| US-007 | As a PM, I want to search for specific tasks by keyword so that I can quickly find work items | Epic 1 | 3 | | Not Started | 3 | US-001 |
| US-008 | As a PM, I want to see a visual progress indicator (% complete) for each project so that I can gauge status at a glance | Epic 1 | 5 | | Not Started | 3 | US-001 |
| US-009 | As a PM, I want to export task lists to CSV so that I can use data in reports or Excel | Epic 1 | 3 | | Not Started | 3 | US-001 |
| TECH-001 | Create RESTful API for task CRUD operations | Epic 1 | 8 | | Not Started | 2 | None |
| TECH-002 | Design PostgreSQL database schema for tasks, projects, resources | Epic 1 | 5 | | Not Started | 2 | None |
| TECH-003 | Build React frontend components for task list view | Epic 1 | 8 | | Not Started | 2 | TECH-001 |

### Medium Priority (Sprint 4-5)

| ID | User Story / Task | Epic | Story Points | Assigned To | Status | Sprint | Dependencies |
|----|-------------------|------|--------------|-------------|--------|--------|--------------|
| US-010 | As a Resource Manager, I want to see team member utilization rates so that I can balance workload | Epic 2 | 8 | | Not Started | 4 | US-001 |
| US-011 | As a Resource Manager, I want to see which team members are assigned to multiple projects so that I can identify conflicts | Epic 2 | 5 | | Not Started | 4 | US-010 |
| US-012 | As a PM, I want to see a visual capacity chart showing who is over/under-utilized so that I can plan assignments | Epic 2 | 8 | | Not Started | 4 | US-010 |
| US-013 | As a PM, I want to view team member skills and expertise so that I can assign appropriate tasks | Epic 2 | 5 | | Not Started | 4 | US-010 |
| US-014 | As a PM, I want alerts when a team member is double-booked so that I can resolve conflicts immediately | Epic 2 | 5 | | Not Started | 4 | US-011 |
| US-015 | As a PM, I want to log project risks with probability and impact ratings so that I can track potential issues | Epic 3 | 8 | | Not Started | 5 | None |
| US-016 | As a PM, I want the system to automatically calculate risk scores (P × I) so that I can prioritize mitigation | Epic 3 | 5 | | Not Started | 5 | US-015 |
| US-017 | As a PM, I want to see risk aging (days open) so that I can address stale risks | Epic 3 | 3 | | Not Started | 5 | US-015 |
| US-018 | As a PM, I want to filter risks by status (Open, Mitigating, Closed) so that I can focus on active risks | Epic 3 | 2 | | Not Started | 5 | US-015 |
| US-019 | As a PM, I want to assign risk owners so that accountability is clear | Epic 3 | 3 | | Not Started | 5 | US-015 |
| US-020 | As a PM, I want to receive email alerts when a risk becomes High priority so that I can take immediate action | Epic 3 | 5 | | Not Started | 5 | US-016 |
| TECH-004 | Implement risk scoring algorithm (Python) | Epic 3 | 8 | | Not Started | 5 | US-016 |
| TECH-005 | Build resource allocation database tables and APIs | Epic 2 | 5 | | Not Started | 4 | TECH-002 |

### Medium-Low Priority (Sprint 6-7)

| ID | User Story / Task | Epic | Story Points | Assigned To | Status | Sprint | Dependencies |
|----|-------------------|------|--------------|-------------|--------|--------|--------------|
| US-021 | As an Executive, I want to see a portfolio dashboard showing all projects (RAG status) so that I can assess overall health | Epic 4 | 13 | | Not Started | 6 | US-001, US-015 |
| US-022 | As an Executive, I want to see key metrics (on-time delivery %, budget variance, risk count) so that I can make informed decisions | Epic 4 | 8 | | Not Started | 6 | US-021 |
| US-023 | As an Executive, I want to drill down from portfolio view into individual projects so that I can investigate issues | Epic 4 | 5 | | Not Started | 6 | US-021 |
| US-024 | As an Executive, I want to export executive summary reports to PDF so that I can share with board members | Epic 4 | 5 | | Not Started | 6 | US-021 |
| US-025 | As a System Admin, I want to configure Jira API connection settings so that task sync works properly | Epic 5 | 5 | | Not Started | 6 | None |
| US-026 | As a PM, I want task data to auto-sync from Jira every 15 minutes so that my dashboard is always current | Epic 5 | 13 | | Not Started | 6 | US-025, TECH-001 |
| US-027 | As a PM, I want to manually trigger a Jira sync if needed so that I can update immediately | Epic 5 | 2 | | Not Started | 6 | US-026 |
| US-028 | As a PM, I want to see the last sync timestamp so that I know how current the data is | Epic 5 | 1 | | Not Started | 6 | US-026 |
| TECH-006 | Build Jira REST API integration service (Python) | Epic 5 | 13 | | Not Started | 6 | US-025 |
| TECH-007 | Implement automated sync scheduler (cron job every 15 min) | Epic 5 | 5 | | Not Started | 6 | TECH-006 |
| US-029 | As a PM, I want to receive a daily email digest of overdue tasks so that I can follow up proactively | Epic 6 | 5 | | Not Started | 7 | US-005 |
| US-030 | As a PM, I want to receive email alerts when a risk is scored as High so that I can take immediate action | Epic 6 | 5 | | Not Started | 7 | US-016 |
| US-031 | As an Executive, I want to receive a weekly portfolio summary email so that I stay informed without logging in | Epic 6 | 5 | | Not Started | 7 | US-021 |
| TECH-008 | Build email notification service (Python + SendGrid API) | Epic 6 | 8 | | Not Started | 7 | None |

### Low Priority (Sprint 7-8)

| ID | User Story / Task | Epic | Story Points | Assigned To | Status | Sprint | Dependencies |
|----|-------------------|------|--------------|-------------|--------|--------|--------------|
| US-032 | As a User, I want to log in using my company Active Directory credentials (SSO) so that I don't need a separate password | Epic 7 | 8 | | Not Started | 7 | None |
| US-033 | As a System Admin, I want to assign role-based permissions (PM, Executive, Read-only) so that users see appropriate data | Epic 7 | 5 | | Not Started | 7 | US-032 |
| US-034 | As a PM, I want to only see projects that I manage so that my dashboard isn't cluttered | Epic 7 | 3 | | Not Started | 7 | US-033 |
| US-035 | As an Executive, I want to see all projects across the portfolio regardless of PM so that I have full visibility | Epic 7 | 2 | | Not Started | 7 | US-033 |
| TECH-009 | Implement Active Directory/SSO integration | Epic 7 | 8 | | Not Started | 7 | None |
| TECH-010 | Build role-based access control (RBAC) middleware | Epic 7 | 5 | | Not Started | 7 | TECH-009 |
| TECH-011 | Security audit and penetration testing | Epic 7 | 8 | | Not Started | 8 | All TECH |
| TECH-012 | Performance testing and optimization | Epic 7 | 5 | | Not Started | 8 | All TECH |
| TECH-013 | Create user documentation and training materials | Epic 7 | 8 | | Not Started | 8 | All US |

---

## Icebox / Future Enhancements (Post-MVP)

*[Items identified but deferred to Phase 2 or later]*

| ID | Description | Reason for Deferral |
|----|-------------|---------------------|
| US-036 | Mobile native apps (iOS/Android) | Out of scope for Phase 1 - responsive web sufficient |
| US-037 | Gantt chart visualization | Nice-to-have, not critical for MVP |
| US-038 | Budget and financial tracking | Handled by existing ERP system |
| US-039 | Client-facing portal | Internal use only in Phase 1 |
| US-040 | AI/ML predictive analytics for risk | Phase 2 opportunity, too complex for MVP |
| US-041 | Integration with Microsoft Project | Out of scope - Jira only for MVP |
| US-042 | Custom report builder | Predefined reports sufficient for MVP |
| US-043 | Real-time collaboration (chat, comments) | Out of scope for Phase 1 |

---

## Story Point Reference

| Points | Complexity | Time Estimate (Dev Hours) |
|--------|------------|---------------------------|
| 1 | Trivial | 1-2 hours |
| 2 | Simple | 2-4 hours |
| 3 | Easy | 4-6 hours |
| 5 | Medium | 6-10 hours (1-1.5 days) |
| 8 | Complex | 10-16 hours (2 days) |
| 13 | Very Complex | 16-24 hours (3 days) |
| 21 | Epic-level | Break down into smaller stories |

---

## Acceptance Criteria Template

Each user story includes acceptance criteria following this format:
- **Given** [context/precondition]
- **When** [action taken]
- **Then** [expected result]

Example (US-001):
- **Given** I am a logged-in PM
- **When** I navigate to the Task Dashboard
- **Then** I see a list of all tasks for my projects with columns: Task Name, Status, Priority, Assignee, Due Date

---

## Velocity Planning

**Estimated Team Velocity**: 40 story points per sprint (2-week sprint)  
**Total Backlog**: ~240 story points  
**Planned Sprints**: 6 development sprints  
**Buffer**: Sprint 7 for fixes, Sprint 8 for UAT/deployment

---

*Product Owner: Sarah Chen*  
*Product Backlog maintained by: Ashley Kissinger, PM*
