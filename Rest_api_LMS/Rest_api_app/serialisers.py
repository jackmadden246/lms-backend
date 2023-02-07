from rest_framework import serializers
from Rest_api_app.models import CodeExercise, AuthUser, UserProfile, UserSubmission

class CodeExerciseSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length= 120)
    category = serializers.CharField(max_length= 50)
    expected_output = serializers.CharField(max_length= 60)

    class Meta:
        model = CodeExercise
        fields = ('description', 'category', 'expected_output',)

    def create(self, validated_data):
        """ Create and return a new Code Exercise instance, given the validated_data
        """
        return CodeExercise.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Code Exercise instance, given the validated data
        """

        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.expected_output = validated_data.get('expected_output', instance.expected_output)

class UserExercisesSerializer(serializers.ModelSerializer):
    code_exercise_id = serializers.IntegerField(read_only = True)

    class Meta:
        model = UserSubmission
        fields = ('code_exercise_id',)

    def create(self, validated_data):
        """ Create and return a new User Submission instance, given the validated_data
        """
        return UserSubmission.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing User Submission instance, given the validated data
        """

        instance.file_url = validated_data.get('file_url', instance.file_url)
        instance.code_exercise_id = validated_data.get('code_exercise_id', instance.code_exercise_id)
        instance.auth_user_id = validated_data.get('auth_user_id', instance.auth_user_id)

class CodeExSerializer(serializers.ModelSerializer):
    id = UserExercisesSerializer(read_only = True)
    
    class Meta:
        model = CodeExercise
        fields = ('id',)
    
    def create(self, validated_data):
        """ Create and return a new User Submission instance, given the validated_data
        """
        return CodeExercise.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing User Submission instance, given the validated data
        """
        instance.id = validated_data.get('id', instance.id)

class AuthUserSerializer(serializers.ModelSerializer):
    nearest_postcode = serializers.CharField(max_length=20) 

    class Meta:
        model = AuthUser
        fields = ('nearest_postcode',)

    def create(self, validated_data):
        """ Create and return a new Auth User instance, given the validated_data
        """
        return AuthUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Auth User instance, given the validated data
        """

        instance.nearest_postcode = validated_data.get('nearest_postcode', instance.nearest_postcode)

class AuthExercisesSerializer(serializers.ModelSerializer):
        exercises = serializers.CharField(max_length = 100)

        class Meta:
            model = AuthUser
            fields = ('exercises',)

        def create(self, validated_data):
            """ Create and return a new Auth User instance, given the validated_data
        """
            return AuthUser.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
        Update and return an existing Auth User instance, given the validated data
            """
            instance.exercises = validated_data.get('exercises', instance.exercises)
    
class AuthExercisesSerializer(serializers.ModelSerializer):
    code_ex_id = AuthExercisesSerializer(many = True, read_only=True)

    class Meta:
            model = CodeExercise
            fields = ('id',)

    def create(self, validated_data):
            """ Create and return a new Code Exercise instance, given the validated_data
        """
            return CodeExercise.objects.create(**validated_data)

    def update(self, instance, validated_data):
            """
        Update and return an existing Code Exercise instance, given the validated data
            """
            instance.id = validated_data.get('id', instance.id)

class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)
    
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name',)

    def create(self, validated_data):
        """ Create and return a new User Profile instance, given the validated_data
        """
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing User Profile instance, given the validated data
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

class AuthID(serializers.ModelSerializer):
     id = serializers.IntegerField(read_only = True)

     class Meta:
        model = AuthUser
        fields = ('id',)
    
     def create(self, validated_data):
        """ Create and return a new User Profile instance, given the validated_data
        """
        return AuthUser.objects.create(**validated_data)

     def update(self, instance, validated_data):
        """ Update and return an existing User Profile instance, given the validated data
         """
        instance.id = validated_data.get('id', instance.id)

class ProfileID(serializers.ModelSerializer):
    auth_user_id = AuthID(many = True)

    class Meta:
        model = UserProfile
        fields = ('auth_user_id',)

    def create(self, validated_data):
        """ Create and return a new User Profile instance, given the validated_data
        """
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ Update and return an existing User Profile instance, given the validated data
         """
        instance.auth_user_id = validated_data.get('auth_user_id', instance.auth_user_id)

class UserSubmissionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    file_url = serializers.CharField(max_length= 60)
    auth_user_id = CodeExSerializer(many = True)

    class Meta:
        model = UserSubmission
        fields = ('id', 'file_url','auth_user_id',)


    def create(self, validated_data):
        """ Create and return a new User Profile instance, given the validated_data
        """
        return UserSubmission.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ Update and return an existing User Profile instance, given the validated data
         """
        instance.id = validated_data.get('id', instance.id)
        instance.file_url = validated_data.get('file_url', instance.file_url)
        instance.auth_user_id = validated_data.get('auth_user_id', instance.auth_user_id)


    
