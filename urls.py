from django.conf.urls import url
import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^login',views.LoginPageView.as_view(), name = 'login'),
    # url(r'^stockstories', views.HomePageView.as_view(), name = 'home'),
    # url(r'^signout', views.SignOutPageView.as_view(), name = 'signout'),
    # url(r'^crypto', views.CryptoPageView.as_view(), name = 'crypto'),
    url(r'^user', views.DashboardPageView.as_view(), name = 'user'),
    url(r'^global', views.GlobalPageView.as_view(), name = 'maps'),
    # url(r'^about', views.AboutUsPageView.as_view(), name = 'about'),
    url(r'^explore', views.CompanyPageView.as_view(), name = 'company-page'),
]
