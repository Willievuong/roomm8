from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProfileSerializer, TaskSerializer, RoomSerializer, HouseholdSerializer
from .models import Profile, Task, Room, Household
import json

@api_view(['GET', 'POST'])
def HouseholdCreateView(request):
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

#------
@api_view(['GET', 'POST'])
def TaskCreateView(request):
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

#--
@api_view(['GET', 'POST'])
def RoomCreateView(request):
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

# CustomUser 
@api_view(['GET', 'PUT', 'DELETE'])
def RoomDetailsView(request, pk):
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
