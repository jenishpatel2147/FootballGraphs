from rest_framework import serializers
from .models import FootGraph

class FootGraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootGraph
        fields = ('id', 'per', 'league', 'position')
 