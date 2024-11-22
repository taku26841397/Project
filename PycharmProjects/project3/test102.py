from bs4 import BeautifulSoup
from urllib import request

url='http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
response=request.urlopen(url)
soup=BeautifulSoup(response)
response.close()

#print(soup)

stopwords_text=soup.text
print(stopwords_text)

stopwords_list=stopwords_text.split("\r\n")
stopwords_list=[word for word in stopwords_list if word]

split_text_list=['私', 'は', '今日', '、', 'スーパー', 'で', '沢山', 'の', 'お', '菓子', 'を', '買っ', 'た','。']
result_text_list=list()

for split_text in split_text_list:
    if split_text not in stopwords_list:
        result_text_list.append(split_text)

print(result_text_list)
