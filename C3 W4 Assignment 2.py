import urllib.error, urllib.request, urllib.parse
from bs4 import BeautifulSoup
url = input("Enter URL: ")
b = int(input("Enter count: "))
a = int(input("Enter position: "))-1

for c in range(b):

    x = urllib.request.urlopen(url).read()
    y = BeautifulSoup(x,'html.parser')
    z = y('a')
    d = z[a].get('href',None)
    url = d
    print('Retrieving:',url)
    #e = z[a].contents[0]
#print(e)
