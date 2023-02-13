from django.db import models
from django.conf import settings

class Language(models.Model):
    language_name = models.TextField(max_length= 60)

class Module(models.Model):
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    module_name = models.TextField(max_length= 200)

class Topic(models.Model):
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)

class Lesson(models.Model):
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)

class CodeExercise(models.Model):
    expected_output = models.TextField(max_length= 60)

class TextBlock(models.Model):
    text = models.TextField(max_length= 300)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_textblocks')
    exercise = models.ForeignKey(CodeExercise,  on_delete=models.CASCADE)
    format = models.IntegerField()







