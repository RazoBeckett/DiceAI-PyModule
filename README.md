# Review Analyzer

A Python package that uses Google's Gemini AI to analyze cafeteria and mess reviews for authenticity.

## Installation

```bash
pip install -e .
```

## Usage

```python
from review_analyzer import ReviewAnalyzer

analyzer = ReviewAnalyzer(api_key="YOUR_GEMINI_API_KEY")
result = analyzer.analyze_review("The food was amazing and service was great!")
print(result)
```
