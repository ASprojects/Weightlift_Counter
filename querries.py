import psycopg2 as pg2
from config_pass import password
import pandas
import datetime

connection = pg2.connect(user="postgres",
                            password=password,
                            host="127.0.0.1",
                            port="5432",
                            database="weightlifting_counter")
#establishin' connec'


cur = connection.cursor()
cur.execute('SELECT * FROM bodyparts;')
bodypart_data = cur.fetchall()
bodypart_df = pandas.DataFrame(bodypart_data, columns=['body_part_id','body_part'])


cur.execute('SELECT * FROM exercises;')
exercise_data = cur.fetchall()
exercise_df = pandas.DataFrame(exercise_data, columns=['body_part_id','exercise','exercise_id'])


#    addtrening = """
#    INSERT INTO public.trening(data, exercise_id, reps, series, weight) VALUES ('%s', %s, %s, %s, %s);
#    """ % (str(datetime.date.today()),
#           b,
#           c,
#           d,
#           e)
#   cur.execute(addtrening)
#    connection.commit()