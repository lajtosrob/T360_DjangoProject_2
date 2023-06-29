from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Character

# Create your views here.

"""
def index(request):
    c = Character.objects.get(name='Hero')
    context = {
        "character": c
    }
    return render(request, "characterapp/character_view.html", context)
"""

class CharacterDetailView(DetailView):
    model = Character

class CharacterListView(ListView):
    model = Character
    context_object_name = 'character'