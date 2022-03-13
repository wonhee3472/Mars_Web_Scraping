# Mars Rover Web Scraping App

## Objective
Build a web application that scrapes various websites for data related to the Mission to Mars and displays the following information in a single HTML page:
* Latest News
* Featured Image
* Facts about the planet
* Images of the hemispheres

<img src='https://www.bitou.net/wp-content/uploads/sites/3/2020/11/mission-to-mars_Header-1366x546.jpg'>

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

### Mars Hemispheres
* Visited the [GUSS Science Center website](https://marshemispheres.com/) to obtain high resolution images for each of Mars' hemispheres


* Select hemisphere links to find image url to the full resolution image

## 2. Update the Web App with Mars' Hemisphere Images and Titles
