#import required libraries
from bs4 import BeautifulSoup
import requests

#ask for username
username = str(input("What is your username? "))

#set proper URL for account
URL = "https://www.instagram.com/" + username + "/"

#get data from url using requests
r = requests.get(URL)

#structure data using BeautifulSoup
s = BeautifulSoup(r.text, "html.parser")

#find the basic profile data of account by checking for meta tag with specified property
meta = s.find("meta", property = "og:description")

#sort through data to return followers, following, and posts
def sort_data(dataset):
    # create dictionary
    data = {}

    # split data and take the first part
    info = dataset.split("-")[0]

    #split the data further into needed parts and assign key values
    data['Followers'] = info.split()[0]
    data['Following'] = info.split()[2]
    data['Posts'] = info.split()[4]

    #return the sorted data
    return(print(data))

#sort through data from the meta tag's html 'content' part. 
sort_data(meta.attrs['content'])
