from flask import Flask, abort, request
from flask_mysqldb import MySQL
import os 
import datetime 
import json 

app = Flask(__name__)

app.config['MYSQL_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASS')
app.config['MYSQL_DB'] = 'roomm8'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

app.route('/login', methods=['POST'])
def login():

  return 0

app.route('/logout', methods=['GET'])
def logout():

  return 0

app.route('/profile/<userID>', methods=['GET'])
def users(userID):

  return 0

app.route('/family/<familyID>', methods=['GET'])
def family(familyID):

  return 0

app.route('/addUser', methods=['POST'])
def addUser():

  return 0

app.route('/deleteUser', methods=['POST'])
def delUser():

  return 0

app.route('/addFamily', methods=['POST'])
def addFamily():

  return 0

app.route('/deleteFamily', methods=['POST'])
def delFamily():

  return 0

app.route('/submitTicket', method=['POST'])
def submitTicket():

  return 0


if __name__ == '__main__':
  app.run(debug=True)
