from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

# register user
class registerserializer(serializers.Serializer):
     username=serializers.CharField()
     email=serializers.EmailField()
     password = serializers.CharField()
     # user already is exits are not
     def validate(self,data):
          if data['username']:
               if User.objects.filter(username=data['username']).exists():
                    raise serializers.ValidationError('Username is taken already')
          if data['email']:
               if User.objects.filter(email=data['email']).exists():
                    raise serializers.ValidationError('email is taken already')
          return data
     
     def create(self,validated_data):
           
          user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
          #  , password=validated_data.set_password(['password']))
          user.set_password(validated_data['password'])
          user.save()
          return validated_data

# login  user
class LoginSerializer(serializers.Serializer):
     username=serializers.CharField()
     password = serializers.CharField()


# members serializer
class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'