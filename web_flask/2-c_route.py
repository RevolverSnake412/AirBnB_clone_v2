#!/usr/bin/python3
"""starts Flask web application"""

if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        """returns Hello HBNB!"""
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """returns HBNB"""
        return "HBNB"

    @app.route('/c/<text>', strict_slashes=False)
    def cisfun(text):
        return 'C ' + text.replace('_', ' ')

    app.run(host='0.0.0.0', port='5000')
