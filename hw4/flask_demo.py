from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/ask')
def button1():
	return render_template('ask.html')


@app.route('/result')
def button2():
	return render_template('result.html')


@app.route('/result/<post_id>')
def result_page(post_id):
	return render_template('result_comments.html',post_id=post_id)

if __name__ == "__main__":
	app.run(debug='true')

