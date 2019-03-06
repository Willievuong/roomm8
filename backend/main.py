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
  cur = mysql.connection.cursor()
  email = request.form.get('email')
  password = request.form.get('password')
  select_stmt = "SELECT * FROM Users where Email=%(email)s AND Password=%(password)s"
  cur.execute(select_stmt, {'email': email, 'password': password})
  rv = list(cur.fetchall())
  if(len(rv) == 0):
    abort(404) # Return error message since profile is not found 
  else: 
     for row in range(len(rv)):
        profile  = {
          "id": int(rv[row]['userID']),
          "firstName": str(rv[row]['firstName']),
          "lastName": str(rv[row]['lastName']),
          "email": str(rv[row]['email']),
          "description": str(rv[row]['description']),
          "lastActive": str(rv[row]['lastActive']),
          "location": str(rv[row]['location'])
        }
      
  return json.dumps(profile)

app.route('/profile/<userID>', methods=['GET'])
def users(userID):
  cur = mysql.connection.cursor()
  select_stmt = "SELECT * FROM users where userid=%(userID)s"
  cur.execute(select_stmt, {'userID' : userID})    
  rv = list(cur.fetchall())
  profile  = {
    "id": int(rv[0]['userID']),
    "firstName": str(rv[0]['firstName']),
    "lastName": str(rv[0]['lastName']),
    "email": str(rv[0]['email']),
    "description": str(rv[0]['description']),
    "lastActive": str(rv[0]['lastActive']),
    "location": str(rv[0]['location'])
  }

  return json.dumps(profile)

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
