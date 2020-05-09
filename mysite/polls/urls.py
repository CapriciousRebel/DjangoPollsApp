from django.urls import path

from . import views

# set namespace polls
app_name = 'polls'

# Map urls on polls/ to their views
urlpatterns = [
    # polls/
    path('', views.IndexView.as_view(), name='index'),
    # polls/<question_id>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # polls/<question_id>/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # polls/<question_id>/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
