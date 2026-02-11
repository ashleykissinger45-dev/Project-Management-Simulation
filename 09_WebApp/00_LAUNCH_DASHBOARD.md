# 🚀 Launch Dashboard

## Quick Access

**Local Server URL:** [http://localhost:8000](http://localhost:8000)

---

## How to Start the Dashboard

### Step 1: Start the Server

Open terminal and run:
```bash
cd "/Users/ashleykissinger/Project Management Simulation/09_WebApp"
python3 -m http.server 8000
```

### Step 2: Open in Browser

Click the link above or manually navigate to:
- **URL:** `http://localhost:8000`
- **Port:** 8000

### Step 3: View the Dashboard

You should see:
- ✅ Project metrics and KPIs
- ✅ Team member directory
- ✅ Task tracking table
- ✅ Risk monitoring
- ✅ Weekly progress reports

---

## Troubleshooting

**Port already in use?**
```bash
# Use a different port
python3 -m http.server 8001
# Then access: http://localhost:8001
```

**Server not starting?**
- Make sure you're in the `09_WebApp` directory
- Check that Python 3 is installed: `python3 --version`

---

## Files

- `index.html` - Main dashboard page
- `style.css` - Styling
- `script.js` - Interactive features

---

**Last Updated:** February 11, 2026
