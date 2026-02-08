# � SprintLab: The Agile Project Management Experience

**Current Project**: Smart Task & Risk Dashboard for TechFlow Solutions

An immersive, hands-on Agile project management simulation where you act as the Project Manager for a real-world software development initiative. Manage sprints, coordinate a development team, track user stories, mitigate risks, and deliver a production dashboard—all following professional PMI/PMBOK standards and Scrum methodology.

## 🎯 Project Overview

**You are**: Ashley Kissinger, Project Manager at TechFlow Solutions  
**Your Mission**: Deliver a Smart Task & Risk Dashboard to consolidate project tracking and eliminate fragmented PM tools causing 23% deadline overruns

**Project Details**:
- **Company**: TechFlow Solutions (250-employee software consulting firm)
- **Budget**: $85,000
- **Timeline**: 12 weeks (Feb 10 - May 1, 2026)
- **Methodology**: Agile/Scrum with 2-week sprints
- **Team**: 2 Developers (Jordan Martinez, Jamie Park), 1 Designer (Sam Kim), 1 QA (Riley Thompson)
- **Sponsor**: Sarah Chen, VP of Delivery Operations
- **Success Criteria**: Dashboard deployed, 100% PM adoption, 40% reduction in admin time, zero unescalated critical risks

## 💼 The Business Problem

TechFlow's 12 project managers currently use fragmented tools (Excel, Jira, email) to track tasks, resources, and risks. This inefficiency has resulted in:

- **23% increase** in deadline overruns (Q4 2025)
- **$150K in penalty fees** from missed project milestones
- **Resource conflicts**: Double-booking incidents across projects
- **6-8 hours/week** PM time spent on manual status reporting
- **Critical risks** becoming issues due to delayed escalation
- **Client NPS score of 52** (target: 75+)

Your dashboard will provide a single source of truth with real-time visibility, automated Jira task sync, risk scoring algorithms, and executive portfolio views.

## ✨ Project Deliverables

### Core Features (240 Story Points Across 7 Epics)

1. **📋 Task Management Dashboard** (55 pts)
   - Real-time task list with status, priority, assignee, deadline
   - Filtering by project, assignee, status, priority
   - Visual progress indicators and overdue flags
   - CSV export capability

2. **👥 Resource Allocation & Utilization** (34 pts)
   - Team member capacity and utilization rates
   - Conflict detection for double-bookings
   - Skill-based resource matching
   - Visual capacity charts

3. **⚠️ Risk Management Module** (42 pts)
   - Risk register with probability/impact ratings
   - Automated risk scoring algorithm (P × I + aging)
   - Risk trend analysis and aging indicators
   - Escalation alerts for high-priority risks

4. **📊 Executive Dashboard** (28 pts)
   - Portfolio health overview (all projects)
   - Key metrics: on-time delivery %, budget variance, risk exposure
   - RAG status (Red/Amber/Green) project summaries
   - Drill-down capability into individual projects

5. **🔄 Jira Integration** (21 pts)
   - Automated task sync from Jira API every 15 minutes
   - Manual sync trigger capability
   - Last sync timestamp visibility

6. **📧 Automated Notifications** (18 pts)
   - Daily email digest: overdue tasks, high risks, resource conflicts
   - Threshold alerts for critical risks
   - Weekly portfolio summary for executives

7. **🔐 User Authentication & Security** (13 pts)
   - Active Directory SSO integration
   - Role-based access control (PM, Executive, Read-only)
   - Project visibility based on user role

## 🛠️ Technology Stack

### Frontend
- **React.js**: Component-based UI framework
- **HTML5/CSS3**: Responsive design with Flexbox/Grid
- **JavaScript ES6+**: Modern frontend logic

### Backend
- **Python Flask** or **Java Spring Boot**: REST API (TBD in Sprint 1)
- **PostgreSQL 14+**: Database for dashboard data
- **Jira REST API v3**: Integration for task synchronization

### DevOps & Tools
- **Git/GitHub**: Version control with GitHub Actions CI/CD
- **AWS**: EC2 for hosting, RDS for database (or on-premises)
- **SendGrid API**: Automated email notifications
- **Active Directory**: SSO authentication

