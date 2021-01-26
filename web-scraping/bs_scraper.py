import os
import pandas
import requests
from bs4 import BeautifulSoup as bs



#----------------------------------------------------#
#                   GLOBAL SETTINGS
#----------------------------------------------------#
#start URL to adjust to our needs
url1 = "http://www.mushroom.world/mushrooms/namelist"
url = "http://www.mushroom.world/show?n=Agaricus-arvensis"
tld = "http://www.mushroom.world"

# Spoofed headers to give us access to the page
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

"""
# Get the URL to each mushroom page
first_req = requests.get(url1, headers)
first_soup = bs(first_req.content, 'html.parser')
mushroom_list = first_soup.find_all("a")

# For each URL, scrape the desired information using our function
for mushroom in mushroom_list:
    # But make sure that the URL is one we want!
    if tld in mushroom.get("href"):
        scrape_data(mushroom)
"""

#----------------------------------------------------#
#
#----------------------------------------------------#
# First, download page HTML for parsing
req = requests.get(url, headers)
soup = bs(req.content, 'html.parser')

# TEXT DATA WRANGLING
# Get the name, both english and latin
name = soup.find("div", class_="caption").get_text().lstrip()
# Now split them into two vars and get rid of all the junk
latin_name, english_name = name.split("(")
latin_name = latin_name.rstrip()
english_name = english_name.rstrip().rstrip(")")

# Get the edibility (it's always the fourth attribute on the information header)
edibility = soup.find_all("div", class_="textus")[3]
edibility, _ = edibility.get_text().split(" (")

# Get the MW URL
mushroomweb_url = mush_url

"""
# IMAGE DATA WRANGLING
# Extract all the "swipebox" elements that contain image references
image_list = soup.findAll("a", class_="swipebox")

# Extract out the filenames for each image from the HREF


# Now download each of these images locally
for image in image_list:
    try:
        img_url = image.get("href").lstrip('')
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:

            with open(url.lstrip('../data/fungi/'), 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
    except:
        pass
"""


#----------------------------------------------------#
# References
#----------------------------------------------------#
# https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
# https://wodan.xyz/python-how-to-download-all-the-images-from-the-website/
