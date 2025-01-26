import requests
from bs4 import BeautifulSoup

# This script fetches and parses a website's content to extract titles and links.
# How to use:
# - Replace `website_url` with the desired URL.
# - Run the script to print all titles and links found on the webpage.

def fetch_website_data(url):
    """
    Fetches and parses website data to extract titles and links.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all headings and links
        data = []
        for item in soup.find_all('a'):
            title = item.text.strip()
            link = item.get('href', '')
            if title and link:
                data.append({'title': title, 'link': link})
        
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    website_url = "https://example.com"  # Change this to the website you want to scrape
    result = fetch_website_data(website_url)
    for entry in result:
        print(f"Title: {entry['title']} - Link: {entry['link']}")