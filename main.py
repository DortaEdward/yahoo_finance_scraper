import requests
from bs4 import BeautifulSoup

def create_url():
    symbol = str(input('Enter Stock Symbol: '))
    url = f'https://finance.yahoo.com/quote/{symbol}'
    return url

def get_html(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
    response = requests.get(url, headers = header)

    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_data(html):

    soup = BeautifulSoup(html,'html.parser')
    name = soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text
    price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text
    change = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text
    previous_close = soup.find('span', {'class': 'Trsdu(0.3s)'}).text
    open_price = soup.find('td',{'class':'Ta(end) Fw(600) Lh(14px)'}).text
    print(f'|Stock Name: {name}|', f'|Stock Price: ${price}|', f'|Change: {change}|', f'|Previous Close: ${previous_close}|', f'|Open Price: ${open_price}|')
    # print(f'Stock Price: ${price}')
    # print(f'Change: {change}')
    # print(f'Previous Close: ${previous_close}')
    # print(f'Open Price: ${open_price}')
    stock_data = {
        'name':name,
        'price':price,
        'change':change ,
        'previous_close': previous_close,
        'open_price': open_price
    }

    return stock_data
    
def main():
    # get users input
    url = create_url()
    # get html
    html = get_html(url)
    # while loop 
    i = True
    while i:
        # parse data
        data = parse_data(html)


if __name__ == '__main__':
    main()