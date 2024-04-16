from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LocationInputForm(FlaskForm):
    town = StringField("Town", validators=[DataRequired()])
    get_location = SubmitField('Get Current Location')
    # (value, label)
    topic = SelectField("Search Topic",
                        choices=[("Recycling Center", "Recycling Center"), ("Animal Adoption", "Animal Adoption"),
                                 ("Volunteer Locations", "Volunteer Locations")])
    submit = SubmitField("Search")