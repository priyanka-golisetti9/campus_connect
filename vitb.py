import requests
from bs4 import BeautifulSoup

url = "https://vishnu.edu.in/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Locate the News & Events section based on the HTML structure
    news_events_section = soup.find('div', class_='main col-md-12')

    # Find all the listing items within the News & Events section
    event_items = news_events_section.find_all('div', class_='listing-item-body')

    for item in event_items:
        event_title = item.find('h3', class_='title').text.strip()
        event_date = item.find('cite').text.strip()
        print(f"Event Title: {event_title}\nEvent Date: {event_date}\n")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
