"""Circle serializers"""
#Django rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#models from cricle
from .models import Circle
class CircleSerializer(serializers.Serializers):
    """Circle serializers"""
    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()
    members_limit = serializers.IntegerField()

class CreateCircleSerializer(serializers.Serializer):
    name = serializers.ChardField(max_length=140)
    slug_name = serializers.SlugField(max_length=40,validators=[UniqueValidator(queryset=Circle.objects.all())])
    about = serializers.ChardField(max_length=255, required=False)

    def create(self,data):
        return Circle.objects.create(**data)
