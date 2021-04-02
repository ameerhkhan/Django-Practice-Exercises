from django.urls import path, include
from . import views
from . import simpleexample, line_example


urlpatterns = [
    path('', views.index, name='index'),
    path('int:fruit_id', views.detail, name='detail'),
    path('SimpleExample/', include('django_plotly_dash.urls')),
    path('LineExample/', include('django_plotly_dash.urls')),
]
