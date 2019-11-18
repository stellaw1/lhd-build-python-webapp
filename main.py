# Our Backend for the App!
# Built with Flask

# Import Flask
import flask

# Create the application
app = flask.Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

# path parameters

# serving hello.html

# serving find.html

# process query


if __name__ == '__main__':
    app.run(debug=True)
