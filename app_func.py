from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from querries import bodypart_df, exercise_df

class WeightForm(FlaskForm):

    bodypart = SelectField('Body part', choices=bodypart_df['body_part'].to_list(),
                           validators=[DataRequired()])
    exercise = SelectField('Exercise', choices=exercise_df['exercise'].to_list(),
                           validators=[DataRequired()])
    series = IntegerField('Number of serie', [NumberRange(min=0, max=10)])
    reps = IntegerField('How many reps?', [NumberRange(min=0, max=10)])
    weight = FloatField('What weight?', [NumberRange(min=0, max=100)])
    submit = SubmitField('Calculate')
    edit = SubmitField('Edit')