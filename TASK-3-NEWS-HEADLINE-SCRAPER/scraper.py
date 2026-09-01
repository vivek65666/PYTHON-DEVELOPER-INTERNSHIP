import requests
from bs4 import BeautifulSoup

# Public news website
url = "https://www.bbc.com/news"

# User-Agent header
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Section/navigation text to ignore
excluded_headlines = {
    "News",
    "More to explore",
    "Most watched",
    "Most read",
    "Also in news",
    "Sport",
    "The BBC is in multiple languages"
}

try:
    # Send GET request
    response = requests.get(url, headers=headers, timeout=10)

    # Check whether the request was successful
    response.raise_for_status()

    # Parse the HTML page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find headline elements
    headline_elements = soup.find_all(["h1", "h2", "h3"])

    unique_headlines = []

    for headline in headline_elements:
        text = headline.get_text(" ", strip=True)

        # Keep meaningful and unique headlines
        if (
            text
            and text not in excluded_headlines
            and text not in unique_headlines
        ):
            unique_headlines.append(text)

    # Save headlines to a text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for number, headline in enumerate(unique_headlines, start=1):
            file.write(f"{number}. {headline}\n")

    print(f"Successfully scraped {len(unique_headlines)} headlines.")
    print("Headlines saved to headlines.txt")

except requests.exceptions.RequestException as error:
    print(f"Error fetching the website: {error}")

except Exception as error:
    print(f"An unexpected error occurred: {error}")