import pytest
from src.agents import multi_ai_agent  # Update with the correct module import

def test_agent_response(capfd):
    query = "Tell me about Apple Inc. stock"
    try:
        multi_ai_agent.print_response(query)
        out, err = capfd.readouterr()
        assert "Apple Inc." in out, "Response did not contain expected company name"
    except Exception as e:
        pytest.fail(f"API call failed: {e}")