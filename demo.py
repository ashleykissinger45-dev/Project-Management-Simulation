#!/usr/bin/env python
"""
Demonstration script for the Project Management Simulation.
Runs an automated simulation to showcase features.
"""
from datetime import datetime
from models import TaskStatus
from simulation_engine import SimulationEngine
from scenarios import create_web_app_project


def run_demo():
    """Run an automated demonstration of the simulation."""
    print("=" * 80)
    print("PROJECT MANAGEMENT SIMULATION - DEMO".center(80))
    print("=" * 80)
    print("\nThis demo showcases the simulation features with automated decisions.\n")
    
    # Create project
    project = create_web_app_project()
    engine = SimulationEngine(project)
    
    print(f"📋 Project: {project.name}")
    print(f"📅 Timeline: {project.start_date.strftime('%Y-%m-%d')} to {project.deadline.strftime('%Y-%m-%d')}")
    print(f"💰 Budget: ${project.budget:,.2f}")
    print(f"👥 Team: {len(project.team)} members")
    print(f"📝 Tasks: {len(project.tasks)}")
    print()
    
    # Auto-assign initial tasks
    print("-" * 80)
    print("PHASE 1: INITIAL TASK ASSIGNMENT")
    print("-" * 80)
    print()
    
    assigned_count = 0
    for _ in range(5):  # Assign first 5 available tasks
        available = project.get_available_tasks()
        if not available:
            break
        
        task = available[0]
        # Find team member with matching skills
        for member in project.team:
            if any(skill in member.skills for skill in task.required_skills):
                if engine.assign_task(task, member):
                    print(f"✓ Assigned {task.task_id} ({task.name}) to {member.name}")
                    assigned_count += 1
                    break
    
    print(f"\n✅ Assigned {assigned_count} tasks\n")
    
    # Simulate 10 days
    print("-" * 80)
    print("PHASE 2: SIMULATING 10 DAYS OF WORK")
    print("-" * 80)
    print()
    
    interesting_events = []
    
    for day in range(1, 11):
        events = engine.advance_day()
        
        if events:
            print(f"\n📅 Day {day} - {project.current_date.strftime('%Y-%m-%d')}:")
            for event in events:
                print(f"  {event['message']}")
                interesting_events.extend(events)
        
        # Auto-assign more tasks as they become available
        available = project.get_available_tasks()
        if available and day % 3 == 0:  # Every 3 days
            task = available[0]
            for member in project.team:
                if len(member.current_tasks) < 2:  # Don't overload
                    if any(skill in member.skills for skill in task.required_skills):
                        engine.assign_task(task, member)
                        break
    
    print(f"\n✅ Completed 10 days of simulation\n")
    
    # Show status
    print("-" * 80)
    print("PHASE 3: PROJECT STATUS")
    print("-" * 80)
    print()
    
    report = engine.get_project_status_report()
    
    print(f"📊 Progress: {report['completion_percentage']:.1f}%")
    print(f"📋 Tasks Completed: {report['tasks']['completed']}/{report['tasks']['total']}")
    print(f"⚙️  In Progress: {report['tasks']['in_progress']}")
    print(f"💰 Budget Used: ${report['budget']['spent']:,.2f} ({report['budget']['percentage_used']:.1f}%)")
    
    status = "✅ ON TRACK" if report['on_schedule'] else "⚠️ BEHIND SCHEDULE"
    print(f"📈 Schedule Status: {status}")
    print(f"😊 Team Morale: {report['team_morale']:.0%}")
    
    if report['issues']['open'] > 0:
        print(f"🔧 Open Issues: {report['issues']['open']}")
    
    print()
    
    # Show some tasks in detail
    print("-" * 80)
    print("PHASE 4: TASK DETAILS")
    print("-" * 80)
    print()
    
    completed_tasks = [t for t in project.tasks.values() if t.status == TaskStatus.COMPLETED]
    in_progress_tasks = [t for t in project.tasks.values() if t.status == TaskStatus.IN_PROGRESS]
    
    if completed_tasks:
        print(f"✓ Completed Tasks ({len(completed_tasks)}):")
        for task in completed_tasks[:3]:  # Show first 3
            print(f"  • {task.task_id}: {task.name}")
        if len(completed_tasks) > 3:
            print(f"  ... and {len(completed_tasks) - 3} more")
        print()
    
    if in_progress_tasks:
        print(f"⚙️  In Progress ({len(in_progress_tasks)}):")
        for task in in_progress_tasks[:3]:  # Show first 3
            progress = (task.actual_hours / task.estimated_hours * 100) if task.estimated_hours > 0 else 0
            print(f"  • {task.task_id}: {task.name} ({progress:.0f}% complete)")
        print()
    
    # Show team status
    print("-" * 80)
    print("PHASE 5: TEAM STATUS")
    print("-" * 80)
    print()
    
    for member in project.team:
        morale_icon = "😊" if member.morale > 0.7 else "😐" if member.morale > 0.5 else "😟"
        print(f"{morale_icon} {member.name} ({member.role})")
        print(f"   Morale: {member.morale:.0%} | Capacity: {member.get_capacity():.0%}")
        if member.current_tasks:
            print(f"   Working on: {len(member.current_tasks)} task(s)")
        print()
    
    # Show interesting events
    if interesting_events:
        print("-" * 80)
        print("PHASE 6: NOTABLE EVENTS")
        print("-" * 80)
        print()
        
        event_types = {}
        for event in interesting_events:
            event_type = event.get('type', 'other')
            event_types[event_type] = event_types.get(event_type, 0) + 1
        
        print("Event Summary:")
        for event_type, count in event_types.items():
            print(f"  • {event_type}: {count} occurrence(s)")
        print()
    
    # Summary
    print("=" * 80)
    print("DEMO COMPLETE".center(80))
    print("=" * 80)
    print()
    print("This demonstration showed:")
    print("  ✓ Project initialization with tasks and team")
    print("  ✓ Automated task assignment based on skills")
    print("  ✓ Day-by-day simulation with work progression")
    print("  ✓ Random event generation (conflicts, issues, scope changes)")
    print("  ✓ Progress tracking and status reporting")
    print("  ✓ Team morale and productivity management")
    print()
    print("To run the interactive simulation, use:")
    print("  python simulation_cli.py")
    print()


if __name__ == "__main__":
    run_demo()
