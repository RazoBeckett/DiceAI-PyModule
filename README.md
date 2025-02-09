# DiceAI - PyModule

A Python package that uses Google's Gemini AI to analyze cafeteria and mess reviews for authenticity and many more...

## Installation

```bash
pip install -e .
```

## Usage

```python
from DiceAI import ReviewAnalyzer

analyzer = ReviewAnalyzer(api_key="YOUR_GEMINI_API_KEY")
# analyzer = ReviewAnalyzer(api_key="YOUR_GEMINI_API_KEY", model="YOUR_DESIRED_AVAILABLE_MODEL") # default is gemini-2.0-flash

result = analyzer.analyze_review("The food was amazing and service was great!")
print(result)
```
