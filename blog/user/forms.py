from flask import flash
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError, InputRequired
from blog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=4, max=20)],
                           render_kw={'class': 'form-control'})
    email = StringField('Емайл', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Роли', choices=[('admin', 'admin'), ('user', 'user')])
    submit = SubmitField('Войти')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            flash('Это имя уже занято. Пожалуйста, выберите другое', 'danger')
            raise ValidationError('That username is taken. Please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            flash('Этот емайл уже занят. Пожалуйста, введите другой', 'danger')
            raise ValidationError('That email is taken. Please choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Емайл', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class AddCommentForm(FlaskForm):
    body = StringField("Ваш комментарий", validators=[InputRequired()])
    submit = SubmitField("Опубликовать")


class UpdateAccountForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=4, max=80)])
    email = StringField('Емайл', validators=[DataRequired(), Email()])
    picture = FileField('Изображение (png, jpj)', validators=[FileAllowed(['jpg', 'png']), ])
    submit = SubmitField('Обновить')

    def validate_username(self, username):
        if username.data != current_user.username:#если имя пользователя совпадает то выбрать другое
            user = User.query.filter_by(username=username.data).first()
            if user:
                flash('Пользователь с таким именем уже зарегистрирован', 'danger')
                raise ValidationError('That username is taken. Please choose a different one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                flash('Этот емеил уже используется, введите другой', 'danger')
                raise ValidationError('That email is taken. Please choose a different one')