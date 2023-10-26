from flask import Flask, render_template, request

app = Flask(__name__)

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/new_extremals')
def new_extremals():
    return render_template('new_extremals.html')

@app.route('/conflict')
def conflict():
    return render_template('conflict.html')

@app.route('/the_way_forward')
def the_way_forward():
    return render_template('the_way_forward.html')

app.run(debug=True)
