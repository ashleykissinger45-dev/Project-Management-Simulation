"""
Sample project scenarios for the simulation.
"""
from datetime import datetime, timedelta
from models import Project, Task, TeamMember, TaskPriority


def create_web_app_project() -> Project:
    """Create a sample web application development project."""
    start_date = datetime.now()
    deadline = start_date + timedelta(days=60)
    
    project = Project(
        name="E-Commerce Web Application",
        description="Develop a modern e-commerce platform with user management, product catalog, and payment processing",
        start_date=start_date,
        deadline=deadline,
        budget=150000.0
    )
    
    # Add team members
    team_members = [
        TeamMember("Sarah Johnson", "Project Manager", ["management", "planning"], 1.2, 1.0),
        TeamMember("Mike Chen", "Frontend Developer", ["react", "javascript", "css"], 1.0, 1.0),
        TeamMember("Emily Rodriguez", "Backend Developer", ["python", "django", "database"], 1.1, 1.0),
        TeamMember("David Kim", "DevOps Engineer", ["aws", "docker", "ci/cd"], 0.9, 0.8),
        TeamMember("Lisa Wang", "UX Designer", ["design", "ui", "prototyping"], 1.0, 1.0),
        TeamMember("James Brown", "QA Engineer", ["testing", "automation", "quality"], 1.0, 0.9)
    ]
    
    for member in team_members:
        project.add_team_member(member)
    
    # Phase 1: Planning and Design
    tasks = [
        Task("T001", "Requirements Gathering", 
             "Gather and document all project requirements",
             40, TaskPriority.CRITICAL, ["management", "planning"], []),
        
        Task("T002", "Technical Architecture Design",
             "Design system architecture and technology stack",
             32, TaskPriority.CRITICAL, ["backend", "planning"], ["T001"]),
        
        Task("T003", "UI/UX Design",
             "Create wireframes and design mockups",
             48, TaskPriority.HIGH, ["design", "ui"], ["T001"]),
        
        Task("T004", "Database Schema Design",
             "Design database schema and relationships",
             24, TaskPriority.HIGH, ["database", "planning"], ["T002"]),
        
        # Phase 2: Infrastructure Setup
        Task("T005", "Development Environment Setup",
             "Set up development environments and tools",
             16, TaskPriority.HIGH, ["devops", "ci/cd"], ["T002"]),
        
        Task("T006", "CI/CD Pipeline Configuration",
             "Configure automated build and deployment pipeline",
             24, TaskPriority.MEDIUM, ["devops", "ci/cd"], ["T005"]),
        
        # Phase 3: Backend Development
        Task("T007", "User Authentication System",
             "Implement user registration, login, and authentication",
             40, TaskPriority.CRITICAL, ["python", "django"], ["T004", "T005"]),
        
        Task("T008", "Product Catalog API",
             "Develop API for product management and catalog",
             48, TaskPriority.CRITICAL, ["python", "django", "database"], ["T004", "T005"]),
        
        Task("T009", "Shopping Cart System",
             "Implement shopping cart functionality",
             32, TaskPriority.HIGH, ["python", "django"], ["T008"]),
        
        Task("T010", "Payment Integration",
             "Integrate payment gateway (Stripe/PayPal)",
             40, TaskPriority.CRITICAL, ["python", "django"], ["T009"]),
        
        Task("T011", "Order Management System",
             "Develop order processing and management",
             40, TaskPriority.HIGH, ["python", "django", "database"], ["T010"]),
        
        # Phase 4: Frontend Development
        Task("T012", "Frontend Project Setup",
             "Initialize React project with routing and state management",
             16, TaskPriority.HIGH, ["react", "javascript"], ["T003", "T005"]),
        
        Task("T013", "User Interface Components",
             "Develop reusable UI components",
             48, TaskPriority.HIGH, ["react", "javascript", "css"], ["T012"]),
        
        Task("T014", "Product Listing Pages",
             "Implement product browsing and filtering",
             40, TaskPriority.HIGH, ["react", "javascript"], ["T013", "T008"]),
        
        Task("T015", "Shopping Cart UI",
             "Create shopping cart interface",
             32, TaskPriority.HIGH, ["react", "javascript"], ["T013", "T009"]),
        
        Task("T016", "Checkout Flow",
             "Implement checkout process and payment UI",
             40, TaskPriority.CRITICAL, ["react", "javascript"], ["T015", "T010"]),
        
        Task("T017", "User Profile Pages",
             "Create user account and profile management pages",
             32, TaskPriority.MEDIUM, ["react", "javascript"], ["T013", "T007"]),
        
        # Phase 5: Testing
        Task("T018", "Unit Testing",
             "Write and execute unit tests for backend and frontend",
             48, TaskPriority.HIGH, ["testing", "automation"], ["T011", "T016"]),
        
        Task("T019", "Integration Testing",
             "Test integration between components",
             40, TaskPriority.HIGH, ["testing", "automation"], ["T018"]),
        
        Task("T020", "User Acceptance Testing",
             "Conduct UAT with stakeholders",
             32, TaskPriority.CRITICAL, ["testing", "management"], ["T019"]),
        
        # Phase 6: Deployment
        Task("T021", "Production Environment Setup",
             "Configure production servers and services",
             24, TaskPriority.CRITICAL, ["aws", "docker", "devops"], ["T006"]),
        
        Task("T022", "Performance Optimization",
             "Optimize application performance",
             32, TaskPriority.MEDIUM, ["backend", "frontend"], ["T020"]),
        
        Task("T023", "Security Audit",
             "Conduct security review and fix vulnerabilities",
             24, TaskPriority.CRITICAL, ["security", "testing"], ["T020"]),
        
        Task("T024", "Production Deployment",
             "Deploy application to production",
             16, TaskPriority.CRITICAL, ["devops", "ci/cd"], ["T021", "T022", "T023"]),
        
        Task("T025", "Documentation",
             "Create user and technical documentation",
             32, TaskPriority.MEDIUM, ["management", "planning"], ["T024"])
    ]
    
    for task in tasks:
        project.add_task(task)
    
    # Add milestones
    project.milestones = {
        "Design Complete": start_date + timedelta(days=15),
        "Backend MVP": start_date + timedelta(days=35),
        "Frontend MVP": start_date + timedelta(days=45),
        "Testing Complete": start_date + timedelta(days=55),
        "Production Launch": deadline
    }
    
    return project


