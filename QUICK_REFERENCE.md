# Quick Reference Guide

## Running the Simulation

### Interactive Mode
```bash
python simulation_cli.py
```

### Demo Mode (Automated)
```bash
python demo.py
```

### Running Tests
```bash
python test_simulation.py
```

## Key Concepts

### Task Status Flow
```
Not Started → In Progress → Completed
                 ↓
              Blocked → In Progress
                 ↓
              Overdue
```

### Team Morale Impact
- **High Morale (>70%)**: Full productivity
- **Medium Morale (50-70%)**: Reduced productivity
- **Low Morale (<50%)**: Significantly reduced productivity

### Morale Factors
- ✅ **Increases**: Completing tasks, being on schedule
- ⚠️ **Decreases**: Overdue tasks, conflicts, technical issues

### Event Types

#### Team Conflicts (5% daily chance)
- Reduces morale of involved members
- Creates communication issues
- Resolved by: Team meetings, one-on-one discussions

#### Scope Changes (3% daily chance)
- Adds additional work hours
- Can affect project timeline
- Handled by: Accept/negotiate/defer decisions

#### Technical Issues (7% daily chance)
- Blocks tasks from progressing
- Requires resolution to unblock
- Fixed by: Technical solutions, escalation

#### Availability Issues (4% daily chance)
- Reduces team member capacity
- Temporary (2-5 days typically)
- Causes: Sick leave, vacation, training

## Decision Making Tips

### Task Assignment
1. Match skills to task requirements
2. Consider current workload (max 2-3 tasks per person)
3. Check team member availability and morale
4. Prioritize critical path tasks

### Issue Resolution
1. Address high-severity issues first
2. Unblock tasks to maintain progress
3. Resolve conflicts quickly to restore morale
4. Document resolutions for learning

### Schedule Management
1. Monitor completion percentage vs. days elapsed
2. Assign available tasks promptly
3. Watch for blockers and bottlenecks
4. Build buffer time for unexpected events

### Budget Management
- Average daily cost: $500 per team member
- Monitor spending vs. completion rate
- Over-budget projects impact success rating

## Success Metrics

### Project Completion
- ✅ **Successful**: On time, within budget, high morale
- ⚠️ **Challenging**: Minor delays or budget overruns
- ❌ **Difficult**: Significant delays, over budget, low morale

### Performance Indicators
- Completion rate vs. timeline
- Budget utilization efficiency
- Team morale maintenance
- Issue resolution speed
- Task overdue frequency

## Keyboard Shortcuts in CLI

- **1-9**: Menu selections
- **Enter**: Continue/Confirm
- **c**: Cancel current operation

## Common Scenarios

### Behind Schedule
**Actions:**
- Assign more tasks in parallel (if team has capacity)
- Resolve blockers immediately
- Focus on critical path tasks
- Consider accepting scope changes to later phase

### Low Team Morale
**Actions:**
- Resolve team conflicts quickly
- Avoid overloading team members
- Complete tasks to provide positive momentum
- Address availability issues

### Multiple Blockers
**Actions:**
- Prioritize by severity and impact
- Resolve issues affecting critical tasks first
- May need to reassign resources
- Document patterns for prevention

### Budget Concerns
**Actions:**
- Monitor daily burn rate
- Assess if scope can be reduced
- Ensure team productivity is maximized
- Track completion velocity

## Customization

### Adjust Event Frequencies
Edit `simulation_engine.py`:
```python
# In _generate_random_events method
if random.random() < 0.05:  # Change probability (0.05 = 5%)
    # Event generation
```

### Add New Scenarios
Create in `scenarios.py`:
```python
def create_my_project() -> Project:
    project = Project(...)
    # Add tasks and team
    return project
```

### Modify Team Skills
Edit scenario files to adjust:
- Team member skills
- Productivity levels (0.5 to 1.5)
- Availability (0.0 to 1.0)
- Initial morale (0.0 to 1.0)

## Troubleshooting

### No Available Tasks
- Check task dependencies
- Ensure prerequisite tasks are completed
- Some tasks require specific completed tasks

### Cannot Assign Task
- Team member lacks required skills
- Check skill match in team overview
- Consider training or hiring (future feature)

### High Budget Usage
- Normal: ~$3,000 per day for 6-person team
- Review if completion rate justifies spending
- Consider if project will finish within budget

## File Structure

```
Project-Management-Simulation/
├── README.md              # Main documentation
├── USER_GUIDE.md          # Comprehensive guide
├── QUICK_REFERENCE.md     # This file
├── models.py              # Data models
├── simulation_engine.py   # Simulation logic
├── scenarios.py           # Project templates
├── simulation_cli.py      # Interactive interface
├── demo.py               # Automated demo
└── test_simulation.py    # Test suite
```

## Support

For issues or questions:
1. Review the USER_GUIDE.md for detailed information
2. Check this Quick Reference for common scenarios
3. Run the demo to see features in action
4. Examine test_simulation.py for usage examples
