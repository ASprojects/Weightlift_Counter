from flask import Flask, render_template, redirect, url_for, request
from queries import get_alldata_query, delete_alldata_query
from app_func import calculate, get_bodyparts_as_string, get_exercises_as_string, get_summary_datas_as_string, get_single_trening_df


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
    return get_alldata_query().to_html()


@app.route('/clear', methods=['GET'])
def clear():
    return delete_alldata_query()


# $$$ SELECT OPTION $$$
@app.route('/bodypart', methods=['POST'])
def bodypart():
    return get_bodyparts_as_string()


@app.route('/exercise', methods=['POST'])
def exercise():
    key = request.args.get('bodypart_var')
    return get_exercises_as_string(key)


@app.route('/trening_date', methods=['POST'])
def trening_date():
    return get_summary_datas_as_string()


# $$$ FUNCTION BUTTONS $$$
@app.route('/single_trening', methods=['POST'])
def single_trening():
    key = request.args.get('trening_date_var')
    return get_single_trening_df(key)





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


"""
from app_func import get_df_from_two_tables
@app.route('/test', methods=['POST', "GET"])
def test():
    print(get_trening_choice())
    return get_df_from_two_tables().to_html()
"""


if __name__ == '__main__':
    app.run(debug=True, port=5010)
