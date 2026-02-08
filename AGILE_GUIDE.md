# How This Project Supports Agile/Scrum Ceremonies

## Overview

This Project Management Simulation is structured to support **Agile/Scrum methodology** while maintaining comprehensive PMI/PMBOK documentation standards. This hybrid approach provides both the flexibility of agile practices and the rigor of professional project management documentation.

---

## 🎯 Agile Structure Overview

The project combines:
- **PMI/PMBOK Framework**: 10 knowledge area folders for comprehensive documentation
- **Scrum Practices**: Dedicated agile ceremony support in Task_Management folder
- **Team Simulation**: Role-based personas for realistic agile team dynamics

---

## 📁 How the Folder Structure Supports Agile

### Core Agile Hub: `03_Project_Execution/Task_Management/`

This is your agile command center with:

```
Task_Management/
├── Product_Backlog/          ← Your prioritized product backlog
│   └── Product_Backlog.md    ← All user stories, ranked by priority
├── Sprint_Backlogs/          ← Individual sprint backlogs
│   └── Sprint_01_Backlog.md (you create these)
├── Sprint_Planning/          ← Sprint ceremony templates
│   ├── Sprint_Template.md
│   └── Sprint_Retrospective_Template.md
├── Scrum_Board.md           ← Visual Kanban-style sprint tracking
└── Definition_of_Done.md     ← Team's quality agreement
```

---

## 🔄 Supported Agile Ceremonies

### 1. **Sprint Planning** (Every 2 weeks)

**What You Do**:
- Review [Product_Backlog/Product_Backlog.md](03_Project_Execution/Task_Management/Product_Backlog/Product_Backlog.md)
- Select high-priority user stories for the sprint
- Estimate story points
- Define sprint goal
- Create commitment in Sprint_Backlogs/Sprint_##_Backlog.md

**Where to Document**:
- Create new file: `Sprint_Backlogs/Sprint_01_Backlog.md` (copy from Sprint_Template.md)
- Update [Scrum_Board.md](03_Project_Execution/Task_Management/Scrum_Board.md) with committed stories
- Log planning meeting in [10_Meeting_Minutes/](10_Meeting_Minutes/)

**Files You'll Use**:
- ✅ Sprint_Planning/Sprint_Template.md (copy this for each sprint)
- ✅ Product_Backlog/Product_Backlog.md (source of work items)
- ✅ Scrum_Board.md (track sprint progress visually)

---

### 2. **Daily Standup** (Every day)

**What You Do**:
- Each team persona answers:
  - What did I do yesterday?
  - What will I do today?
  - Any blockers?
- Update task statuses
- Identify and resolve blockers

**Where to Document**:
- Update [Scrum_Board.md](03_Project_Execution/Task_Management/Scrum_Board.md) - move user stories across columns (Backlog → In Progress → In Review → Done)
- Log standups in current Sprint_##_Backlog.md under "Daily Standup Notes"
- Save detailed meeting logs to [07_Stakeholder_Management/Communication_Log/](07_Stakeholder_Management/Communication_Log/)

**Files You'll Use**:
- ✅ Scrum_Board.md (update task status)
- ✅ Sprint_Backlogs/Sprint_##_Backlog.md (daily notes section)
- ✅ 10_Meeting_Minutes/Daily_Standup_Template.md (if you want detailed notes)

---

### 3. **Sprint Review** (End of each sprint)

**What You Do**:
- Demo completed work to stakeholders (self-review or record video)
- Review which user stories met Definition of Done
- Get acceptance/feedback
- Move incomplete work back to Product Backlog

**Where to Document**:
- Complete "Sprint Review" section in Sprint_##_Backlog.md
- Update [Scrum_Board.md](03_Project_Execution/Task_Management/Scrum_Board.md) - mark completed items as "Done"
- Log meeting in [10_Meeting_Minutes/](10_Meeting_Minutes/)
- Update [04_Monitoring_and_Controlling/Status_Reports/](04_Monitoring_and_Controlling/Status_Reports/) with sprint results

