from flask import redirect,render_template,url_for,Blueprint,request,current_app,flash

action = Blueprint("action",__name__)

@action.route('/add',methods=['POST','GET'])
def add():
    if_empty = {None:'Unknown'}
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author') or if_empty[None]
        user_op = current_app.config['useroperate']
        if not title:
            return redirect(url_for('action.add'))
        else:
            add_book = user_op.add_books(title,author)
            flash(f'{title} successfully added','success')
            return render_template('add.html')
    else:
        return render_template('add.html')

@action.route('/handling/<int:book_id>',methods=['POST','GET'])
def handling():
    if 'update' in request.form:
        return render_template('add.html')
    elif 'delete':
        return render_template('delete.html')




