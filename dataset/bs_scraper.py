import os
import sys
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


#----------------------------------------------------#
#                   SETTINGS
#----------------------------------------------------#
# Start URL, adjust to our needs
url = "http://www.mushroom.world/mushrooms/namelist"
tld = "http://www.mushroom.world/"
save_directory = "./mushie_images/"

# Spoofed HTTP headers to give us access to the page
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }



#----------------------------------------------------#
#                   SCRAPE_SHROOM
#       Takes a Mushroom World mushroom URL
#       Scrapes text data, Saves to CSV
#       Scrapes images, saves locally
#----------------------------------------------------#
def scrape_shroom(url):
    # First, download page HTML for parsing
    req = requests.get(url, headers)
    soup = bs(req.content, 'html.parser')

    # Create the Dataframe to store all the info
    df = pd.DataFrame(columns=['latin_name',
                                'english_name',
                                'edibility',
                                'filename',
                                'mushroomworld_url',
                                'image_url'])

    #----------- TEXT DATA WRANGLING ----------#
    # Get the name, both english and latin
    name = soup.find("div", class_="caption").get_text().lstrip()
    try:
        # Now split them into two vars and get rid of all the junk
        latin_name, english_name = name.split("(")
        latin_name = latin_name.rstrip()
        english_name = english_name.rstrip().rstrip(")")
    except:
        latin_name = name
        english_name = "N/A"

    # Get the edibility (it's always the fourth attribute on the information header)
    edibility = soup.find_all("div", class_="textus")[3].get_text()
    try:
        edibility, _ = edibility.split(" (")
    except:
        pass

    #----------- IMAGE DATA WRANGLING ----------#
    # Extract all the "swipebox" elements that contain image references
    href_list = soup.findAll("a", class_="swipebox")

    # Now download each of these images locally
    for image in href_list:
        # First, concatenate the image filename with the TLD
        # To get the image URL on Mushroom.World
        img_url = image.get("href").lstrip('/..')
        img_url = tld + img_url

        # Next, get just the image filename without any URL business
        img_filename = image.get("href").lstrip('/../data/fungi/')

        # Now try to download the image from Mushroom.World
        try:
            response = requests.get(img_url)
            if response.status_code == 200:
                with open(save_directory + img_filename, 'wb') as f:
                    f.write(requests.get(img_url).content)
                    f.close()
        except:
            pass

        # Now we have to save all that image data to a data frame
        df = df.append({ 'latin_name' : latin_name,
                         'english_name' : english_name,
                         'edibility' : edibility,
                         'filename' : img_filename,
                         'mushroomworld_url' : url,
                         'image_url' : img_url
            },
            sort=False,
            ignore_index=True
            )
        # END FOR

    return df
    #END SCRAPE_SHROOM



#----------------------------------------------------#
#                    MAIN DRIVER
#----------------------------------------------------#
def main():
    # Check that the file doesn't exist first before making it
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Create the Dataframe to store all the info
    df = pd.DataFrame(columns=['latin_name',
                                'english_name',
                                'edibility',
                                'filename',
                                'mushroomworld_url',
                                'image_url'])

    # Get the URL to each mushroom page
    first_req = requests.get(url, headers)
    first_soup = bs(first_req.content, 'html.parser')
    mushroom_list = first_soup.find_all("a")

    # For each URL, scrape the desired information using our function
    for mushroom in mushroom_list:
        # But make sure that the URL is one we want!
        if tld in mushroom.get("href"):
            df_out = scrape_shroom(mushroom.get("href"))
            df = df.append(df_out)

    # Throw all that scraped data into a CSV
    df.to_csv(save_directory + "_scraped_data.csv")


main()


#----------------------------------------------------#
#                    REFERENCES
#----------------------------------------------------#
# https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
# https://wodan.xyz/python-how-to-download-all-the-images-from-the-website/
