import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
url = 'https://github.com/'+github_user
r = requests.get(url, verify=False)
soup = bs(r.content, 'html.parser')

profile_image = soup.find('img')['src']
print(profile_image)
