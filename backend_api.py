from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import psutil
import os

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production!
    allow_methods=["*"],
    allow_headers=["*"],
)

# Resolve full path to log file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "airtracker_debug.log")
log_lines = []

# Async task to tail the log file
async def tail_log():
    global log_lines
    print("👀 Waiting for log file...")

    while not os.path.exists(LOG_FILE):
        await asyncio.sleep(1)

    print("📂 Log file found. Reading existing lines...")
    with open(LOG_FILE, "r") as f:
        for line in f.readlines():
            log_lines.append(line.strip())

        f.seek(0, 2)  # Move to end of file
        print("🔁 Start tailing logs...")
        while True:
            line = f.readline()
            if line:
                print(f"📥 New log: {line.strip()}")
                log_lines.append(line.strip())
                if len(log_lines) > 200:
                    log_lines = log_lines[-200:]
            else:
                await asyncio.sleep(1)

# Start tailing when app launches
@app.on_event("startup")
async def startup_event():
    try:
        asyncio.create_task(tail_log())
    except Exception as e:
        print("❌ Failed to start log tailing:", e)

# Return last 50 log lines
@app.get("/logs")
def get_logs():
    return {"logs": log_lines[-50:]}

# Return system health info
@app.get("/health")
def get_health():
    return {
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
    }

# Return last 20 alerts (warning or error)
@app.get("/alerts")
def get_alerts():
    alerts = [line for line in log_lines if "WARNING" in line or "ERROR" in line]
    return {"alerts": alerts[-200:]}
