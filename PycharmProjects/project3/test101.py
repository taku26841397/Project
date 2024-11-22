from bs4 import BeautifulSoup
from urllib import request
import re


url='https://www.aozora.gr.jp/cards/000879/files/128_15261.html'

response=request.urlopen(url)
soup=BeautifulSoup(response)
response.close()

#print(soup)

main_text=soup.find('div',class_='main_text')
#print(main_text)


tags_to_delete=main_text.find_all(['rp','rt'])
for tag in tags_to_delete:
    tag.decompose()

#print(main_text)

main_text=main_text.get_text()
#print(main_text)

main_text = re.sub(r"[\u3000 \n \r]", "", main_text)
print(main_text)