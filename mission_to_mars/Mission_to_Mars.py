from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Sets the executable path and initializes the Chrome browser in Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

news_title = slide_elem.find('div', class_='content_title').get_text()
news_paragraph = slide_elem.find('div', class_='article_teaser_body').get_text()

# Visit the URL for images
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

# Use the base URL to create an absoulte URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns = ['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df.to_html()

browser.quit()
