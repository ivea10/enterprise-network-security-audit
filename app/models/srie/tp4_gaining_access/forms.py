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


class HydraForm(FlaskForm):
    loginPath = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "loginPath"})
    
    passPath = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "passPath"})
    
    host = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "host"})
    
    service = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "service"})
    
    submit = SubmitField('Submit')

class NetcatForm(FlaskForm):
    host = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "Host"})
    
    submit = SubmitField('Submit')

class MetasploitForm(FlaskForm):
    
    submit = SubmitField('Submit')
