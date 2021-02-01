# Python Script for Scraping Data from http://www.mushroom.world/mushrooms/namelist


import scrapy


class mushroom_scraper(scrapy.Spider):
    name = 'posts'

    start_urls = ['http://www.mushroom.world/mushrooms/namelist']

    