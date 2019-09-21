from django.db import models


class Household(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.TextField()
    address = models.TextField()
    user_size = models.IntegerField(null=True)

    def __str__(self):
        return "{}".format(self)

class Profile(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    facebook_id = models.TextField(null=True)
    first_name = models.TextField()
    last_name = models.TextField()
    nickname = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    household_id = models.TextField(null=True)
    pin = models.TextField(null=True) #TODO: Not doing this in plaintext...

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
    household_id = models.TextField(null=True)

    def __str__(self):
        return "{}".format(self)

# Room 
class Room(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.TextField()
    household_id = models.TextField(null=True)

    def __str(self):
        return "{}".format(self)

