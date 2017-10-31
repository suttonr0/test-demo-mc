from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
	return 'Hello World'

@app.route('/goodbye/')
def goodbye():
	return 'Goodbye'

@app.route('/htmlpage/')
def showHtml():
	return render_template('webpage.html')

if __name__ == "__main__":
	app.run()