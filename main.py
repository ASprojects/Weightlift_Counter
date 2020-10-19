from flask import Flask, render_template
from querries import get_alldata_query, delete_alldata_query

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


@app.route('/clear', methods=['POST'])
def clear():
    apply_query = delete_alldata_query()
    return apply_query


if __name__ == '__main__':
    app.run(debug=True, port=5001)
