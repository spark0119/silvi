from flask import render_template
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import user

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Sean'}
    posts = [
        {
            'author': {'username':'Chloe'},
            'body': 'Your dad and I are having..'
        },
        {
            'author': {'username':'Sean'},
            'body': 'We are sitting in a cafe'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/reflection')
def reflection():

    return render_template('reflection.html', title='Reflection', user=user)
