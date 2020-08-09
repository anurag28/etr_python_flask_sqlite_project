from os import abort

from flask import url_for, redirect, render_template, request, Blueprint, flash
from myproject import db
from myproject.models import Movie, User
from myproject.movies.forms import AddMovieForm, SearchMovieForm
from flask_login import current_user, login_required
from sqlalchemy import join
from sqlalchemy.sql import select

movie = Blueprint('movie', __name__)


@movie.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()

    if form.validate_on_submit():
        new_movie = Movie(name=form.name.data, cast=form.cast.data,
                          genre=form.genre.data, rating=form.rating.data,
                          review=form.comment.data, user_id=current_user.id)
        db.session.add(new_movie)
        db.session.commit()
        db.session.flush()
        # movie_id = new_movie.id
        # user_id = current_user.id
        # new_post = Post(user_id=user_id, movie_id=movie_id)
        # db.session.add(new_post)
        # db.session.commit()
        return redirect(url_for('core.index'))

    return render_template('add_movie.html', form=form)


@movie.route('/<int:movie_id>')
def movie_post(movie_id):

    post_movie = Movie.query.get_or_404(movie_id)
    return render_template('movie_post.html', post=post_movie, name=post_movie.name,
                           cast=post_movie.cast, genre=post_movie.genre,
                           review=post_movie.review, rating=post_movie.rating)


@movie.route('/<int:movie_id>/delete', methods=['POST'])
@login_required
def delete_post(movie_id):
    post_movie = Movie.query.get_or_404(movie_id)
    if post_movie.audience != current_user:
        abort(403)
    db.session.delete(post_movie)
    db.session.commit()
    flash('Post has been deleted')
    return redirect(url_for('core.index'))


@movie.route('/<int:movie_id>/update', methods=['GET'])
@login_required
def update(movie_id):
    post_movie = Movie.query.get_or_404(movie_id)
    if post_movie.audience != current_user:
        abort(403)
    form = AddMovieForm()
    if form.validate_on_submit():
        post_movie.name = form.name.data
        post_movie.cast = form.cast.data
        post_movie.review = form.comment.data
        post_movie.rating = form.rating.data
        post_movie.genre = form.genre.data
        db.session.commit()
        flash("POst Updated")
        return redirect('movie.movie_post', movie_id=post_movie.id)
    elif request.method == 'GET':
        form.name.data = post_movie.name
        form.cast.data = post_movie.cast
        form.comment.data = post_movie.review
        form.rating.data = post_movie.rating
        form.genre.data = post_movie.genre
    return render_template('add_movie.html', form=form)


@movie.route('/search_movies', methods=['GET', 'POST'])
def search_movies():
    form = SearchMovieForm()

    if form.validate_on_submit():
        if form.name.data:
            # movie_data = db.session.query(Movie.name, Post.date, Movie.cast, Movie.rating, Post.user_id).join(Post, Movie.id == Post.movie_id).filter_by(Movie.name == form.name.data).all()
            #return redirect(url_for('movie.search_results', form.name.data))
            return redirect(url_for('core.index'))
    return render_template('search_movie.html', form=form)


