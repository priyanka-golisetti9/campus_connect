from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # Your web scraping code
    url = "https://www.svecw.edu.in/#2"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    news_ul = soup.find('ul', class_='latestnews')
    news_items = [li_tag.text.strip() for li_tag in news_ul.find_all('li')]

    # Render the template with the scraped data
    return render_template('index.html', news_items=news_items)

if __name__ == '__main__':
    app.run(debug=True)
