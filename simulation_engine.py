"""
Simulation engine for the Project Management Simulation.
Handles time progression, task execution, and event generation.
"""
import random
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from models import (
    Project, Task, TeamMember, Issue, TaskStatus, TaskPriority,
    IssueType
)


class SimulationEngine:
    """Manages the simulation logic and event generation."""
    
    def __init__(self, project: Project):
        self.project = project
        self.events: List[Dict] = []
        self.day_count = 0
        self.random_seed = random.randint(1, 10000)
        random.seed(self.random_seed)
    
    def advance_day(self) -> List[Dict]:
        """Advance simulation by one day and return events."""
        self.day_count += 1
        self.project.current_date += timedelta(days=1)
        day_events = []
        
        # Process work on tasks
        work_events = self._process_daily_work()
        day_events.extend(work_events)
        
        # Check for overdue tasks
        overdue_events = self._check_overdue_tasks()
        day_events.extend(overdue_events)
        
        # Generate random events
        random_events = self._generate_random_events()
        day_events.extend(random_events)
        
        # Update team morale
        self._update_team_morale()
        
        # Update project metrics
        self._update_project_metrics()
        
        self.events.extend(day_events)
        return day_events
    
    def _process_daily_work(self) -> List[Dict]:
        """Process work on in-progress tasks."""
        events = []
        
        for member in self.project.team:
            if not member.current_tasks:
                continue
            
            # Each member works 8 hours per day, adjusted by capacity
            available_hours = 8.0 * member.get_capacity()
            
            # Distribute hours among assigned tasks
            hours_per_task = available_hours / len(member.current_tasks)
            
            for task in member.current_tasks[:]:  # Copy list to allow modification
                hours_completed = task.progress_work(hours_per_task, member)
                
                if task.status == TaskStatus.COMPLETED:
                    self.project.completed_tasks.append(task.task_id)
                    member.complete_task(task)
                    events.append({
                        'type': 'task_completed',
                        'task': task.name,
                        'member': member.name,
                        'date': self.project.current_date,
                        'message': f"✓ {member.name} completed task: {task.name}"
                    })
                    
                    # Small morale boost on completion
                    member.morale = min(1.0, member.morale + 0.05)
        
        return events
    
    def _check_overdue_tasks(self) -> List[Dict]:
        """Check for newly overdue tasks."""
        events = []
        
        for task in self.project.tasks.values():
            if (task.status == TaskStatus.IN_PROGRESS and 
                task.is_overdue(self.project.current_date) and
                task.status != TaskStatus.OVERDUE):
                
                task.status = TaskStatus.OVERDUE
                events.append({
                    'type': 'task_overdue',
                    'task': task.name,
                    'date': self.project.current_date,
                    'severity': 'high',
                    'message': f"⚠ Task overdue: {task.name} (due {task.due_date.strftime('%Y-%m-%d')})"
                })
                
                # Decrease morale when tasks are overdue
                if task.assigned_to:
                    task.assigned_to.morale = max(0.3, task.assigned_to.morale - 0.1)
        
        return events
    
    def _generate_random_events(self) -> List[Dict]:
        """Generate random events like conflicts, scope changes, etc."""
        events = []
        
        # Team conflict (5% chance per day)
        if random.random() < 0.05 and len(self.project.team) >= 2:
            events.extend(self._generate_team_conflict())
        
        # Scope change request (3% chance per day)
        if random.random() < 0.03:
            events.extend(self._generate_scope_change())
        
        # Technical issue (7% chance per day)
        if random.random() < 0.07 and self.project.get_in_progress_tasks():
            events.extend(self._generate_technical_issue())
        
        # Team member unavailability (4% chance per day)
        if random.random() < 0.04:
            events.extend(self._generate_availability_issue())
        
        return events
    
    def _generate_team_conflict(self) -> List[Dict]:
        """Generate a team conflict event."""
        member1, member2 = random.sample(self.project.team, 2)
        
        conflict_types = [
            "disagreement on technical approach",
            "communication breakdown",
            "resource allocation dispute",
            "conflicting priorities"
        ]
        
        conflict_type = random.choice(conflict_types)
        
        # Add to conflicts list
        if member2.name not in member1.conflicts_with:
            member1.conflicts_with.append(member2.name)
        if member1.name not in member2.conflicts_with:
            member2.conflicts_with.append(member1.name)
        
        # Reduce morale
        member1.morale = max(0.3, member1.morale - 0.15)
        member2.morale = max(0.3, member2.morale - 0.15)
        
        # Create issue
        issue_id = f"CONFLICT-{len(self.project.issues) + 1}"
        issue = Issue(
            issue_id=issue_id,
            title=f"Team conflict: {member1.name} and {member2.name}",
            description=f"Conflict due to {conflict_type}",
            issue_type=IssueType.COMMUNICATION,
            severity=3,
            impact="Reduced team productivity and morale"
        )
        self.project.add_issue(issue)
        
        return [{
            'type': 'team_conflict',
            'members': [member1.name, member2.name],
            'reason': conflict_type,
            'date': self.project.current_date,
            'severity': 'medium',
            'message': f"⚡ Conflict between {member1.name} and {member2.name}: {conflict_type}"
        }]
    
    def _generate_scope_change(self) -> List[Dict]:
        """Generate a scope change request."""
        change_types = [
            ("New feature requested", "high", 40),
            ("Requirements clarification needed", "medium", 16),
            ("Design change requested", "medium", 24),
            ("Integration requirement added", "high", 32)
        ]
        
        change_type, priority, additional_hours = random.choice(change_types)
        
        self.project.scope_changes.append({
            'type': change_type,
            'date': self.project.current_date,
            'additional_hours': additional_hours,
            'priority': priority
        })
        
        return [{
            'type': 'scope_change',
            'change': change_type,
            'impact': f"{additional_hours} additional hours",
            'date': self.project.current_date,
            'severity': 'high',
            'message': f"📋 Scope change: {change_type} (+{additional_hours}h)"
        }]
    
    def _generate_technical_issue(self) -> List[Dict]:
        """Generate a technical issue."""
        in_progress = self.project.get_in_progress_tasks()
        if not in_progress:
            return []
        
        affected_task = random.choice(in_progress)
        
        issue_types = [
            ("Integration failure", IssueType.TECHNICAL, 4),
            ("Performance problem", IssueType.TECHNICAL, 3),
            ("Bug discovered", IssueType.QUALITY, 3),
            ("Dependency conflict", IssueType.TECHNICAL, 4),
            ("Environment issue", IssueType.TECHNICAL, 2)
        ]
        
        issue_title, issue_type, severity = random.choice(issue_types)
        
        # Block the task
        affected_task.status = TaskStatus.BLOCKED
        affected_task.blockers.append(issue_title)
        
        # Create issue
        issue_id = f"TECH-{len(self.project.issues) + 1}"
        issue = Issue(
            issue_id=issue_id,
            title=f"{issue_title} in {affected_task.name}",
            description=f"Technical issue blocking task progress",
            issue_type=issue_type,
            severity=severity,
            impact=f"Task {affected_task.name} is blocked"
        )
        issue.affected_tasks.append(affected_task.task_id)
        self.project.add_issue(issue)
        
        return [{
            'type': 'technical_issue',
            'issue': issue_title,
            'task': affected_task.name,
            'date': self.project.current_date,
            'severity': 'high',
            'message': f"🔧 Technical issue: {issue_title} blocking {affected_task.name}"
        }]
    
    def _generate_availability_issue(self) -> List[Dict]:
        """Generate team member availability issue."""
        member = random.choice(self.project.team)
        
        reasons = [
            ("sick leave", 0.0, 2),
            ("other commitments", 0.5, 3),
            ("vacation", 0.0, 5),
            ("training", 0.3, 2)
        ]
        
        reason, availability, duration = random.choice(reasons)
        old_availability = member.availability
        member.availability = availability
        
        return [{
            'type': 'availability_change',
            'member': member.name,
            'reason': reason,
            'availability': availability,
            'duration': f"{duration} days",
            'date': self.project.current_date,
            'severity': 'medium',
            'message': f"👤 {member.name} availability reduced due to {reason}"
        }]
    
    def _update_team_morale(self):
        """Update team morale based on project conditions."""
        overdue_count = len(self.project.get_overdue_tasks())
        on_schedule = self.project.is_on_schedule()
        
        for member in self.project.team:
            # Gradual morale recovery
            if member.morale < 0.8:
                member.morale = min(0.8, member.morale + 0.02)
            
            # Negative impact from overdue tasks
            if overdue_count > 0:
                member.morale = max(0.3, member.morale - 0.01 * overdue_count)
            
            # Positive impact from being on schedule
            if on_schedule:
                member.morale = min(1.0, member.morale + 0.01)
    
    def _update_project_metrics(self):
        """Update project budget and other metrics."""
        # Calculate daily costs (simplified)
        daily_cost = len(self.project.team) * 500  # $500 per team member per day
        self.project.spent_budget += daily_cost
    
    def assign_task(self, task: Task, member: TeamMember) -> bool:
        """Assign a task to a team member."""
        # Check if member has required skills
        if not any(skill in member.skills for skill in task.required_skills):
            return False
        
        # Assign the task
        task.assigned_to = member
        task.status = TaskStatus.IN_PROGRESS
        task.start_date = self.project.current_date
        
        # Set due date based on estimate
        estimated_days = task.estimated_hours / (8 * member.productivity)
        task.due_date = self.project.current_date + timedelta(days=estimated_days)
        
        member.assign_task(task)
        return True
    
    def resolve_issue(self, issue_id: str, resolution: str) -> bool:
        """Resolve an issue and unblock affected tasks."""
        if issue_id not in self.project.issues:
            return False
        
        issue = self.project.issues[issue_id]
        issue.resolve(resolution)
        
        # Unblock affected tasks
        for task_id in issue.affected_tasks:
            if task_id in self.project.tasks:
                task = self.project.tasks[task_id]
                task.status = TaskStatus.IN_PROGRESS
                task.blockers = [b for b in task.blockers if issue.title not in b]
        
        # Resolve conflicts if it's a communication issue
        if issue.issue_type == IssueType.COMMUNICATION:
            for member in self.project.team:
                member.conflicts_with.clear()
                member.morale = min(1.0, member.morale + 0.1)
        
        return True
    
    def get_project_status_report(self) -> Dict:
        """Generate a comprehensive project status report."""
        total_tasks = len(self.project.tasks)
        completed = len(self.project.completed_tasks)
        in_progress = len(self.project.get_in_progress_tasks())
        not_started = len([t for t in self.project.tasks.values() 
                          if t.status == TaskStatus.NOT_STARTED])
        blocked = len([t for t in self.project.tasks.values() 
                      if t.status == TaskStatus.BLOCKED])
        overdue = len(self.project.get_overdue_tasks())
        
        days_elapsed = (self.project.current_date - self.project.start_date).days
        days_remaining = (self.project.deadline - self.project.current_date).days
        
        open_issues = len([i for i in self.project.issues.values() if not i.is_resolved])
        
        return {
            'project_name': self.project.name,
            'current_date': self.project.current_date.strftime('%Y-%m-%d'),
            'days_elapsed': days_elapsed,
            'days_remaining': days_remaining,
            'completion_percentage': self.project.get_completion_percentage(),
            'on_schedule': self.project.is_on_schedule(),
            'tasks': {
                'total': total_tasks,
                'completed': completed,
                'in_progress': in_progress,
                'not_started': not_started,
                'blocked': blocked,
                'overdue': overdue
            },
            'budget': {
                'total': self.project.budget,
                'spent': self.project.spent_budget,
                'percentage_used': self.project.get_budget_used_percentage()
            },
            'issues': {
                'total': len(self.project.issues),
                'open': open_issues,
                'resolved': len(self.project.issues) - open_issues
            },
            'team_morale': sum(m.morale for m in self.project.team) / len(self.project.team) if self.project.team else 0,
            'scope_changes': len(self.project.scope_changes)
        }
