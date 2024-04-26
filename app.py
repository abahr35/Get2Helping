import dotenv
import os
from flask import Flask, render_template, flash
from googleplaces import GooglePlaces
from forms import LocationInputForm

dotenv.load_dotenv()
gtoken = str(os.getenv("GTOKEN"))
flasktoken = str(os.getenv("FLASKTOKEN"))

app = Flask(__name__)
app.config['SECRET_KEY'] = flasktoken
gglObj = GooglePlaces(gtoken)


@app.route('/')
def home():  # put application's code here
    return render_template('home.html', name="Get2Helping")


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html', name="About")


@app.route('/testmaps')
def test_maps():
    query = gglObj.nearby_search(location="Carol Stream,IL", keyword="Recycling Center", radius=5000)
    for place in query.places:
        place.get_details()
    return render_template('ResultingMaps.html', places=query.places)


@app.route('/search', methods=["GET", "POST"])
def search():
    form = LocationInputForm()
    if form.validate_on_submit():
        query = gglObj.nearby_search(location=form.town.data, keyword=form.topic.data, radius=5000)

        UserLocation = form.town.data
        for place in query.places:
            place.get_details()
        flash(f"Searching for {form.topic.data} ", "success")
        return render_template("ResultingMaps.html", places=query.places, userlocation=UserLocation)
    else:
        flash("Query Unsuccessful. Please check Town and Topic", "danger")
    return render_template("search.html", form=form)


if __name__ == '__main__':
    app.run()
