from snack import app,db
from flask import render_template,redirect,request,url_for,flash
from snack.models import User
from flask_bcrypt import Bcrypt


bcrypt=Bcrypt(app)


@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/signup',methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name= request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        p=bcrypt.generate_password_hash(password)

        new_user=User(
            name=name,
            email=email,
            password=p
        )

        db.session.add(new_user)
        db.session.commit()
        flash('Account for %s created successfully'%name)
        return redirect('/signup')
    return render_template('sign.html')