from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    base_url = 'https://eenadu.net'  # Replace with your desired base URL
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    return render_template('index.html', links=links)

@app.route('/view')
def view():
    url = request.args.get('url')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    fullstory_div = soup.find('div', {'class': 'fullstory'}) or soup.find('section', {'class': 'fullstory'})
    if fullstory_div:
        # Extract headings and paragraphs while preserving their HTML structure
        headings_and_paragraphs = fullstory_div.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])
        text_content = ''.join(str(tag) for tag in headings_and_paragraphs)
        return render_template('view.html', text_content=text_content)
    else:
        # Extract all links on the page
        links = soup.find_all('a', href=True)
        return render_template('index.html', links=links)


if __name__ == '__main__':
    app.run(debug=True, port=6060)