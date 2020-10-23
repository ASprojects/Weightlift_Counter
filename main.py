from flask import Flask, render_template, redirect, url_for
from queries import get_alldata_query, delete_alldata_query, get_bodypart_choice_df
#from app_func import calculate


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
    apply_query = get_alldata_query()
    return apply_query.to_html()


@app.route('/clear', methods=['GET'])
def clear():
    apply_query = delete_alldata_query()
    return apply_query


################################
"""
@app.route('/calculate', methods=['POST'])
def calculate():
    calculate()
    return redirect(url_for("weight_homepage"))
"""


@app.route('/bodypart', methods=['POST'])
def bodypart():
    print(get_bodypart_choice_df()['body_part'].to_list())
    return get_bodypart_choice_df()['body_part'].to_list()


if __name__ == '__main__':
    app.run(debug=True, port=5001)
