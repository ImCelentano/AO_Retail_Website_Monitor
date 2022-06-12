import requests
from bs4 import BeautifulSoup
import time
import boto3

client = boto3.client('sns', 'eu-west-2')

def get_page_html(url):
    headers = {
    'authority': 'ao.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://ao.com/l/gaming/1/107-290/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("span", {"class": "inStockText text-body-sm"}) 
    print(out_of_stock_divs)   
    return out_of_stock_divs

def check_inventory():
    #url = "" #Instock product for testing
    url = "" #OOS product you want to monitor
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        print("In stock") 
        mUrl = ""
        data = {"content": 'in stock now! --> ' + url} 
        response = requests.post(mUrl, json=data)
        #client.publish(PhoneNumber='+xxx', Message='in stock now! --> ' + url')
        time.sleep(300)
        check_inventory()    
    else:
        print("Out of stock")
        time.sleep(2000)
        check_inventory()

check_inventory()
