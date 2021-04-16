from django.shortcuts import render, redirect
import requests
import django
import json

# Create your views here.
def index(req:django.core.handlers.wsgi.WSGIRequest):
    return render(req, 'index.html')


def byId(req:django.core.handlers.wsgi.WSGIRequest):
    if  req.method == 'POST':
        post = req.POST or None
        if post:
            poke_id = post['id-input']
            return redirect(req, 'pokemon')
        else:
            return redirect('index')
    return render(req, 'byid.html')

def byName(req:django.core.handlers.wsgi.WSGIRequest):
    if req.method == 'POST':
        post = req.POST or None
        if post:
            poke_id = post['name-input']
    return render(req, 'byname.html')

def pokemon(req, id):
    data = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(id))
    data = json.loads(data.text)
    abilities = data['abilities']
    abilities = [i['ability']['name'].title() for i in abilities]
    basexp = data['base_experience']
    name = data['forms'][0]['name'].title()
    moves = data['moves']
    movenames = [i['move']['name'] for i in moves]
    return render(req, 'pokemon.html', {'abilities': abilities, 'basexp': basexp, 'name': name, 'moves':moves})