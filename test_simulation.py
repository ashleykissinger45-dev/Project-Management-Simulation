"""
Tests for the Project Management Simulation.
Simple validation tests for core functionality.
"""
from datetime import datetime, timedelta
from models import (
    Project, Task, TeamMember, Issue, TaskStatus, TaskPriority, IssueType
)
from simulation_engine import SimulationEngine
from scenarios import create_web_app_project, create_mobile_app_project


def test_project_creation():
    """Test creating a project."""
    start_date = datetime.now()
    deadline = start_date + timedelta(days=30)
    
    project = Project(
        name="Test Project",
        description="Test Description",
        start_date=start_date,
        deadline=deadline,
        budget=10000.0
    )
    
    assert project.name == "Test Project"
    assert project.budget == 10000.0
    assert len(project.tasks) == 0
    assert len(project.team) == 0
    print("✓ test_project_creation passed")


def test_task_creation():
    """Test creating a task."""
    task = Task(
        task_id="T001",
        name="Test Task",
        description="Test Description",
        estimated_hours=40,
        priority=TaskPriority.HIGH,
        required_skills=["python"],
        dependencies=[]
    )
    
    assert task.task_id == "T001"
    assert task.status == TaskStatus.NOT_STARTED
    assert task.estimated_hours == 40
    assert task.actual_hours == 0.0
    print("✓ test_task_creation passed")


def test_team_member_creation():
    """Test creating a team member."""
    member = TeamMember(
        name="John Doe",
        role="Developer",
        skills=["python", "javascript"],
        productivity=1.0,
        availability=1.0
    )
    
    assert member.name == "John Doe"
    assert member.role == "Developer"
    assert len(member.skills) == 2
    assert member.get_capacity() == 0.8  # Initial morale is 0.8
    print("✓ test_team_member_creation passed")


def test_task_dependencies():
    """Test task dependency checking."""
    task1 = Task("T001", "Task 1", "First task", 10, TaskPriority.HIGH, ["python"], [])
    task2 = Task("T002", "Task 2", "Second task", 10, TaskPriority.HIGH, ["python"], ["T001"])
    
    assert task1.can_start([])
    assert not task2.can_start([])
    assert task2.can_start(["T001"])
    print("✓ test_task_dependencies passed")


def test_task_assignment():
    """Test assigning a task to a team member."""
    start_date = datetime.now()
    deadline = start_date + timedelta(days=30)
    
    project = Project("Test", "Test", start_date, deadline, 10000)
    
    member = TeamMember("Dev", "Developer", ["python"], 1.0, 1.0)
    task = Task("T001", "Task", "Description", 40, TaskPriority.HIGH, ["python"], [])
    
    project.add_team_member(member)
    project.add_task(task)
    
    engine = SimulationEngine(project)
    success = engine.assign_task(task, member)
    
    assert success
    assert task.status == TaskStatus.IN_PROGRESS
    assert task.assigned_to == member
    assert task in member.current_tasks
    print("✓ test_task_assignment passed")


def test_work_progression():
    """Test that work progresses on tasks."""
    start_date = datetime.now()
    deadline = start_date + timedelta(days=30)
    
    project = Project("Test", "Test", start_date, deadline, 10000)
    
    member = TeamMember("Dev", "Developer", ["python"], 1.0, 1.0)
    task = Task("T001", "Task", "Description", 8, TaskPriority.HIGH, ["python"], [])
    
    project.add_team_member(member)
    project.add_task(task)
    
    engine = SimulationEngine(project)
    engine.assign_task(task, member)
    
    # After one day, task should have made progress
    engine.advance_day()
    
    assert task.actual_hours > 0
    # With 8 hours work and 1.0 productivity and 0.8 morale, should complete in about 2 days
    print("✓ test_work_progression passed")


def test_task_completion():
    """Test that tasks complete correctly."""
    start_date = datetime.now()
    deadline = start_date + timedelta(days=30)
    
    project = Project("Test", "Test", start_date, deadline, 10000)
    
    member = TeamMember("Dev", "Developer", ["python"], 2.0, 1.0)  # High productivity
    task = Task("T001", "Task", "Description", 4, TaskPriority.HIGH, ["python"], [])
    
    project.add_team_member(member)
    project.add_task(task)
    
    engine = SimulationEngine(project)
    engine.assign_task(task, member)
    
    # Advance a few days to ensure completion
    for _ in range(3):
        engine.advance_day()
    
    assert task.status == TaskStatus.COMPLETED
    assert task.task_id in project.completed_tasks
    print("✓ test_task_completion passed")


def test_issue_creation():
    """Test creating and resolving an issue."""
    issue = Issue(
        issue_id="I001",
        title="Test Issue",
        description="Test Description",
        issue_type=IssueType.TECHNICAL,
        severity=3,
        impact="Testing impact"
    )
    
    assert issue.issue_id == "I001"
    assert not issue.is_resolved
    
    issue.resolve("Fixed the issue")
    
    assert issue.is_resolved
    assert issue.resolution == "Fixed the issue"
    print("✓ test_issue_creation passed")


def test_project_metrics():
    """Test project metric calculations."""
    start_date = datetime.now()
    deadline = start_date + timedelta(days=30)
    
    project = Project("Test", "Test", start_date, deadline, 10000)
    
    # Add some tasks
    for i in range(5):
        task = Task(f"T{i:03d}", f"Task {i}", "Description", 10, TaskPriority.HIGH, ["python"], [])
        project.add_task(task)
    
    # Complete 2 tasks
    project.completed_tasks = ["T000", "T001"]
    
    completion = project.get_completion_percentage()
    assert completion == 40.0  # 2 out of 5 tasks = 40%
    print("✓ test_project_metrics passed")


def test_scenario_creation():
    """Test that predefined scenarios create properly."""
    web_project = create_web_app_project()
    assert web_project is not None
    assert len(web_project.tasks) > 0
    assert len(web_project.team) > 0
    
    mobile_project = create_mobile_app_project()
    assert mobile_project is not None
    assert len(mobile_project.tasks) > 0
    assert len(mobile_project.team) > 0
    
    print("✓ test_scenario_creation passed")


def test_simulation_engine():
    """Test simulation engine basic functionality."""
    project = create_web_app_project()
    engine = SimulationEngine(project)
    
    # Test status report generation
    report = engine.get_project_status_report()
    assert report is not None
    assert 'project_name' in report
    assert 'tasks' in report
    assert 'budget' in report
    
    # Test day advancement
    initial_date = project.current_date
    engine.advance_day()
    assert project.current_date > initial_date
    
    print("✓ test_simulation_engine passed")


def run_all_tests():
    """Run all tests."""
    print("=" * 80)
    print("RUNNING PROJECT MANAGEMENT SIMULATION TESTS")
    print("=" * 80)
    print()
    
    tests = [
        test_project_creation,
        test_task_creation,
        test_team_member_creation,
        test_task_dependencies,
        test_task_assignment,
        test_work_progression,
        test_task_completion,
        test_issue_creation,
        test_project_metrics,
        test_scenario_creation,
        test_simulation_engine
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print()
    print("=" * 80)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 80)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
