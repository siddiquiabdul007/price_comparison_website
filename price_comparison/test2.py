from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import csv

app = Flask(__name__)

def scrape_and_save_data():
    url = 'https://www.zomato.com/bangalore/delivery?dishv2_id=68987'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    data = []
    for item in soup.select('.jumbo-tracker'):
        name = item.find('h4', class_='sc-1hp8d8a-0').get_text().strip()
        rating = item.find('div', class_='sc-1q7bklc-6').get_text().strip()
        offer = item.find('p', class_='sc-1hez2tp-0').get_text().strip()

        div_tags = item.find_all('p', class_='sc-1hez2tp-0')
        text_div = None
        if len(div_tags) >= 2:
            text_div = div_tags[3].get_text(strip=True)

        data.append([name, text_div, rating, offer])

    # Set CSV file path
    csv_file = 'pizza_data.csv'

    # Write data to CSV file with 'utf-8' encoding
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Prices', 'Rating', 'Offer'])  # Write header
        writer.writerows(data)  # Write rows

    print("Data has been saved to", csv_file)

@app.route('/pizza')
def pizza_page():
    scrape_and_save_data()
    return render_template('pizza.html')

if __name__ == '__main__':
    app.run()
