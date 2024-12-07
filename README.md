# Project Title
This project focuses on analyzing solar energy data from various regions to understand the relationship between different climatic and environmental variables such as Global Horizontal Irradiance (GHI), ambient temperature (Tamb), wind speed (WS), relative humidity (RH), and barometric pressure (BP). The goal is to provide insights into solar power generation efficiency and to optimize the usage of solar energy in different geographical locations.

## Setup Instructions
1. Clone the repository.
2. Navigate to the project directory.
3. Run `python scripts/setup_environment.py` to set up your environment.
4. Install dependencies using `pip install -r requirements.txt`.

## Usage
- Run Jupyter notebooks:
  - `notebooks/JupiterNotebook1.ipynb`: Main data exploration and analysis.
  - `notebooks/ModelTraining.ipynb`: Model training and evaluation (if applicable).
- Run scripts:
  - `scripts/data_cleaning.py`: Data cleaning process.
  - `scripts/generate_reports.py`: Report generation from analysis.

## Testing
- Run unit tests using GitHub Actions on push/pull requests.
- Locally, run `pytest tests/` to execute the test suite.
