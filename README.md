# insta-profile-info
A Python-based Instagram profile web scraper that returns the number of followers, following, and posts from a given instagram username. 

## Getting Started:
### Set up:
Download libraries
```python
pip install beautifulsoup4
pip install requests
```
**Example User Input:** github

**Example Output** {'Followers': '570K', 'Following': '54', 'Posts': '1,083'}



## How It's Made:

### Tech used: 
Python - Libraries: `BeautifulSoup`, `Requests`

### Steps:

**1. User Input** 

The user will input the profile target's username.
```Python
username = str(input("What is your username? "))
```
**2. URL Structuring** 

Create the public URL of the account's profile using string concatenation.

```python
URL = "https://www.instagram.com/" + username + "/"
```

**3. Data Retrieval** 

Use Requests to scrape the data from the created URL.

```python
r = requests.get(URL)
``` 

**4. HTML Structuring** 

Using BeautifulSoup, the text content of the URL is better structured using "html.parser".

```python
s = BeautifulSoup(r.text, "html.parser")
```

**5. Retrieving Profile Metadata** 

I use .find() to retrieve the basic profile data from the html. 

```python
meta = s.find("meta", property = "og:description")
```

**6. Finalizing Data** 

I extract the following, followers, and post data from the metadata and return the data in the form of a dictionary.

```python
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
```


## Lessons Learned:

1. How to use HTTPS requests and retrieve HTML
   - I created the URL and then used `request.get(URL)`.
2. How to parse through HTML data using BeautifulSoup
   - I used `BeautifulSoup(r.text, "html.parser") ` to properly structure Instagram's html.
3. How to use developer tools to read website HTML
   - I used Chrome's developer tools to understand the meta tags and content within.
4. How to sort through data into a readable finished product
   - I used dictionaries and `.split()` to return the following, followers, and post data in a readable format.

## Acknowledgements:
I used a GeeksforGeeks article as a basis and reference sheet while I was making this project.I used the article as a starting point to understand BeautifulSoup and Requests. I wrote much of the code while reading the article. However, I emphasized treating this as a learning experience, making sure to write, research, and understand each line of code. 

