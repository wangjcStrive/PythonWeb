from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}   # fake user
    posts = [   # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)


# pass a form instance to render_template
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # when form is showing to user, validate_on_submit will return false
    # whenever user submit a request, validate_on_submit will collect all data, check data, will return true once all action are done
    if form.validate_on_submit():   #
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sing in', form=form)
