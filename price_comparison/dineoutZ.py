import requests
from bs4 import BeautifulSoup

url = 'https://www.zomato.com/bangalore/dine-out?dishv2_id=56691'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

for item in soup.select('.jumbo-tracker'):
    name = item.find('h4', class_='sc-1hp8d8a-0').get_text().strip()
    rating = item.find('div', class_='sc-1q7bklc-6').get_text().strip()
    distance = item.find('p', class_='sc-1hez2tp-0').get_text().strip()

    div_tags = item.find_all('p', class_='sc-1hez2tp-0')
    text_div = None
# Extract text from the second div tag
    if len(div_tags) >= 2:
        text_div = div_tags[3].get_text(strip=True)
    # else:
    #     # text_div = div_tags[0].get_text(strip=True)
    #     print('No second div found')
    #cuisine = item.select('.sc-1hp8d8a-2.kjIICB')[0].text.strip()
    # price = item.find('div', class_="sc-doUfgd").get_text().strip()
    # item_price = item.find('div', class_="sc-1hez2tp-0 sc-dhmstB gNfAaa").get_text().strip(' ')
    # price_list = [price.text.strip() for price in prices]
    
    #delivery_time = item.select('.sc-1hp8d8a-4.kudNph')[0].text.strip()
    
    print("Name:", name)
    #print("Cuisine:", cuisine)
    print("Prices:", text_div)
    print("Rating:", rating)
    print("Distance:", distance)
    #print("Delivery Time:", delivery_time)
    print("____________")
