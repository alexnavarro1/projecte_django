from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.game_list, name='games-list'),
    path('games/<slug:slug>/', views.game_detail, name='games-detail'),
    path('developers/', views.developer_list, name='developers-list'),
    path('developers/<slug:slug>/', views.developer_detail, name='developers-detail'),
    path('genres/', views.genre_list, name='genres-list'),
    path('genres/<slug:slug>/', views.genre_game_list, name='genre-games'),
    path('404/', views.test_404, name='test-404'),
]
