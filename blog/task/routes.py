from flask import Blueprint, render_template, flash, request
from flask_login import login_required
from blog.task.forms import QubValueForm, QubSquareForm, QubPerimeterForm

tasks = Blueprint('tasks', __name__, template_folder='templates')


@tasks.route('/tasks', methods=['GET', 'POST'])
@login_required
def list_tasks():
    return render_template('task/tasks.html', title='Задачи')


@tasks.route('/tasks/qub_ValueTask', methods=['GET', 'POST'])
@login_required
def qub_ValueTask():
    form = QubValueForm()
    if form.is_submitted():
        Perimetr = request.form['answer']
        if Perimetr == '29791':
            flash('Ответ верный', 'success')
            return render_template('task/tasks_qub_ValueTask.html', QubValueForm=form, title='Задачи')
        else:
            flash('Ответ не верный', 'danger')
    return render_template('task/tasks_qub_ValueTask.html', title='Задачи', QubValueForm=form)


@tasks.route('/tasks/qub_PerimetrTask', methods=['GET', 'POST'])
@login_required
def qub_PerimetrTask():
    form = QubPerimeterForm()
    if form.is_submitted():
        Perimetr = request.form['answer']
        if Perimetr == '372':
            flash('Ответ верный', 'success')
            return render_template('task/tasks_qub_PerimetrTask.html', QubPerimeterForm=form, title='Задачи')
        else:
            flash('Ответ не верный', 'danger')
    return render_template('task/tasks_qub_PerimetrTask.html', title='Задачи', QubPerimeterForm=form)


@tasks.route('/tasks/qub_SquareTask', methods=['GET', 'POST'])
@login_required
def qub_SquareTask():
    form = QubSquareForm()
    if form.is_submitted():
        Perimetr = request.form['answer']
        if Perimetr == '5766':
            flash('Ответ верный', 'success')
            return render_template('task/tasks_qub_SquareTask.html', QubSquareForm=form, title='Задачи')
        else:
            flash('Ответ не верный', 'danger')
    return render_template('task/tasks_qub_SquareTask.html', title='Задачи', QubSquareForm=form)