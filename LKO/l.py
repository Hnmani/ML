import requests
url="https://www.india.com/news/india/lucknow-nagar-nigam-election-results-winners-list-names-of-winning-candidates-of-congress-bjp-aimim-sp-bsp-aap-2698937/"
data=requests.get(url)

from bs4 import BeautifulSoup

soup=BeautifulSoup(data.text,'html.parser')

lucknowdist=soup.find('table',{'width':'617'})

lc=lucknowdist.findAll('td',attrs={'width':'204'})

def te(a):
  return a.text
l=list(map(te,lc))

import sqlite3

conn= sqlite3.connect('lucknow.sqlite')
cur=conn.cursor()
cur.execute('Drop table if exists Lucknow')
cur.execute('create table Lucknow (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name  TEXT UNIQUE)')
for d in l:
    d=d.replace('Ward','Lucknow')
    print(d)
    cur.execute('insert or ignore into Lucknow (name) values (?)',(d,))
    conn.commit()
