from flask import Flask,redirect,render_template,Blueprint,request,current_app,url_for,flash,session
from werkzeug.security import generate_password_hash,check_password_hash
import librarydb

auth = Blueprint("auth",__name__)

@auth.route('/signup',methods=['POST','GET'])
def signup():
    u_id = current_app.config['userid']
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        existing = u_id.get_username(username)
        if existing:
            flash(f'{username} already exist','error')
            # return redirect(url_for('auth.signup'))
            return render_template('signup.html')
        elif len(username) == 0 or len(password) == 0:
            flash('Username and Password cannot be empty', 'error')
            # return redirect(url_for('auth.signup'))
            return render_template('signup.html')
        else:
            flash('Sign up successfully','success')
            password_hashed = generate_password_hash(password)
            u_id.sign_up(username,password_hashed)
            # return redirect(url_for('auth.signup'))
            return render_template('signup.html')
    else:
        return render_template('sign.html')
@auth.route('/',methods=['POST','GET'])
def login():
    u_id = current_app.config['userid']
    if request.method == 'POST':
        user = request.form.get('username')
        passwrd = request.form.get('password')
        u_login = u_id.get_username(user)
        if u_login:
            if check_password_hash(u_login['passwd'],passwrd):
                flash('Login successfully','success')
                session['username'] = u_login['username']
                return redirect(url_for('libsys'))
            else:
                flash('Incorrect password','error')
                return render_template('login.html')
        else:
            flash('Incorrect username', 'error')
            return render_template('login.html')
    else:
        return render_template('login.html')
@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))



