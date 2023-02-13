from django.shortcuts import render
from rest_framework import viewsets
from .serialisers import CodeExerciseSerializer, ModuleSerializer, ModuleLanguageSerializer, LessonTopicSerializer, TextBlockExerciseSerializer, TextBlockLessonSerializer , ModuleTopicSerializer, TopicSerializer, LessonSerializer, LanguageSerializer, TextBlockSerializer
from .models import CodeExercise, Topic, Lesson, Module, Language, TextBlock
# Create your views here.
# Create a viewset 

class CodeExerciseViewSet(viewsets.ModelViewSet):
    # Define queryset
    queryset = CodeExercise.objects.all()
    # specify serializer to be used

    serializer_class = CodeExerciseSerializer

class ModuleLanguageViewSet(viewsets.ModelViewSet):
    # Define queryset
    queryset = Module.objects.all()
    # specify serializer to be used

    serializer_class = ModuleLanguageSerializer

class LessonTopicViewSet(viewsets.ModelViewSet):
     # Define queryset
    queryset = Lesson.objects.all()
    # specify serializer to be used

    serializer_class = LessonTopicSerializer

class TextBlockLessonViewSet(viewsets.ModelViewSet):
     # Define queryset
    queryset = TextBlock.objects.all()
    # specify serializer to be used

    serializer_class = TextBlockLessonSerializer


class TextBlockExerciseViewSet(viewsets.ModelViewSet):
     # Define queryset
    queryset = TextBlock.objects.all()
    # specify serializer to be used

    serializer_class = TextBlockExerciseSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    # Define queryset
    queryset = Module.objects.all()
    # specify serializer to be used

    serializer_class = ModuleSerializer

class ModuleTopicSet(viewsets.ModelViewSet):
    # Define queryset
    queryset = Module.objects.all()
    # specify serializer to be used

    serializer_class = ModuleTopicSerializer

class TopicViewSet(viewsets.ModelViewSet):
     # Define queryset
    queryset = Topic.objects.all()
    # specify serializer to be used

    serializer_class = TopicSerializer

class LanguageViewSet(viewsets.ModelViewSet):
     # Define queryset
    queryset = Language.objects.all()
    # specify serializer to be used

    serializer_class = LanguageSerializer

class LessonViewSet(viewsets.ModelViewSet):
     # Define queryset
    queryset = Lesson.objects.all()
    # specify serializer to be used

    serializer_class = LessonSerializer


class TextBlockViewSet(viewsets.ModelViewSet):
     # Define queryset
    queryset = TextBlock.objects.all()
    # specify serializer to be used

    serializer_class = TextBlockSerializer


# class UserProfileViewSet(viewsets.ModelViewSet):

#     queryset_2 = UserProfile.objects.all()

#     serializer_class_1 = UserProfileSerializer

# class UserSubmissionViewSet(viewsets.ModelViewSet):
#     queryset_3 = UserSubmission.objects.all()

#     serializer_class_2 = UserSubmissionSerializer

# class AuthUserViewSet(viewsets.ModelViewSet):
#     queryset_3 = AuthUser.objects.all()

#     serializer_class_3 = AuthUserSerializer