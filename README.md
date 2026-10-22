# stage-ecms-backend

Backend service for Stage ECMS e-commerce platform.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python src/app.py
   ```

## API Endpoints

- `POST /shipping` - Calculate shipping cost (returns 10% of order value)