def create_mobile_app_project() -> Project:
    """Create a sample mobile app development project."""
    start_date = datetime.now()
    deadline = start_date + timedelta(days=45)
    
    project = Project(
        name="Fitness Tracking Mobile App",
        description="Cross-platform mobile app for fitness tracking and workout planning",
        start_date=start_date,
        deadline=deadline,
        budget=80000.0
    )
    
    # Add team members
    team_members = [
        TeamMember("Alex Turner", "Lead Developer", ["react-native", "javascript", "mobile"], 1.1, 1.0),
        TeamMember("Maria Garcia", "Mobile Developer", ["react-native", "javascript"], 1.0, 1.0),
        TeamMember("Chris Anderson", "Backend Developer", ["node", "mongodb", "api"], 1.0, 1.0),
        TeamMember("Nina Patel", "UX Designer", ["design", "mobile-ui", "prototyping"], 1.0, 0.9)
    ]
    
    for member in team_members:
        project.add_team_member(member)
    
    # Add tasks
    tasks = [
        Task("M001", "Requirements and Planning",
             "Define app features and technical requirements",
             24, TaskPriority.CRITICAL, ["planning"], []),
        
        Task("M002", "UI/UX Design",
             "Create app design and user flows",
             32, TaskPriority.HIGH, ["design", "mobile-ui"], ["M001"]),
        
        Task("M003", "Backend API Development",
             "Develop REST API for app data",
             40, TaskPriority.CRITICAL, ["node", "mongodb", "api"], ["M001"]),
        
        Task("M004", "User Authentication",
             "Implement user registration and login",
             24, TaskPriority.CRITICAL, ["react-native", "javascript"], ["M003"]),
        
        Task("M005", "Workout Tracking Feature",
             "Build workout logging and tracking",
             40, TaskPriority.HIGH, ["react-native", "javascript"], ["M002", "M003"]),
        
        Task("M006", "Progress Dashboard",
             "Create progress visualization and stats",
             32, TaskPriority.MEDIUM, ["react-native", "javascript"], ["M005"]),
        
        Task("M007", "Social Features",
             "Add friend connections and sharing",
             24, TaskPriority.LOW, ["react-native", "javascript"], ["M004"]),
        
        Task("M008", "Testing and Bug Fixes",
             "Test app on multiple devices and fix issues",
             32, TaskPriority.HIGH, ["testing", "mobile"], ["M006"]),
        
        Task("M009", "App Store Submission",
             "Prepare and submit to app stores",
             16, TaskPriority.CRITICAL, ["mobile"], ["M008"])
    ]
    
    for task in tasks:
        project.add_task(task)
    
    return project
