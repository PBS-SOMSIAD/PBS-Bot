from fastapi import FastAPI
from datetime import datetime,timedelta
import time

from src.model import PromptRequest

app = FastAPI()

start_time = time.time()


@app.get("/health")
async def health_check():

    uptime = time.time() - start_time
    uptime_str = str(timedelta(seconds=uptime))
    return {
        "status": "ok",
        "uptime": uptime_str,
        "timestamp": datetime.now().isoformat()
    }


@app.post("/prompt")
async def prompt(request: PromptRequest):
    # Simulate processing time
    time.sleep(1)
    return {
        "session_id": request.session_id,
        "prompt": request.prompt,
        "response": f"Processed prompt: {request.prompt}"
    }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, log_level="info")


