from django.shortcuts import render
import random

def index(request):
    backgrounds = [
        'anime/images/background1.jpg',
        'anime/images/background2.jpg',
        'anime/images/background3.jpg'
    ]
    background = random.choice(backgrounds)
    return render(request, 'anime/index.html', {'background': background})
