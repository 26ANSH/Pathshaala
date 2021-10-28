from django.db import models

# Create your models here.
# create a user
class user_student(models.Model):
    # user_id
    user_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email_confirmed = models.BooleanField(default=False)
