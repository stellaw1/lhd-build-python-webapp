# Our Backend for the App!
# Built with Flask

# Import Flask
import flask
import requests

# Create the application
app = flask.Flask(__name__)

API_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&locationbias=ipbias&fields=formatted_address,name,rating&"


@app.route('/') #http://127.0.0.1:5000/
def hello():
    msg = "Hello David! <br> jk"
    
    return msg

# path parameters
@app.route('/<name>') ##http://127.0.0.1:5000/<name>
def personal_hello(name):

    return "hello, " + name

# serving hello.html
@app.route('/fancy/<name>')
def some_page(name):
    return flask.render_template('hello.html', name=name)

# serving find.html
@app.route('/find',  methods=['GET'])
def find_page():
    return flask.render_template('find.html')

# process query
@app.route('/process_query', methods=['POST'])
def process_query():
    data = flask.request.form
    location = data['some_location']
    print(location)

    # if location == "stella":
    #     return flask.render_template('stella.html', name=location)
    # if location == "david":
    #     return flask.render_template('stella.html', name=location)
    # else:
    #     return flask.render_template('found.html', name=location)
    
    requestString = formRequest(location)
    responses = makeGET(requestString)['candidates']
    return flask.render_template('find.html', responses=responses)

def formRequest(input):
    return API_URL + "key=" + readKey() + "&input=" + input

def makeGET(input):
    response = requests.get(input)
    if response:
        return response.json()
    else:
        return "Error GETting that URL. Check to see if it is well-formed?"

def readKey():
    # fetches key from secrets.findplacefromtext
    f = open("secrets.txt", "r")
    contents = f.read()
    return contents.strip()

if __name__ == '__main__':
    app.run(debug=True)
