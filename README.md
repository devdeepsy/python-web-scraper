# Exam Question Downloader & Local DB Integration

A robust Python command-line utility designed to acquire UPSC and JEE competitive exam preparation questions and seamlessly map them into a structured localhost SQLite database. 

## Features
- **Dynamic Retrieval**: Built using `requests` and `BeautifulSoup4` to target open-source educational platforms.
- **Fail-Safe Processing**: Includes an integrated fallback system ensuring complete local schema generation and database hydration even during network dropouts or remote server blocks.
- **Local SQLite Integration**: Stores cleanly structured relational rows containing question bodies, isolated choices (A, B, C, D), and explicit answer values.

## Prerequisites
Ensure Python 3.8+ is installed on your local system.

## Setup & Installation

1. Clone or extract this project folder into your directory.
2. Install the required external dependencies:
   ```bash
   pip install -r requirements.txt