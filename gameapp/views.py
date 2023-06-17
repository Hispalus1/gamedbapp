from django.shortcuts import render
from django.views.generic import DetailView
from .models import Game, Hodnoceni, Developer


def index(request):
    context = {
        'nadpis': 'Nejnovější Hry',
        'nadpis2': 'Nejlépe hodnocené',
        'games': Game.objects.order_by('-datum')[:3],
        'pocet': Game.objects.all().count(),
        'gamez': Game.objects.order_by('hodnoceni')[:3]

    }
    return render(request, 'index.html', context=context)


def games(request):
    context = {
        'games': Game.objects.all(),
    }
    return render(request, 'seznam.html', context=context)


def developer(request):
    context = {
        'developers': Developer.objects.all(),
    }
    return render(request, 'seznamD.html', context=context)


class GameDetailView(DetailView):
    model = Game
    template_name = 'hry/detail.html'
    context_object_name = 'game'


class DeveloperDetailView(DetailView):
    model = Developer
    template_name = 'dev/detail.html'
    context_object_name = 'dev'
