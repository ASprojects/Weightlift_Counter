from flask import Flask, render_template, redirect, url_for
from queries import get_alldata_query, delete_alldata_query
from app_func import calculate, get_bodyparts_as_string, get_exercises_as_string


app = Flask(__name__, template_folder='templates')
app.secret_key = 'Ziobro, przestań mi rodzinę prześladować'


# $$$ TEMPLATE SITES $$$
@app.route('/', methods=['GET', 'POST'])
def weight_homepage():
    return render_template("weight.html")


@app.route('/summary_menu', methods=['POST', 'GET'])
def menu():
    return render_template("summary.html")


# $$$ SINGLE BUTTONS $$$
@app.route('/show_all', methods=['POST', 'GET'])
def show_all():
    return get_alldata_query()


@app.route('/clear', methods=['GET'])
def clear():
    return delete_alldata_query()


# $$$ SELECT BUTTONS $$$
@app.route('/bodypart', methods=['POST'])
def bodypart():
    return get_bodyparts_as_string()


@app.route('/exercise', methods=['POST'])
def exercise():
    return get_exercises_as_string()


####################################
### UNDONE, PLEASE WAIT, WORKING ###
####################################
@app.route('/calculate', methods=['POST'])
def calculate():
    calculate()
    return redirect(url_for("weight_homepage"))
####################################
######   UNDER CONSTRUCTION   ######
####################################


if __name__ == '__main__':
    app.run(debug=True, port=5001)
