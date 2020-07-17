from flask import render_template, url_for, redirect, request, Blueprint, flash
from flask_login import login_user, login_required, current_user, logout_user
from myproject import db
from myproject.models import User, Post
from myproject.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from myproject.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)

# Register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Thanks for registration")
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

# Login
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Login success")

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form=form)

# Logout
@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))

# Account
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateUserForm()

    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic
        current_user.name = form.name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Profile Updated")
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.name.data = current_user.name
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)


# Posts