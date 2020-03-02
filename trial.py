print("Helloes")

# Let's uhhhhhhhh load beautifulsouppp

from bs4 import BeautifulSoup
import requests

URL = 'https://en.wikipedia.org/wiki/Aardvark'
#header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                        'AppleWebKit/537.36 (KHTML, like Gecko) '
#                        'Chrome/51.0.2704.103 Safari/537.36'}

content = requests.get(URL)
soup = BeautifulSoup(content.text, 'html.parser')

row = soup.find("div")
print(row)            # Print row with HTML formatting
print("=========Text Result==========")
print(row.get_text()) # Print row as text

x = row.get_text()


#req = requests.get(url,headers= header)

html = req.text

soup = BeautifulSoup(html,'html.parser')