### Automation Scripts
- **Python**: Jira sync scheduler (every 15 min)
- **Python**: Risk scoring algorithm
- **Python**: Email notification service
- **Cron jobs**: Automated database backups

## 📁 Project Structure

This project follows **PMI/PMBOK standards** with **Agile/Scrum execution**:

```
SprintLab/
│
├── README.md                           # This file
├── AGILE_GUIDE.md                     # How to use agile ceremonies
│
├── 01_Project_Initiation/             # Initiation documents
│   ├── Business_Case as Project Manager

### Prerequisites

- Modern web browser (Chrome, Firefox, Safari, Edge)
- Git installed
- Code editor (VS Code recommended)
- Python 3.9+ or Java 11+ (for backend development)
- PostgreSQL 14+ (local or Docker)

### Your First Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/ashleykissinger45-dev/SprintLab-The-Agile-Project-Management-Experience.git
   cd "Project Management Simulation"
   ```

2. **Read your project assignment**
   ```bash
   # Start with these documents in order:
   # 1. 2_Scenario.md - Understand the business problem
   # 2. 3_Project_Charter.md - Review scope, budget, timeline
   # 3. 01_Project_Initiation/Stakeholder_Register.md - Know your stakeholders
   # 4. 03_Project_Execution/Task_Management/Product_Backlog.md - See all 43 user stories
   # 5. AGILE_GUIDE.md - Learn how to run agile ceremonies
   ```

3. **Prepare for Sprint 1 kickoff (February 10, 2026)**
   - Review the complete product backlog (240 story points)
   - Identify Sprint 1 user stories (target: ~40 story points)
   - Plan your first sprint planning meeting
   - Set up your Scrum board
Key Project Documents

### Must-Read Documents
1. **[Project Scenario](2_Scenario.md)** - Complete business context and problem statement
2. **[Project Charter](3_Project_Charter.md)** - Official project authorization with scope, budget, timeline
3. **[Product Backlog](03_Project_Execution/Task_Management/Product_Backlog/Product_Backlog.md)** - 43 user stories you need to deliver
4. **[Stakeholder Register](01_Project_Initiation/Stakeholder_Register.md)** - 14 stakeholders with power/interest analysis
5. **[AGILE_GUIDE.md](AGILE_GUIDE.md)** - Complete guide to running agile ceremonies in this project

### Working Documents You'll Fill Out
- **Sprint Backlogs**: Create one per sprint from template
- **Scrum Board**: Update daily with task progress
- **Communication Log**: Record all team meetings and decisions
- **Status Reports**: Weekly progress updates for sponsor
- **Issue Log**: Track blockers and impediments
- **Risk Log**: Identify and manage project risks
- **Retrospectives**: Document lessons learned after each sprint

## 🎯 Your Success Metrics

As PM, you're accountable for:

| Metric | Target | Baseline | Measurement |
|--------|--------|----------|-------------|
| **Deployment Date** | May 1, 2026 | N/A | Hard deadline for client proposal |
| **PM Admin Time** | 4 hrs/week | 7 hrs/week | 40% reduction via automation |
| **Deadline Overruns** | ≤17% | 23% | 25% improvement |
| **Unescalated Critical Risks** | 0 per quarter | 2 per quarter | Risk log tracking |
| **Dashboard Adoption** | 100% (12/12 PMs) | 0% | Login analytics |
| **Client NPS** | 75+ | 52 | +23 point improvement |
| **Jira Sync Latency** | ≤15 minutes | Manual entry | Automated integration |

## 📅 Sprint Schedule

| Sprint | Dates | Focus | Story Points |
|--------|-------|-------|--------------|
| **Sprint 1** | Feb 10-21 | Planning, requirements, design, architecture | ~40 |
| **Sprint 2** | Feb 24-Mar 7 | Task management dashboard MVP | ~40 |
| **Sprint 3** | Mar 10-21 | Task features + resource allocation start | ~40 |
| **Sprint 4** | Mar 24-Apr 4 | Resource allocation + risk module start | ~40 |
| **Sprint 5** | Apr 7-18 | Risk module + executive dashboard | ~40 |
| **Sprint 6** | Apr 21-May 1 | Jira integration + notifications | ~40 |

