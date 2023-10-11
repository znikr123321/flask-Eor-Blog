import os
import secrets

from PIL import Image
from flask import current_app
from flask_login import current_user


#обрезание фото


def save_picture_post_author(form_picture, post):
    random_hex = secrets.token_hex(16)# рандомное имя для изображений
    _, f_ext = os.path.splitext(form_picture.filename)#распаковкочка, разбивает на 2 части
    picture_fn = random_hex + f_ext
    full_path = os.path.join(current_app.root_path, 'static', 'profile_pics/', 'users/', current_user.username,
                             'post_images')# для создания своей папки с фото
    try:
        os.remove(
            os.path.join(current_app.root_path,
                         f'static/profile_pics/users/{current_user.username}/post_images/{post.image_post}'))
    except:
        print('Изображение не найдено, возможно оно было удалено!')
    if not os.path.exists(full_path):# если папки не существует то сздам путь
        os.mkdir(full_path)
    picture_path = os.path.join(full_path, picture_fn)# объединение путей
    output_size = (500, 500)
    i = Image.open(form_picture) #открытие изображения
    i.thumbnail(output_size) #делаем миниатюрку
    i.save(picture_path)
    return picture_fn