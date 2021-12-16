#I use this in Pycharm, you will need to manually import "request" and "BeautifulSoup" libraries

# Import libraries
from bs4 import BeautifulSoup
import requests

# Prompt user to enter the URL
# url = input("Type URL here: -")

# Uses a txt file with the urls in
url = "http://URL.com"

# Make a request to get the URL
page = requests.get(url)

# Get the response code of given URL
response_code = str(page.status_code)

# Display the text of the URL in str
data = page.text

# Use BeautifulSoup to use the built-in methods
soup = BeautifulSoup(data)

# If you would prefer the output written to a text file
f = open('c:\TEXTfile.txt', 'w')
for link in soup.find_all('a'):
    print(f"Url: {link.get('href')} " + f"| Status Code: {response_code}", file=f)
