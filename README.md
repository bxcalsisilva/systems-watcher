# systems-watcher
Watcher and alert of system inactivity


# Work flow
- Starts at XX:00 (to define)
- Look for the file of the day in google drive
    - If file not found till XX:00 (to define) send alert
- Store file size and timestamp
- Sleep for X minutes (to define)
    - Get fileSize and if not changed rise flag
- If x flags (to define) are rised send alert
- End at XX:00 (to define)

# Considerations
- May want to not send alert if message already send X days ago
    - Avoid alerts on consecutive days when problem takes several days to fix.
- Create filter in email client of supervisors to store alerts