from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class BugReportForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    description = TextAreaField('Bug Description', validators=[DataRequired(), Length(min=10)])
    severity = RadioField(
        'Severity',
        choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit Bug Report')
