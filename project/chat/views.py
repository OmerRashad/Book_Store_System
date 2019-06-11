# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.shortcuts import render,get_object_or_404, redirect
from .models import Word
from django.http import HttpResponse
from django.views.generic import DetailView,ListView

from .models import Word

def index(request):
    word = Word.objects.order_by('-count')
    return render(request, 'chat/index.html', {'Word':word})


def room(request, room_name,search = None):
    if search:
        word , created = Word.objects.get_or_create(roomName = search)
        if word:
            counter = word.count + 1
            Word.objects.filter(roomName = search).update(count = counter)
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name))
        })

def view_detail(request,search):
    # searchWord = request.POST.get('room-name-input')
    request.session['searchWord'] = search

    return redirect('room')

class trendingRoomNames(ListView):
    model = Word
    template_name = 'chat/index.html'
    context_object_name = 'Word'
