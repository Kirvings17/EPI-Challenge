# EPI-Challenge

The application:
- Loads CSV or Excel data
- Cleans invalid, duplicate, or missing values
- Optionally exports the cleaned data
- Answers analysis questions through a command-line menu

Requirements
- Python 3.9+
- pandas
- openpyxl (required for Excel files)

Install dependencies:

`pip install pandas openpyxl`

Setup
- Place your dataset file (e.g. worldData.csv or worldData.xlsx) inside the data/ folder.
- Run the Application
    * From the project src folder, run:
    `python main.py`
- Follow the instructions in the terminal.


Assumption: 
- All numeric fields (area_km2, pop, lifeExp, gdpPercap) must be greater than or equal to 0.
- lifeExp values are assumed to be realistic and therefore cannot exceed 120 years.
- String values are treated as case-sensitive unless normalized during cleaning. For example, "San Diego" and "San diego" would be considered different values unless explicitly standardised.