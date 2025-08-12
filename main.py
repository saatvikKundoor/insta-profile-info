from bs4 import BeautifulSoup
import requests
username = str(input("What is your username?"))
URL = "https://www.instagram.com/" + username
print(URL)
