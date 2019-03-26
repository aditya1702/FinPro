from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class HistoricalData(models.Model):
	organization = models.CharField(max_length=20)
	date = models.DateField(auto_now_add=False)
	open = models.FloatField(default=0)
	close = models.FloatField(default=0)
	high = models.FloatField(default=0)
	low = models.FloatField(default=0)
	volume = models.IntegerField(default=0)
   
	def __str__(self):
		return self.organization

class RealTimeData(models.Model):
	organization = models.CharField(max_length=20)
	date = models.DateTimeField(auto_now_add=True)
	open = models.FloatField(default=0)
	close = models.FloatField(default=0)
	high = models.FloatField(default=0)
	low = models.FloatField(default=0)
	volume = models.IntegerField(default=0)

	def __str__(self):
		return self.organization

class NewsArchive(models.Model):
	headline = models.CharField(max_length=500)
	news_link = models.CharField(max_length = 500)
	organization = models.CharField(max_length =10)
	date = models.DateField(auto_now_add=False)

	def __str__(self):
		return self.headline

class CryptoHistoricalData(models.Model):
	crypto = models.CharField(max_length=20)
	market = models.CharField(max_length=10)
	date = models.DateField(auto_now_add=False)
	open = models.FloatField(default=0)
	high = models.FloatField(default=0)
	low = models.FloatField(default=0)	
	close = models.FloatField(default=0)
	volume = models.FloatField(default=0)
	market_Cap = models.FloatField(default=0)
	country_code = models.CharField(max_length=5, default='USA')

	def __str__(self):
		return self.crypto

class CryptoRealTimeData(models.Model):
	crypto = models.CharField(max_length=20)
	market = models.CharField(max_length=10)
	date = models.DateTimeField(auto_now_add=True)
	open = models.FloatField(default=0)
	high = models.FloatField(default=0)
	low = models.FloatField(default=0)	
	close = models.FloatField(default=0)
	volume = models.IntegerField(default=0)
	market_Cap = models.FloatField(default=0)
	country_code = models.CharField(max_length=5, default='USA')

	def __str__(self):
		return self.crypto

class StockExchangeData(models.Model):
	index = models.CharField(max_length=20)
	country = models.CharField(max_length=20)	
	status = models.CharField(max_length=10)
	value = models.FloatField(default=0)
	daily_change = models.FloatField(default=0)
	ytd_change = models.FloatField(default=0)
	year_change = models.FloatField(default=0)
	threeYear_change = models.FloatField(default=0)
	country_code = models.CharField(max_length=5)

	def __str__(self):
		return self.index