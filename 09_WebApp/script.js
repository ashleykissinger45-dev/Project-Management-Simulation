// ============================================
// Project Management Dashboard - Main Script
// ============================================

// Sample Data (In a real app, this would come from a database or API)
const projectData = {
    tasks: [
        {
            id: 1,
            name: "Create Project Charter",
            assignee: "Ashley Kissinger",
            status: "not-started",
            priority: "high",
            dueDate: "2026-02-15"
        },
        {
            id: 2,
            name: "Develop Business Case",
            assignee: "Ashley Kissinger",
            status: "not-started",
            priority: "high",
            dueDate: "2026-02-12"
        },
        {
            id: 3,
            name: "Complete Stakeholder Register",
            assignee: "Ashley Kissinger",
            status: "not-started",
            priority: "high",
            dueDate: "2026-02-12"
        },
        {
            id: 4,
            name: "Sprint 1 Planning Meeting",
            assignee: "Whole Team",
            status: "not-started",
            priority: "high",
            dueDate: "2026-02-10"
        },
        {
            id: 5,
            name: "Request Jira API Access from IT Security",
            assignee: "Ashley Kissinger",
            status: "not-started",
            priority: "high",
            dueDate: "2026-02-12"
        },
        {
            id: 6,
            name: "Define Technical Architecture",
            assignee: "Jordan Martinez",
            status: "not-started",
            priority: "high",
            dueDate: "2026-02-14"
        },
        {
            id: 7,
            name: "Create UI/UX Wireframes",
            assignee: "Sam Kim",
            status: "not-started",
            priority: "medium",
            dueDate: "2026-02-16"
        },
        {
            id: 8,
            name: "Set up Development Environment",
            assignee: "Jamie Park",
            status: "not-started",
            priority: "medium",
            dueDate: "2026-02-13"
        }
    ],
    team: [
        {
            id: 1,
            name: "Ashley Kissinger",
            role: "Project Manager",
            initials: "AK",
            email: "ashley.kissinger@techflowsolutions.com"
        },
        {
            id: 2,
            name: "Jordan Martinez",
            role: "Senior Full Stack Developer",
            initials: "JM",
            email: "jordan.martinez@techflowsolutions.com"
        },
        {
            id: 3,
            name: "Jamie Park",
            role: "Backend Developer",
            initials: "JP",
            email: "jamie.park@techflowsolutions.com"
        },
        {
            id: 4,
            name: "Sam Kim",
            role: "UI/UX Designer",
            initials: "SK",
            email: "sam.kim@techflowsolutions.com"
        },
        {
            id: 5,
            name: "Riley Thompson",
            role: "QA Engineer",
            initials: "RT",
            email: "riley.thompson@techflowsolutions.com"
        }
    ],
    risks: [
        {
            id: 1,
            description: "Jira API access delay from IT Security (due Feb 12)",
            probability: "medium",
            impact: "high",
            status: "active",
            owner: "Ashley Kissinger"
        },
        {
            id: 2,
            description: "Resource availability constraints (50% allocation)",
            probability: "medium",
            impact: "high",
            status: "active",
            owner: "Ashley Kissinger"
        },
        {
            id: 3,
            description: "Scope creep from stakeholders",
            probability: "high",
            impact: "medium",
            status: "active",
            owner: "Ashley Kissinger"
        },
        {
            id: 4,
            description: "Technical dependencies delays",
            probability: "medium",
            impact: "medium",
            status: "active",
            owner: "Jordan Martinez"
        }
    ]
};

// ============================================
// Initialize Dashboard on Page Load
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('Dashboard initializing...');
    
    // Update metrics
    updateMetrics();
    
    // Load sections
    loadTasks();
    loadTeam();
    loadRisks();
    
    // Set up navigation
    setupNavigation();
    
    // Set up event listeners
    setupEventListeners();
    
    // Update last modified date
    updateLastModified();
    
    console.log('Dashboard loaded successfully!');
});

// ============================================
// Metrics & Overview Functions
// ============================================

function updateMetrics() {
    // Total tasks
    const totalTasks = projectData.tasks.length;
    document.getElementById('totalTasks').textContent = totalTasks;
    
    // Completed tasks
    const completedTasks = projectData.tasks.filter(t => t.status === 'complete').length;
    document.getElementById('completedTasks').textContent = completedTasks;
    
    // Active risks
    const activeRisks = projectData.risks.filter(r => r.status === 'active').length;
    document.getElementById('activeRisks').textContent = activeRisks;
    
    // Team members
    document.getElementById('teamMembers').textContent = projectData.team.length;
    
    // Progress percentage
    const progressPercent = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;
    document.getElementById('progressPercent').textContent = progressPercent;
    document.getElementById('progressBar').style.width = progressPercent + '%';
}

