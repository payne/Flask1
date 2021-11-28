# https://nickymarino.com/2021/04/13/create-python-web-apps-with-flask-and-replit/

from flask import Flask, render_template

# Create a flask app
app = Flask(__name__, template_folder='templates', static_folder='static')


# Index page
@app.route('/')
def hello():
    return "Hello World!"


@app.route('/tutorial')
def tutorial():
    tutorial_url = "https://nickymarino.com/2021/04/13/create-python-web-apps-with-flask-and-replit/"
    return f"<h1>tutorial is <a href={tutorial_url}>{tutorial_url}</a></h1>"


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)
