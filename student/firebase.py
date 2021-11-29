import pyrebase
import json

CONFIG = {
  'apiKey': "AIzaSyCG3GCdUeHoEobqLSQM2UxXe0hYnzSPtXI",
  'authDomain': "pathshaala-e8244.firebaseapp.com",
  'databaseURL': "https://pathshaala-e8244-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "pathshaala-e8244",
  'storageBucket': "pathshaala-e8244.appspot.com",
  'messagingSenderId': "6017147021",
  'appId': "1:6017147021:web:b3d814a7f6b00b205782c4"
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