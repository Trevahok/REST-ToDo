from .models import Task
from rest_framework import  serializers
from django.contrib.auth.models import User

class TaskSerializer(serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Task
        fields= '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', )