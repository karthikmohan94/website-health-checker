# Website Health Checker

A simple Python command-line tool that checks whether websites are reachable, reports their HTTP status codes, measures response time, and saves the results to a CSV file.

## Features

- Check one or multiple websites in a single run
- Automatically adds `https://` when needed
- Displays HTTP status codes
- Measures website response time
- Handles connection errors and timeouts
- Saves every check to `results.csv`
- Adds timestamps to saved results
- Ignores empty website entries

## Technologies Used

- Python
- Requests
- CSV
- Datetime
- Time

## Python Concepts Demonstrated

This project uses several core Python concepts, including:

- Functions
- Variables
- Lists
- Loops
- Conditionals
- String methods
- Exception handling with `try` and `except`
- File handling
- Working with CSV files
- External Python packages
- HTTP requests

## Installation

Clone the repository:

```bash
git clone https://github.com/karthikmohan94/website-health-checker
```

Move into the project folder:

```bash
cd website-health-checker
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required package:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python main.py
```

Enter one or multiple website URLs separated by commas:

```text
google.com, github.com, python.org
```

Example output:

```text
==============================
     WEBSITE HEALTH CHECKER
==============================

Checking https://google.com...

----- RESULT -----
Website: https://google.com
Status: ONLINE
HTTP Status Code: 200
Response Time: 0.42 seconds
```

The results are also saved automatically to:

```text
results.csv
```

Example:

```text
Checked At,Website,Status,HTTP Status Code,Response Time
2026-10-05 15:45:00,https://google.com,ONLINE,200,0.42
```

## Project Structure

```text
website-health-checker/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Why I Built This Project

I built this project to strengthen my understanding of Python, HTTP requests, error handling, file operations, and working with external libraries while creating a practical tool related to web development.

## Future Improvements

Possible improvements include:

- Categorizing 2xx, 3xx, 4xx, and 5xx responses separately
- Adding repeated monitoring
- Exporting JSON reports
- Adding automated tests
- Adding a graphical or web-based interface
