from flask import Flask, render_template
import pandas as pd


app = Flask(__name__, template_folder='templates')
app.secret_key = 'Wow, that\'s secret'


@app.route('/', methods=['GET', 'POST'])
def weight():
    return render_template("weight.html")


@app.route('/summary_menu', methods=['POST', 'GET'])
def menu():
    return render_template("summary.html")


@app.route('/show_all', methods=['POST'])
def showall():
    showall = showall()
    return showall.to_html()


@app.route('/clear', methods=['POST'])
def clear():
    clear = clear()
    return clear


if __name__ == '__main__':
    app.run(debug=True, port=5001)

#  runs the app
