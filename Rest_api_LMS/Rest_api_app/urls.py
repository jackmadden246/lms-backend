from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

from Rest_api_app.views import (
    CodeExerciseViewSet, 
    ModuleLanguageViewSet, 
    LessonTopicViewSet,
    TextBlockExerciseViewSet,
    TextBlockLessonViewSet,
    ModuleViewSet,
    TopicViewSet,
    LanguageViewSet,
    LessonViewSet,
    TextBlockViewSet,
)

app_name = 'rest_api_app'


# Define the router path and viewset to be used 
router.register('LMS/CodeExercises', CodeExerciseViewSet, basename='code_exercises')
router.register('LMS/ModuleLanguages', ModuleLanguageViewSet, basename='module languages')
router.register('LMS/LessonTopics', LessonTopicViewSet, basename='lesson topics')
router.register('LMS/TextBlockExercises', TextBlockExerciseViewSet, basename='text block exercises')
router.register('LMS/TextBlockLessons', TextBlockLessonViewSet, basename='text block lessons')
router.register("LMS/Topics", TopicViewSet, basename = 'topics')
router.register("LMS/Lessons", LessonViewSet, basename = 'lessons')
router.register("LMS/Languages", LanguageViewSet, basename = 'languages')
router.register("LMS/Module", ModuleViewSet, basename = 'module')
router.register("LMS/TextBlock", TextBlockViewSet, basename = 'text_blocks')


urlpatterns = [
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
