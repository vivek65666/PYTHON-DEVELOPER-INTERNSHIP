# Python News Headline Scraper

A simple Python web scraper that collects news headlines from a public news website using `requests` and `BeautifulSoup`.

## Task Objective

The objective of this project is to automate the collection of news headlines from a public website and save the collected data into a text file.

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- HTML
- Git
- GitHub

## Features

- Sends an HTTP GET request to a public news website
- Uses a User-Agent header
- Parses HTML using BeautifulSoup
- Extracts headlines from HTML heading tags
- Removes duplicate and unwanted section headings
- Saves the collected headlines into `headlines.txt`
- Includes error handling using `try-except`

## Project Structure

```text
TASK-3-NEWS-HEADLINE-SCRAPER/
│
├── scraper.py
├── headlines.txt
├── requirements.txt
├── .gitignore
└── README.md