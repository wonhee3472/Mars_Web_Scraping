#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# set the executable path, and then set up the URL (NASA Mars News) for scraping.
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# assign the url and instruct the browser to visit it
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# This line of code serves two purposes:
# First, we're searching for elements with a specific combination of tag (div) and attribute (list_text)
# for example, ul.item_list would be found in HTML as <ul class="item_list">
# Second, we're also telling our browser to wait one second before searching for components. 
# The optional delay is useful because sometimes dynamic pages take a little while to load, 
# especially if they are image-heavy.


# In[4]:


# Set up the HTML parser:
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
# We've assigned slide_elem as the variable to look for the <div /> tag and 
# its descendent (the other tags within the <div /> element)


# ## Scraping Mars Data: The News
# 
# The data Robin wants to collect from this particular website is the most recent news article along with its summary. Remember, the code for this will eventually be used in an application that will scrape live data with the click of a button—this site is dynamic and the articles will change frequently, which is why Robin is removing the manual task of retrieving each new article.

# In[5]:


slide_elem.find('div', class_='content_title')
# When we do this, we're saying, "This variable holds a ton of information, 
# so look inside of that information to find this specific data." 
# The data we're looking for is the content title, which we've specified by saying, 
# "The specific data is in a <div /> with a class of 'content_title'."


# In[6]:


# But we need to get just the text, and the extra HTML stuff isn't necessary. 
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ## Scraping Mars Data: Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
# The indexing chained at the end of the first line of code means we want the browser to select the second button


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='headerimage').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Scraping Mars Data: Mars Facts

# In[13]:


# Visit URL
url = 'https://galaxyfacts-mars.com/'
browser.visit(url)


# In[14]:


# <tbody> is the body of the table—the headers, columns, and rows.
# <tr> is the tag for each table row
# <td> is the stored table data
# Instead of scraping each row, or the data in each <td />, 
# we're going to scrape the entire table with Pandas' .read_html() function.

df = pd.read_html("https://galaxyfacts-mars.com/")[0]
# The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML. 
# By specifying an index of 0, we're telling Pandas to pull only the first table it encounters, 
# or the first item in the list. Then, it turns the table into a DataFrame.

df.columns=['description', 'Mars', 'Earth']
# we assign columns to the new DataFrame for additional clarity.

df.set_index('description', inplace=True)
# By using the .set_index() function, we're turning the Description column into the DataFrame's index. 
# inplace=True means that the updated index will remain in place, without having to reassign the DataFrame to a new variable.

df


# In[15]:


# Pandas also has a way to easily convert our DataFrame back into HTML-ready code using the .to_html() function
df.to_html()
# After adding this exact block of code to Robin's web app, 
# the data it's storing will be presented in an easy-to-read tabular format.


# In[16]:


browser.quit()


# ## Mission_to_Mars_Challenge

# In[17]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[18]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[19]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[20]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[21]:


slide_elem.find('div', class_='content_title')


# In[22]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[23]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[24]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[25]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[26]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[27]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[28]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[29]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[30]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[31]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[32]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[33]:


html = browser.html
html_soup = soup(html, 'html.parser')


# In[34]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.


# In[35]:


for div in html_soup.find_all('div', class_="item"):
    hemispheres = {}
    img_url = 'https://marshemispheres.com/' + div.find("img")["src"]
    img_title = div.find("img")["alt"].replace(" thumbnail", "")
    hemispheres["img_url"] = img_url
    hemispheres["title"] = img_title
    hemisphere_image_urls.append(hemispheres)


# In[36]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[37]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




