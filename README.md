# AI Trading Backend

AI Trading Backend is a demo backend service built with FastAPI that generates simple trading recommendations and analyses uploaded files. This project is intended for educational and demonstration purposes only and does not provide financial advice.

## Features

- **Analyze uploaded files**: Accepts uploaded documents (e.g., images, PDFs) and extracts text for analysis using Pytesseract.
- **Generate recommendations**: Provides random buy or sell suggestions with basic confidence scores via a simple algorithm in `recommendation.py`.
- **API endpoints**: Implements a `/analyze` POST endpoint using FastAPI.
- **Extensible architecture**: You can extend the recommendation logic to include real trading algorithms, machine learning models or integrate with exchanges.

## Getting Started

```bash
# Clone the repository
git clone https://github.com/JohnnyRoXoR/ai-trading-backend.git
cd ai-trading-backend

# Create virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
pip install -r requirements.txt

# Run the API server
uvicorn main:app --reload
```

Once the server is running, send a POST request to `http://localhost:8000/analyze` with a file attached (form-data key `file`) to receive a recommendation.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING](CONTRIBUTING.md) guidelines for details on how to submit bug reports, feature requests, and pull requests.

## Disclaimer

This project is for educational and demonstration purposes only and **should not** be used for real trading or investment decisions. The random recommendations provided by this demo are not financial advice.

## Support

If you find this project useful, please consider supporting its development by buying us a coffee at <https://www.buymeacoffee.com/aitradingbackend>. Your support helps maintain and improve this project.
