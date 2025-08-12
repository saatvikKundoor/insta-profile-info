from bs4 import BeautifulSoup
import requests
username = str(input("What is your username? "))
URL = "https://www.instagram.com/" + username + "/"
r = requests.get(URL)
s = BeautifulSoup(r.text, "html.parser")
meta = s.find("meta", property = "og:description")
def sort_data(dataset):
    data = {}
    info = dataset.split("-")[0]
    data['Followers'] = info.split()[0]
    data['Following'] = info.split()[2]
    data['Posts'] = info.split()[4]
    return(print(data))
    
sort_data(meta.attrs['content'])
print(meta)
