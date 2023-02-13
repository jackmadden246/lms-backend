from django.contrib import admin
from . models import * 

admin.site.register(Language)
admin.site.register(Module)
admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(CodeExercise)
admin.site.register(TextBlock)