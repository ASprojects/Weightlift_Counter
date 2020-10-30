import psycopg2 as pg2
from config_pass import password
import pandas as pd
import datetime


connection = pg2.connect(user="postgres",
                         password=password,
                         host="127.0.0.1",
                         port="5432",
                         database="weightlifting_counter")


def get_alldata_query():
    cur = connection.cursor()
    cur.execute('SELECT * FROM trening;')
    trenings_data = cur.fetchall()
    trenings_df = pd.DataFrame(trenings_data, columns=['data', 'body part', 'exercise', 'reps', 'series', 'weight'])
    return trenings_df


def delete_alldata_query():
    cur = connection.cursor()
    cur.execute('DELETE FROM public.trening;')
#    connection.commit()                        # <=== blocked for now
    return 'cleared all the data'


def get_exercise_choice_df():
    cur = connection.cursor()
    cur.execute('SELECT * FROM exercises;')
    exercise_data = cur.fetchall()
    exercise_df = pd.DataFrame(exercise_data, columns=['exercise_id', 'exercise', 'body_part_id'])
    return exercise_df


def get_bodypart_choice_df():
    cur = connection.cursor()
    cur.execute('SELECT * FROM bodyparts;')
    bodypart_data = cur.fetchall()
    bodypart_df = pd.DataFrame(bodypart_data, columns=['body_part_id', 'body_part'])
    return bodypart_df


def get_summary_menu_datas_df():
    cur = connection.cursor()
    cur.execute('SELECT DISTINCT data FROM trening ORDER BY data ASC;')
    summary_menu_data = cur.fetchall()
    summary_menu_data_df = pd.DataFrame(summary_menu_data, columns=['data'])
    return summary_menu_data_df


# ## UNDONE, PLEASE WAIT, WORKING ###
def insert_add_new_stats(res):
    add_new_stats = """
        INSERT INTO public.trening(data, exercise, series, reps, weight, body_part) VALUES ('%s', '%s', %s, %s, %s, '%s');
        """ % (str(datetime.date.today()),
               res.get("exercise_value", ""),
               res.get("series_value", ""),
               res.get("reps_value", ""),
               res.get("weight_value", ""),
               res.get("bodypart_value", ""))
    cur = connection.cursor()
    cur.execute(add_new_stats)
    connection.commit()
    return
# #####   UNDER CONSTRUCTION   ######
