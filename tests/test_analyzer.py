import json

import pytest

from review_analyzer import ReviewAnalyzer


# Fixture to create an analyzer instance with a default model
@pytest.fixture
def analyzer():
    return ReviewAnalyzer(
        api_key="YOUR_API_KEY", model="gemini-2.0-flash"
    )  # Replace with a valid key from a secure source


def test_analyze_review_valid(analyzer):
    """Test a valid review input and ensure the output format is correct."""
    review = "The food was cold and service was slow. Portions were small for $12."
    result = analyzer.analyze_review(review)

    assert isinstance(result, str), "Output should be a JSON string"

    parsed_result = json.loads(result)

    assert isinstance(parsed_result, dict), "Parsed result should be a dictionary"
    assert "verdict" in parsed_result, "Missing 'verdict' field"
    assert "Confidence Score" in parsed_result, "Missing 'Confidence Score' field"
    assert "Key Reasons" in parsed_result, "Missing 'Key Reasons' field"
    assert isinstance(
        parsed_result["Key Reasons"], list
    ), "'Key Reasons' should be a list"


def test_analyze_review_empty(analyzer):
    """Test empty review input to ensure it raises a ValueError."""
    with pytest.raises(ValueError, match="Review text must be a non-empty string"):
        analyzer.analyze_review("")


def test_analyze_review_invalid_input(analyzer):
    """Test None as input to ensure it raises a ValueError."""
    with pytest.raises(ValueError, match="Review text must be a non-empty string"):
        analyzer.analyze_review(None)


def test_analyze_review_non_string(analyzer):
    """Test a non-string input (integer) to ensure it raises a ValueError."""
    with pytest.raises(ValueError, match="Review text must be a non-empty string"):
        analyzer.analyze_review(123)
