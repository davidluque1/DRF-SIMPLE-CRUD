from rest_framework import serializers
from .models import GraphicsCard

class GraphicsCardSerializer(serializers.ModelSerializer):

	class Meta:
		model = GraphicsCard
		fields = ['manufacturer', 'model', 'minimumWatts']