from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash,check_password_hash
from dotenv import load_dotenv
load_dotenv()
import os


app = Flask(__name__)

# need to configure the cloud!
MONGO_LINK=os.getenv("MONGO_LINK")
app.config["MONGO_URI"] = MONGO_LINK

mongo = PyMongo(app)

print("hello world")

# add,get and delete the information
@app.route('/addInfo',methods=['POST'])
def addInfo():
    # _json = request.json
    # _information = _json['info']
    # mongo.db.info.insert({'info':_information})
    mongo.db.info.insert({'info':request.args['info']})
    resp = jsonify("Added information")
    resp.status_code = 200
    return resp

@app.route('/getInfo')
def getInfo():
    information = mongo.db.info.find()
    resp = dumps(information)
    return resp

@app.route('/deleteInfo',methods=['DELETE'])
def deleteInfo():
    mongo.db.info.delete_many({})
    resp = jsonify("Information deleted successfully")
    resp.status_code = 200
    return resp
    

# adding and getting the Q and A

@app.route('/addQandA',methods=['POST'])
def addQandA():
    # _json = request.json
    # _query = _json['query']
    # _answer = _json['answer']
    mongo.db.qanda.insert({'query':request.args['q'],'answer':request.args['answer']})
    resp = jsonify("Q and A added")
    resp.status_code = 200
    return resp
   

@app.route("/QandA")
def QandA():
    QandA = mongo.db.qanda.find()
    resp = dumps(QandA)
    return resp


if __name__ =="__main__":
    app.run(debug=True,port=6622)