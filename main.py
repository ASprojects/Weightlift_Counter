from flask import Flask, render_template, request
from app_func import WeightForm
import pandas as pd
from querries import exercise_df, bodypart_df

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
    workday_df_trening = workday_df.merge(exercise_df, on='exercise').merge(bodypart_df, on=['body_part_id','body_part']) #joining all dframes
    return workday_df_trening.to_dict()


@app.route('/edit', methods=['POST'])
def editing():
    return "Editor"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
#runs the app