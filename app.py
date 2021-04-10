import gscholarFetcher
from flask import Flask, request, jsonify, make_response,redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return "All Okay",200

@app.route('/getAuthor',methods=['GET'])
def respond():
    author = request.args.get('author','')
    uni = request.args.get('uni','')
    response = gscholarFetcher.get_author(author,uni)
    return jsonify(response)

if __name__ == '__main__':
    app.run()
