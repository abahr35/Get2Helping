from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html', name="Get2Helping")


if __name__ == '__main__':
    app.run()
