import json
import sys
import flask
from flask import Flask, Response,request
from flask_ngrok import run_with_ngrok

from commit_api import *
#import urllib.request
app = Flask(__name__)
run_with_ngrok(app)
'''@app.route('/')

def index():
    """Index page"""
    return 'Welcome'



@app.route('/github/', methods=['GET', 'POST', 'HEAD'])
def api_github_message():
    """api for sending comments"""
    if request.headers['Content-Type'] == 'application/json':
        print('inside server ')
        my_info = json.dumps(request.json)
        payload = json.loads(my_info)
        return payload

'''

@app.route('/github/', methods=['GET', 'POST', 'HEAD'])

def api_github_message():
    """api for sending comments"""
    if request.headers['Content-Type'] == 'application/json':
        print('inside server ')
        my_info = flask.json.dumps(request.json)
        payload = flask.json.loads(my_info)
        if not payload['action'] == 'closed':
            apicall_obj = api_call()
            apicall_obj.postman()
            res = Response(flask.json.dumps(apicall_obj.critical_files()), status=200, mimetype='application.json')
            return res
        prediction_response = flask.json.dumps({"state": "closed pull request"})
        app.logger.info("closed pull request")
        res = Response(flask.json.dumps(apicall_obj.critical_files()), status=200, mimetype='application.json')
        return res


@app.route("/commit_api_call/", methods=['GET', 'POST'])
def commit_api_result():
    apicall_obj = api_call()
    apicall_obj.postman()
    return flask.json.dumps(apicall_obj.critical_files())


if __name__ == "__main__":
    app.run()
