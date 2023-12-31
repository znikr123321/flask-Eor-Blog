from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Статья', validators=[DataRequired()])
    category = SelectField('Категории', choices=[('Многоугольники', 'Многоугольник'), ('Окружности', 'Шары'), ('Цилиндры', 'Цилиндр')])
    tag_form = StringField('Тэг')
    picture = FileField('Изображение (png, jpg)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Опубликовать')


class PostUpdateForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Статья', validators=[DataRequired()])
    category = SelectField('Категории', choices=[('Многоугольники', 'Многоугольник'), ('Окружности', 'Шары'), ('Цилиндры', 'Цилиндр')])
    picture = FileField('Изображение (png, jpg)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Опубликовать')


class CommentUpdateForm(FlaskForm):
    body = StringField('Заголовок', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')
