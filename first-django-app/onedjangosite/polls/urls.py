from django.urls import path

#removed "from ." to get rid of a warning/error.
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:question_id>/', views.detail, name='detail'), #correspond to detail function created in Views.py
    # path('<int:question_id>/results/', views.results, name='results'), #same as above.
    # path('<int:question_id>/vote/', views.vote, name='vote')
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #Note that the name of the matched pattern in the path strings of the second and third patterns has changed from <question_id> to <pk>.
]