// ============================================
// Task Management Functions
// ============================================

function loadTasks(filter = 'all') {
    const taskList = document.getElementById('taskList');
    
    let filteredTasks = projectData.tasks;
    if (filter !== 'all') {
        filteredTasks = projectData.tasks.filter(t => t.status === filter);
    }
    
    if (filteredTasks.length === 0) {
        taskList.innerHTML = '<div class="empty-state"><p>No tasks match the current filter.</p></div>';
        return;
    }
    
    taskList.innerHTML = filteredTasks.map(task => `
        <div class="task-item" data-task-id="${task.id}">
            <h3>${task.name}</h3>
            <p><strong>Assigned to:</strong> ${task.assignee}</p>
            <p><strong>Status:</strong> <span class="status-badge status-${task.status}">${formatStatus(task.status)}</span></p>
            <p><strong>Priority:</strong> ${formatPriority(task.priority)}</p>
            <p><strong>Due Date:</strong> ${formatDate(task.dueDate)}</p>
        </div>
    `).join('');
}

function formatStatus(status) {
    return status.split('-').map(word => 
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
}

function formatPriority(priority) {
    const icons = {
        high: '🔴 High',
        medium: '🟡 Medium',
        low: '🟢 Low'
    };
    return icons[priority] || priority;
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
        month: 'short', 
        day: 'numeric', 
        year: 'numeric' 
    });
}

// ============================================
// Team Management Functions
// ============================================

function loadTeam() {
    const teamGrid = document.getElementById('teamGrid');
    
    teamGrid.innerHTML = projectData.team.map(member => `
        <div class="team-card">
            <div class="team-avatar">${member.initials}</div>
            <div class="team-name">${member.name}</div>
            <div class="team-role">${member.role}</div>
            <div class="team-email" style="font-size: 0.85rem; color: var(--text-light); margin-top: 0.5rem;">${member.email}</div>
        </div>
    `).join('');
}

// ============================================
// Risk Management Functions
// ============================================

function loadRisks() {
    const riskList = document.getElementById('riskList');
    
    const activeRisks = projectData.risks.filter(r => r.status === 'active');
    
    if (activeRisks.length === 0) {
        riskList.innerHTML = '<div class="empty-state"><p>No active risks identified.</p></div>';
        return;
    }
    
    riskList.innerHTML = activeRisks.map(risk => `
        <div class="risk-item" data-risk-id="${risk.id}">
            <h3>${risk.description}</h3>
            <p><strong>Probability:</strong> ${formatPriority(risk.probability)}</p>
            <p><strong>Impact:</strong> ${formatPriority(risk.impact)}</p>
            <p><strong>Owner:</strong> ${risk.owner}</p>
            <p><strong>Status:</strong> <span class="status-badge status-${risk.status}">${risk.status}</span></p>
        </div>
    `).join('');
}

// ============================================
// Navigation Functions
// ============================================

function setupNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            link.classList.add('active');
            
            // Scroll to section
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ============================================
// Event Listeners
// ============================================

function setupEventListeners() {
    // Task filter
    const taskFilter = document.getElementById('taskFilter');
    if (taskFilter) {
        taskFilter.addEventListener('change', (e) => {
            loadTasks(e.target.value);
        });
    }
    
    // Add task button
    const addTaskBtn = document.getElementById('addTaskBtn');
    if (addTaskBtn) {
        addTaskBtn.addEventListener('click', () => {
            alert('Add Task functionality - to be implemented!\n\nThis would open a form to create a new task.');
        });
    }
    
    // Add risk button
    const addRiskBtn = document.getElementById('addRiskBtn');
    if (addRiskBtn) {
        addRiskBtn.addEventListener('click', () => {
            alert('Add Risk functionality - to be implemented!\n\nThis would open a form to log a new risk.');
        });
    }
}

// ============================================
// Utility Functions
// ============================================

function updateLastModified() {
    const lastUpdatedElement = document.getElementById('lastUpdated');
    if (lastUpdatedElement) {
        const now = new Date();
        lastUpdatedElement.textContent = now.toLocaleDateString('en-US', {
            month: 'long',
            day: 'numeric',
            year: 'numeric'
        });
    }
}

// ============================================
// Export functions for testing (optional)
// ============================================

// Uncomment if you want to test functions in the console
// window.dashboardFunctions = {
//     updateMetrics,
//     loadTasks,
//     loadTeam,
//     loadRisks
// };
