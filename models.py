"""
Core data models for the Project Management Simulation.
"""
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional, Dict
import random


class TaskStatus(Enum):
    """Task status enumeration."""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    BLOCKED = "Blocked"
    COMPLETED = "Completed"
    OVERDUE = "Overdue"


class TaskPriority(Enum):
    """Task priority enumeration."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class IssueType(Enum):
    """Issue type enumeration."""
    TECHNICAL = "Technical"
    RESOURCE = "Resource"
    SCOPE = "Scope"
    COMMUNICATION = "Communication"
    QUALITY = "Quality"


class TeamMember:
    """Represents a team member with skills and availability."""
    
    def __init__(self, name: str, role: str, skills: List[str], 
                 productivity: float = 1.0, availability: float = 1.0):
        self.name = name
        self.role = role
        self.skills = skills
        self.productivity = productivity  # 0.5 to 1.5
        self.availability = availability  # 0.0 to 1.0
        self.current_tasks: List['Task'] = []
        self.morale = 0.8  # 0.0 to 1.0
        self.conflicts_with: List[str] = []
    
    def get_capacity(self) -> float:
        """Get current capacity based on availability and morale."""
        return self.availability * self.morale
    
    def assign_task(self, task: 'Task'):
        """Assign a task to this team member."""
        self.current_tasks.append(task)
    
    def complete_task(self, task: 'Task'):
        """Remove a completed task from current tasks."""
        if task in self.current_tasks:
            self.current_tasks.remove(task)
    
    def __repr__(self):
        return f"TeamMember({self.name}, {self.role})"


class Task:
    """Represents a project task with dependencies and assignments."""
    
    def __init__(self, task_id: str, name: str, description: str,
                 estimated_hours: float, priority: TaskPriority,
                 required_skills: List[str], dependencies: List[str] = None):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.estimated_hours = estimated_hours
        self.actual_hours = 0.0
        self.priority = priority
        self.required_skills = required_skills
        self.dependencies = dependencies or []
        self.status = TaskStatus.NOT_STARTED
        self.assigned_to: Optional[TeamMember] = None
        self.start_date: Optional[datetime] = None
        self.due_date: Optional[datetime] = None
        self.completion_date: Optional[datetime] = None
        self.blockers: List[str] = []
    
    def can_start(self, completed_tasks: List[str]) -> bool:
        """Check if all dependencies are completed."""
        return all(dep in completed_tasks for dep in self.dependencies)
    
    def is_overdue(self, current_date: datetime) -> bool:
        """Check if task is overdue."""
        if self.due_date and self.status != TaskStatus.COMPLETED:
            return current_date > self.due_date
        return False
    
    def progress_work(self, hours: float, member: TeamMember) -> float:
        """Progress work on the task and return hours completed."""
        if self.status == TaskStatus.COMPLETED:
            return 0.0
        
        effective_hours = hours * member.productivity
        self.actual_hours += effective_hours
        
        if self.actual_hours >= self.estimated_hours:
            self.status = TaskStatus.COMPLETED
            self.completion_date = datetime.now()
            return self.estimated_hours - (self.actual_hours - effective_hours)
        
        return effective_hours
    
    def __repr__(self):
        return f"Task({self.task_id}, {self.name}, {self.status.value})"


class Issue:
    """Represents a project issue that needs resolution."""
    
    def __init__(self, issue_id: str, title: str, description: str,
                 issue_type: IssueType, severity: int, impact: str):
        self.issue_id = issue_id
        self.title = title
        self.description = description
        self.issue_type = issue_type
        self.severity = severity  # 1-5
        self.impact = impact
        self.created_date = datetime.now()
        self.resolved_date: Optional[datetime] = None
        self.resolution: Optional[str] = None
        self.is_resolved = False
        self.affected_tasks: List[str] = []
    
    def resolve(self, resolution: str):
        """Resolve the issue."""
        self.is_resolved = True
        self.resolved_date = datetime.now()
        self.resolution = resolution
    
    def __repr__(self):
        return f"Issue({self.issue_id}, {self.title}, {self.issue_type.value})"


class Project:
    """Represents a project with tasks, team, and timeline."""
    
    def __init__(self, name: str, description: str, start_date: datetime,
                 deadline: datetime, budget: float):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.deadline = deadline
        self.budget = budget
        self.spent_budget = 0.0
        self.current_date = start_date
        
        self.tasks: Dict[str, Task] = {}
        self.team: List[TeamMember] = []
        self.issues: Dict[str, Issue] = {}
        self.completed_tasks: List[str] = []
        
        self.milestones: Dict[str, datetime] = {}
        self.scope_changes: List[Dict] = []
        self.risk_log: List[Dict] = []
    
    def add_task(self, task: Task):
        """Add a task to the project."""
        self.tasks[task.task_id] = task
    
    def add_team_member(self, member: TeamMember):
        """Add a team member to the project."""
        self.team.append(member)
    
    def add_issue(self, issue: Issue):
        """Add an issue to the project."""
        self.issues[issue.issue_id] = issue
    
    def get_available_tasks(self) -> List[Task]:
        """Get tasks that can be started."""
        available = []
        for task in self.tasks.values():
            if (task.status == TaskStatus.NOT_STARTED and 
                task.can_start(self.completed_tasks)):
                available.append(task)
        return available
    
    def get_in_progress_tasks(self) -> List[Task]:
        """Get tasks currently in progress."""
        return [t for t in self.tasks.values() 
                if t.status == TaskStatus.IN_PROGRESS]
    
    def get_overdue_tasks(self) -> List[Task]:
        """Get overdue tasks."""
        return [t for t in self.tasks.values() 
                if t.is_overdue(self.current_date)]
    
    def get_completion_percentage(self) -> float:
        """Calculate project completion percentage."""
        if not self.tasks:
            return 0.0
        completed = len(self.completed_tasks)
        total = len(self.tasks)
        return (completed / total) * 100
    
    def get_budget_used_percentage(self) -> float:
        """Calculate budget usage percentage."""
        if self.budget == 0:
            return 0.0
        return (self.spent_budget / self.budget) * 100
    
    def is_on_schedule(self) -> bool:
        """Check if project is on schedule."""
        if not self.tasks:
            return True
        
        total_days = (self.deadline - self.start_date).days
        elapsed_days = (self.current_date - self.start_date).days
        
        if elapsed_days == 0:
            return True
        
        expected_completion = (elapsed_days / total_days) * 100
        actual_completion = self.get_completion_percentage()
        
        return actual_completion >= expected_completion * 0.9
    
    def __repr__(self):
        return f"Project({self.name}, {self.get_completion_percentage():.1f}% complete)"
