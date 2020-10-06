from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from querries import bodypart_df, exercise_df, sum_querry


class WeightForm(FlaskForm):

    bodypart = SelectField('Body part', choices=bodypart_df['body_part'].to_list(),
                           validators=[DataRequired()])
    exercise = SelectField('Exercise', choices=exercise_df['exercise'].to_list(),
                           validators=[DataRequired()])
    series = IntegerField('Number of serie', validators=[NumberRange(min=1, max=10, message="chose from 1 to 10")])
    reps = IntegerField('How many reps?', validators=[NumberRange(min=1, max=10, message="chose from 1 to 10")])
    weight = FloatField('What weight?', validators=[NumberRange(min=1, max=100, message="chose from 1 to 100")])
    submit = SubmitField('Calculate')
    edit = SubmitField('View/Edit')
    clear = SubmitField('Clear all data')
    summary = SubmitField('Go to summary page')


class SummaryForm(FlaskForm):

    trening = SelectField('Choose trening date', choices=sum_querry()['data'].to_list(), validators=[DataRequired()])
    submit = SubmitField('Show summary')
    back = SubmitField('Go back')
    refresh = SubmitField('Refresh')
