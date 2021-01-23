from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your models here.
ARTISTS = {
    'francis-cabrel': {'name': 'Francis Cabrel'},
    'lej': {'name': 'Elijay'},
    'rosana': {'name': 'Rosana'},
    'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}


ALBUMS = [
    {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
    {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
    {'name': 'Luna Nueva', 'artists': [
        ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]

# Create your views here.


def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)


def listing(request):
    album = ["<li>{}</li>".format(album["name"]) for album in ALBUMS]
    return HttpResponse("<h1>Store</h1><ul>{}</ul>".format("\n".join(album)))


def detail(request, album_id):
    album = ALBUMS[int(album_id)]

    return HttpResponse("Le nom de l'album est {}".format(album["name"]))


def search(request):
    query = request.GET.get("query")

    if not query:
        message = "Aucun artiste n'a été demandé"
    else:
        albums = [album for album in ALBUMS if query in " ".join(
            artist["name"] for artist in album["artists"])]

        if len(albums) == 0:
            message = "Aucun album trouvé"
        else:
            albums = ["<li>{}</li>".format(album["name"]) for album in albums]
            message = albums

    return HttpResponse(message)
