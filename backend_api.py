# backend_api.py
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

LOG_FILE = "app.log"
log_lines = []

async def tail_log():
    global log_lines
    # If file does not exist yet, wait until created
    while not os.path.exists(LOG_FILE):
        await asyncio.sleep(1)

    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)  # Go to end of file
        while True:
            line = f.readline()
            if line:
                log_lines.append(line.strip())
                if len(log_lines) > 200:  # keep last 200 lines
                    log_lines = log_lines[-200:]
            else:
                await asyncio.sleep(1)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(tail_log())

@app.get("/logs")
def get_logs():
    return {"logs": log_lines[-50:]}  # last 50 lines

@app.get("/health")
def get_health():
    return {
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
    }

@app.get("/alerts")
def get_alerts():
    alerts = [line for line in log_lines if "WARNING" in line or "ERROR" in line]
    return {"alerts": alerts[-20:]}  # last 20 alerts

