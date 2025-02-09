"""
DiceAI Module

This module provides the `ReviewAnalyzer` class, which uses Google's Gemini AI
to analyze cafeteria and mess reviews for authenticity. It evaluates reviews based
on factors like food quality, hygiene, pricing, and service to determine whether
a review is genuine or potentially fake.

Features:
- Detects fake or authentic reviews using AI analysis.
- Evaluates reviews based on key attributes such as hygiene, pricing, and sentiment.
- Returns a structured JSON response with a verdict, confidence score, and key reasons.

Usage:
    from DiceAI import ReviewAnalyzer

    analyzer = ReviewAnalyzer(api_key="YOUR_API_KEY")
    review_text = "The food was cold and service was slow."
    result = analyzer.analyze_review(review_text)
    print(result)  # JSON string with analysis results

Raises:
- ValueError: If the input review is empty or not a string.
- json.JSONDecodeError: If the API response is not a valid JSON.
- genai.ApiError: If there's an error communicating with the Gemini API.
"""

from DiceAI.analyzer import ReviewAnalyzer

__version__ = "0.1.0"
__all__ = ["ReviewAnalyzer"]
