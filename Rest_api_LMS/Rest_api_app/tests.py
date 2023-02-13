from django.test import TestCase
from Rest_api_app.models import *

class LanguageTestCase(TestCase):

    def test_if_this_works(self):
        Test = CodeExercise.objects.create(id = 1, expected_output = "hello jack")
        test_output = Test.expected_output
        id_check = Test.id

    def testing(self):
        test = self.test_if_this_works()
        # CodeExercise.objects.create(id = 2, expected_output = "I am the champion")
        self.assertEqual(test.test_output, "hello jack")
        # self.assertEqual(I_am_the_champion, "I am the champion")

class ModuleTestCase(TestCase):
    def db_2(self):
         Test2 = Module.objects.create(module_name = "Java")
         test2_output = Test2.module_name
    def test_time(self):
        test_2 = self.db_2()
        self.assertEqual(test_2.test2_output, 'Hello')