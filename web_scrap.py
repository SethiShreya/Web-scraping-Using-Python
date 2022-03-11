import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
# paste below the url where you want to scrap data
url= 'https://the-bibliofile.com/2022-historical-fiction-books-new-anticipated/'
# send a get request to scrap data from the url provided
page= requests.get(url)

# this will beautify the content of the get request as html tags
soup= BeautifulSoup(page.content, 'html.parser')
# these three lines will extract the specified tag and store data in variable
bookname= soup.findAll(attrs= {'class': 'listtitle'})
authorsname= soup.findAll(attrs= {'class': 'listmeta'})
date_stuff= soup.findAll(attrs= {'class': 'listtext'})

data= []
# this loop will extract all the relevant info from the extracted data and create a csv file to store all the extracted data
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
