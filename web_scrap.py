import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url= 'https://the-bibliofile.com/2022-historical-fiction-books-new-anticipated/'
page= requests.get(url)

soup= BeautifulSoup(page.content, 'html.parser')
bookname= soup.findAll(attrs= {'class': 'listtitle'})
authorsname= soup.findAll(attrs= {'class': 'listmeta'})
date_stuff= soup.findAll(attrs= {'class': 'listtext'})

data= []
for i in range(22):
    name= bookname[i].text
    authors= authorsname[i].text
    date_line= date_stuff[i].text
    for l in re.findall("Date: ..............", date_line):
        date= l.replace('Date: ', '')
        data.insert((i+1), [name, authors, date])
df= pd.DataFrame(data, columns= ['Book Name', "Author's Name", 'Date'])
df.to_csv('Historical_Fiction_Books_list.csv')
print('Csv made')
