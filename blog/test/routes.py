from flask import render_template, redirect, url_for, Blueprint, request, flash

from blog.test.forms import QubPerimeterTestForm

tests = Blueprint('tests', __name__, template_folder='templates')


@tests.route('/tests/test1', methods=['GET', 'POST'])
def test():
    form = QubPerimeterTestForm()
    if form.validate_on_submit():
        answer3 = request.form['question3']
        if answer3 != True :
            flash('Ответ верный', 'success')
            return render_template('test/test1.html', QubPerimeterTestForm=form)
        else:
            flash('Ответ не верный', 'danger')
            return render_template('test/test1.html', QubPerimeterTestForm=form)
    return render_template('test/test1.html', QubPerimeterTestForm=form)