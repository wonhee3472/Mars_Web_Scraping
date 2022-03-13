# The first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL.
# The second line says we'll use PyMongo to interact with our Mongo database.
# The third line says that to use the scraping code, we will convert from Jupyter notebook to Python.
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping_mars

# Setting up Flask
app = Flask(__name__)

# app.config["MONGO_URI"] tells Python that our app will connect to Mongo using a URI, 
# a uniform resource identifier similar to a URL.
# "mongodb://localhost:27017/mars_app" is the URI we'll be using to connect our app to Mongo. 
# This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "mars_app"
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
# This route tells Flask what to display when we're looking at the home page, index.html
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)
# mars = mongo.db.mars.find_one() uses PyMongo to find the "mars" collection in our database,
# which we will create when we convert our Jupyter scraping code to Python Script.
# "return render_template("index.html" tells Flask to return an HTML template using an index.html file
# ", mars=mars)" tells Python to use the "mars" collection in MongoDB

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping_mars.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect("/", code=302)
# This route will run the function that we create just beneath it
# The first line assigns a new variable that points to our Mongo database
# The second line creates a new variable to hold the newly scraped data
# In the second line, we're referencing the "scrape_all" function in the scraping.py
# The last line updates the database using ".update_one()"

# .update_one(query_parameter, {"$set": data}, options)
# In the query_parameter, we can specify a field (e.g. {"news_title": "Mars Landing Successful"}), in which case MongoDB will update a document with a matching news_title. Or it can be left empty ({}) to update the first matching document in the collection.
# Next, we'll use the data we have stored in mars_data. The syntax used here is {"$set": data}. This means that the document will be modified ("$set") with the data in question.
# Finally, the option we'll include is upsert=True. This indicates to Mongo to create a new document if one doesn't already exist, and new data will always be saved (even if we haven't already created a document for it).

# Finally, we will add a redirect after successfully scraping the data: return redirect('/', code=302). This will navigate our page back to / where we can see the updated content.

if __name__ == "__main__":
    app.run()
# This final bit of code we need for Flask is to tell it to run