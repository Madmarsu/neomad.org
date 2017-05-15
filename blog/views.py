from flask import (
    request, render_template, redirect, url_for, abort, flash
)
from flask_login import current_user, login_required

from core import app, db
from core.helpers import url_for_user, url_for_article
from user.models import User
from .models import Article, clean_html


@app.route('/articles')
def article_list():
    articles = Article.objects.all()
    return render_template('blog/article_list.html', articles=articles)


@app.route('/@<string:author>/<string:slug>-<string:id>', methods=['get'])
def article(author, slug, id):
    try:
        article = Article.objects.get(id=id)
    except db.errors.ValidationError:
        abort(404)
    except Article.DoesNotExist:
        abort(404)
    if article.slug != slug or article.author.slug != author:
        return redirect(url_for_article(article), 301)
    return render_template('blog/article.html', article=article,
                           edit=(current_user.is_authenticated and
                                 author == current_user.slug))


@app.route('/article/write', methods=['get', 'post'])
@login_required
def article_create():
    article = Article(content='')
    article.author = User.objects.get(id=current_user.id)
    errors = []
    if request.method == 'POST':
        article.title = request.form.get('title')
        article.content = request.form.get('content')
        if article.title != '' and clean_html(article.content) != '':
            article.save()
        else:
            errors.append('Your article must have a title and a content')
    return render_template('blog/article.html', article=article, edit=True,
                           errors=errors)


@app.route('/article/<string:id>/edit', methods=['post'])
@login_required
def article_edit(id):
    user = User.objects.get(id=current_user.id)
    try:
        article = Article.objects.get(author=user, id=id)
    except Article.DoesNotExist:
        abort(404)
    article.title = request.form.get('title')
    article.content = request.form.get('content')
    errors = []
    if article.title != '' and clean_html(article.content) != '':
        article.save()
    else:
        errors.append('Your article must have a title and a content')
    return render_template('blog/article.html', article=article, edit=True,
                           errors=errors)


@app.route('/article/<string:id>/delete', methods=['get'])
@login_required
def article_delete(id):
    user = User.objects.get(id=current_user.id)
    try:
        article = Article.objects.get(author=user, id=id).delete()
    except Article.DoesNotExist:
        abort(404)
    flash('You article was deleted.', 'success')
    return redirect(url_for_user(user))
