import pytest
import pandas as pd
from datetime import datetime
from src.utils import format_stock_data, validate_stock_symbol, format_datetime

def test_format_stock_data():
    data = [{"Symbol": "AAPL", "Price": 150.25}, {"Symbol": "NVDA", "Price": 450.60}]
    result = format_stock_data(data)
    
    assert "AAPL" in result and "NVDA" in result, "Stock symbols not formatted correctly."
    assert "150.25" in result and "450.60" in result, "Prices not formatted correctly."

def test_validate_stock_symbol():
    assert validate_stock_symbol("AAPL") == True, "Valid stock symbol failed."
    assert validate_stock_symbol("nVDA") == False, "Lowercase symbol should fail."
    assert validate_stock_symbol("1234") == False, "Numeric symbols should fail."
    assert validate_stock_symbol("AAPL!") == False, "Symbols with special chars should fail."

def test_format_datetime():
    dt = datetime(2024, 3, 10, 15, 30, 45)
    assert format_datetime(dt) == "2024-03-10 15:30:45", "Datetime format mismatch."

