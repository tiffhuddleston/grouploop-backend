from rest_framework import serializers
from .models import Circle, Member


class CircleSerializer(serializers.ModelSerializer):
    member = serializers.HyperlinkedRelatedField(
        view_name='member_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Circle
        fields = ('id', 'title', 'description', 'member')


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    circle = CircleSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Member
        fields = ('id', 'name', 'github', 'linkedin',
                  'twitter', 'instagram', 'facebook', 'circle')
