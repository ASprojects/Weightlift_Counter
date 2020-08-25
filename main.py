from flask import Flask, render_template
from app_func import WeightForm

app = Flask(__name__, template_folder='templates')
app.secret_key = 'Wow, that\'s secret'


@app.route('/')
def weight():
    form = WeightForm()
    return render_template("weight.html", form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
#runs the app