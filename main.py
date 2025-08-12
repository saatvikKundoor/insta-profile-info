from bs4 import BeautifulSoup
import requests
username = str(input("What is your username?"))
URL = "https://www.instagram.com/" + username + "/"
r = requests.get(URL)
s = BeautifulSoup(r.text, "html.parser")
meta = s.find("meta", property = "og:description")
print(meta)
