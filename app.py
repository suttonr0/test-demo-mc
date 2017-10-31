from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
	return 'Hello World'

@app.route('/goodbye/')
def goodbye():
	return 'Goodbye'

@app.route('/htmlpage/<name>')
def showHtml(name):
	return render_template('webpage.html', input = name)

if __name__ == "__main__":
	app.run()