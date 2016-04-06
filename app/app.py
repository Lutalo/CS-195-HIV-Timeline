import events
from flask import Flask
from flask import render_template

app = Flask(__name__)
db = events.initialize()

@app.route('/')
def index(tile='Home'):
	timelineJSON = events.jsonTable()
	return render_template("index.html", timelineJSON=timelineJSON)

@app.route('/about')
def about(title='About Us'):
	return render_template("about.html", title=title )

@app.route('/service')
def service(title='Service'):
	return render_template("service.html")

@app.route('/information')
def information(title=''):
	return render_template("information.html")

@app.route('/getinvolved')
def getInvolved(title=''):
	return render_template("getinvolved.html")

if __name__ == '__main__':
	#App can be rendered at -> localhost:5000 or 127.0.0.1:5000
	app.run(debug=True)

