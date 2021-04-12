"""Circle serializers"""

from rest_framework import serializers

class CircleSerializer(serializers.Serializers):
    """Circle serializers"""
    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()
    members_limit = serializers.IntegerField()