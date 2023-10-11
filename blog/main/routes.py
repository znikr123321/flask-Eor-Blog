from flask import Blueprint, render_template, request
from flask_login import login_required

from blog.models import Post, User

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home():
    return render_template('main/index.html', title='Главная')


@main.route('/blog', methods=['POST', 'GET'])
@login_required
def blog():
    all_posts = Post.query.order_by(Post.title.desc()).all()
    all_users = User.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)

    return render_template('main/blog.html', title='Блог', posts=posts,
                           all_posts=all_posts, all_users=all_users)


@main.route('/AboutUs')
def AboutUs():
    return render_template('main/AboutUs.html')


@main.route('/Teory')
@login_required
def Teory():
    return render_template('main/Teory.html')


@main.route('/Problems')
def Problems():
    return render_template('main/Problems.html')