from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    user = {'username': 'Herivelton'}
    # posts = [
    #     {
    #         'author': {'username': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'username': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     }
    # ]
    return render_template("home.html",**locals())

    
@app.route('/linkedin')
def linkedin():
    return render_template("linkedin.html")    
    
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

if __name__ == '__main__':
    app.run(debug=True)