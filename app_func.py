from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange

class WeightForm(FlaskForm):

    bodypart = SelectField('Body part', choices=['a','b'],
                           validators=[DataRequired()])
    exercise = SelectField('Exercise', choices=['a','b'],
                           validators=[DataRequired()])
    series = IntegerField('Number of serie', [NumberRange(min=0, max=10)])
    reps = IntegerField('How many reps?', [NumberRange(min=0, max=10)])
    weight = FloatField('What weight?', [NumberRange(min=0, max=10)])