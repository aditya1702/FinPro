from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SearchForm
from django.http import HttpResponseRedirect, HttpResponse
from newsapi import NewsApiClient
import json
from .models import HistoricalData
from .models import CryptoHistoricalData
from django.db import connection
import datetime
from datetime import datetime
from datetime import timedelta 
import itertools
import twitter

# Create your views here.
class IndexPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class LoginPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login.html', context=None)

class HomePageView(TemplateView):
     def get(self, request, **kwargs):
        return render(request, 'stockstories.html', context=None)

class CryptoPageView(TemplateView):
 def get(self, request, **kwargs): 
        NewsJson=[]

        if request.GET.get('news_from') is not None:
            date = datetime.strptime(request.GET.get('news_from'), "%Y-%m-%d")
            date1 = datetime.strftime(date - timedelta(days=2), "%Y-%m-%d")
            date2 = datetime.strftime(date + timedelta(days=2), "%Y-%m-%d")
            print(date1)
            print(date2)
        else:
            date1 = request.GET.get('news_from')
            date2 = request.GET.get('news_from')
        
        newsapi = NewsApiClient(api_key='* API Key Here *')
        news = newsapi.get_everything(q=request.GET.get('org'),language='en', sources=' * news sources here *', 
                                        sort_by='relevancy', from_parameter=date1, to=date2, page=1)
        for article in news['articles']:
            data= {}
            data['title'] = article['title']
            data['url'] = article['url']
            data['source'] = article['source']['name']
            NewsJson.append(data)
                       
        StockJson = []
        for obj in CryptoHistoricalData.objects.filter(crypto=request.GET.get('org')):
            data = {}
            data['timestamp'] = str(obj.date)
            data['open'] = obj.open
            data['high'] = obj.high
            data['low'] = obj.low
            data['close'] = obj.close
            data['volume'] = obj.volume
            StockJson.append(data)
        print(StockJson)
        
        consumer_key = "* API Key Here *"
        consumer_secret = "* API Key Here *"
        access_token = "* API Key Here *"
        access_token_secret = "* API Key Here *"
        tweet = twitter.Api(consumer_key=consumer_key,
                          consumer_secret=consumer_secret,
                          access_token_key=access_token,
                          access_token_secret= access_token_secret)
        TweetJson=[]

        if request.GET.get('news_from') is not None:
            results = tweet.GetSearch(
                        raw_query="q="+request.GET.get('org')+"&since="+request.GET.get('news_from')+
                        "&count=3&result_type=popular")
            for tweet in range(len(results)):
                data={}
                data['text'] = results[tweet].text
                data['name'] = results[tweet].user.screen_name
                data['url'] = results[0].urls[0].expanded_url
                TweetJson.append(data)

        context = {
            'news': NewsJson[:3], 
            'stock_values': StockJson,
            'org_stock': request.GET.get('org'),
            'chart_type': request.GET.get('chart_type'),
            'date': request.GET.get('news_from'),
            'tweet':TweetJson[:3]
        }
        return render(request, 'crypto.html', context)

class UserPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'user.html', context=None)

class GlobalPageView(TemplateView):
    def get(self, request, **kwargs):
        NewsJson=[]

        date2 = "2018-04-26"
        date1 = "2018-04-24"

        newsapi = NewsApiClient(api_key='* API Key Here *')
        news = newsapi.get_everything(q=request.GET.get('org'),language='en', sources=' * news sources here *', 
                                        sort_by='relevancy', from_parameter=date1, to=date2, page=1)
        print(news)
        for article in news['articles']:
            data= {}
            data['title'] = article['title']
            data['url'] = article['url']
            data['source'] = article['source']['name']
            NewsJson.append(data)

        consumer_key = "* API Key Here *"
        consumer_secret = "* API Key Here *"
        access_token = "* API Key Here *"
        access_token_secret = "* API Key Here *"
        tweet = twitter.Api(consumer_key=consumer_key,
                          consumer_secret=consumer_secret,
                          access_token_key=access_token,
                          access_token_secret= access_token_secret)
        TweetJson=[]

        if request.GET.get('org') is not None:
            results = tweet.GetSearch(
                        raw_query="q="+request.GET.get('org')+"&since="+date1+
                        "&count=3&result_type=popular")
            for tweet in range(len(results)):
                data={}
                data['text'] = results[tweet].text
                data['name'] = results[tweet].user.screen_name
                #data['url'] = results[0].urls[0].expanded_url
                TweetJson.append(data)

        context = {
            'news': NewsJson[:3], 
            'org': request.GET.get('org'),
            'date': date2,
            'tweet':TweetJson[:3]
        }
        return render(request, 'global.html', context)

class AboutUsPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'about.html', context=None) 

class ExplorePageView(TemplateView):
    def get(self, request, **kwargs): 
        NewsJson=[]
        
        if request.GET.get('news_from') is not None:
            date = datetime.strptime(request.GET.get('news_from'), "%Y-%m-%d")
            date1 = datetime.strftime(date - timedelta(days=2), "%Y-%m-%d")
            date2 = datetime.strftime(date + timedelta(days=2), "%Y-%m-%d")
            print(date1)
            print(date2)
        else:
            date1 = request.GET.get('news_from')
            date2 = request.GET.get('news_from')

        newsapi = NewsApiClient(api_key='"* API Key Here *"')
        news = newsapi.get_everything(q=request.GET.get('org'),language='en', sources=' * news sources here *', 
                                        sort_by='relevancy', from_parameter=date1, to=date2, page=1)
        for article in news['articles']:
            data= {}
            data['title'] = article['title']
            data['url'] = article['url']
            data['source'] = article['source']['name']
            NewsJson.append(data)

            
        StockJson = []
        for obj in HistoricalData.objects.filter(organization=request.GET.get('org')):
            data = {}
            data['timestamp'] = str(obj.date)
            data['open'] = obj.open
            data['high'] = obj.high
            data['low'] = obj.low
            data['close'] = obj.close
            data['volume'] = obj.volume
            StockJson.append(data)
        
        consumer_key = "* API Key Here *"
        consumer_secret = "* API Key Here *"
        access_token = "* API Key Here *"
        access_token_secret = "* API Key Here *"
        tweet = twitter.Api(consumer_key=consumer_key,
                          consumer_secret=consumer_secret,
                          access_token_key=access_token,
                          access_token_secret= access_token_secret)
        TweetJson=[]

        if request.GET.get('news_from') is not None:
            results = tweet.GetSearch(
                        raw_query="q="+request.GET.get('org')+"&since="+request.GET.get('news_from')+
                        "&count=3&result_type=popular")
            for tweet in range(len(results)):
                data={}
                data['text'] = results[tweet].text
                data['name'] = results[tweet].user.screen_name
                data['url'] = results[0].urls[0].expanded_url
                TweetJson.append(data)
        print(TweetJson)

        context = {
            'news': NewsJson[:3], 
            'stock_values': StockJson,
            'org_stock': request.GET.get('org'),
            'chart_type': request.GET.get('chart_type'),
            'date': request.GET.get('news_from'),
            'tweet':TweetJson[:3]
        }
        return render(request, 'explore.html', context)

class SignOutPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'signout.html', context=None)

class SingupPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'signup.html', context=None)
