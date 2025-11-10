from flask import redirect,render_template,url_for,Blueprint,request,current_app,flash

action = Blueprint("action",__name__)

@action.route('/add',methods=['POST','GET'])
def add():
    if_empty = {None:'Unknown'}
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author') or if_empty[None]
        user_op = current_app.config['useroperate']

        if title:
            add_book = user_op.add_books(title,author)
            flash(f'{title} successfully added','success')
            return render_template('add.html')
        else:
            return redirect(url_for('action.add'))
    else:
        return render_template('add.html')
@action.route('/actionhandling/<int:book_id>',methods=['POST','GET'])
def actionhandling(book_id):
        useractions = current_app.config['useraction']
        if request.method == 'GET':
            if 'delete' in request.args:
                return render_template('delete.html', book_id=book_id)
            elif 'update' in request.args:
                return render_template('update.html', book_id=book_id)

        if request.method == 'POST':
            if 'yes' in request.form:
                request.form.get('yes')
                book_id = useractions.delete(book_id)
                flash('Deleted successfully','success')
                return redirect(url_for('libsys',book_id=book_id))
            else:
                return redirect(url_for('libsys',book_id=book_id))

@action.route('/update/<int:book_id>',methods=['POST','GET'])
def update(book_id):
    if request.method == 'GET':
        if 'update' in request.args:
            return render_template('update.html',book_id=book_id)

    if request.method == 'POST':
        if 'yes' in request.form:
            #request.form.get('yes')
            useraction = current_app.config['useraction']
            book_available = useraction.book_available(book_id)
            book_borrowed = useraction.book_borrowed(book_id)
            if book_available:
                useraction.update_to_borrowed(book_id)
                flash('Successfully updated','success')
                return redirect(url_for('libsys',book_id=book_id))
            elif book_borrowed:
                useraction.update_to_available(book_id)
                flash('Successfully updated', 'success')
                return redirect(url_for('libsys', book_id=book_id))
        else:
            return redirect(url_for('libsys', book_id=book_id))

# @action.route('/handling/<int:book_id>',methods=['POST','GET'])
# def handling(book_id):
#     if 'update' in request.form:
#         return render_template('add.html',book_id=book_id)
#     elif 'delete':
#         return render_template('delete.html',book_id=book_id)



