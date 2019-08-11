from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello 'Web Application' World!"


@app.route('/practice3/input')
def input_name():
    return render_template('input.html')


@app.route('/practice3/output', methods=["POST"])
def output_name():
    return "こんにちは、" + request.form['name']


if __name__ == "__main__":
    app.run()
