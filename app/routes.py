from flask import Flask, render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    user={'username': 'Herivelton'}
    return render_template('home.html', title='Autenticação de usuário', user = user)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('about'))
    return render_template('login.html', title='Sign In', form=form)
