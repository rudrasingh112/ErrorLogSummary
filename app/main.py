from fastapi import FastAPI, BackgroundTasks
from app.database import log_collection, client
from app.models import LogEntry, AnalysisRequest
from app.services.ai_service import LogAnalyst
from datetime import datetime, timedelta, timezone

app = FastAPI(title='AI Log Monitor')

analyst = LogAnalyst()


@app.on_event("startup")
async def ping_server():
    try:
        await client.admin.command("ping")
        print("success")
    except Exception as e:
        print(f"unable to connect to mongoDB due to : {e}")

@app.post("/ingest")
async def ingest_log(log: LogEntry):
    try:
        await log_collection.insert_one(log.model_dump())
        return {"status": "Log recorded"}
    except ValueError:
        return {"status": "Failed"}
    
@app.post("/analyze")
async def ask_ai(request: AnalysisRequest):
    start_time = datetime.now(timezone.utc) - timedelta(minutes= request.time_window_minutes)
    cursor = log_collection.find({"timestamp": {"$gte":start_time}})
    logs = await cursor.to_list(length=100)

    result = await analyst.analyze(request.question, logs=logs)
    if result:
        return result
    else:
        return {"status": "No analysis found"}
