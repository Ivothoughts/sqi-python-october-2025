# import requests
# from bs4 import BeautifulSoup

# url = "https://afr.808ball9.com/"

# response = requests.get(url)

# with open("Score808.html", "w") as f:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     f.write(soup.prettify())

import requests

from bs4 import BeautifulSoup

url = "https://www.freelancer.com/dashboard"

response = requests.get(url)

with open("free.html", "w") as f:
    soup = BeautifulSoup(response.text, 'html.parser')
    f.write(soup.prettify())