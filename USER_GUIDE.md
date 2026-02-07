# Project Management Simulation

A comprehensive project management simulation designed to replicate real-world PM workflows. This interactive command-line application allows you to practice managing software development projects with realistic challenges including missed deadlines, team conflicts, and scope changes.

## Features

### Core Functionality
- **Project Planning**: Work breakdown structures with task dependencies
- **Task Tracking**: Monitor task status, progress, and completion
- **Team Coordination**: Manage team members with different skills and productivity levels
- **Issue Resolution**: Handle technical issues, conflicts, and blockers
- **Progress Reporting**: Generate comprehensive status reports and metrics

### Realistic Challenges
- **Missed Deadlines**: Tasks can become overdue, affecting team morale and project schedule
- **Team Conflicts**: Random conflicts between team members reduce productivity
- **Scope Changes**: Unexpected requirement changes add work to the project
- **Technical Issues**: Bugs and integration problems can block task progress
- **Resource Constraints**: Team members have varying availability and capacity

### Project Scenarios
1. **E-Commerce Web Application**: 60-day project with 6 team members
   - Full-stack development with frontend, backend, and DevOps
   - 25 tasks across planning, development, testing, and deployment phases
   - Budget: $150,000

2. **Fitness Tracking Mobile App**: 45-day project with 4 team members
   - Cross-platform mobile development
   - 9 tasks from design to app store submission
   - Budget: $80,000

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ashleykissinger45-dev/Project-Management-Simulation.git
   cd Project-Management-Simulation
   ```

2. No additional dependencies required - uses only Python standard library!

## Usage

### Running the Simulation
```bash
python simulation_cli.py
```

### Main Menu Options
1. **View Project Status**: Overview of project health, progress, and metrics
2. **View Tasks**: Detailed task list with filtering by status
3. **View Team**: Team member details including morale and current assignments
4. **View Issues**: Open and resolved issues affecting the project
5. **Assign Tasks**: Assign available tasks to team members
6. **Resolve Issue**: Address and resolve project issues
7. **Advance Time**: Progress the simulation by one day
8. **Generate Status Report**: Comprehensive project status report
9. **Exit Simulation**: Exit the application

### Gameplay Tips
- **Start by assigning tasks**: Assign tasks to team members based on their skills and availability
- **Monitor team morale**: Low morale reduces productivity - resolve conflicts quickly
- **Watch for blockers**: Resolve issues immediately to unblock tasks
- **Balance workload**: Don't overload team members with too many concurrent tasks
- **Plan for delays**: Random events can delay your schedule - build in buffer time
- **Review reports regularly**: Generate status reports to track budget and schedule

## Architecture

### Core Components

#### 1. Data Models (`models.py`)
- **Project**: Main project container with tasks, team, and timeline
- **Task**: Individual work items with dependencies, estimates, and status
- **TeamMember**: Team members with skills, productivity, and morale
- **Issue**: Problems and blockers that need resolution

#### 2. Simulation Engine (`simulation_engine.py`)
- **Time Progression**: Day-by-day simulation advancement
- **Task Execution**: Automatic progress on assigned tasks
- **Event Generation**: Random events (conflicts, scope changes, issues)
- **Metrics Tracking**: Budget, schedule, and morale tracking

#### 3. Scenarios (`scenarios.py`)
- **Predefined Projects**: Ready-to-run project templates
- **Task Dependencies**: Realistic work breakdown structures
- **Team Composition**: Balanced teams with complementary skills

#### 4. CLI Interface (`simulation_cli.py`)
- **Interactive Menus**: User-friendly command-line interface
- **Status Displays**: Visual progress bars and formatted output
- **Decision Points**: Task assignment and issue resolution

## Project Metrics

### Progress Tracking
- **Completion Percentage**: Tasks completed vs. total tasks
- **Schedule Status**: On track or behind schedule
- **Budget Usage**: Spent vs. allocated budget
- **Team Morale**: Average team happiness (affects productivity)

### Task States
- **Not Started**: Task awaiting assignment
- **In Progress**: Actively being worked on
- **Blocked**: Cannot progress due to issues
- **Completed**: Successfully finished
- **Overdue**: Past the due date

### Issue Types
- **Technical**: Bugs, integration failures, performance issues
- **Resource**: Availability and capacity problems
- **Scope**: Requirements changes and additions
- **Communication**: Team conflicts and breakdowns
- **Quality**: Quality assurance problems

## Educational Value

This simulation helps develop:
- **Planning Skills**: Creating work breakdown structures and task dependencies
- **Resource Management**: Assigning work based on skills and capacity
- **Risk Management**: Identifying and mitigating project risks
- **Problem Solving**: Handling unexpected challenges and setbacks
- **Decision Making**: Prioritizing tasks and resolving conflicts
- **Time Management**: Balancing schedule constraints and quality
- **Stakeholder Communication**: Generating status reports and updates

## Customization

### Creating New Scenarios
Add new project scenarios in `scenarios.py`:

```python
def create_custom_project() -> Project:
    project = Project(
        name="My Project",
        description="Project description",
        start_date=datetime.now(),
        deadline=datetime.now() + timedelta(days=30),
        budget=50000.0
    )
    
    # Add team members
    project.add_team_member(TeamMember(
        name="Developer",
        role="Developer",
        skills=["python", "javascript"],
        productivity=1.0,
        availability=1.0
    ))
    
    # Add tasks
    project.add_task(Task(
        task_id="T001",
        name="Task Name",
        description="Description",
        estimated_hours=40,
        priority=TaskPriority.HIGH,
        required_skills=["python"],
        dependencies=[]
    ))
    
    return project
```

### Adjusting Difficulty
Modify event probabilities in `simulation_engine.py`:
- Team conflicts: Default 5% per day
- Scope changes: Default 3% per day
- Technical issues: Default 7% per day
- Availability issues: Default 4% per day

## Examples

### Sample Session
```
=================================================================================
                         PROJECT MANAGEMENT SIMULATION
=================================================================================

Welcome to the comprehensive project management simulation!
Practice managing real-world projects with realistic challenges.

Select a project scenario:
1. E-Commerce Web Application (60 days, 6 team members)
2. Fitness Tracking Mobile App (45 days, 4 team members)
3. Exit

Enter your choice (1-3): 1

Project: E-Commerce Web Application
Timeline: 2026-02-07 to 2026-04-08
Budget: $150,000.00
Team Size: 6 members
Total Tasks: 25

MAIN MENU
1. View Project Status
2. View Tasks
3. View Team
...
```

## Contributing

Contributions are welcome! Areas for enhancement:
- Additional project scenarios
- More event types and challenges
- Advanced scheduling algorithms
- Gantt chart visualization
- Export reports to file
- Save/load game state
- Multiplayer mode

## License

This project is open source and available for educational purposes.

## Credits

Created as a comprehensive project management training tool to help developers and project managers practice real-world scenarios in a safe, simulated environment.
