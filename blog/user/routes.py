import os
import shutil
from datetime import datetime

import sqlalchemy
from flask import Blueprint, render_template, flash, url_for, request
from flask_login import current_user, logout_user, login_required, login_user
from werkzeug.utils import redirect

from blog import bcrypt, db
from blog.models import User, Post
from blog.settings import UPLOAD_FOLDER
from blog.user.forms import RegistrationForm, LoginForm, UpdateAccountForm
from blog.user.utils import save_picture, random_avatar

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/admin', methods=['GET'])
def admin_panel():
    return redirect(url_for('any_page'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.blog'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password,
                    image_file=random_avatar(form.username.data), role=form.role.data)
        db.session.add(user)
        db.session.commit()

        flash('Ваш аккаунт был создан. Вы можете войти на блог', 'success')
        return redirect(url_for('users.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": {}'.format(getattr(form, field).label.text, error))

    return render_template('user/register.html', form_registration=form, title='Регистрация', legend='Регистрация')


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.blog'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Вы вошли как пользователь {current_user.username}', 'info')
            return redirect(next_page) if next_page else redirect(url_for('users.account'))
        else:
            flash('Войти не удалось. Пожалуйста, проверьте электронную почту или пароль', 'danger')
    return render_template('user/login.html', form_login=form, title='Логин', legend='Войти')


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    user = User.query.filter_by(username=current_user.username).first()
    posts = Post.query.all()
    users = User.query.all()
    form = UpdateAccountForm()

    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    elif form.validate_on_submit():
        #для обновления папки пользователя
        path_one = os.path.join(os.getcwd(), UPLOAD_FOLDER, user.username)
        path_two = os.path.join(os.getcwd(), UPLOAD_FOLDER, form.username.data)
        os.rename(path_one, path_two)

        current_user.username = form.username.data
        current_user.email = form.email.data

        if form.picture.data:
            current_user.image_file = save_picture(form.picture.data, user)
        else:
            form.picture.data = current_user.image_file

        db.session.commit()
        flash('Ваш аккаунт был обновлён!', 'success')
        return redirect(url_for('users.account'))
    #ищем фото текущего пользователя
    image_file = url_for('static',
                         filename=f'profile_pics' + '/users/' + current_user.username + '/account_img/' +
                                  current_user.image_file)
    return render_template('user/account.html', title='Аккаунт',
                           image_file=image_file, form_update=form, posts=posts, users=users, user=user)


@users.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user) \
        .order_by(Post.date_posted.desc()) \
        .paginate(page=page, per_page=3)

    return render_template('user/user_posts.html', title='Общий блог>', posts=posts, user=user)


@users.route('/user_delete/<string:username>', methods=['GET', 'POST'])
@login_required
def delete_user(username):
    try:
        user = User.query.filter_by(username=username).first_or_404()
        # проверка на админа для удаления
        if user and not user.is_admin:
            db.session.delete(user)
            db.session.commit()
            full_path = os.path.join(os.getcwd(), UPLOAD_FOLDER, user.username)#удаление файлов пользователя
            shutil.rmtree(full_path)#удаление полного дерева

            flash(f'Пользователь {username} был удалён!', 'info')
            return redirect(url_for('users.account'))
    #проверка на посты пользователя
    except sqlalchemy.exc.IntegrityError:
        flash(f'У пользователя {username} есть контент!', 'warning')
        return redirect(url_for('users.account'))
    except FileNotFoundError:
        return redirect(url_for('users.account'))

    else:
        flash('Администрация!', 'info')
        return redirect(url_for('users.account'))


@users.route('/logout')
def logout():
    current_user.last_seen = datetime.now()
    db.session.commit()
    logout_user()
    return redirect(url_for('main.home'))
