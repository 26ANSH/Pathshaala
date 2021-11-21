from asyncio import tasks
import firebase_admin
from firebase_admin import credentials, firestore, storage
import random
from google.cloud.firestore import ArrayUnion
import datetime

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "pathshaala-e8244",
  "private_key_id": "e9fad178e9e8495dcc2f33e77431fbf81e6a045e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCgWBygbDYW4MDw\nnbtXDpMvrm0oVuOEGPRw1Ia4mZsnLLAFKXXD2jZUyvr1jl23jDvZUqQFPblFF0cH\nuYF7mhXI87N6EVC7WLbSVxOWjYzoktoEel225ARgLZU4U9O0hgdikPr42k0sroX7\n11lSA1QkFbxrB0vouFO+aaI2VTQ9ZyrnCuL8t7deWpwW8Zb5RBLLkKFNyV2KUbIt\nBR6ZXpU5Deasq96Mw+VtxkAZBWQiArGYnBQg6k0r80ke/td5cIZJEzaO/p+M51K2\ngLE3aPm773ZXWLcQIkz9zl6LHC+1YkWKU+Q0WNSNVpEssw/oJ7IgO33opBC5Yw/+\n5uUpS5j9AgMBAAECggEACG0Y9AU7wnAFM5/WXHjTm0nbSqdmRWbaUaOZgNHxqVlb\n1qmbGrO47zPLhGP64M5pxr3lCLF5rvvOK8W/3DL4uhq0b9HBIFdFJECXMu41XXN6\nKYoUqqvI3xUGJnOhSHdSpAdiaPlv3M0/FUD33Kt4HH1X7XfwsUYegH8kmx5XJHLW\nLvmyac53JqsljLUayulvrCQIUyJUCQU35nXeaz7Ce1Q43AKl0qrBY/dWxgiLAWTk\nqF7JV0B7mLIc+JxdgPiHrrzaAJrO+lTkix4DqzGzJ7E6UPkemSaZzSu2fOes9uy9\nlVYBjNcYRlbCqrggsSoZLiiLO0EraHzeL/Nih9suMQKBgQDLl+3/VGe2mhh1f+BM\nLnAoW/dqu4R/WLNLyZcyhRT4uiesXpynUYzLjxTGqP1nInvVEIQFJjFe/RrMYv92\nO6ZhkG+plu+Z7FduHcwXaI36s0nsfWooMU6RIkE82/5mfolWZTTHiziuG6L5TLtr\nauxGjot69MwFG7LnOryToXE1PwKBgQDJnjYPGrf/MhlmhtCC/Hb1BcV7BNc3JL2N\nEKP4e/e3sdbAriIbx4LqZG/bwFxaNyKCWNwrEvfAmqYdYv85AK+h83hiC59B5nGm\nKCAG1nv5R/L98XZ4Gsxg5FvM5kI37K+RVQWf3kyqphpk6/M58xBuOdjwiHp8ekkV\nrSd1RDt2wwKBgHWirH5qW56zfMxvfb8m2eFH+jZucMlQDBEPQtCK+qoYjZHX/PXk\nddCsNJnwzLIJx7k9WLrM7Zvv7MsJrIe5QZJ/7TT1JC4w0/epOeKQo/CmJWGCuZLN\nopLTUxSCHIVGOb50rcFaXP6ks08OmgAgALNn64m45iVRctaOJqW6k3nrAoGAfCXq\nvcRDFmYgE+zhyjZxfZEPOCAT8cWy3oEnpqOXNsrQJRdUs2xX5cLwyg0aEQcwPbk/\n4VotqrDPpvrFk7EjdQL51s23RBoFUz4T8oHyFt7B9rLPs0c1IFidWn9SuSMKPOBw\ntS9qYA4l5I0R2VYdgPIn7nzrh2i5Rhq4WFIql4cCgYBWddBXlQRqjnxiQEAKPuik\nkitWuvHmcgHd4PXcjTFL52TItwvHd0GzozkGxBGNpGZaeB50J8xZz+BQjQWwSiGf\nN+mLkNkBEFB817j2iCI5OxpAdkVYWHANif9ihSlkilGaYHqR2ZpHE2PzjpXzj4YG\nbyVEugisheUhNeZ1sHipyA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-8me30@pathshaala-e8244.iam.gserviceaccount.com",
  "client_id": "108558708255419972534",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8me30%40pathshaala-e8244.iam.gserviceaccount.com"
})
firebase_admin.initialize_app(cred)


