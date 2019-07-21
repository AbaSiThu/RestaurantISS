from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:restaurant_id>/', views.category, name='category'),

    path('<int:restaurant_id>/detail/', views.detail, name='detail'),
   
    path('<int:restaurant_id>/vote/', views.vote, name='vote'),

    path('<int:review_id>/reply/', views.reply, name='replt'),

    path('<int:review_id>/commentData/', views.commentData, name='commentData'),
]