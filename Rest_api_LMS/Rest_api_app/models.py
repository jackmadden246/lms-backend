from django.db import models

class CodeExercise(models.Model):
    description = models.TextField(max_length= 120)
    category = models.CharField(max_length= 50)
    expected_output = models.TextField(max_length= 60)

class AuthUser(models.Model):
    nearest_postcode = models.CharField(max_length=20)
    exercises = models.ManyToManyField(CodeExercise)

class UserProfile(models.Model):
    auth_user_id = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

class UserSubmission(models.Model):
    file_url = models.TextField(max_length= 60)
    code_exercise_id = models.OneToOneField(CodeExercise, on_delete=models.CASCADE)
    auth_user_id = models.ForeignKey(AuthUser, on_delete=models.CASCADE)