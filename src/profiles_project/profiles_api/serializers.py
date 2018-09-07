from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id','name','email','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        """ Crreates and returns new user"""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user