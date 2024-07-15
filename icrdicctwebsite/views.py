from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context ={
        'title' : 'International Conference on Research and Development in Information, Communication and Computing Technologies - 2025 (ICRDICCT’ 2025)',
        'description' : 'Join ICRDICCT’2025 on April 4th & 5th, 2025, hosted by E.G.S. Pillay Engineering College, India. Explore innovations in ICT through paper presentations, exhibitions, and industry interactions. Engage with researchers, professionals, and students advancing technology and management fields.'
    }
    return render(request, 'pages/index.html', context)

