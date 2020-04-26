# to grab the webpage
from urllib.request import urlopen as uReq
# to parse the webpage
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
# opening up connection, grabbing the web page
uClient = uReq(my_url)

# download the html content in a variable
page_html = uClient.read()

# close the connection
uClient.close()

# parse the html
page_soup = soup(page_html, 'html.parser')

# grabs each graphic card. finaAll() returns a list
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, 'w')

headers = "Brand, Product_Name, Shipping_price\n"
f.write(headers)

for container in containers:
	brand = container.findAll("a", {"class":"item-brand"})[0].img['title']
	
	# text is the written text in the anchor
	product_name = container.findAll("a", {"class":"item-title"})[0].text
	
	shipping_price = container.findAll("li", {"class":"price-ship"})[0].text.strip()

	# print("Brand: ",brand)
	# print("Product_name: ",product_name)
	# print("Shipping_price: ",shipping_price)
	# print()
	f.write(brand + "," + product_name.replace(',','|') + "," + shipping_price + "\n")
f.close()