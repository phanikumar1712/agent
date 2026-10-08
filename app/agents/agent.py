from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from app.config.settings import settings
from app.tools import TOOLS


def create_agent():
    """
    Create and configure the LangChain agent.
    """

    llm = ChatOpenAI(
        model=settings.MODEL_NAME,
        temperature=0,
        api_key=settings.OPENAI_API_KEY,
    )

    system_prompt = """
You are a helpful AI assistant.

You have access to several tools.

Rules:

1. Use tools whenever they are appropriate.
2. Use web_search for information that may be current.
3. Use calculator for mathematical calculations.
4. Use get_current_datetime when the user asks for the current date or time.
5. Do not fabricate tool results.
6. Give concise but useful answers.
7. Explain your reasoning at a high level when useful.
"""

    agent = create_react_agent(
        model=llm,
        tools=TOOLS,
        prompt=system_prompt,
    )

    return agent