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

@app.route('/support')
def service(title='Services | Community Support'):
	return render_template("support.html")

@app.route('/testing')
def service(title='Services | Testing'):
	return render_template("testing.html")

@app.route('/aboutHIV')
def information(title='Information | About HIV'):
	return render_template("abouthiv.html")

@app.route('/prevention')
def information(title='Information | Prevention'):
	return render_template("prevention.html")

@app.route('/videos')
def information(title='Information | Videos'):
	return render_template("videos.html")

@app.route('/getinvolved')
def getInvolved(title=''):
	return render_template("getinvolved.html")

if __name__ == '__main__':
	#App can be rendered at -> localhost:5000 or 127.0.0.1:5000
	app.run(debug=True)

