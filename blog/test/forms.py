from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField


class QubPerimeterTestForm(FlaskForm):
    question1 = BooleanField('S=100', default=False)
    question2 = BooleanField('S=110', default=False)
    question3 = BooleanField('S=112', default=False)
    submit = SubmitField('Отправить')