**Files You'll Use**:
- ✅ Sprint_Backlogs/Sprint_##_Backlog.md (Sprint Review section)
- ✅ Definition_of_Done.md (verify all criteria met)
- ✅ Status_Reports/ (create sprint completion report)

---

### 4. **Sprint Retrospective** (End of each sprint, after review)

**What You Do**:
- Reflect on the sprint process (not the product)
- Identify what went well
- Identify what could improve
- Create action items for next sprint
- Update team practices

**Where to Document**:
- Use [Sprint_Planning/Sprint_Retrospective_Template.md](03_Project_Execution/Task_Management/Sprint_Planning/Sprint_Retrospective_Template.md)
- Save completed retro as: `Sprint_Planning/Sprint_01_Retrospective.md`
- Action items go to [04_Monitoring_and_Controlling/Issue_Log.md](04_Monitoring_and_Controlling/Issue_Log.md)
- Lessons learned go to [05_Project_Closeout/Lessons_Learned.md](05_Project_Closeout/Lessons_Learned.md)

**Files You'll Use**:
- ✅ Sprint_Retrospective_Template.md (copy for each sprint)
- ✅ Issue_Log.md (track action items)
- ✅ Lessons_Learned.md (document insights)

---

### 5. **Backlog Grooming/Refinement** (Mid-sprint or as needed)

**What You Do**:
- Review upcoming user stories
- Clarify acceptance criteria
- Estimate story points
- Prioritize and reorder backlog
- Break down large stories into smaller ones

**Where to Document**:
- Update [Product_Backlog/Product_Backlog.md](03_Project_Execution/Task_Management/Product_Backlog/Product_Backlog.md)
- Add new user stories as you identify them
- Adjust priorities based on learning/feedback
- Document grooming decisions in Communication_Log/

**Files You'll Use**:
- ✅ Product_Backlog.md (the living backlog)
- ✅ Requirements_Documentation.md (source of user stories)

---

## 📊 Daily Agile Workflow

### As a Project Manager (You), here's your daily routine:

1. **Morning - Standup** (5-15 min)
   - Review [Scrum_Board.md](03_Project_Execution/Task_Management/Scrum_Board.md)
   - Role-play each team member's update (or use ChatGPT voice for realistic simulation)
   - Update task statuses: move cards across board
   - Log standup notes in current Sprint backlog

2. **During Day - Execution**
   - Work on tasks (coding, documentation, design, testing)
   - Update Scrum_Board.md as work progresses
   - Log blockers in [Issue_Log.md](04_Monitoring_and_Controlling/Issue_Log.md)
   - Communicate decisions in Communication_Log/

3. **End of Day - Wrap-Up**
   - Update burndown in Sprint_##_Backlog.md
   - Review Definition of Done for completed work
   - Prepare tomorrow's standup updates

---

## 🎨 Using the Scrum Board

[Scrum_Board.md](03_Project_Execution/Task_Management/Scrum_Board.md) is your visual dashboard:

### Board Columns:
1. **📋 BACKLOG** - Work selected for this sprint, not started
2. **🔄 IN PROGRESS** - Currently being worked on (limit 1-2 per person!)
3. **👀 IN REVIEW** - Code review, QA testing, or approval needed
4. **✅ DONE** - Meets Definition of Done, complete

### How to Use:
- **Add rows** to each section for your user stories
- **Move user stories** between sections by editing the markdown tables
- **Update metrics** at the top (story points completed, days remaining, etc.)
- **Track blockers** in the Blockers section
- **Update daily** - this is your single source of truth for sprint progress

---

## 🔗 How Agile Integrates with PMI Documentation

Your project uniquely combines agile execution with traditional PM documentation:

