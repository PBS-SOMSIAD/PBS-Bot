from fastapi import FastAPI
from datetime import datetime,timedelta
import time
from service import process_prompt
from src.model import PromptRequest, ModelOutput

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
    response = await process_prompt(request)
    return {
        "prompt": request.prompt,
        "response": f"Processed prompt: {response.response}",
    }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, log_level="info")