**Total**: 240 story points across 6 sprints

## 💡 What You'll Experience

### Agile/Scrum Ceremonies You'll Run
- ✅ **Sprint Planning** (every 2 weeks): Select user stories, estimate, commit
- ✅ **Daily Standups** (daily): Team updates, blockers, progress
- ✅ **Sprint Reviews** (end of sprint): Demo completed work
- ✅ **Sprint Retrospectives** (end of sprint): Process improvements
- ✅ **Backlog Grooming** (mid-sprint): Refine upcoming stories

### Project Management Skills You'll Practice
- ✅ Stakeholder management and communication
- ✅ Sprint planning and backlog prioritization
- ✅ Risk identification and mitigation
- ✅ Team coordination and conflict resolution
- ✅ Status reporting and executive communication
- ✅ Scope management and change control
- ✅ Quality assurance and Definition of Done
- ✅ Velocity tracking and burndown charts
- ✅ Budget monitoring and resource allocation

### Technical Skills You'll Apply
- ✅ Full-stack web development (React + Python/Java)
- ✅ RESTful API design and implementation
- ✅ Database design (PostgreSQL)
- ✅ API integration (Jira REST API)
- ✅ Automation scripting (Python)
- ✅ Git version control and CI/CD
- ✅ Security implementation (SSO, RBAC)
- ✅ Performance testing and optimiz              # Quality standards
│   └── Quality_Management_Plan.md
│
├── 09Who This Is For

- **Aspiring Project Managers**: Get hands-on experience managing a real project without instructions
- **Agile Practitioners**: Practice Scrum ceremonies and agile principles
- **Full-Stack Developers**: Build a complete dashboard application with modern tech stack
- **Career Changers**: Demonstrate both PM and technical skills in one portfolio project
- **Students**: Learn project management by doing, not just reading
- **Portfolio Builders**: Showcase ability to deliver complex projects end-to-end

## 🎯 Learning Outcomes

By completing this project, you will:

1. **Manage a realistic agile project** from kickoff to deployment
2. **Run authentic Scrum ceremonies** (planning, standups, reviews, retros)
3. **Coordinate a cross-functional team** (dev, design, QA)
4. **Navigate stakeholder expectations** with varying power/interest levels
5. **Make PM decisions autonomously** without step-by-step instructions
6. **Deliver working software** solving a real business problem
7. **Track velocity and burndown** like real agile teams
8. **Handle risks proactively** before they become issues
9. **Document professionally** following PMI/PMBOK standards
10. **Build a portfolio piece** demonstrating multi-disciplinary expertise

## 🤝 Team Simulation

Your team consists of personas with distinct roles and personalities:

- **Jordan Martinez** (Senior Full Stack Developer): 8 years experience, Python/React expert, pragmatic, focuses on clean code
- **Jamie Park** (Backend Developer): 4 years experience, Java specialist, detail-oriented, security-conscious
- **Sam Kim** (UI/UX Designer): 6 years experience, user-centric, collaborative, advocates for simplicity
- **Riley Thompson** (QA Engineer): 5 years experience, thorough, quality-focused, catches edge cases

**Tip**: Use ChatGPT Voice Mode to simulate realistic team meetings and conversations!

## 📊 Project Complexity

This is an **intermediate-to-advanced** simulation:

### Complexity Factors
- 43 user stories across 7 epics (240 story points)
- 14 stakeholders with competing interests
- $85K budget with 15% contingency
- 12-week timeline with hard deadline
- Integration dependencies (Jira API)
- Security requirements (SSO, RBAC)
- Multiple user roles (PM, Executive, Read-only)
- Production deployment expectations

### What Makes It Realistic
- ❌ **No step-by-step instructions** - figure it out like a real PM
- ✅ **Authentic constraints** - budget, timeline, resources
- ✅ **Real dependencies** - waiting on IT Security for API access
- ✅ **Stakeholder pressures** - sponsor wants demo for $2M client
- ✅ **Technical decisions** - Python vs. Java, AWS vs. on-prem
- ✅ **Scope management** - stakeholders will want more features
- ✅ **Risk management** - API downtime, resource availability, security vulnerabilities

