from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProfileSerializer, TaskSerializer, RoomSerializer, HouseholdSerializer
from .models import Profile, Task, Room, Household
import json

@api_view(['GET', 'POST'])
def HouseholdCreateView(request):
    '''
        The route for 
            GET: household class for obtaining all instances of household
            POST: creating a new household instance

        Args: 
            POST: The object to be created 

        Return:
            HTTP 200: An list of all instance of household
                 201: A new household object was created
                 400: Error in creating the new object

        Raises: 
            None
    '''

    if request.method == 'GET':
        queryset = Household.objects.all()
        serializer = HouseholdSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HouseholdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def HouseholdDetailsView(request, pk):
    '''
        The route for
            GET: querying the object with the unique identifier 
            PUT: querying for the object, and updating it with new fields given in the body
            DELETE: deleting the object with the queried id 

        Args:
            pk (int): The unique identifier used to identify the object

        Return: 
            GET: The object with the corresponding primary key
            PUT: The newly updated object with the corresponding primary key
            DELETE: 204 status code for successful delete
        Raises: 
            None
    '''
    try:
        query = Household.objects.get(pk=pk)
    except Household.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HouseholdSerializer(query)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HouseholdSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def ProfileCreateView(request):
    '''
        The route for 
            GET: profile class for obtaining all instances of profile
            POST: creating a new profile instance

        Args: 
            POST: The object to be created 

        Return:
            HTTP 200: An list of all instance of profile
                 201: A new profile object was created
                 400: Error in creating the new object

        Raises: 
            None
    '''
    if request.method == 'GET':
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ProfileDetailsView(request, pk):
    '''
        The route for
            GET: querying the object with the unique identifier 
            PUT: querying for the object, and updating it with new fields given in the body
            DELETE: deleting the object with the queried id 

        Args:
            pk (int): The unique identifier used to identify the object

        Return: 
            GET: The object with the corresponding primary key
            PUT: The newly updated object with the corresponding primary key
            DELETE: 204 status code for successful delete
        Raises: 
            None
    '''
    try:
        query = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(query)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def TaskCreateView(request):
    '''
        The route for 
            GET: Task class for obtaining all instances of task
            POST: creating a new task instance

        Args: 
            POST: The object to be created 

        Return:
            HTTP 200: An list of all instance of task
                 201: A new task object was created
                 400: Error in creating the new object

        Raises: 
            None
    '''
    if request.method == 'GET':
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def TaskDetailsView(request, pk):
    '''
        The route for
            GET: querying the object with the unique identifier 
            PUT: querying for the object, and updating it with new fields given in the body
            DELETE: deleting the object with the queried id 

        Args:
            pk (int): The unique identifier used to identify the object

        Return: 
            GET: The object with the corresponding primary key
            PUT: The newly updated object with the corresponding primary key
            DELETE: 204 status code for successful delete
        Raises: 
            None
    '''
    try:
        query = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(query)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def RoomCreateView(request):
    '''
        The route for 
            GET: Room class for obtaining all instances of Room
            POST: creating a new Room instance

        Args: 
            POST: The object to be created 

        Return:
            HTTP 200: An list of all instance of Room
                 201: A new Room object was created
                 400: Error in creating the new object

        Raises: 
            None
    ''' 
    if request.method == 'GET':
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def RoomDetailsView(request, pk):
    '''
        The route for
            GET: querying the object with the unique identifier 
            PUT: querying for the object, and updating it with new fields given in the body
            DELETE: deleting the object with the queried id 

        Args:
            pk (int): The unique identifier used to identify the object

        Return: 
            GET: The object with the corresponding primary key
            PUT: The newly updated object with the corresponding primary key
            DELETE: 204 status code for successful delete
        Raises: 
            None
    '''
    try:
        query = Room.objects.get(pk=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomSerializer(query)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RoomSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Query All User from a specific household 
@api_view(['GET'])
def GetUserHousehold(request, household_id):
    '''
        Get an list of user ids from a specific household
    '''
    
    try: 
        queryset = Profile.objects.filter(household_id=household_id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProfileSerializer(queryset, many=True)
    # print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def GetTaskHousehold(request, household_id):
    '''
        Get The latest task from a household
        TODO: Hardcoded to be 4 task for now, need to think of a way to implement it later
    '''
    try: 
        queryset = Task.objects.filter(household_id=household_id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def GetRoomHousehold(request, household_id):
    '''
        Get The latest room from a household
    '''
    try: 
        queryset = Room.objects.filter(household_id=household_id)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = RoomSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def PinCheck(request):
    '''
        Checking ther pin

    '''

    user_id = request.data['user_id']
    user_pin = request.data['userPin']
    user_check_id = request.data['user_check_id']
    user_check_pin = request.data['checkUserPin']

    print(user_check_id)

    try: 
        user_query = Profile.objects.get(id=user_id)
    except Profile.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    try: 
        user_check_query = Profile.objects.get(id=user_check_id)
    except Profile.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = (ProfileSerializer(user_query)).data
    user_check = (ProfileSerializer(user_check_query)).data

    if user['pin'] == user_pin and user_check['pin'] == user_check_pin: 
        return Response(status=status.HTTP_200_OK)
    else: 
        return Response(status=status.HTTP_400_BAD_REQUEST)
