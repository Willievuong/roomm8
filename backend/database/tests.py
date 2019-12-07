from django.test import TestCase
import datetime
from .models import *
from rest_framework.test import APIClient
from rest_framework import status 
from django.urls import reverse
import json 
from datetime import datetime

class ModelTestCase(TestCase):
    # This class defines the test suite for all models
    def setUp(self):
        self.client = APIClient()
        time = datetime.utcnow()
        time = str(time)

        self.household_data = {
                "name": "Trap Haus",
                "address": "Somewhere cool ;)",
                "user_size": 7
            }


        self.room_data = {
                "name": "Living Room",
                "household_id": 1
            }

        self.profile_data = {
                "first_name": "Janet",
                "last_name": "He",
                "nickname": "Janet",
                "household_id": 1,
                "pin": 1234,
                
            }


        self.task_data = {
                "room_id": 1,
                "name": "Clean the living room",
                "start_date": time,
                "end_date": time,
                "user_id": 3,
                "status": "Incompleted",
                "household_id": 1
            }

    #Need to define create test case 
    def test_api_model_profile(self):
        self.response = self.client.post(
          reverse('profile'),    
          self.profile_data,
          format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

        profile = Profile.objects.get() 
        response = self.client.get(
            reverse('profile_details',
            kwargs={'pk': profile.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertContains(response, profile)

        profile = Profile.objects.get()
        change_profile = self.profile_data
        change_profile['first_name'] = 'Its a new name!'
        res = self.client.put(
            reverse('profile_details', kwargs={'pk': profile.id}),
            change_profile, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        profile = Profile.objects.get()
        response = self.client.delete(
            reverse('profile_details', kwargs={'pk': profile.id}),
            format='json', follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)    

    def test_api_model_task(self):
        self.response = self.client.post(
          reverse('task'),    
          self.task_data,
          format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

        task = Task.objects.get() 
        response = self.client.get(
            reverse('task_details',
            kwargs={'pk': task.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        task = Task.objects.get()
        change_task = self.task_data
        change_task['name'] = 'Its a new new name'
        res = self.client.put(
            reverse('task_details', kwargs={'pk': task.id}),
            change_task, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        task = Task.objects.get()
        response = self.client.delete(
            reverse('task_details', kwargs={'pk': task.id}),
            format='json', follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)    

    def test_api_model_household(self):
        self.response = self.client.post(
          reverse('household'),    
          self.household_data,
          format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

        household = Household.objects.get() 
        response = self.client.get(
            reverse('household_details',
            kwargs={'pk': household.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
  
        household = Household.objects.get()
        change_household = self.household_data
        change_household['name'] = 'Its a new new name'
        res = self.client.put(
            reverse('household_details', kwargs={'pk': household.id}),
            change_household, format='json'
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        household = Household.objects.get()
        response = self.client.delete(
            reverse('household_details', kwargs={'pk': household.id}),
            format='json', follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)    

    def test_api_model_room(self):
        self.response = self.client.post(
          reverse('room'),    
          self.room_data,
          format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

        room = Room.objects.get() 
        response = self.client.get(
            reverse('room_details',
            kwargs={'pk': room.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        room = Room.objects.get()
        change_room = self.room_data
        change_room['name'] = 'Its a new new name'
        res = self.client.put(
            reverse('room_details', kwargs={'pk': room.id}),
            change_room, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        room = Room.objects.get()
        response = self.client.delete(
            reverse('room_details', kwargs={'pk': room.id}),
            format='json', follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)    