from snack import app
from flask import render_template,redirect,request,url_for

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/signup')
def sign_up():
    return render_template('sign.html')