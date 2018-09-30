import requests
from selenium import webdriver
from bs4 import BeautifulSoup


browser = './chromedriver.exe'
url = 'http://openaccess.thecvf.com/ECCV2018.py'
header = 'http://openaccess.thecvf.com/'



browser = webdriver.Chrome(browser)
browser.get(url)
html = BeautifulSoup(browser.page_source, 'html.parser')
urls = ['{}{}'.format(header, a.get('href')) for a in html.find_all('a')]# if type(a.get('href')) is str]# and a.get('href')[-9:] == 'paper.pdf']


good_urls = []
for n,u in enumerate(urls):
    if u[-9:] == 'paper.pdf':
        good_urls += [u]

nb_pdf = len(good_urls)
print(nb_pdf)

for n,u in enumerate(good_urls):
    name = u.split('/')[-1]   
    print(str(n)+'/'+str(nb_pdf)+': '+name)
    response = requests.get(u)
    with open('papers/eccv18/'+name, 'wb') as f:
        f.write(response.content)


