from bs4 import BeautifulSoup

file_path = 'html_files/Ground beef - Walmart.com.html'
with open(file_path) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

for list_view in soup.select('div[data-testid="list-view"]'):
    sub_soup = list_view
    product = ""
    for description in sub_soup.select('span[data-automation-id="product-title"]'):
        product += description.text
    for price in sub_soup.select('div[data-automation-id="product-price"] > span[class="w_iUH7"]'):
        if 'current' in price.text:
            product += ' ' + price.text
    print(product)