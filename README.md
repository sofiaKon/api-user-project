# User Data API Project

This project fetches user data from a public REST API, converts JSON into a pandas DataFrame, performs basic analysis, and saves the result to a CSV file.

## Features

- Sends a GET request to a public API
- Parses JSON data
- Extracts nested fields
- Builds a pandas DataFrame
- Counts users and unique cities
- Shows city frequency
- Saves data to `users.csv`

## Technologies

- Python
- requests
- pandas
- REST API
- JSON

## API Source

The project uses this public test API:

`https://jsonplaceholder.typicode.com/users`

## Project Structure

```bach

api_project/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

## How to Run

1. Create and activate a virtual environment
2. Install dependencies
3. Run the script

python -m pip install -r requirements.txt
python main.py

## Output

The script:

- prints a user table
- shows simple statistics
- saves the result as users.csv

## Learning Goals

This project was created to practice:

- working with APIs
- handling JSON
- using pandas for analysis
- saving structured data to CSV
