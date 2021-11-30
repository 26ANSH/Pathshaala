import pyrebase

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
storage=firebase.storage()

def create_user(email, password):
  try:
    user = auth.create_user_with_email_and_password(email, password)
    return user['localId']
  except:
    return 400

def teacher_login(email, password):
  try:
    user = auth.sign_in_with_email_and_password(email, password)
    return user['localId']
  except:
    return 400

def uploadimage(fr, to):
  location = storage.child(to)
  location.put(fr)
  return storage.child(to).get_url()