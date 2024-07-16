import os
import json
from django.shortcuts import render
from django.conf import settings

def index(request):

    json_file_path = os.path.join(settings.BASE_DIR, 'icrdicctwebsite', 'json', 'dataset', 'hero_items.json')

    # Read data from JSON file
    with open(json_file_path, 'r') as file:
        hero_items = json.load(file)

   
    context ={

        'hero_items': hero_items,

        'title' : 'International Conference on Research and Development in Information, Communication and Computing Technologies - 2025 (ICRDICCT’ 2025)',
        'description' : 'Join ICRDICCT’2025 on April 4th & 5th, 2025, hosted by E.G.S. Pillay Engineering College, India. Explore innovations in ICT through paper presentations, exhibitions, and industry interactions. Engage with researchers, professionals, and students advancing technology and management fields.'
    }

    return render(request, 'pages/index.html', context)

