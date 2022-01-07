import requests
from bs4 import BeautifulSoup

user_date = input("Which year do you want to travel to? Please enter the date in this format YYYY-MM-DD:\n")

# construct url
url = f"https://www.billboard.com/charts/hot-100/{user_date}"

# debug
print(url)
