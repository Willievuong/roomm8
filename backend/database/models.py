from django.db import models


class Profile(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    facebook_id = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self)

# Task
class Task(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    room_id = models.TextField() 
    name = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    user_id = models.TextField()
    user_check_id = models.TextField(null=True)
    status = models.TextField() 

    def __str__(self):
        return "{}".format(self)

# Room 
class Room(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.TextField()

    def __str(self):
        return "{}".format(self)