db = firestore.client()


# # db.collection('trial').add({'name':'Ansh', 'Age':19})

# # add data in collection with id = ansh_12345
# ansh = db.collection('trial').document('ansh_1245').update({'ansh_12345':'ok'})
# print(ansh)


def _new_user(id, fname, lname,email, country, gender):
    num = int('{:06}'.format(random.randrange(1, 10**6)))
    db.collection('teachers').document(id).set({
        'id':id,
        'email':email,
        'first_name':fname,
        'last_name':lname,
        'courses':[],
        'country':country,
        'gender':gender,
        'token': num
    })
    return num

def get_token(id):
  # num = int('{:06}'.format(random.randrange(1, 10**6)))
  return db.collection('teachers').document(id).get().to_dict()['token']

def _new_course(name, teacher_id, description, tags, img):
  time = datetime.datetime.now()
  tags = tags.split(',')
  tags = list(map(str.strip, tags))
  print(tags)
  course = db.collection('courses').document()
  details = {'id':course.id, 'name':name, 'teacher_id':teacher_id, 'description':description, 'tags':tags, 'img':img, 'from':time, 'students':[]}
  course.set(details)
  details = {'id':course.id, 'name':name, 'description':description, 'img':img, 'from':time,'tags':tags, 'students':0}
  db.collection('teachers').document(teacher_id).update({'courses':ArrayUnion([details])})

def get_courses(teacher_id):
  return db.collection('teachers').document(teacher_id).get().to_dict()['courses']

def add_student(email, t_id):
  time = datetime.datetime.now()
  checking = db.collection('students').where('email', '==', email).stream()

  for check in checking:
    id = check.id
    students = db.collection('teachers').document(t_id).collection('students').where('id', '==' , id).stream()
    for student in students:
      return 400, id
    db.collection('teachers').document(t_id).collection('students').document(id).set({'id':id, 'email':email, 'added':time})
    return 200, id

  new = db.collection('students').document()
  id = new.id
  new.set({'email':email, 'id':id, 'verified':False, 'created':time, 'courses':[]})
  db.collection('teachers').document(t_id).collection('students').document(id).set({'id':id, 'email':email, 'added':time})
  return 201, id


# _new_user('ansh_1111111111', 'ansh', 'anshemail')
# ok = db.collection('students').document('student_1').collection('course').update("cpp")

# students = db.collection('students').document('student_1')
# print(ok.get().to_dict())
# for i in students.stream():
#     print(i.id)
#     print(i.to_dict())

# new_course = db.collection('courses').document('course_12345').set({'name':'C++', 'level':'Beginner'}, merge=True)
# st = ['19bcs4077', '19bcs4074']
# st.sort()
# new_course = db.collection('courses').document('course_12345').update({'students':ArrayUnion(['ok1'])})
# print(new_course)

# course = db.collection('courses').document('course_12345').get().to_dict()
# students = list(course['students'])
# new_st = db.collection('courses').document('course_12345').document('students')
# print(new_st)

# assignments = db.collection('courses').document('course_12345').collection(u'assignments').document().set({u'name':u'assignment_1', u'marks':u'10'})
# for doc in assignments:
#   print(doc.id)
#   print(doc.data)

# db.collection('courses').document('jbjbjuj').set({'students':[], 'name':'name', 'description':'description', 'tags':'tags','teacher_id':1234})

# courses = ['12345', '123456']

# ok = db.collection('students').where(u'courses',u'array_contains_any',courses).stream()
# print('ok =>',ok)
# for o in ok:
#   print(o.id)

# teacher_id = "74bdcm23765i9sncu4i32o23
# course_id = teacher_id[:6] + random
# print(course_id)

# teacher = 'gJBGl5uxMeNRtlkWLysQl6mUqLn2'
# _new_course('C++ For Begineers', teacher, 'description'

# ok = db.collection('teachers').document('gJBGl5uxMeNRtlkWLysQl6mUqLn2').collection('students').where('id', '==', '1111123456').stream()
# print(ok)
# db.collection('teachers').document('gJBGl5uxMeNRtlkWLysQl6mUqLn2').document('students').set({'email':email})


# print(add_student('okok@gmail.com', 'gJBGl5uxMeNRtlkWLysQl6mUqLn2'))


# checking = db.collection('students').where('email', '==', 'anshv@gmail.com').stream()

# for check in checking:
#   print('ok', check.id)