from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProfileSerializer, TaskSerializer, RoomSerializer, HouseholdSerializer
from .models import Profile, Task, Room, Household

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
    except query.DoesNotExist:
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
    except query.DoesNotExist:
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
    except query.DoesNotExist:
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
    except query.DoesNotExist:
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
