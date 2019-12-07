from django.test import TestCase
import datetime
from .models import *
from rest_framework.test import APIClient
from rest_framework import status 
from django.urls import reverse
from encryption.encrypt import decrypt
import random
import json 

class ModelTestCase(TestCase):
    # This class defines the test suite for all models

    def setUp(self):
        #Define test client and other variables 
        pass
    
    #Need to define create test case 
    def test_model_create_profile(self): 
        pass
