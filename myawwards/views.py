from .forms import SignupForm
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html')


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)