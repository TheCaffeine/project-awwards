from django.shortcuts import render, redirect
from .forms import SignupForm
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, 'index.html')


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    print(queryset)
    serializer_class = ProfileSerializer


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)