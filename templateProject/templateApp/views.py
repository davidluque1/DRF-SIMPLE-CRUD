from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GraphicsCardSerializer
from .models import GraphicsCard

class GraphicsCardViewSet(viewsets.ModelViewSet):

	serializer_class = GraphicsCardSerializer
	queryset = GraphicsCard.objects.all()
