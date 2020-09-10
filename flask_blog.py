from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == "__main__":
	app.run(debug=True)
