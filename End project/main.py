from flask import Flask, render_template, request



app = Flask(__name__)

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

app.run(debug=True)
