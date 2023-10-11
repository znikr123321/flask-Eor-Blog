import os
import secrets
import random
import shutil

from PIL import Image
from flask import current_app

#обрез фото


def save_picture(form_picture, user):
    random_hex = secrets.token_hex(16)# рандомное имя для изображений
    _, f_ext = os.path.splitext(form_picture.filename)#распаковкочка, разбивает на 2 части
    picture_fn = random_hex + f_ext
    full_path = os.path.join(current_app.root_path, 'static', 'profile_pics/', 'users', user.username,
                             'account_img')# для создания своей папки с фото
    try:
        os.remove(
            os.path.join(current_app.root_path,
                         f'static/profile_pics/users/{user.username}/account_img/{user.image_file}'))
    except:
        print('Изображение не найдено, возможно оно было удалено!')
    if not os.path.exists(full_path):# если папки не существует то сздам путь
        os.mkdir(full_path)
    picture_path = os.path.join(full_path, picture_fn)# объединение путей
    output_size = (300, 300)
    i = Image.open(form_picture)#открытие изображения
    i.thumbnail(output_size)#делаем миниатюрку
    i.save(picture_path)
    return picture_fn


def random_avatar(user):
    full_path = os.path.join(os.getcwd(), 'blog/static', 'profile_pics', 'users', user, 'account_img')
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    full_path_avatar = os.path.join(os.getcwd(), 'blog/static/Avatars/')
    list_avatars = os.listdir(full_path_avatar)
    lst = random.choice(list_avatars)
    random_image_file = os.path.join(full_path_avatar, lst)
    shutil.copy(random_image_file, full_path)
    return lst

