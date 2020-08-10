from flask import render_template, request, Blueprint, redirect, url_for, flash
from myproject.models import Movie
from myproject import db
from myproject.core.forms import SendEmailForm
import smtplib
from flask_login import current_user


core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get(1, type=int)
    movie_posts = Movie.query.order_by(Movie.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', movie_posts=movie_posts)


@core.route('/about')
def about():
    return render_template('about.html')


@core.route('/<int:movie_id>/send', methods=['POST', 'GET'])
def send_email(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = SendEmailForm()

    if form.validate_on_submit():
        sender_email = form.sender_email.data
        receiver_email = form.receiver_email.data
        password = form.password.data
        subject = form.subject.data
        body = f"Hey buddy,\n\nHere is an amazing movie you must watch,\n{movie.name}\nGenre: {movie.genre}\nStarring{movie.cast}\n\nEnjoy!"
        message = f'Subject: {subject}\n\n{body}'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        flash('Email sent successfully')
        return redirect(url_for('core.index'))
    elif request.method == 'GET':
        form.subject.data = "Hey, don't forget to watch this movie"
        form.body.data = f"Hey buddy,\n\nHere is an amazing movie you must watch,\n{movie.name}\nGenre: {movie.genre}\nStarring{movie.cast}\n\nEnjoy!!"
    return render_template('sending_email.html', form=form)


