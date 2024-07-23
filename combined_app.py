from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Scrape code for the first website
def scrape_website1():
    url1 = 'https://www.iitm.ac.in/happenings/events'
    response1 = requests.get(url1, verify=False)

    if response1.status_code == 200:
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        event_elements = soup1.find_all('div', class_='col-md-3 col-sm-4')

        scraped_data = []
        for event_element in event_elements:
            event_title = event_element.find('h5', class_='section__cardheading').text.strip()
            try:
                date_and_time_elements = event_element.select('.section__cardimg ul li')
                event_date = date_and_time_elements[0].text.strip()
                event_time = date_and_time_elements[1].text.strip()
            except IndexError:
                event_date = "N/A"
                event_time = "N/A"

            scraped_data.append({
                "website": "MIT",
                "event_title": event_title,
                "event_date": event_date,
                "event_time": event_time
            })

        return scraped_data
    else:
        return []

# Scrape code for the second website
def scrape_website2():
    url2 = "https://www.svecw.edu.in/#2"
    response2 = requests.get(url2)
    html_content = response2.text
    soup2 = BeautifulSoup(html_content, 'html.parser')

    news_ul = soup2.find('ul', class_='latestnews')

    news_items = []
    for li_tag in news_ul.find_all('li'):
        news_text = li_tag.text.strip()
        news_items.append({
            "website": "SVECW",
            "news_item": news_text
        })

    return news_items

@app.route('/')
def index():
    # Call the scraping functions
    scraped_data1 = scrape_website1()
    scraped_data2 = scrape_website2()

    # Render the template with the scraped data
    return render_template('combined_index.html', scraped_data1=scraped_data1, scraped_data2=scraped_data2)

if __name__ == '__main__':
    app.run(debug=True)