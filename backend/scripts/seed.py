import time
from datetime import datetime
import requests

# Living Room : 0
# Kitchen : 1
# Hallway Bathroom 2
# Corner Bathroom 3

room = [
    {
        "name": "Living Room",
        "household_id": 1
    },
    {   
        "name": "Kitchen",
        "household_id": 1
    },
    {
        "name": "Hallway Bathroom",
        "household_id": 1
    },
    {
        "name": "Corner Bathroom",
        "household_id": 1
    }
]

BACKEND_URL = "http://localhost:8000/"

def create_room():
    '''
        Populating the database with a list of room
    '''

    print("CREATING ROOM")
    for i in room:
        r = requests.post(BACKEND_URL + "room/", json=i)
        print(r)

user = [
    {
        "first_name": "Janet",
        "last_name": "He",
        "nickname": "Janet",
        "household_id": 1,
        "pin": 1234,
        
    }, 
    {   "first_name": "Mohammed",
        "last_name": "Ameen",
        "nickname": "Mo",
        "household_id": 1,
        "pin": 1234,
    },
    {
        "first_name": "William",
        "last_name": "Vuong",
        "nickname": "Will",
        "household_id": 1,
        "pin": 1234,
    },
    {
        "first_name": "Aishwarya",
        "last_name": "Niraula",
        "nickname": "Aishwarya",
        "household_id": 1,
        "pin": 1234,
    },
    {
        "first_name": "Humberto",
        "last_name": "Madueno",
        "nickname": "Berto",
        "household_id": 1,
        "pin": 1234,
    },
    {
        "first_name": "Sammuel",
        "last_name": "Ayala",
        "nickname": "Sammy",
        "household_id": 1,
        "pin": 1234,
    },
    {   "first_name": "Fermin",
        "last_name": "Vargas",
        "nickname": "Fermin",
        "household_id": 1,
        "pin": 1234,
    }
]

def create_user():
    '''
        Populating the database with a list of users
    '''

    print("CREATING USER")
    for i in user:
        r = requests.post(BACKEND_URL + "profile/", json=i)
        print(r)

time = datetime.utcnow()
time = str(time)

task = [
    {
        "room_id": 1,
        "name": "Clean the living room",
        "start_date": time,
        "end_date": time,
        "user_id": 3,
        "status": "Incompleted",
        "household_id": 1
    },
    {
        "room_id": 2,
        "name": "Clean the kitchen",
        "start_date": time,
        "end_date": time,
        "user_id": 4,
        "status": "Incompleted",
        "household_id": 1
    },
    {
        "room_id": 3,
        "name": "Clean the hallway bathroom",
        "start_date": time,
        "end_date": time,
        "user_id": 6,
        "status": "Incompleted",
        "household_id": 1
    },
    {
        "room_id": 4,
        "name": "Clean the corner bathroom",
        "start_date": time,
        "end_date": time,
        "user_id": 7,
        "status": "Incompleted",
        "household_id": 1
    },
]

#TODO: Full flesh out the task 
def create_task(): 
    '''
        Populating the house with a list of task
    '''

    print("CREATING TASK")
    for i in task: 
        r = requests.post(BACKEND_URL + "task/", json=i)
        print(r)


household = [
    {
        "name": "Trap Haus",
        "address": "Somewhere cool ;)",
        "user_size": 7
    }
]

def create_household():
    '''
        Populating the database with a single house 
    '''
    print("CREATING HOUSEHOLD")
    for i in household: 
        r = requests.post(BACKEND_URL + "household/", json=i)
        print(r)


# create_household()
# create_room()
create_task()
# create_user()