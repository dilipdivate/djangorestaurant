
from rest_framework import serializers
from menu.models import Menu
from django.contrib.auth.hashers import make_password
from user.models import User
# from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    # menus = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Menu.objects.all()
    # )
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    confirmPassword = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password',
                  'confirmPassword', 'firstName', 'middleName', 'lastName', 'mobile', 'intro', 'is_vendor', 'is_chef', 'is_agent',  'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = User.objects.create_user(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            firstName=self.validated_data['firstName'],
            middleName=self.validated_data['middleName'],
            lastName=self.validated_data['lastName'],
            mobile=self.validated_data['mobile'],
            # is_admin=self.validated_data['is_admin'],
            # is_staff=self.validated_data['is_staff'],
            is_vendor=self.validated_data['is_vendor'],
            is_chef=self.validated_data['is_chef'],
            is_agent=self.validated_data['is_agent'],
            intro=self.validated_data['intro'],
            profile=self.validated_data['profile'],
        ),
        password = self.validated_data['password']
        confirmPassword = self.validated_data['confirmPassword']
        if password != confirmPassword:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        # user.set_password(password)
        # # user.password = make_password('password')
        # user.save()
        # To Create Token
        # token = Token.objects.create(user=user)
        # print(token)
        return user

    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         email=validated_data['email'],
    #         username=validated_data['username'],
    #     ),
    #     # password = validated_data['password']
    #     # confirmPassword = validated_data['confirmPassword']
    #     # if password != confirmPassword:
    #     #     raise serializers.ValidationError(
    #     #         {'password': 'Passwords must match.'})
    #     # user.set_password(password)
    #     # # user.password = make_password('password')
    #     # user.save()
    #     # To Create Token
    #     Token.objects.create(user=user)
    #     return user

# Login Serializer


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    # def validate(self, data):
    #     user = authenticate(**data)
    #     if user and user.is_active:
    #         return user
    #     raise serializers.ValidationError("Incorrect Credentials")
