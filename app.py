# -*- coding: utf-8 -*-
from flask import Flask     # web app framework
from flask import make_response # json returns
import json
from flask import request   # grab request params from url
import random
from flask import render_template  # to display html pages

app = Flask(__name__)   # init flask

@app.route('/')
def index():
    return render_template('index.html')

# route to grab random quote:
# http://127.0.0.1:5000/random?limit=10
@app.route('/random', methods=['GET'])
def random_quote():
    # read file with quotes and convert to json:
    with open('quotes.json') as data_file:
        quotes = json.load(data_file)
    # extract the number of quotes the user wants:
    param = request.args.get('limit')
    if param is None: 
        limit = 1  
    elif int(param) > 20:
        limit = 20 
    elif int(param) < 1:
        limit = 1
    else:
        limit = int(param)
    # grab limit amount of random numbers between 0 and len(quotes)
    random_quotes = random.sample(quotes, limit)   
    #return quotes:
    if limit < 2: # one quote --> no quotes array
        return_json = { 
            "source": "ShayShay API",
            "quote": random_quotes[0]
            }
    else: # multiple quotes
        return_json = { 
            "source": "Shay Shay API",
            "quotes": random_quotes
            }
    
    # prepare for json return, otherwise "dict" exception
    res = json.dumps(return_json, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r


# signature:
@app.route('/mood')
def hello_world():
    return 'cups of the rose ...'

# flask server:
if __name__ == '__main__':
    #app.run(debug=False, port=80) #run app in debug mode on port 5000
    app.run(debug=False, port=5000) #run app in debug mode on port 5000 or terminal "flask run"

