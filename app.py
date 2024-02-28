from flask import Flask, render_template, url_for, flash, redirect
from googleplaces import GooglePlaces
from forms import LocationInputForm
import dotenv, os
dotenv.load_dotenv()
gtoken = str(os.getenv("GTOKEN"))
flasktoken = str(os.getenv("FLASKTOKEN"))

app = Flask(__name__)
app.config['SECRET_KEY'] = flasktoken
gglObj = GooglePlaces(gtoken)

@app.route('/')
def home():  # put application's code here
    return render_template('home.html', name="Get2Helping")

@app.route('/testmaps')
def test_maps():
    query = gglObj.nearby_search(location="Carol Stream, Illinois", keyword="Recycling Center", radius=5000)
    return render_template('testMaps.html', places=query.places)

@app.route('/search', methods=["GET", "POST"])
def search():
    form = LocationInputForm()
    if form.validate_on_submit():
        query = gglObj.nearby_search(location=form.town.data, keyword=form.topic.data, radius=5000)
        flash(f"Searching for {form.topic.data} ", "success")
        return render_template("testMaps.html", places=query.places)
    else:
        flash("Query Unsuccessful. Please check Town and Topic", "danger")
    return render_template("search.html", form=form)


if __name__ == '__main__':
    app.run()
