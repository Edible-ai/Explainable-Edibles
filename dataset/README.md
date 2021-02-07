## Mushroom Dataset Scraper
This is a web scraper built to retrieve images and text data of mushrooms from Mushroom.world, along with some simple data points. It was built using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), then [Selenium](https://www.selenium.dev/) functionality was added on to allow for image scraping from Google Images.

---
#### Prerequisites
You will need:
* Python 3.7+
* Pipenv
* An active internet connection


To install all the dependencies and start the virtual env, run the commands:
```sh
$ pipenv install
$ pipenv shell
```

Then, you will need to download the appropriate [ChromeDriver](http://chromedriver.chromium.org/downloads) for your operating system and browser. This allows Selenium to programmatically navigate Google Images.
Place this executable in the same directory as the Image_scraper jupyterlab notebook.


---
#### Usage
Launch Jupyterlab within the virtual env by running the command:
```sh
$ jupyter-lab
```
Then follow the notebook
