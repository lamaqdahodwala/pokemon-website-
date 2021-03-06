from django.shortcuts import render, redirect
import requests
import django.http
from django.core.handlers.wsgi import WSGIRequest
import json

# Create your views here.
def index(req:WSGIRequest):
    return render(req, 'index.html')


def byId(req:WSGIRequest):
    if  req.method == 'POST':
        post = req.POST or None
        if post:
            poke_id = post['id-input']
            return redirect(req, 'pokemon.html')
        else:
            return redirect('index')
    return render(req, 'byid.html')

def findpokemon(req:WSGIRequest):
    id = req.GET.get('id-input')
    if id is None:
        return django.http.HttpResponse('Please provide an ID')
    else:
        return redirect(f'pokemon/{id}')

def findpokemonbyname(req:WSGIRequest):
    name = req.GET.get('name-input')
    if name is None:
        return django.http.HttpResponse("Please provide a name")
    else:
        data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
        idcont = json.loads(data.text)
        return redirect(f'pokemon/{idcont["id"]}')
    

def byName(req:WSGIRequest):
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
    return render(req, 'pokemon.html', {'abilities': abilities, 'basexp': basexp, 'name': name, 'moves':movenames})