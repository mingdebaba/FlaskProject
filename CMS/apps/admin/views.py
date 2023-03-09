from flask import Blueprint, render_template, request, session, redirect, url_for
from .models import Users

bp = Blueprint("admin", __name__, url_prefix='/admin')


@bp.route("/login/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('admin/login.html')
    else:
        user = request.form.get('username')
        pwd = request.form.get('password')
        users = Users.query.filter_by(username=user).first()
        if users:
            if user == users.username and users.check_password(pwd):
                session['user_id'] = users.uid
                # print(session['user_id'])
                print("right password")
                return redirect(url_for('admin.index'))
            else:
                # print("wrong information")
                error = "wrong information"
                return render_template('admin/login.html', message="dont try anyway")


@bp.route('/')
def index():
    return render_template('admin/index.html')


@bp.route("/admin")
def index():
    return render_template('admin/login.html')
