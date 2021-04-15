from django.shortcuts import render, redirect
import requests
import json

# Create your views here.
def index(req):
    return render(req, 'index.html')


def byId(req):
    if  req.method == 'POST':
        post = req.POST or None
        if post:
            poke_id = post['id-input']
            text = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(poke_id)).text
            data = json.loads(text)
            with open('test.json', 'w') as f:
                json.dump(data, f, indent='    ')
        else:
            return redirect('index')
    return render(req, 'byid.html')