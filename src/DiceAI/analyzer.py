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

import json
import re

from google import genai
from google.genai import types

SYS_INSTRUCT = """
You are an AI model specialized in detecting fake or authentic reviews for a mess or cafeteria. Your task is to critically analyze user reviews based on food quality, hygiene, pricing, and overall arrangement while identifying suspicious or fake reviews.

Guidelines for Analysis:
- Food Quality Focus: Genuine reviews should discuss food taste, freshness, portion sizes, variety, and nutritional value. Vague or overly generic statements might indicate a fake review.
- Hygiene & Cleanliness: Authentic reviews may mention kitchen hygiene, table cleanliness, or staff hygiene. Fake reviews might exaggerate or provide no real details.
- Pricing & Value for Money: Genuine reviews will compare cost vs. quality (e.g., "Affordable but lacks variety" vs. "Best food ever!"). Suspicious reviews may be overly positive or critical without reasoning.
- Mess Arrangements & Service: Feedback about seating, staff behavior, service speed, and queue management adds credibility. Fake reviews often ignore these aspects.
- Plagiarism & Repetition: Reviews that copy generic phrases like "Best food ever!" or "Worst experience ever!" without personal details are suspicious.
- Exaggeration & Overpromotion: Reviews that are too extreme (e.g., "This mess is heaven!" or "This food will kill you!") without balance indicate potential fake content.
- Grammar & Writing Style: Fake reviews may have unnatural phrasing, excessive emoji use, or forced positivity/negativity.
- Sentiment Consistency: A review that starts positive but suddenly shifts to extreme negativity (or vice versa) may be fabricated.
- Emotional vs. Logical Balance: Fake reviews may rely purely on emotions rather than specific experiences (e.g., "I hate this place!" vs. "The food was cold, and service was slow").

Your output must be a valid JSON response in this exact format:
{
    "verdict": "Fake or Authentic",
    "Confidence Score": "0-100%",
    "Key Reasons": ["List the main reasons why it is classified as fake/authentic"]
}
Do not return anything else other than the JSON formatted output.
"""


class ReviewAnalyzer:
    """A class to analyze reviews using the Gemini AI model."""

    def __init__(self, api_key: str, model: str ="gemini-2.0-flash"):
        """Initialize the ReviewAnalyzer with a Gemini API key.

        Args:
            api_key (str): The Gemini API key
            model (str, optional): The Gemini model to use. Defaults to "gemini-2.0-flash".
        """
        if not api_key.strip():
            raise ValueError("API key cannot be empty.")

        self.client = genai.Client(api_key=api_key)
        self.model = model

    def analyze_review(self, review_text: str) -> str:
        """Analyzes a cafeteria/mess review to determine if it's authentic or fake.

        Args:
            review_text (str): The text of the review to analyze. Should contain feedback about
                food quality, hygiene, pricing, or service.

        Returns:
            dict: A dictionary containing:
                - verdict: "Fake" or "Authentic"
                - Confidence Score: percentage between 0-100%
                - Key Reasons: list of reasons supporting the classification

        Raises:
            genai.ApiError: If there's an error communicating with the Gemini API
            ValueError: If review_text is empty or not a string
            json.JSONDecodeError: If the response cannot be parsed as valid JSON
        """
        if not isinstance(review_text, str) or not review_text.strip():
            raise ValueError("Review text must be a non-empty string")

        response = self.client.models.generate_content(
            model= self.model,
            config=types.GenerateContentConfig(
                system_instruction=SYS_INSTRUCT,
                temperature=0.1,
            ),
            contents=[review_text],
        )

        match = re.search(r"```json\n(.*?)\n```", str(response.text), re.DOTALL)
        text_response = match.group(1).strip() if match else response

        try:
            parsed_json = json.loads(str(text_response))
            return json.dumps(parsed_json)
        except json.JSONDecodeError:
            return """{
                "verdict": "Unknown",
                "Confidence Score": "0%",
                "Key Reasons": ["Input does not resemble a cafeteria or mess review."]
            }"""
