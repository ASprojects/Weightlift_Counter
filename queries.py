import psycopg2 as pg2
from config_pass import password, host
import pandas as pd
import datetime
import logging


def get_alldata_query():
    connection = pg2.connect(user="postgres",
                             password=password,
                             host=host,
                             port="5432",
                             database="weightlifting_counter")
    cur = connection.cursor()
    cur.execute('SELECT * FROM trening;')
    trenings_data = cur.fetchall()
    trenings_df = pd.DataFrame(trenings_data, columns=['data', 'body part', 'exercise', 'series', 'reps', 'weight'])
    return trenings_df


def delete_alldata_query():
    connection = pg2.connect(user="postgres",
                             password=password,
                             host=host,
                             port="5432",
                             database="weightlifting_counter")
    cur = connection.cursor()
    cur.execute('DELETE FROM public.trening;')
    connection.commit()
    connection.close()
    return 'cleared all the data'


def get_exercise_choice_df():
    connection = pg2.connect(user="postgres",
                             password=password,
                             host=host,
                             port="5432",
                             database="weightlifting_counter")
    cur = connection.cursor()
    cur.execute('SELECT * FROM exercises;')
    exercise_data = cur.fetchall()
    exercise_df = pd.DataFrame(exercise_data, columns=['exercise_id', 'exercise', 'body_part_id'])
    return exercise_df


def get_bodypart_choice_df():
    connection = pg2.connect(user="postgres",
                             password=password,
                             host=host,
                             port="5432",
                             database="weightlifting_counter")
    cur = connection.cursor()
    cur.execute('SELECT * FROM bodyparts;')
    bodypart_data = cur.fetchall()
    bodypart_df = pd.DataFrame(bodypart_data, columns=['body_part_id', 'body_part'])
    return bodypart_df


def get_summary_menu_datas_df():
    connection = pg2.connect(user="postgres",
                             password=password,
                             host=host,
                             port="5432",
                             database="weightlifting_counter")
    cur = connection.cursor()
    cur.execute('SELECT DISTINCT data FROM trening ORDER BY data ASC;')
    summary_menu_data = cur.fetchall()
    summary_menu_data_df = pd.DataFrame(summary_menu_data, columns=['data'])
    return summary_menu_data_df


def insert_add_new_stats(req):
    connection = pg2.connect(user="postgres",
                             password=password,
                             host=host,
                             port="5432",
                             database="weightlifting_counter")
    cur = connection.cursor()
    try:
        add_new_stats = """
            INSERT INTO public.trening(data, body_part, exercise, series, reps, weight) 
            VALUES ('%s', '%s', '%s', %s, %s, %s);
            """ % (str(datetime.date.today()),
                   req.get("bodypart_value", ""),
                   req.get("exercise_value", ""),
                   req.get("series_value", ""),
                   req.get("reps_value", ""),
                   req.get("weight_value", ""))
        cur.execute(add_new_stats)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.exception(e)
    connection.close()
    return 'ok'
