from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
	return 'Hello World'

@app.route('/goodbye/')
def goodbye():
	return 'Goodbye'

if __name__ == "__main__":
	app.run()