# from google.cloud import firestore
# import firebase_admin
# from firebase_admin import credentials, firestore, storage

# db = firebase_admin.get_app()

# def get_courses_for_students():
#     data = list()
#     courses = db.collection('courses').stream()
#     for course in courses:
#         course = course.reference
#         student = course.collection('students').where('email', '==', 'bxss').stream()
#         for i in student:
#             data.append(course.get().to_dict())
#     return data