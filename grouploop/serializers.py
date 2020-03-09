from rest_framework import serializers
from .models import Circle, User


class CircleSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Circle
        fields = ('id', 'title', 'description', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    circle = CircleSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'github', 'linkedin',
                  'twitter', 'instagram', 'facebook', 'circle')
