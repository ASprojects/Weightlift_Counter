import psycopg2 as pg2
from config_pass import password
import pandas as pd

connection = pg2.connect(user="postgres",
                            password=password,
                            host="127.0.0.1",
                            port="5432",
                            database="weightlifting_counter") #establishing connection

cur = connection.cursor()


cur.execute('SELECT * FROM bodyparts;')
bodypart_data = cur.fetchall() #data from db
bodypart_df = pd.DataFrame(bodypart_data, columns=['body_part_id','body_part'])


cur.execute('SELECT * FROM exercises;')
exercise_data = cur.fetchall()
exercise_df = pd.DataFrame(exercise_data, columns=['exercise_id','exercise','body_part_id'])

"""cur.execute('SELECT * FROM exercises;')
trening_data = cur.fetchall()
trening_df = """