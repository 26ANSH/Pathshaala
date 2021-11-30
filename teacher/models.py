from asyncio import tasks
import firebase_admin
from firebase_admin import credentials, firestore, storage
import random
from google.cloud.firestore import ArrayUnion, Increment
import datetime


# Firebase Credentials
# Fill your firebase Details which you get from console.firebase.com

cred = credentials.Certificate({
  "type": "",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": ""
})


firebase_admin.initialize_app(cred)

db = firestore.client()

def _new_user(id, fname, lname,email, country, gender):
    num = int('{:06}'.format(random.randrange(1, 10**6)))
    db.collection('teachers').document(id).set({
        'id':id,
        'email':email,
        'first_name':fname,
        'last_name':lname,
        'country':country,
        'gender':gender,
        'token': num,
        'metadata':{'students':0,'studentLimit':500,'courses':0,'courseLimit':10}
    })
    return num

def get_token(id):
  return db.collection('teachers').document(id).get().to_dict()['token']

def _new_course(name, teacher_id, description, tags, img):
  # random_number = str(random.randint((10**(3)), (10**(3))))
  time = datetime.datetime.now()
  tags = tags.split(',')
  tags = list(map(str.strip, tags))
  course = db.collection('courses').document()
  code = video_code()
  details = {'id':course.id, 'code':name.replace(' ', '-'), 'live': code ,'name':name.title(), 'teacher_id':teacher_id, 'description':description, 'tags':tags, 'img':img, 'from':time, 'students':[], 'students':0}
  course.set(details)
  db.collection('teachers').document(teacher_id).update({'metadata.courses': Increment(1)})

def get_meta(id):
  meta = db.collection('teachers').document(id).get().to_dict()['metadata']
  meta['total_course_percent'] = (meta['courses']/meta['courseLimit']) * 100
  meta['total_students_percent'] = (meta['students']/meta['studentLimit']) * 100
  return meta

def get_courses(teacher_id):
  courses = db.collection('courses').where('teacher_id', '==', teacher_id).get()
  courses = [i.to_dict() for i in courses]
  return courses

def add_student(email, c_id):
  time = datetime.datetime.now()
  checking = db.collection('students').where('email', '==', email).stream()

  for check in checking:
    id = check.id
    students = db.collection('courses').document(c_id).collection('students').where('id', '==' , id).stream()
    for student in students:
      return 400, student.to_dict()
    data = check.to_dict()
    data = {'id':id, 'email':email, 'added':time, 'verified':data['verified'], 'name':data['name']}
    db.collection('courses').document(c_id).collection('students').document(id).set(data)
    db.collection('courses').document(c_id).update({'students': Increment(1)})
    return 200, data

  new = db.collection('students').document()
  id = new.id
  db.collection('courses').document(c_id).update({'students': Increment(1)})
  new.set({'email':email, 'id':id, 'verified':False, 'created':time})
  db.collection('courses').document(c_id).collection('students').document(id).set({'id':id, 'email':email, 'added':time, 'verified':False, 'name':'Invite Sent'})
  return 100, id

def get_student_details(code, t_id):
  return [student.to_dict() for student in db.collection('courses').where('code', '==', code).where('teacher_id', '==', t_id).get()[0].reference.collection('students').get()]
  
def video_code():
  nums=[8,4,4,4,12]
  code = ''
  for num in nums:
    random_number = str(random.randint((10**(num-1)), (10**(num))))
    code += random_number + '-'
  return code[:-1]

def get_course(code, t_id):
  return list(db.collection('courses').where('code', '==', code).where('teacher_id', '==', t_id).stream())[0].to_dict()