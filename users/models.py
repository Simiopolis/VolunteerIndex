from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	insert_date = models.DateTimeField('date inserted')

	def __unicode__(self):
		return self.first_name
