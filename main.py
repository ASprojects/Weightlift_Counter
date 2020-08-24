from flask import Flask, render_template
from app_func import WeightForm
import psycopg2 as pg2
from config_pass import password


app = Flask(__name__, template_folder='templates')
app.secret_key = 'Wow, that\'s secret'

'''
connection = pg2.connect(user="postgres",
                            password=password,
                            host="127.0.0.1",
                            port="5432",
                            database="weightlifting_counter")
'''

@app.route('/')
def weight():
    form = WeightForm()
    return render_template("weight.html", form=form)



if __name__ == '__main__':
    app.run(debug=False, port=5001)