import logging
import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    logging.error("GROQ_API_KEY is missing!")
    raise ValueError("GROQ_API_KEY missing")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY


#Web search agent - finds latest financial news
web_search_agent = Agent(
    name= "Web Search Agent",
    role= "Search the web for financial news and insights",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions=[
        "ALways include sources",
        "Summarize financial news concisely"
    ],
    show_tool_calls=True,
    markdown = True,
)


#Finance Agent - fetches stock market data
finance_agent = Agent(
    name = "Finance AI Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True,
                           stock_fundamentals= True, company_news= True)],
    instructions=[
        "Use tables to display stock data",
        "Provide insights based on trends",
        "Summarize analyst recommendations"
    ],
    show_tool_calls=True,
    markdown=True,
)


#Multi agent system - coordinates multiple agents 
multi_ai_agent = Agent(
    team = [web_search_agent, finance_agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Always include sources",
        "Use tables to display financial data"
    ],
    show_tool_calls=True,
    markdown=True,
)

logging.info("All AI agents initialized successfully")
