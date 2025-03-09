import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import logging
from src.agents import multi_ai_agent
from src.config import LOGS_DIR

def get_stock_analysis(stock_symbol):
    logging.info(f"Fetching stock analysis for {stock_symbol}")
    response = multi_ai_agent.print_response(
        f"Summarize analyst recommendation and share the latest news for {stock_symbol}"
    )
    return response

if __name__ == "__main__":
    print("Welcome to StockSage AI!")
    while True:
        stock_symbol = input("Enter a stock symbol (or type 'exit' to quit): ").upper()
        if stock_symbol == "EXIT":
            print("Goodbye!")
            break
        result = get_stock_analysis(stock_symbol)
        print(result)
