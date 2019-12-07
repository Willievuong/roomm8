import requests
import json

'''
    Clearing the database for future use
'''


BACKEND_URL = 'http://localhost:8000/'


def clear_user():
    '''
        Clearing all the user by first obtaining a list of users
    '''

    user_list = json.loads((requests.get(BACKEND_URL + 'profile/')).text)

    print('Deleting all users')
    for i in user_list: 
        user_id = i['id']

        r = requests.delete(BACKEND_URL + 'profile/' + str(user_id) + '/')
        print(r)

def clear_room():
    '''
        Clearing all the rooms by first obtaining a list of rooms 
    '''

    room_list = json.loads((requests.get(BACKEND_URL + 'room/').text))

    print('Deleting all rooms')
    for i in room_list: 
        room_id = i['id']

        r = requests.delete(BACKEND_URL + 'room/' + str(room_id) + '/')
        print(r)

def clear_task():
    '''
        Clearing all the tasks by first obtaining a list of tasks 
    '''

    task_list = json.loads((requests.get(BACKEND_URL + 'task/').text))

    print('Deleting all task')
    for i in task_list: 
        task_id = i['id']

        r = requests.delete(BACKEND_URL + 'task/' + str(task_id) + '/')
        print(r)


def clear_household():
    '''
        Clearing all the household by first obtaining a list of household 
    '''

    house_list = json.loads((requests.get(BACKEND_URL + 'household/').text))

    print('Deleting all house')
    for i in house_list: 
        house_id = i['id']

        r = requests.delete(BACKEND_URL + 'household/' + str(house_id) + '/')
        print(r)

clear_task()