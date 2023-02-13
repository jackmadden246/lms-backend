from rest_framework import serializers
from Rest_api_app.models import CodeExercise, Module, Topic, Language, TextBlock, Lesson

class CodeExerciseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    expected_output = serializers.CharField(max_length= 60)

    class Meta:
        model = CodeExercise
        fields = ('id', 'expected_output',)

    def create(self, validated_data):
        """ Create and return a new Code Exercise instance, given the validated_data
        """
        return CodeExercise.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Code Exercise instance, given the validated data
        """
        instance.id = validated_data.get('id', instance.id)
        instance.expected_output = validated_data.get('expected_output', instance.expected_output)


class ModuleSerializer(serializers.ModelSerializer):
        module_name = serializers.CharField(max_length= 200)

        class Meta:
            model = Module
            fields = ('module_name',)

        def create(self, validated_data):
            """ Create and return a new Module instance, given the validated_data
            """
            return Module.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing Module instance, given the validated data
            """

            instance.module_name = validated_data.get('module_name', instance.module_name)
 

class ModuleLanguageSerializer(serializers.ModelSerializer):
        language_id = serializers.IntegerField(read_only = True)
       
        class Meta:
            model = Module
            fields = ('language_id',)

      
        def create(self, validated_data):
            """ Create and return a new Module instance, given the validated_data
            """
            return Module.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing Module instance, given the validated data
            """

            instance.language_id = validated_data.get('language_id', instance.language_id)


class LanguageModuleSerializer(serializers.ModelSerializer):
    language_name_field = ModuleLanguageSerializer(read_only = True)

    class Meta:
            model = Language
            fields = ('language_name_field',)

    def create(self, validated_data):
            """ Create and return a new Language instance, given the validated_data
            """
            return Language.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Language instance, given the validated data
            """

            instance.language_name_field = validated_data.get('language_name_field', instance.language_name_field)

class LanguageSerializer(serializers.ModelSerializer):
     id = serializers.IntegerField(read_only = True)
     language_name = serializers.CharField(max_length = 300)

     class Meta:
            model = Language
            fields = ('id','language_name',)

     def create(self, validated_data):
            """ Create and return a new Language instance, given the validated_data
            """
            return Language.objects.create(**validated_data)

     def update(self, instance, validated_data):
            """
            Update and return an existing Language instance, given the validated data
            """

            instance.id = validated_data.get('id', instance.id)
            instance.language_name = validated_data.get('language_name', instance.language_name)

class TopicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)

    class Meta:
            model = Topic
            fields = ('id',)

    def create(self, validated_data):
            """ Create and return a new Topic instance, given the validated_data
            """
            return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Topic instance, given the validated data
            """

            instance.id = validated_data.get('id', instance.id)

class ModuleTopicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)

    class Meta:
            model = Module
            fields = ('id',)

    def create(self, validated_data):
            """ Create and return a new Module instance, given the validated_data
            """
            return Module.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Module instance, given the validated data
            """

            instance.module_id = validated_data.get('module_id', instance.module_id)

class TopicModuleSerializer(serializers.ModelSerializer):
    topic_id_field = ModuleTopicSerializer(many = True)

    class Meta:
            model = Topic
            fields = ('topic_id_field',)

    def create(self, validated_data):
            """ Create and return a new Topic instance, given the validated_data
            """
            return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Topic instance, given the validated data
            """

            instance.topic_id_field = validated_data.get('topic_id_field', instance.topic_id_field)


class LessonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)

    class Meta:
            model = Lesson
            fields = ('id',)

    def create(self, validated_data):
            """ Create and return a new Lesson instance, given the validated_data
            """
            return Lesson.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Lesson instance, given the validated data
            """

            instance.id = validated_data.get('id', instance.id)

class LessonTopicSerializer(serializers.ModelSerializer):
    topic_id = serializers.IntegerField(read_only = True)

    class Meta:
            model = Lesson
            fields = ('topic_id',)

    def create(self, validated_data):
            """ Create and return a new Lesson instance, given the validated_data
            """
            return Lesson.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Lesson instance, given the validated data
            """

            instance.topic_id = validated_data.get('topic_id', instance.topic_id)

class TopicLessonSerializer(serializers.ModelSerializer):
        topic_field = LessonTopicSerializer(read_only = True)

        class Meta:
                    model = Topic
                    fields = ('module_field',)

        def create(self, validated_data):
                    """ Create and return a new Topic instance, given the validated_data
                    """
                    return Topic.objects.create(**validated_data)

        def update(self, instance, validated_data):
                    """
                    Update and return an existing Topic instance, given the validated data
                    """

                    instance.module_field = validated_data.get('module_field', instance.module_field)

            

class TextBlockSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    text = serializers.CharField(max_length = 300)
    format = serializers.IntegerField(read_only = True)

    class Meta:
            model = TextBlock
            fields = ('id', 'text', 'format',)

        
    def create(self, validated_data):
            """ Create and return a new Text Block instance, given the validated_data
            """
            return TextBlock.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Text Block instance, given the validated data
            """

            instance.id = validated_data.get('id', instance.id)
            instance.text = validated_data.get('text', instance.text)
            instance.format = validated_data.get('format', instance.format)

class TextBlockLessonSerializer(serializers.ModelSerializer):
    lesson = serializers.CharField(max_length = 400)

    class Meta:
            model = TextBlock
            fields = ('lesson',)
    
    def create(self, validated_data):
            """ Create and return a new Text Block instance, given the validated_data
            """
            return TextBlock.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Text Block instance, given the validated data
            """

            instance.lesson = validated_data.get('lesson', instance.lesson)
            
class TextBlockLessSerializer(serializers.ModelSerializer):
    lesson_field = TextBlockLessonSerializer(read_only = True)

    class Meta:
            model = Lesson
            fields = ('lesson_field',)

    def create(self, validated_data):
            """ Create and return a new Lesson instance, given the validated_data
            """
            return Lesson.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Lesson instance, given the validated data
            """

            instance.lesson_field = validated_data.get('lesson_field', instance.lesson_field)

class TextBlockExerciseSerializer(serializers.ModelSerializer):
    exercise = serializers.CharField(max_length = 300)

    class Meta:
            model = TextBlock
            fields = ('exercise',)

    def create(self, validated_data):
            """ Create and return a Text Block instance, given the validated_data
            """
            return TextBlock.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Text Block instance, given the validated data
            """

            instance.exercise = validated_data.get('exercise', instance.exercise)

class TextBlockCodeSerializer(serializers.ModelSerializer):
    exercise_field = TextBlockExerciseSerializer(read_only = True)

    class Meta:
            model = CodeExercise
            fields = ('exercise_field',)

    def create(self, validated_data):
            """ Create and return a Code Exercise instance, given the validated_data
            """
            return CodeExercise.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
            Update and return an existing Code Exercise instance, given the validated data
            """

            instance.exercise_field = validated_data.get('exercise_field', instance.exercise_field)