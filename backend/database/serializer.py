from rest_framework import serializers
from .models import Profile, Task, Room, Household

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = ('id', 'name', 'address', 'user_size')
        read_only_fields = ['id']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'nickname', 'first_name', 'last_name', 'facebook_id', 'date_created')
        read_only_fields = ['id']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        field = ('id', 'room_id', 'start_date', 'end_date', 'user_id', 'user_check_id', 'status')
        read_only_fields = ['id']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        field = ('id', 'name')
        read_only_fields = ['id']

