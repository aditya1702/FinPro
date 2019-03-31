from django.conf.urls import url
from FinPro import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^dashboard', views.DashboardPageView.as_view(), name = 'dashboard'),
    url(r'^maps', views.GlobalPageView.as_view(), name = 'maps'),
    url(r'^company-page', views.CompanyPageView.as_view(), name = 'company-page'),
    url(r'^login', views.LoginPageView.as_view(), name = 'login'),
    url(r'^chart-update', views.ChartUpdateView.as_view(), name = 'chart-update')
]
