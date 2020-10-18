from flask import Flask, render_template
from querries import showall, clear


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
def showall():
    apply_showall = showall()
    return apply_showall.to_html()


@app.route('/clear', methods=['POST'])
def clear():
    apply_clear = clear()
    return apply_clear


if __name__ == '__main__':
    app.run(debug=True, port=5001)
