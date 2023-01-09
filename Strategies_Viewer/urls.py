from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='strategies_home'),
    path('chart', views.chart_view, name='chart_view'),
    # path('about/', views.about, name='about'),
]
