import time
import requests

# Living Room : 0 
# Kitchen : 1 
# Hallway Bathroom 2 
# Corner Bathroom 3 

room = ["Living Room", "Kitchen", "Hallway Bathroom", "Corner Bathroom"]

BACKEND_URL = "http://localhost:8000/"

def create_room():
    '''
        Populating the database with a list of room
    '''

    print("CREATING ROOM")
    for i in room:
        data = {
            "name": i
        } 

        r = requests.post(BACKEND_URL + "room/", json=data)
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
        "nick_name": "Janet"
    }, 
    {   "first_name": "Mohammed",
        "last_name": "Ameen",
        "nick_name": "Mo"
    },
    {
        "first_name": "William",
        "last_name": "Vuong",
        "nick_name": "Will"
    },
    {
        "first_name": "Aishwarya",
        "last_name": "Niraula",
        "nick_name": "Aishwarya"
    },
    {
        "first_name": "Humberto",
        "last_name": "Madueno",
        "nick_name": "Berto"
    },
    {
        "first_name": "Sammuel",
        "last_name": "Ayala",
        "nick_name": "Sammy"
    },
    {   "first_name": "Fermin",
        "last_name": "Vargas",
        "nick_name": "Fermin"
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
