# DiceAI - PyModule

A Python package that uses Google's Gemini AI to analyze cafeteria and mess reviews for authenticity and many more...

## Features

- Detects the authenticity of cafeteria and mess reviews.

- Supports multiple Gemini AI models.

- Easy-to-use API for quick integration.

## Installation

Install the package using:

```bash
pip install -e .
```

## Usage

### Basic Example:

```python
from DiceAI import ReviewAnalyzer

analyzer = ReviewAnalyzer(api_key="YOUR_GEMINI_API_KEY")

# Optionally, specify a different model (default is gemini-2.0-flash)
# analyzer = ReviewAnalyzer(api_key="YOUR_GEMINI_API_KEY", model="YOUR_DESIRED_AVAILABLE_MODEL")

result = analyzer.analyze_review("The food was amazing and service was great!")
print(result)
```

### Changing the AI Model

You can switch to a different Gemini AI model after initalization:

```python
analyzer.change_model("gemini-2.0-flash")
```

## License

This project is licensed under the [MIT](https://opensource.org/license/mit) License.

## Contributing

We welcome contributions! Feel free to submit issues or pull requests.

## Contact

For inquiries, reach out via GitHub Issues.
