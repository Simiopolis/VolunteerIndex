from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email_address = models.CharField(max_length=50)
	phone_number = models.IntegerField(max_length=10)
	skill_description = models.CharField(max_length=200)

	def __unicode__(self):
		return self.first_name + self.last_name
