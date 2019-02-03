from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from .models import Task
from .serializers import TaskSerializer,UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class  = TaskSerializer

class UserViewSet(ModelViewSet):
    """
     API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

def home(request):
    return render(request, 'home.html')