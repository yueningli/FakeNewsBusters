from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
