from django.urls import path
from recommendation.views import task_recommendation_view, music_recommendation_view

urlpatterns = [
    path('task_recommendation/', task_recommendation_view, name='task_recommendation'),
    path('music_recommendation/', music_recommendation_view, name='music_recommendation'),
]
