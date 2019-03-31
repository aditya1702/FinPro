from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(primary_key = True, max_length = 20)
    name = models.CharField(max_length = 50)
    stocks = models.TextField(blank = True)

    def __str__(self):
        return self.username


class StockData(models.Model):
    ids = models.IntegerField(primary_key = True, default = 0)
    symbol = models.CharField(max_length = 128)
    date = models.CharField(max_length = 128)
    open = models.FloatField(default = 0)
    high = models.FloatField(default = 0)
    low = models.FloatField(default = 0)
    close = models.FloatField(default = 0)
    volume = models.FloatField(default = 0)
    adj_close = models.FloatField(default = 0)
    volume_delta = models.FloatField(default = 0)
    cr = models.FloatField(default = 0)
    so = models.FloatField(default = 0)
    sma = models.FloatField(default = 0)
    ema = models.FloatField(default = 0)
    macd = models.FloatField(default = 0)
    boll = models.FloatField(default = 0)
    boll_ub = models.FloatField(default = 0)
    boll_lb = models.FloatField(default = 0)
    rsi = models.FloatField(default = 0)
    tr = models.FloatField(default = 0)
    atr = models.FloatField(default = 0)
    dma = models.FloatField(default = 0)
    trix = models.FloatField(default = 0)
    vr = models.FloatField(default = 0)
    wr = models.FloatField(default = 0)
    timestamp = models.IntegerField(default = 0)

    def __str__(self):
        return self.symbol

class SectorData(models.Model):
    symbol = models.CharField(primary_key = True, max_length = 128)
    name = models.TextField()
    sector = models.TextField()

    def __str__(self):
        return (self.symbol,self.sector)



