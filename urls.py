from django.conf.urls import url
from StockStories import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.IndexPageView.as_view(), name='index'),
    url(r'^login',views.LoginPageView.as_view(), name='login'),
    url(r'^stockstories', views.HomePageView.as_view(), name='home'),
    url(r'^signout', views.SignOutPageView.as_view(), name='signout'),
    url(r'^crypto', views.CryptoPageView.as_view(), name='crypto'),
    url(r'^user', views.UserPageView.as_view(), name='user'),
    url(r'^global', views.GlobalPageView.as_view(), name='global'),
    url(r'^about', views.AboutUsPageView.as_view(), name='about'),
    url(r'^explore', views.ExplorePageView.as_view(), name='explore'),
]
