from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str

class ModelOutput(BaseModel):
    response: str