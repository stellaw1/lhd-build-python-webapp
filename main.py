# Our Backend for the App!
# Built with Flask

# Import Flask
import flask


# Create the application
app = flask.Flask(__name__)

API_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&locationbias=ipbias&fields=formatted_address,name,rating&"


@app.route('/')
def hello():
    return "Hello World!"

# path parameters
@app.route('/<name>')
def hello_name(name):
    return name

# serving hello.html
@app.route('/hello/<name>')
def personal_hello(name):
    # you can do preprocessing here!
    return flask.render_template('hello.html', name=name)

# serving find.html
@app.route('/find', methods=['GET'])
def serve_page():
    return flask.render_template('find.html')

# process query
@app.route('/process_query', methods=['POST'])
def process_query():
    data = flask.request.form  # is a dictionary
    location = data['some_location']
    requestString = formRequest(location)
    responses = makeGET(requestString)["candidates"]
    return flask.render_template('find.html', responses=responses)


def formRequest(input):
    # TODO
    return ""  # return some string


def makeGET(input):
    # TODO
    return None  # return some response


def readKey():
    f = open("secrets.txt", "r")
    contents = f.read()
    return contents.strip()


if __name__ == '__main__':
    app.run(debug=True)
