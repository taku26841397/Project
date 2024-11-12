from bs4 import BeautifulSoup
from urllib import request


url='https://www.aozora.gr.jp/cards/000879/files/128_15261.html'

response=request.urlopen(url)
soup=BeautifulSoup(response)
response.close()

#print(soup)

main_text=soup.find('div',class_='main_text')
print(main_text)


tags_to_delete=main_text.find_all([''])