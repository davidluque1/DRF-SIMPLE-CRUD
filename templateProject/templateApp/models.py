from django.db import models


class GraphicsCard(models.Model):

	manufacturer = models.CharField(max_length=50) ## ex Nvidia, ATI
	model = models.CharField(max_length=50) ## ex GTX-1080
	
	minimumWatts = models.FloatField()

	def __str__(self):
		return str(self.id) + self.manufacturer + self.model
