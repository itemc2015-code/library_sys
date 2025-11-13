from flask import  Flask,render_template,redirect,session,flash,url_for,current_app,request
from auth import auth
from actions import action
from librarydb import Users,Operate,Actions

app = Flask(__name__)
app.secret_key = 'mysecretkeygit '
app.config['userid'] = Users()
app.config['useroperate'] = Operate()
app.config['useraction'] = Actions()

app.register_blueprint(auth,url_prefix='/')
app.register_blueprint(action,url_prefix='/')

@app.route('/libsys',methods=['POST','GET'])
def libsys():
    user_session = session.get('username')
    if not user_session:
        flash('Invalid login, Login first', 'error')
        # return redirect(url_for('auth.login'))
        return render_template('login.html')

    useroperate = current_app.config['useroperate']
    status_type = request.args.get('filter')
    #if request.method == 'GET':
    if status_type == 'available':
        view_books = useroperate.available()

    elif status_type == 'borrowed':
        view_books = useroperate.borrowed()

    elif status_type == 'allbooks':
        view_books = useroperate.view()

    #return render_template('main.html',view_books=view_books)
    else:
        view_books = useroperate.view()
    return render_template('main.html',view_books=view_books)

if __name__ == "__main__":
    app.run(debug=True)

