#!flask/bin/python
"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask

app = Flask(__name__, static_url_path = "")
app.config['DEBUG'] = True

# default page
@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404