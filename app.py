import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! Welcome to Flask!'

@app.route('/about')
def about():
    return 'This is a simple Flask application.'

if __name__ == '__main__':
    # Debug mode can be controlled via FLASK_DEBUG environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    app.run(debug=debug_mode)
