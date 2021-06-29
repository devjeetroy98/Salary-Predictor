from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class YearsForm(FlaskForm):
    years= StringField('Enter IT experience in years:', validators=[DataRequired()])
    submit = SubmitField("Submit")