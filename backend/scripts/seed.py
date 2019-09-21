import time
import requests

# Living Room : 0
# Kitchen : 1
# Hallway Bathroom 2
# Corner Bathroom 3

room = [
    {
        "name": "Living Room",
        "household_id": 0
    },
    {   
        "name": "Kitchen",
        "household_id": 0
    },
    {
        "name": "Hallway Bathroom",
        "household_id": 0
    },
    {
        "name": "Corner Bathroom",
        "household_id": 0
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

task = [
    {
        "room_id": 0,
        "name": "Clean the living room",
        "start_date": time.asctime( time.localtime(time.time()) ),
        "end_date": time.asctime( time.localtime(time.time()) ),
        "user_id": 0,
        "status": "Incompleted"
    }
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


user = [
    {
        "first_name": "Janet",
        "last_name": "He",
        "nickname": "Janet",
        'household_id': 0
    }, 
    {   "first_name": "Mohammed",
        "last_name": "Ameen",
        "nickname": "Mo",
        'household_id': 0
    },
    {
        "first_name": "William",
        "last_name": "Vuong",
        "nickname": "Will",
        'household_id': 0
    },
    {
        "first_name": "Aishwarya",
        "last_name": "Niraula",
        "nickname": "Aishwarya",
        'household_id': 0
    },
    {
        "first_name": "Humberto",
        "last_name": "Madueno",
        "nickname": "Berto",
        'household_id': 0
    },
    {
        "first_name": "Sammuel",
        "last_name": "Ayala",
        "nickname": "Sammy",
        'household_id': 0
    },
    {   "first_name": "Fermin",
        "last_name": "Vargas",
        "nickname": "Fermin",
        'household_id': 0
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

create_room()