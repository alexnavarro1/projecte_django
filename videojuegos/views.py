from django.shortcuts import render, get_object_or_404
from .models import Game, Developer, Genre
from django.http import Http404

def index(request):
    games = Game.objects.order_by('-created_at')[:3]
    return render(request, 'index.html', {'games': games})

def game_list(request):
    games = Game.objects.order_by('-created_at')
    return render(request, 'game_list.html', {'games': games})

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'game_detail.html', {'game': game})

def developer_list(request):
    developers = Developer.objects.all()
    return render(request, 'developer_list.html', {'developers': developers})

def developer_detail(request, slug):
    developer = get_object_or_404(Developer, slug=slug)
    return render(request, 'developer_detail.html', {'developer': developer})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def genre_game_list(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    games = genre.game_set.order_by('-created_at')
    return render(request, 'genre_game_list.html', {'genre': genre, 'games': games})

def test_404(request):
    raise Http404()
