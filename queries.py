import psycopg2 as pg2
from config_pass import password
import pandas as pd

connection = pg2.connect(user="postgres",
                         password=password,
                         host="127.0.0.1",
                         port="5432",
                         database="weightlifting_counter")


def get_alldata_query():
    cur = connection.cursor()
    cur.execute('SELECT * FROM trening;')
    trenings_data = cur.fetchall()
    trenings_df = pd.DataFrame(trenings_data, columns=['data', 'exercise', 'reps', 'series', 'weight'])
    return trenings_df


"""
def delete_alldata_query():
    cur = connection.cursor()
    cur.execute('DELETE FROM public.trening;')
    connection.commit()
    return 'cleared all the data'

$$$ Query with blocked commit $$$
      |
      V
"""
def delete_alldata_query():
    cur = connection.cursor()
    cur.execute('DELETE FROM public.trening;')
    return 'cleared all the data'
