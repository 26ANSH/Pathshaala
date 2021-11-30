import pyrebase
import json

# Fill your Firebase Details here - 
CONFIG = {
  'apiKey': "",
  'authDomain': "",
  'databaseURL': "",
  'projectId': "",
  'storageBucket': "",
  'messagingSenderId': "",
  'appId': ""
};

# start firebase authentication
firebase = pyrebase.initialize_app(CONFIG)
auth = firebase.auth()

def create_user(email, password):
  try:
    user = auth.create_user_with_email_and_password(email, password)
    return user['localId']
  except Exception as e:
      msg = json.loads(e.args[1])['error']['message']
      return 400

def student_login(email, password):
  try:
    user = auth.sign_in_with_email_and_password(email, password)
    return user['localId']
  except:
    return 400