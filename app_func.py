from flask import request
import pandas as pd
from queries import get_exercise_choice_df, get_bodypart_choice_df, insert_add_new_stats

"""
def calculate():
    workday = {
        'series': int(request.form.getlist("series")[0]),
        'reps': int(request.form.getlist('reps')[0]),
        'weight': float(request.form.getlist('weight')[0]),
        'body_part': request.form.getlist('bodypart')[0],
        'exercise': request.form.getlist('exercise')[0],
                }
    workday_df = pd.DataFrame(workday, index=[0])
    workday_df_trening = workday_df.merge(get_exercise_choice_df(),
                                          on='exercise',
                                          how="left").merge(get_bodypart_choice_df(),
                                                            on=['body_part_id', 'body_part'],
                                                            how="left")
    return insert_add_new_stats(workday_df_trening)
"""