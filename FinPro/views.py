from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
import requests
from bs4 import BeautifulSoup
import pandas as pd
from newsapi import NewsApiClient
from .models import StockData, UserInfo
from datetime import datetime
from datetime import timedelta
import twitter
import pandas as pd
import numpy as np


# Create your views here.
class LoginPageView(TemplateView):
    template_name = 'login.html'
    def post(self, request, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if UserInfo.objects.filter(username = username).exists():
                user = UserInfo.objects.filter(username = username)[0]
                if user.password == password:
                    print("HELLO")
                    return HttpResponseRedirect('/dashboard/?user=' + str(username))
        return render(request, 'login.html', context = None)

class SignupPageView(TemplateView):
    template_name = "register.html"
    def post(self, request, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if not (UserInfo.objects.filter(username = username).exists() or
                    UserInfo.objects.filter(email = email).exists()):
                UserInfo.objects.create(username = username, email = email, password = password)
                return HttpResponseRedirect('/dashboard/?user=' + str(username))
        return render(request, 'register.html', context = None)

class ProfilePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'profile.html', context=None)

class GlobalPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'maps.html', context = None)

class DashboardPageView(TemplateView):
    TICKER_DICT = {
        "Twitter": 'TWTR',
        "Facebook": 'FB',
        "Amazon": 'AMZN',
        "Apple": 'AAPL',
        "Tesla": 'TSLA',
        "Google": 'GOOGL',
        "Netflix": 'NFLX',
        "Microsoft": 'MSFT'
    }
    CEO_DICT = {
        "Twitter": "Jack Dorsey",
        "Facebook": "Mark Zuckerberg",
        "Amazon": "Jeff Bezos",
        "Apple": "Tim Cook",
        "Tesla": "Elon Musk",
        "Google": "Sundar Pichai",
        "Netflix": "Reed Hastings",
        "Microsoft": "Satya Nadela"
    }
    SECTOR_DICT = {
        "Twitter": "Tech",
        "Facebook": "Tech",
        "Amazon": "Consumer",
        "Apple": "Consumer",
        "Tesla": "Automobile",
        "Google": "Tech",
        "Netflix": "Tech",
        "Microsoft": "Tech"
    }

    def get(self, request, **kwargs):

        # Watchlist Data
        watchlist_json = []
        for stock in ["Twitter", "Facebook", "Amazon", "Netflix"]:
            data = {}
            data['name'] = stock
            data['ticker'] = self.TICKER_DICT[stock]
            watchlist_json.append(data)

        # Top Gainers and Loosers
        top_gainers_html = requests.get('https://finance.yahoo.com/gainers/', headers = {'User-agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(top_gainers_html.content, "html.parser")
        top_gainers = []
        for row in soup.table.find_all('tr')[1:]:
            a = row.find_all('td')
            symbol = a[0].text.replace("\n", "")
            name = a[1].text.replace("\n", "")
            price = a[2].text.replace("\n", "")
            change = a[4].text.replace("\n", "")
            top_gainers.append((symbol, name, price, change))

        top_losers_html = requests.get('https://finance.yahoo.com/losers/', headers = {'User-agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(top_losers_html.content, "html.parser")
        top_losers = []
        for row in soup.table.find_all('tr')[1:]:
            a = row.find_all('td')
            symbol = a[0].text.replace("\n", "")
            name = a[1].text.replace("\n", "")
            price = a[2].text.replace("\n", "")
            change = a[4].text.replace("\n", "")
            top_losers.append((symbol, name, price, change))

        top_gainers_json = []
        for stock in top_gainers[:4]:
            data = {}
            data['name'] = stock[1]
            data['ticker'] = stock[0]
            data['price'] = '$' + str(stock[2])
            data['change'] = stock[3]
            data['color'] = '#3FA75F'
            top_gainers_json.append(data)

        top_losers_json = []
        for stock in top_losers[:4]:
            data = {}
            data['name'] = stock[1]
            data['ticker'] = stock[0]
            data['price'] = '$' + str(stock[2])
            data['change'] = stock[3]
            data['color'] = '#da1e1e'
            top_losers_json.append(data)

        # Recent News Articles Data
        news_json = []
        newsapi = NewsApiClient(api_key='d5b51067a83741ba88a9fc8022ce2fe1')
        news = newsapi.get_top_headlines(country = 'us',
                                         category = 'business',
                                         page = 1)
        for article in news['articles']:
            data = {}
            if article['urlToImage'] is None:
                continue
            data['title'] = article['title']
            data['image'] = article['urlToImage']
            data['url'] = article['url']
            data['source'] = article['source']['name']
            data['content'] = article['content']
            news_json.append(data)

        context = {
            'username': request.GET.get('user'),
            'news': news_json[:5],
            'watchlist': watchlist_json,
            'top_gainers': top_gainers_json,
            'top_losers': top_losers_json
        }
        return render(request, 'dashboard.html', context = context)

class ChartUpdateView(TemplateView):
    def get(self, request, **kwargs):
        chart_type = request.GET.get('chart_type')
        return HttpResponse(2)

class CompanyPageView(TemplateView):
    TICKER_DICT = {
        "Twitter": "TWTR",
        "Facebook": "FB",
        "Amazon": "AMZN",
        "Apple": "AAPL",
        "Tesla": "TSLA",
        "Google": "GOOGL",
        "Netflix": "NFLX",
        "Microsoft": "MSFT"
    }
    CEO_DICT = {
        "Twitter": "Jack Dorsey",
        "Facebook": "Mark Zuckerberg",
        "Amazon": "Jeff Bezos",
        "Apple": "Tim Cook",
        "Tesla": "Elon Musk",
        "Google": "Sundar Pichai",
        "Netflix": "Reed Hastings"
    }
    SECTOR_DICT = {
        "Twitter": "Tech",
        "Facebook": "Tech",
        "Amazon": "Consumer",
        "Apple": "Consumer",
        "Tesla": "Automobile",
        "Google": "Tech",
        "Netflix": "Tech"
    }
    def get(self, request, **kwargs):

        organization = request.GET.get('org')
        username = request.GET.get('user')

        # News Articles Data
        news_json = []
        today = datetime.today().strftime('%Y-%m-%d')
        yesterday = (datetime.today() - timedelta(days = 10)).strftime('%Y-%m-%d')

        newsapi = NewsApiClient(api_key = 'd5b51067a83741ba88a9fc8022ce2fe1')
        news = newsapi.get_everything(q = organization,
                                      language = 'en',
                                      sources = 'reuters',
                                      sort_by = 'relevancy',
                                      from_param = yesterday,
                                      to = today,
                                      page = 1)
        for article in news['articles']:
            data = {}
            if article['urlToImage'] is None:
                continue
            data['title'] = article['title']
            data['image'] = article['urlToImage']
            data['url'] = article['url']
            data['source'] = article['source']['name']
            news_json.append(data)

        # Stocks OHLC and Volume Data
        stock_objects = StockData.objects.filter(symbol = self.TICKER_DICT[organization])
        stock_json = []
        volume_json = []
        for obj in stock_objects:
            stock_data = {}
            stock_data['DATE'] = obj.date
            stock_data['HIGH'] = np.round(obj.high, 2)
            stock_data['LOW'] = np.round(obj.low, 2)
            stock_data['OPEN'] = np.round(obj.open, 2)
            stock_data['CLOSE'] = np.round(obj.close, 2)
            stock_data['TURNOVER'] = np.round(obj.volume, 2)
            stock_json.append(stock_data)

            volume_data = []
            volume_data.append(obj.timestamp)
            volume_data.append(obj.volume)
            volume_json.append(volume_data)

        # Technical Indicators Data
        timestamps = []
        opens = []
        highs = []
        lows = []
        closes = []
        volumes = []
        for obj in stock_objects:
            timestamps.append(obj.timestamp)
            opens.append(np.round(obj.open, 2))
            highs.append(np.round(obj.high, 2))
            lows.append(np.round(obj.low, 2))
            closes.append(np.round(obj.close, 2))
            volumes.append(int(obj.volume))

        technical_charts_data = pd.DataFrame()
        technical_charts_data['timestamp'] = timestamps
        technical_charts_data['open'] = opens
        technical_charts_data['high'] = highs
        technical_charts_data['low'] = lows
        technical_charts_data['close'] = closes
        technical_charts_data['volume'] = volumes
        technical_charts_data.to_csv('./Finpro/assets/ohlc.csv', header = False, index = False)

        # Comparison Data
        watchlist_stocks = ["Twitter", "Facebook", "Amazon", "Netflix"]
        if organization not in watchlist_stocks:
            watchlist_stocks.append(organization)
        comparison_data = []
        for stock in watchlist_stocks:

            # Get the data
            stock_objects = StockData.objects.filter(symbol = self.TICKER_DICT[stock])
            comp_json = []
            for obj in stock_objects:
                comp_data = []
                comp_data.append(obj.timestamp)
                comp_data.append(obj.close)
                comp_json.append(comp_data)

            comparison_data.append(comp_json)

        # Twitter Data
        consumer_key = "VAv4Am1zyvKdJCVFEx371BCPL"
        consumer_secret = "7C3K5ahVU3AfuFzw8i2PxyoW43WbTUu8rBKFlqDZsFGLxteRlT"
        access_token = "746633234960752640-heriMLyGPKdNFS6xHpJu8xCOVss6PAM"
        access_token_secret = "AeiYZJXePoyoI46M4ymFRJLI84UmlVXY9sUiGD1A2qp8e"
        tweet = twitter.Api(consumer_key = consumer_key,
                            consumer_secret = consumer_secret,
                            access_token_key = access_token,
                            access_token_secret = access_token_secret)
        tweet_json = []
        results = tweet.GetSearch(
            raw_query = "q=" + organization + "&since=" + yesterday +
                      "&count=1000&result_type=popular")
        for tweet in range(len(results)):
            data = {}
            data['text'] = results[tweet].text
            data['id'] = results[tweet].id
            data['name'] = results[tweet].user.screen_name
            data['profile_image'] = results[tweet].user.profile_image_url
            tweet_json.append(data)

        # Recommendations
        recommendations_json = []
        for stock in list(self.TICKER_DICT.keys())[:4]:
            data = {}
            data['name'] = stock
            data['ticker'] = self.TICKER_DICT[stock]
            data['perc'] = np.random.choice(['80', '70', '90', '30', '60'])
            data['action'] = np.random.choice(['buy', 'sell'])
            recommendations_json.append(data)

        context = {
            'username': username,
            'news': news_json[:5],
            'stock_values': stock_json,
            'org_stock': self.TICKER_DICT[organization],
            'tweets': tweet_json[:10],
            'org_ceo': self.CEO_DICT[organization],
            'org_sector': self.SECTOR_DICT[organization],
            'volume_json': volume_json,
            'recommendations': recommendations_json,
            'comparison_stocks': watchlist_stocks,
            'comparison_data': comparison_data
        }
        return render(request, 'company-page.html', context)
