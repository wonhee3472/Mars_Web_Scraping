# Mars Web Scraping App
<img src='https://www.bitou.net/wp-content/uploads/sites/3/2020/11/mission-to-mars_Header-1366x546.jpg'>

## Objective
Build a web application that scrapes various websites for data related to planet Mars and displays the following information in a single HTML page:
* Latest News
* Featured Image
* Facts about the planet
* Images of the hemispheres

## 1. Scraping Mars Data
Followings are what I scraped from the different websites for various information about Mars.

### NASA Mars News 
* Scraped the [NASA Mars News Site](https://redplanetscience.com)
![](mission_to_mars/images/Title_Text.png)

### JPL Mars Space Images - Featured Image
* Visited the url for JPL Featured Space Image [here](https://spaceimages-mars.com)
* Used Splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `img_url`
![](mission_to_mars/images/Feature_Image.png)

### Mars Facts
* Visited [the Mars Facts webpage](https://galaxyfacts-mars.com/)
* Used Pandas to convert the data to a HTML table string
![](mission_to_mars/images/Mars_Facts.png)

### Mars Hemispheres
* Visited the [GUSS Science Center website](https://marshemispheres.com/) to obtain high resolution images for each of Mars' hemispheres
* Selected hemisphere links to find image url to the full resolution image
* Saved both the image url string for the full resolution hemisphere image, and the hemisphere title containing the hemisphere name.
* Used a Python dictionary to store the data using the keys `img_url` and `title`.
* Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere
![](mission_to_mars/images/Mars_Hemispheres.png)

# MongoDB and Flask Application
Exported the [Mission_to_Mars notebook](mission_to_mars/Mission_to_Mars.ipynb) into a `Python` [script](mission_to_mars/scraping_mars.py). Using this script as the starting point, I started to define the scraping process by adding functions to scrape through the websites and loop through the HTML tags to return the information used to create a database which is stored in `MongoDB`

![](mission_to_mars/images/scrape_all_script.png)

Using the database in `Mongo`, I created a `Flask` app to connect to the information and created the [app routes](mission_to_mars/app.py):
* Route called `/scrape` imports `scraping_mars.py` script and call each function `scrape_all` function.
* Root route `/` queries the Mongo database and passes the mars data into an HTML template to display the data.
* Template HTML file called `index.html` will take the mars data dictionary and display all of the data in the appropriate HTML elements.

# Mission to Mars App
![](mission_to_mars/images/Mars_Screenshot.png)
