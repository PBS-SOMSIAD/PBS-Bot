from model import ModelOutput,PromptRequest

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from src.config import SETTINGS

ollama_model = OpenAIModel(
    model_name=SETTINGS.model,  # replace with your model name
    provider=OpenAIProvider(base_url=SETTINGS.base_url)
)

agent = Agent(
    model=ollama_model,
    output_type=ModelOutput,
    deps_type=str,
    system_prompt="Jesteś Patryk pomocny model językowy, który odpowiada na pytania i wykonuje polecenia użytkownika."
)

async def process_prompt(request: PromptRequest) -> ModelOutput:
    """
    Process the prompt using and returning the response.

    Args:
        request (str): The input prompt to process.

    Returns:
        ModelOutput: The response from the model.
    """
    response = await agent.run(
        request.prompt
    )
    return response.output
