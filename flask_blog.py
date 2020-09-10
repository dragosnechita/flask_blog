from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '176a9ac4de31a515a74728bb89302d75'

posts = [
	{'author':'Dragos',
	'title':'My first blog post',
	'content':'This is my first blog post, yay',
	'date_posted': "sep 08 2020"
	},
	{'author':'Dragos',
	'title':'My second blog post',
	'content':'This is my second blog post, yay again',
	'date_posted': "sep 08 2020"
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@myblog.com' and form.password.data == 'password':
			flash('You have been logged in', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccessful, please check user and password', 'danger')
	return render_template('login.html', title='Login', form=form)
	


if __name__ == "__main__":
	app.run(debug=True)
