from flask import Flask, render_template, request, redirect, url_for
from app_func import WeightForm, SummaryForm
import pandas as pd
from querries import exercise_df, bodypart_df, connection
import datetime

app = Flask(__name__, template_folder='templates')
app.secret_key = 'Wow, that\'s secret'


@app.route('/', methods=['GET', 'POST'])
def weight():
    form = WeightForm()
    return render_template("weight.html", form=form)


@app.route('/calculate', methods=['POST'])
def calculating():
    workday = {
        'series': int(request.form.getlist("series")[0]),
        'reps': int(request.form.getlist('reps')[0]),
        'weight': float(request.form.getlist('weight')[0]),
        'body_part': request.form.getlist('bodypart')[0],
        'exercise': request.form.getlist('exercise')[0],
    }

    workday_df = pd.DataFrame(workday, index=[0]) #pandas dataframe from dict
    workday_df_trening = workday_df.merge(exercise_df, on='exercise', how="left").merge(bodypart_df, on=['body_part_id','body_part'], how="left") #joining all dframes

    cur = connection.cursor()
    addtrening = """
        INSERT INTO public.trening(data, exercise_id, reps, series, weight) VALUES ('%s', %s, %s, %s, %s);
        """ % (str(datetime.date.today()),
               workday_df_trening['exercise_id'][0],
               workday_df_trening['reps'][0],
               workday_df_trening['series'][0],
               workday_df_trening['weight'][0])
    cur.execute(addtrening)
    connection.commit()
    return redirect(url_for("weight"))



@app.route('/summary', methods=['POST'])
def summary():
    form = SummaryForm()
    return render_template("summary.html", form=form)



@app.route('/sum_trening', methods=['POST'])
def sum_trening():
    return "new things gonna come out here"



@app.route('/edit', methods=['POST'])
def editing():
    cur = connection.cursor()
    cur.execute('SELECT * FROM trening;')
    trenings_data = cur.fetchall()
    trenings_df = pd.DataFrame(trenings_data, columns=['data', 'exercise', 'reps', 'serie', 'weight'])
    return trenings_df.to_html()



@app.route('/clear', methods=['POST'])
def clearing():
    cur = connection.cursor()
    cur.execute('DELETE FROM public.trening;')
    connection.commit()
    return "cleared all the data"



if __name__ == '__main__':
    app.run(debug=True, port=5001)
#runs the app