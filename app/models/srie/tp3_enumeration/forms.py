# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Create forms to be passed to the frontend
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, Length, ValidationError


class TelnetForm(FlaskForm):
    host = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Host"})
    
    port = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Port"})
    
    submit = SubmitField('Submit')

class NmapForm(FlaskForm):
    host = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "Host"})
    
    submit = SubmitField('Submit')

class Enum4linuxForm(FlaskForm):
    host = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Host"})
    
    submit = SubmitField('Submit')
