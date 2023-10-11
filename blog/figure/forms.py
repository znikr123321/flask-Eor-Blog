from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired


class QubPerimeterForm(FlaskForm):
    side = FloatField('Введите число', validators=[DataRequired()] )
    submit = SubmitField('Рассчитать')


class QubVolumeForm(FlaskForm):
    side = FloatField('Введите число', validators=[DataRequired()] )
    submit = SubmitField('Рассчитать')


class QubSquareForm(FlaskForm):
    side = FloatField('Введите число', validators=[DataRequired()] )
    submit = SubmitField('Рассчитать')


class CilindrValueForm(FlaskForm):
    Square = FloatField('Введите число', validators=[DataRequired()] )
    Hight = FloatField('Введите число', validators=[DataRequired()] )
    submit = SubmitField('Рассчитать')