## 🚧 Project Status

**Phase**: Initiation → Planning (Ready for Sprint 1)  
**Kickoff Date**: February 10, 2026  
**Current Status**: Project chartered and authorized  
**Next Milestone**: Sprint 1 Planning Meeting  
**Days Until Deadline**: 83 days (May 1, 2026)

## 📧 Stakeholder Contacts

**Project Sponsor**: Sarah Chen (sarah.chen@techflowsolutions.com) - Weekly check-ins Friday 11 AM  
**PMO Director**: Michael Rodriguez (michael.rodriguez@techflowsolutions.com) - PMO alignment  
**CTO**: David Park (david.park@techflowsolutions.com) - Technical architecture approval  
**IT Security**: Maya Patel (maya.patel@techflowsolutions.com) - Jira API access needed by Feb 12

## 🔗 Important Links

- **Repository**: [SprintLab-The-Agile-Project-Management-Experience](https://github.com/ashleykissinger45-dev/SprintLab-The-Agile-Project-Management-Experience)
- **Project Charter**: [3_Project_Charter.md](3_Project_Charter.md)
- **Product Backlog**: [Product_Backlog.md](03_Project_Execution/Task_Management/Product_Backlog/Product_Backlog.md)
- **Agile Guide**: [AGILE_GUIDE.md](AGILE_GUIDE.md)
- **Scrum Board**: [Scrum_Board.md](03_Project_Execution/Task_Management/Scrum_Board.md)

## ⚠️ Important Notes

1. **This is a simulation** - You are the only person, but you manage multiple personas
2. **No external dependencies** - Build what you can, simulate integrations if needed
3. **Focus on PM practice** - The dashboard is secondary to learning project management
4. **Document everything** - Real PMs create extensive documentation
5. **Iterate and improve** - Use retrospectives to enhance your process
6. **It's okay to struggle** - Real projects are complex; figuring it out is the learning

## 🎉 Getting Started Challenge

**Your first PM task**: Review all project documents and prepare for the Sprint 1 planning meeting on February 10, 2026. What user stories will you commit to? How will you organize your first sprint?

**No one will tell you what to do. That's the point. You're the PM.** 🚀
   # Option 2: Use a local server (recommended)
   cd 9_WebApp
   python3 -m http.server 8000
   # Then navigate to http://localhost:8000
   ```

3. **Start exploring!**
   - View project metrics and team members
   - Track tasks and update their status
   - Monitor identified risks
   - Review weekly progress reports

## 📖 Documentation

This README provides:

- Complete project overview and objectives
- Project scope and methodology
- Team roles and responsibilities
- Task management, risk tracking, and reporting processes
- Budget planning and monitoring
- WebApp dashboard overview and usage
- Suggested next steps and future enhancements

## 💡 What You'll Learn

### Technical Skills
- ✅ Building responsive web applications with HTML/CSS/JavaScript
- ✅ Using Git for version control and collaboration
- ✅ Frontend architecture and best practices
- ✅ DOM manipulation and event handling
- ✅ Debugging with browser DevTools

### Project Management Skills
- ✅ Task breakdown and tracking
- ✅ Team coordination and role assignment
- ✅ Risk identification and mitigation
- ✅ Status reporting and metrics tracking
- ✅ Professional documentation

## 🎓 Use Cases

- **Students**: Learn web development and project management fundamentals
- **Self-learners**: Build portfolio projects demonstrating multiple skills
- **Bootcamps**: Practical application for teaching PM and development concepts
- **Interview Prep**: Showcase technical and organizational capabilities
- **Team Training**: Template for real project workflows

## 🤝 Contributing

This is an educational project. Feel free to fork, modify, and adapt it for your own learning purposes!

## 📝 Project Status

**Current Phase**: Active Development  
**Last Updated**: February 7, 2026  
**Version**: 1.0

## 📧 Contact

**Project Maintainer**: Ashley Kissinger  
**Repository**: [Project-Management-Simulation](https://github.com/ashleykissinger45-dev/Project-Management-Simulation)

## 📄 License

This project is provided for educational and personal use.

---

⭐ **Star this repo** if you find it helpful for learning web development and project management!
