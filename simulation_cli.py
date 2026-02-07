"""
Command-line interface for the Project Management Simulation.
"""
import sys
from datetime import datetime
from typing import Optional
from models import Project, Task, TeamMember, TaskStatus
from simulation_engine import SimulationEngine
from scenarios import create_web_app_project, create_mobile_app_project


class SimulationCLI:
    """Command-line interface for managing the simulation."""
    
    def __init__(self, project: Project):
        self.project = project
        self.engine = SimulationEngine(project)
        self.running = True
    
    def run(self):
        """Main simulation loop."""
        self.print_header()
        self.print_project_info()
        
        while self.running:
            self.print_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.view_status()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.view_team()
            elif choice == "4":
                self.view_issues()
            elif choice == "5":
                self.assign_tasks()
            elif choice == "6":
                self.resolve_issue()
            elif choice == "7":
                self.advance_simulation()
            elif choice == "8":
                self.generate_report()
            elif choice == "9":
                self.running = False
                print("\n👋 Thank you for using the Project Management Simulation!")
            else:
                print("\n❌ Invalid choice. Please try again.")
            
            if self.running and choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                input("\nPress Enter to continue...")
    
    def print_header(self):
        """Print simulation header."""
        print("=" * 80)
        print("PROJECT MANAGEMENT SIMULATION".center(80))
        print("=" * 80)
        print("\nWelcome to the comprehensive project management simulation!")
        print("Practice managing real-world projects with realistic challenges.\n")
    
    def print_project_info(self):
        """Print project information."""
        print(f"Project: {self.project.name}")
        print(f"Description: {self.project.description}")
        print(f"Timeline: {self.project.start_date.strftime('%Y-%m-%d')} to {self.project.deadline.strftime('%Y-%m-%d')}")
        print(f"Budget: ${self.project.budget:,.2f}")
        print(f"Team Size: {len(self.project.team)} members")
        print(f"Total Tasks: {len(self.project.tasks)}")
        print()
    
    def print_menu(self):
        """Print main menu."""
        print("\n" + "=" * 80)
        print("MAIN MENU".center(80))
        print("=" * 80)
        print("1. View Project Status")
        print("2. View Tasks")
        print("3. View Team")
        print("4. View Issues")
        print("5. Assign Tasks")
        print("6. Resolve Issue")
        print("7. Advance Time (1 day)")
        print("8. Generate Status Report")
        print("9. Exit Simulation")
    
    def view_status(self):
        """Display project status overview."""
        print("\n" + "=" * 80)
        print("PROJECT STATUS OVERVIEW".center(80))
        print("=" * 80)
        
        report = self.engine.get_project_status_report()
        
        print(f"\n📅 Current Date: {report['current_date']}")
        print(f"⏱️  Days Elapsed: {report['days_elapsed']}")
        print(f"⏳ Days Remaining: {report['days_remaining']}")
        
        status_icon = "✅" if report['on_schedule'] else "⚠️"
        print(f"{status_icon} Schedule Status: {'On Track' if report['on_schedule'] else 'Behind Schedule'}")
        
        print(f"\n📊 Progress: {report['completion_percentage']:.1f}% complete")
        self.print_progress_bar(report['completion_percentage'])
        
        print(f"\n📋 Tasks:")
        print(f"  • Total: {report['tasks']['total']}")
        print(f"  • Completed: {report['tasks']['completed']} ✓")
        print(f"  • In Progress: {report['tasks']['in_progress']} ⚙️")
        print(f"  • Not Started: {report['tasks']['not_started']} ○")
        print(f"  • Blocked: {report['tasks']['blocked']} 🚫")
        print(f"  • Overdue: {report['tasks']['overdue']} ⚠️")
        
        print(f"\n💰 Budget:")
        print(f"  • Total: ${report['budget']['total']:,.2f}")
        print(f"  • Spent: ${report['budget']['spent']:,.2f}")
        print(f"  • Remaining: ${report['budget']['total'] - report['budget']['spent']:,.2f}")
        print(f"  • Usage: {report['budget']['percentage_used']:.1f}%")
        
        print(f"\n🔧 Issues:")
        print(f"  • Open: {report['issues']['open']}")
        print(f"  • Resolved: {report['issues']['resolved']}")
        
        morale_icon = "😊" if report['team_morale'] > 0.7 else "😐" if report['team_morale'] > 0.5 else "😟"
        print(f"\n{morale_icon} Team Morale: {report['team_morale']:.1%}")
        
        if report['scope_changes'] > 0:
            print(f"\n📋 Scope Changes: {report['scope_changes']}")
    
    def view_tasks(self):
        """Display task list with filtering options."""
        print("\n" + "=" * 80)
        print("TASK LIST".center(80))
        print("=" * 80)
        
        print("\nFilter by status:")
        print("1. All Tasks")
        print("2. Not Started")
        print("3. In Progress")
        print("4. Completed")
        print("5. Blocked")
        print("6. Overdue")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        tasks = list(self.project.tasks.values())
        
        if choice == "2":
            tasks = [t for t in tasks if t.status == TaskStatus.NOT_STARTED]
        elif choice == "3":
            tasks = [t for t in tasks if t.status == TaskStatus.IN_PROGRESS]
        elif choice == "4":
            tasks = [t for t in tasks if t.status == TaskStatus.COMPLETED]
        elif choice == "5":
            tasks = [t for t in tasks if t.status == TaskStatus.BLOCKED]
        elif choice == "6":
            tasks = self.project.get_overdue_tasks()
        
        if not tasks:
            print("\n📝 No tasks match the selected filter.")
            return
        
        print(f"\n📋 Showing {len(tasks)} task(s):\n")
        
        for task in sorted(tasks, key=lambda t: t.task_id):
            status_icon = self._get_status_icon(task.status)
            priority_icon = "🔴" if task.priority.value >= 3 else "🟡" if task.priority.value == 2 else "🟢"
            
            print(f"{status_icon} {task.task_id}: {task.name}")
            print(f"   Priority: {priority_icon} {task.priority.name}")
            print(f"   Status: {task.status.value}")
            
            if task.assigned_to:
                print(f"   Assigned to: {task.assigned_to.name}")
            
            if task.due_date:
                print(f"   Due: {task.due_date.strftime('%Y-%m-%d')}")
            
            if task.status == TaskStatus.IN_PROGRESS:
                progress = (task.actual_hours / task.estimated_hours * 100) if task.estimated_hours > 0 else 0
                print(f"   Progress: {progress:.0f}% ({task.actual_hours:.1f}/{task.estimated_hours:.1f}h)")
            
            if task.dependencies:
                print(f"   Dependencies: {', '.join(task.dependencies)}")
            
            if task.blockers:
                print(f"   ⚠️ Blockers: {', '.join(task.blockers)}")
            
            print()
    
    def view_team(self):
        """Display team members and their status."""
        print("\n" + "=" * 80)
        print("TEAM OVERVIEW".center(80))
        print("=" * 80)
        
        if not self.project.team:
            print("\n👥 No team members found.")
            return
        
        print(f"\n👥 Team Size: {len(self.project.team)} members\n")
        
        for member in self.project.team:
            morale_icon = "😊" if member.morale > 0.7 else "😐" if member.morale > 0.5 else "😟"
            availability_icon = "✅" if member.availability >= 0.8 else "⚠️" if member.availability >= 0.5 else "🚫"
            
            print(f"\n{member.name} - {member.role}")
            print(f"  Skills: {', '.join(member.skills)}")
            print(f"  {morale_icon} Morale: {member.morale:.0%}")
            print(f"  {availability_icon} Availability: {member.availability:.0%}")
            print(f"  Productivity: {member.productivity:.1f}x")
            print(f"  Current Capacity: {member.get_capacity():.0%}")
            
            if member.current_tasks:
                print(f"  📋 Assigned Tasks ({len(member.current_tasks)}):")
                for task in member.current_tasks:
                    print(f"     • {task.task_id}: {task.name}")
            else:
                print(f"  💤 No assigned tasks")
            
            if member.conflicts_with:
                print(f"  ⚡ Conflicts with: {', '.join(member.conflicts_with)}")
    
    def view_issues(self):
        """Display project issues."""
        print("\n" + "=" * 80)
        print("ISSUES AND BLOCKERS".center(80))
        print("=" * 80)
        
        if not self.project.issues:
            print("\n✅ No issues found. Great work!")
            return
        
        open_issues = [i for i in self.project.issues.values() if not i.is_resolved]
        resolved_issues = [i for i in self.project.issues.values() if i.is_resolved]
        
        if open_issues:
            print(f"\n🔧 Open Issues ({len(open_issues)}):\n")
            for issue in sorted(open_issues, key=lambda i: i.severity, reverse=True):
                severity_icon = "🔴" if issue.severity >= 4 else "🟡" if issue.severity >= 2 else "🟢"
                print(f"{severity_icon} {issue.issue_id}: {issue.title}")
                print(f"   Type: {issue.issue_type.value}")
                print(f"   Severity: {issue.severity}/5")
                print(f"   Impact: {issue.impact}")
                print(f"   Created: {issue.created_date.strftime('%Y-%m-%d')}")
                
                if issue.affected_tasks:
                    print(f"   Affected Tasks: {', '.join(issue.affected_tasks)}")
                
                print()
        
        if resolved_issues:
            print(f"\n✅ Resolved Issues ({len(resolved_issues)}):\n")
            for issue in resolved_issues[-5:]:  # Show last 5
                print(f"✓ {issue.issue_id}: {issue.title}")
                print(f"   Resolution: {issue.resolution}")
                print()
    
    def assign_tasks(self):
        """Assign tasks to team members."""
        print("\n" + "=" * 80)
        print("TASK ASSIGNMENT".center(80))
        print("=" * 80)
        
        available_tasks = self.project.get_available_tasks()
        
        if not available_tasks:
            print("\n📝 No tasks available for assignment.")
            print("   (All dependencies must be completed first)")
            return
        
        print(f"\n📋 Available Tasks ({len(available_tasks)}):\n")
        
        for i, task in enumerate(available_tasks, 1):
            priority_icon = "🔴" if task.priority.value >= 3 else "🟡"
            print(f"{i}. {priority_icon} {task.task_id}: {task.name}")
            print(f"   Estimated: {task.estimated_hours}h")
            print(f"   Required Skills: {', '.join(task.required_skills)}")
            print()
        
        task_choice = input("Select task number (or 'c' to cancel): ").strip()
        
        if task_choice.lower() == 'c':
            return
        
        try:
            task_idx = int(task_choice) - 1
            if task_idx < 0 or task_idx >= len(available_tasks):
                print("\n❌ Invalid task selection.")
                return
            
            selected_task = available_tasks[task_idx]
        except ValueError:
            print("\n❌ Invalid input.")
            return
        
        # Show available team members
        print(f"\n👥 Team Members:\n")
        
        for i, member in enumerate(self.project.team, 1):
            has_skills = any(skill in member.skills for skill in selected_task.required_skills)
            skill_icon = "✅" if has_skills else "❌"
            
            print(f"{i}. {member.name} - {member.role}")
            print(f"   {skill_icon} Skills Match | Capacity: {member.get_capacity():.0%}")
            print(f"   Current Tasks: {len(member.current_tasks)}")
            print()
        
        member_choice = input("Select team member number (or 'c' to cancel): ").strip()
        
        if member_choice.lower() == 'c':
            return
        
        try:
            member_idx = int(member_choice) - 1
            if member_idx < 0 or member_idx >= len(self.project.team):
                print("\n❌ Invalid team member selection.")
                return
            
            selected_member = self.project.team[member_idx]
        except ValueError:
            print("\n❌ Invalid input.")
            return
        
        # Assign the task
        if self.engine.assign_task(selected_task, selected_member):
            print(f"\n✅ Successfully assigned {selected_task.name} to {selected_member.name}")
            print(f"   Due date: {selected_task.due_date.strftime('%Y-%m-%d')}")
        else:
            print(f"\n❌ Cannot assign task. {selected_member.name} lacks required skills.")
    
    def resolve_issue(self):
        """Resolve an open issue."""
        print("\n" + "=" * 80)
        print("ISSUE RESOLUTION".center(80))
        print("=" * 80)
        
        open_issues = [i for i in self.project.issues.values() if not i.is_resolved]
        
        if not open_issues:
            print("\n✅ No open issues to resolve!")
            return
        
        print(f"\n🔧 Open Issues ({len(open_issues)}):\n")
        
        for i, issue in enumerate(open_issues, 1):
            severity_icon = "🔴" if issue.severity >= 4 else "🟡"
            print(f"{i}. {severity_icon} {issue.issue_id}: {issue.title}")
            print(f"   Type: {issue.issue_type.value} | Severity: {issue.severity}/5")
            print()
        
        issue_choice = input("Select issue number to resolve (or 'c' to cancel): ").strip()
        
        if issue_choice.lower() == 'c':
            return
        
        try:
            issue_idx = int(issue_choice) - 1
            if issue_idx < 0 or issue_idx >= len(open_issues):
                print("\n❌ Invalid issue selection.")
                return
            
            selected_issue = open_issues[issue_idx]
        except ValueError:
            print("\n❌ Invalid input.")
            return
        
        print(f"\nResolving: {selected_issue.title}")
        print("\nSuggested resolution approaches:")
        
        if selected_issue.issue_type.value == "Technical":
            print("1. Implement technical fix and code review")
            print("2. Escalate to senior developer")
            print("3. Research alternative solution")
        elif selected_issue.issue_type.value == "Communication":
            print("1. Schedule team meeting to address conflicts")
            print("2. One-on-one discussions with involved parties")
            print("3. Implement new communication protocol")
        elif selected_issue.issue_type.value == "Scope":
            print("1. Accept scope change and adjust timeline")
            print("2. Negotiate reduced scope")
            print("3. Defer to future release")
        else:
            print("1. Implement immediate fix")
            print("2. Create workaround solution")
            print("3. Adjust project plan")
        
        resolution = input("\nEnter resolution description: ").strip()
        
        if resolution:
            if self.engine.resolve_issue(selected_issue.issue_id, resolution):
                print(f"\n✅ Issue {selected_issue.issue_id} resolved successfully!")
            else:
                print(f"\n❌ Failed to resolve issue.")
        else:
            print("\n❌ Resolution description required.")
    
    def advance_simulation(self):
        """Advance simulation by one day."""
        print("\n" + "=" * 80)
        print(f"ADVANCING TIME: Day {self.engine.day_count + 1}".center(80))
        print("=" * 80)
        
        events = self.engine.advance_day()
        
        print(f"\n📅 Current Date: {self.project.current_date.strftime('%Y-%m-%d')}")
        
        if events:
            print(f"\n📢 Events ({len(events)}):\n")
            for event in events:
                print(f"  {event['message']}")
        else:
            print("\n✨ No significant events today. Work continues smoothly.")
        
        # Show quick status update
        completion = self.project.get_completion_percentage()
        print(f"\n📊 Project Progress: {completion:.1f}%")
        self.print_progress_bar(completion)
        
        # Check for project completion
        if completion >= 100:
            self.project_completed()
    
    def generate_report(self):
        """Generate comprehensive status report."""
        print("\n" + "=" * 80)
        print("COMPREHENSIVE STATUS REPORT".center(80))
        print("=" * 80)
        
        report = self.engine.get_project_status_report()
        
        print(f"\n📋 Project: {report['project_name']}")
        print(f"📅 Report Date: {report['current_date']}")
        print(f"⏱️  Timeline: Day {report['days_elapsed']} of {report['days_elapsed'] + report['days_remaining']}")
        
        print("\n" + "-" * 80)
        print("PROGRESS SUMMARY")
        print("-" * 80)
        
        print(f"\nCompletion: {report['completion_percentage']:.1f}%")
        self.print_progress_bar(report['completion_percentage'])
        
        status = "ON TRACK ✅" if report['on_schedule'] else "BEHIND SCHEDULE ⚠️"
        print(f"Status: {status}")
        
        print("\n" + "-" * 80)
        print("TASK BREAKDOWN")
        print("-" * 80)
        
        tasks = report['tasks']
        print(f"\nTotal Tasks: {tasks['total']}")
        print(f"  ✓ Completed: {tasks['completed']} ({tasks['completed']/tasks['total']*100:.1f}%)")
        print(f"  ⚙️ In Progress: {tasks['in_progress']}")
        print(f"  ○ Not Started: {tasks['not_started']}")
        print(f"  🚫 Blocked: {tasks['blocked']}")
        print(f"  ⚠️ Overdue: {tasks['overdue']}")
        
        print("\n" + "-" * 80)
        print("BUDGET STATUS")
        print("-" * 80)
        
        budget = report['budget']
        print(f"\nTotal Budget: ${budget['total']:,.2f}")
        print(f"Spent: ${budget['spent']:,.2f} ({budget['percentage_used']:.1f}%)")
        print(f"Remaining: ${budget['total'] - budget['spent']:,.2f}")
        
        budget_status = "WITHIN BUDGET ✅" if budget['percentage_used'] < 100 else "OVER BUDGET ⚠️"
        print(f"Status: {budget_status}")
        
        print("\n" + "-" * 80)
        print("RISK ASSESSMENT")
        print("-" * 80)
        
        issues = report['issues']
        print(f"\nOpen Issues: {issues['open']}")
        print(f"Resolved Issues: {issues['resolved']}")
        
        morale = report['team_morale']
        morale_status = "HIGH 😊" if morale > 0.7 else "MODERATE 😐" if morale > 0.5 else "LOW 😟"
        print(f"Team Morale: {morale:.0%} - {morale_status}")
        
        if report['scope_changes'] > 0:
            print(f"\n⚠️ Scope Changes: {report['scope_changes']}")
        
        # Recommendations
        print("\n" + "-" * 80)
        print("RECOMMENDATIONS")
        print("-" * 80)
        print()
        
        if tasks['overdue'] > 0:
            print("⚠️ Address overdue tasks immediately")
        
        if issues['open'] > 3:
            print("⚠️ High number of open issues - prioritize resolution")
        
        if morale < 0.6:
            print("⚠️ Low team morale - consider team building activities")
        
        if not report['on_schedule']:
            print("⚠️ Project behind schedule - review timeline and resources")
        
        if budget['percentage_used'] > 80:
            print("⚠️ Budget usage high - monitor expenses closely")
        
        if tasks['blocked'] > 0:
            print("⚠️ Blocked tasks require immediate attention")
    
    def project_completed(self):
        """Handle project completion."""
        print("\n" + "=" * 80)
        print("PROJECT COMPLETED! 🎉".center(80))
        print("=" * 80)
        
        report = self.engine.get_project_status_report()
        
        days_elapsed = report['days_elapsed']
        deadline_days = (self.project.deadline - self.project.start_date).days
        
        if days_elapsed <= deadline_days:
            print("\n✅ Congratulations! You completed the project ON TIME!")
        else:
            days_late = days_elapsed - deadline_days
            print(f"\n⚠️ Project completed {days_late} days late.")
        
        budget_used = report['budget']['percentage_used']
        if budget_used <= 100:
            print(f"✅ Project completed WITHIN BUDGET ({budget_used:.1f}%)")
        else:
            print(f"⚠️ Project went over budget ({budget_used:.1f}%)")
        
        print(f"\n📊 Final Statistics:")
        print(f"  Duration: {days_elapsed} days")
        print(f"  Tasks Completed: {report['tasks']['completed']}")
        print(f"  Issues Resolved: {report['issues']['resolved']}")
        print(f"  Scope Changes: {report['scope_changes']}")
        print(f"  Final Team Morale: {report['team_morale']:.0%}")
        
        print("\n" + "=" * 80)
        
        self.running = False
    
    def _get_status_icon(self, status: TaskStatus) -> str:
        """Get icon for task status."""
        icons = {
            TaskStatus.NOT_STARTED: "○",
            TaskStatus.IN_PROGRESS: "⚙️",
            TaskStatus.BLOCKED: "🚫",
            TaskStatus.COMPLETED: "✓",
            TaskStatus.OVERDUE: "⚠️"
        }
        return icons.get(status, "?")
    
    def print_progress_bar(self, percentage: float, width: int = 50):
        """Print a progress bar."""
        filled = int(width * percentage / 100)
        bar = "█" * filled + "░" * (width - filled)
        print(f"  [{bar}] {percentage:.1f}%")


def main():
    """Main entry point for the simulation."""
    print("\n" + "=" * 80)
    print("PROJECT MANAGEMENT SIMULATION".center(80))
    print("=" * 80)
    print("\nSelect a project scenario:")
    print("1. E-Commerce Web Application (60 days, 6 team members)")
    print("2. Fitness Tracking Mobile App (45 days, 4 team members)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        project = create_web_app_project()
    elif choice == "2":
        project = create_mobile_app_project()
    elif choice == "3":
        print("\n👋 Goodbye!")
        return
    else:
        print("\n❌ Invalid choice. Exiting.")
        return
    
    cli = SimulationCLI(project)
    cli.run()


if __name__ == "__main__":
    main()
