from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
#ex: /app/
    path('', views.index, name='index'),
#ex: /app/2/
    path('<int:question_id>/', views.detail, name='detail'),
#ex: /app/2/results/
    path('<int:question_id>/results/', views.results, name='results'),
#ex: /app/2/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
