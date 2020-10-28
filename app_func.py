import pandas as pd
from queries import get_exercise_choice_df, get_bodypart_choice_df, get_summary_menu_datas_df, get_alldata_query
import datetime


def get_df_from_two_tables():
    select_df = get_exercise_choice_df().merge(get_bodypart_choice_df())
    select_exercise_df = select_df['exercise'].to_list()
    select_bodypart_df = select_df['body_part'].to_list()
    string_dataframe = pd.DataFrame({'body_part': select_bodypart_df, 'exercise': select_exercise_df})
    return string_dataframe


def get_bodyparts_as_string():
    bodypart_list = get_df_from_two_tables()['body_part'].drop_duplicates().to_list()
    bodypart_string = ";".join(bodypart_list)
    return bodypart_string


def get_exercises_as_string(bodypart_key):
    is_key = get_df_from_two_tables()['body_part'] == bodypart_key
    exercise_df = get_df_from_two_tables()[is_key]
    exercise_list = exercise_df['exercise'].to_list()
    exercise_string = ";".join(exercise_list)
    return exercise_string


def get_summary_datas_as_string():
    datas_list = get_summary_menu_datas_df()['data'].to_list()
    formated_datas_list=[]
    for data in datas_list:
        data = data.strftime("%Y-%m-%d")
        formated_datas_list.append(data)
    datas_string = ";".join(formated_datas_list)
    return datas_string


def get_single_trening_df(data_key):
    key = datetime.datetime.strptime(data_key, '%Y-%m-%d').strftime('(%Y, %m, %d)')
    formated_key = datetime.datetime.strptime(key, '(%Y, %m, %d)').date()
    is_key = get_alldata_query()['data'] == formated_key
    single_trening_df = get_alldata_query()[is_key]
    print(single_trening_df.to_html())
    return single_trening_df.to_html()
