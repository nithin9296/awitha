from django.db import models

# Create your models here.


class profitandloss(models.Model):
	documentid = models.IntegerField(default=0)
	glcode = models.IntegerField(default=0)
	gldescription = models.CharField(max_length=30)
	amount = models.IntegerField(default=0)

	def __str__(self):
		return str(self.gldescription)


class balancesheet(models.Model):
	documentid = models.IntegerField(default=0)
	glcode = models.IntegerField(default=0)
	gldescription = models.CharField(max_length=30)
	amount = models.IntegerField(default=0)

	def __str__(self):
		return str(self.gldescription)


