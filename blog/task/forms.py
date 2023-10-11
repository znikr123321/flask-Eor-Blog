from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class QubValueForm(FlaskForm):
    answer = StringField('Введите ответ', validators=[DataRequired()] )
    submit = SubmitField('Отправить')


class QubPerimeterForm(FlaskForm):
    answer = StringField('Введите ответ', validators=[DataRequired()] )
    submit = SubmitField('Отправить')


class QubSquareForm(FlaskForm):
    answer = StringField('Введите ответ', validators=[DataRequired()] )
    submit = SubmitField('Отправить')