| Agile Artifact | PMI/PMBOK Document | How They Connect |
|----------------|-------------------|------------------|
| Product Backlog | Requirements_Documentation.md | Backlog sourced from requirements |
| Sprint Backlog | Task_Management/*.md | Sprint tasks aligned with WBS/schedule |
| Burndown Chart | Status_Reports/ | Sprint progress reported to stakeholders |
| Retrospective | Lessons_Learned.md | Process improvements captured |
| Definition of Done | Quality_Management_Plan.md | Quality standards defined |
| Velocity Tracking | Status_Reports/ | Team performance metrics |
| Sprint Reviews | Meeting_Minutes/ | Stakeholder demos documented |
| Blockers/Impediments | Issue_Log.md, Risk_Management/ | Issues & risks tracked formally |

This integration means:
- ✅ You practice agile (fast, iterative, adaptive)
- ✅ You maintain professional documentation (auditable, complete, PMI-compliant)
- ✅ You demonstrate both skillsets to employers

---

## 📝 Template Workflow Example

### Starting Sprint 1

1. **Sprint Planning Meeting**
   ```bash
   # Copy sprint template
   cp Sprint_Planning/Sprint_Template.md Sprint_Backlogs/Sprint_01_Backlog.md
   ```

2. **Fill out Sprint 01 Backlog**
   - Set sprint goal
   - Select user stories from Product_Backlog.md
   - Assign story points
   - Break into tasks
   - Assign to team members (personas)

3. **Update Scrum Board**
   - Add all sprint user stories to "BACKLOG" section of Scrum_Board.md
   - Set sprint dates and goals at top

4. **Daily Execution**
   - Each day: update Scrum_Board.md (move cards)
   - Each day: add standup notes to Sprint_01_Backlog.md
   - Track blockers in Issue_Log.md

5. **Sprint End**
   - Fill out Sprint Review section in Sprint_01_Backlog.md
   - Copy Sprint_Retrospective_Template.md → Sprint_01_Retrospective.md
   - Complete retrospective
   - Move incomplete work back to Product_Backlog.md

6. **Repeat** for Sprint 2, 3, 4...

---

## 🎓 Simulating Team Interactions

### Using ChatGPT Voice for Realistic Meetings

You can simulate agile ceremonies using ChatGPT Voice Mode:

1. **Before the Meeting**:
   - Prepare agenda in meeting template
   - Review relevant documents (backlog, board, etc.)

2. **During the Meeting** (ChatGPT Voice):
   - Say: "Let's have our sprint planning meeting. You play [Alex, Jordan, Sam, Riley]. I'm Ashley, the PM."
   - Go through ceremony steps naturally
   - ChatGPT will role-play each persona based on their personalities in Team_Directory.md

3. **After the Meeting**:
   - Save meeting notes to Communication_Log/2026-02-##_Meeting.md
   - Update relevant documents (backlog, board, action items)

### Example Prompt for Sprint Planning:
```
"Let's simulate our Sprint 1 Planning Meeting. I'm Ashley Kissinger, Project Manager. 
You'll role-play Alex (BA), Jordan (Developer), Sam (Designer), and Riley (QA).

We need to:
1. Define our Sprint 1 goal
2. Select user stories from our product backlog
3. Estimate story points
4. Assign work

The sprint runs Feb 10-21. Let's discuss what we can commit to delivering."
```

---

## ✅ Agile Success Checklist

Use this to ensure you're getting the full agile experience:

### Sprint Planning
- [ ] Product backlog is prioritized
- [ ] Sprint goal is clear and achievable
- [ ] User stories are estimated with story points
- [ ] Team has committed to sprint backlog
- [ ] Sprint backlog document created
- [ ] Scrum board updated

### Daily Standups
- [ ] Happening daily (or at least 3x/week)
- [ ] Each persona provides update
- [ ] Blockers identified and addressed
- [ ] Scrum board updated
- [ ] Notes logged

### Sprint Review
- [ ] Completed work demonstrated
- [ ] Definition of Done verified
- [ ] Stakeholder feedback received
- [ ] Incomplete work moved back to backlog
- [ ] Velocity calculated

### Sprint Retrospective
- [ ] What went well identified
- [ ] Improvements identified
- [ ] Action items created with owners
- [ ] Process changes documented
- [ ] Team commitment to improvements

### Backlog Management
- [ ] Product backlog is living document
- [ ] New stories added as discovered
- [ ] Stories refined with acceptance criteria
- [ ] Backlog reprioritized regularly
- [ ] Technical debt tracked

---

## 🚀 Getting Started with Your First Sprint

### Ready to begin? Here's your action plan:

1. **✅ Fill out Product_Backlog.md** (30 minutes)
   - Add 10-15 user stories for your dashboard features
   - Prioritize them (High/Medium/Low)
   - Estimate story points (1, 2, 3, 5, 8, 13)

2. **✅ Hold Sprint Planning** (1 hour)
   - Copy Sprint_Template.md → Sprint_01_Backlog.md
   - Select 5-8 user stories for Sprint 1
   - Define sprint goal
   - Break stories into tasks

3. **✅ Setup Scrum Board** (15 minutes)
   - Add Sprint 1 stories to Scrum_Board.md
   - Set sprint dates
   - Initialize metrics

4. **✅ Start Daily Execution**
   - Daily standups
   - Update board
   - Code/design/test

5. **✅ End Sprint 1** (2 hours)
   - Sprint Review
   - Sprint Retrospective
   - Celebrate! 🎉

---

## 📚 Additional Resources

### Templates You Can Use:
- [Sprint_Template.md](03_Project_Execution/Task_Management/Sprint_Planning/Sprint_Template.md) - Copy for each sprint
- [Sprint_Retrospective_Template.md](03_Project_Execution/Task_Management/Sprint_Planning/Sprint_Retrospective_Template.md) - Copy for each retro  
- [Daily_Standup_Template.md](10_Meeting_Minutes/Templates/Daily_Standup_Template.md) - For detailed standup notes
- [Meeting_Minutes_Template.md](10_Meeting_Minutes/Templates/Meeting_Minutes_Template.md) - For any agile ceremony

### Reference Documents:
- [Definition_of_Done.md](03_Project_Execution/Task_Management/Definition_of_Done.md) - Your quality standard
- [Team_Directory.md](03_Project_Execution/Team_Management/Team_Directory.md) - Team member personas
- [Communication_Management_Plan.md](02_Project_Planning/Communication_Management_Plan.md) - How team communicates

---

## ❓ Common Questions

**Q: Do I need to simulate all team members every day?**  
A: You can simplify! Focus on 2-3 key updates per standup. As you code, switch "hats" between developer, PM, and QA perspectives.

**Q: How long should sprints be?**  
A: Recommended 1-2 weeks for this project. Shorter sprints = more practice with ceremonies.

**Q: Do I need to fill out EVERY document?**  
A: No! Focus on agile essentials (Product Backlog, Sprint Backlogs, Scrum Board, Retros). Fill PMI documents as they add value.

**Q: Can I skip ceremonies?**  
A: You can, but you'll miss valuable practice! Retros especially teach you to improve your process.

**Q: How do I track story points if I'm working alone?**  
A: Use time as proxy: 1 point = 1-2 hours, 3 points = half day, 5 points = full day, 8 points = 2 days, 13 points = too big, break it down!

---

## 🎯 Final Notes

This structure gives you **authentic agile experience** while building an impressive portfolio project. You'll learn:
- How to prioritize work (product backlog management)
- How to estimate effort (story points)
- How to track progress (burndown, velocity)
- How to iterate and improve (retrospectives)
- How to communicate in agile teams (ceremonies, standups)

And you'll have **professional documentation** proving you can manage projects using industry standards!

**Ready to start your first sprint?** Begin with Product_Backlog.md and go from there! 🚀

---

*Guide created: February 7, 2026*  
*Owner: Ashley Kissinger, Project Manager*
