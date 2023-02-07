from django.shortcuts import render
from rest_framework import viewsets
from .serialisers import CodeExerciseSerializer, UserProfileSerializer, UserSubmissionSerializer, AuthUserSerializer
from .models import CodeExercise, UserProfile, UserSubmission, AuthUser
# Create your views here.
# Create a viewset 

class CodeExerciseViewSet(viewsets.ModelViewSet):
    # Define queryset
    queryset = CodeExercise.objects.all()
    # specify serializer to be used

    serializer_class = CodeExerciseSerializer


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset_2 = UserProfile.objects.all()

    serializer_class_1 = UserProfileSerializer

class UserSubmissionViewSet(viewsets.ModelViewSet):
    queryset_3 = UserSubmission.objects.all()

    serializer_class_2 = UserSubmissionSerializer

class AuthUserViewSet(viewsets.ModelViewSet):
    queryset_3 = AuthUser.objects.all()

    serializer_class_3 = AuthUserSerializer