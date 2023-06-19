from flask import Flask, render_template, flash, redirect
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/posts')
def post():
    user = {'username': 'Miguel'}
    posts = [
        {'author': {'username': 'Chris'},
         'post': 'Today was a good day!'},
        {'author': {'username': 'John'},
         'post': 'The avengers movie was fun!'
         }
    ]
    return render_template('index.html', title='Home', posts=posts, user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/posts')
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True)
