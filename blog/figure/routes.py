from flask import Blueprint, render_template, flash, request
from flask_login import login_required

from blog.figure.forms import QubPerimeterForm, QubVolumeForm, QubSquareForm, CilindrValueForm

figures = Blueprint('figures', __name__, template_folder='templates')


@figures.route('/figure', methods=['GET', 'POST'])
@login_required
def list_figures():
    return render_template('figure/figures.html', title='Фигуры')


@figures.route('/figure/qub', methods=['GET', 'POST'])
@login_required
def qub():
    return render_template('figure/qub.html', title='Куб')


@figures.route('/figure/cilindr', methods=['GET', 'POST'])
@login_required
def cilindr():
    return render_template('figure/сilindr.html', title='Цилиндр')


@figures.route('/figure/qub_perimetr', methods=['GET', 'POST'])
@login_required
def qub_perimetr():
    form = QubPerimeterForm()
    if form.is_submitted():
        Perimetr = request.form['side']
        Perimetr = float(Perimetr)
        if Perimetr > 0:
            Perimetr = Perimetr*12
            return render_template('figure/qub_perimetr.html', QubPerimeterForm=form, Perimetr=Perimetr)
        else:
            flash('Некорректное значение')
    return render_template('figure/qub_perimetr.html', QubPerimeterForm=form)


@figures.route('/figure/qub_volume', methods=['GET', 'POST'])
@login_required
def qub_volume():
    form = QubVolumeForm()
    if form.is_submitted():
        Volume = request.form['side']
        Volume = float(Volume)
        if Volume > 0:
            Volume = Volume * Volume * Volume
            return render_template('figure/qub_volume.html', QubVolumeForm=form, Volume=Volume)
        else:
            flash('Некорректное значение')
    return render_template('figure/qub_volume.html', QubVolumeForm=form)


@figures.route('/figure/qub_square', methods=['GET', 'POST'])
@login_required
def qub_square():
    form = QubSquareForm()
    if form.is_submitted():
        Square = request.form['side']
        Square = float(Square)
        if Square > 0:
            Square = 6*(Square * Square)
            return render_template('figure/qub_square.html', QubSquareForm=form, Square=Square)
        else:
            flash('Некорректное значение')
    return render_template('figure/qub_square.html', QubSquareForm=form)


@figures.route('/figure/cilindr_value', methods=['GET', 'POST'])
@login_required
def cilindr_value():
    form = CilindrValueForm()
    if form.is_submitted():
        Square = request.form['Square']
        Hight = request.form['Hight']
        Square = float(Square)
        Hight = float(Hight)

        if Square < 0 or Hight < 0:
            flash('Некорректное значение')
        else:
            Volume = (Square * Hight)
            return render_template('figure/cilindr_value.html', CilindrValueForm=form, Volume=Volume)
    return render_template('figure/cilindr_value.html', CilindrValueForm=form)
