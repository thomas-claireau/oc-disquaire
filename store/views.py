"""Views of the Store's app

    Functions:
            index
            listing
            detail
            search
    """
from django.http import HttpResponse

from store.models import Album


def index(request):
    """Initial route (/) of the app

        Args:
                request (object): Django's request

        Returns:
                HttpResponse: Django's httpresponse
        """
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    album = ["<li>{}</li>".format(album) for album in albums]
    return HttpResponse("<h1>Index</h1><ul>{}</ul>".format("\n".join(album)))


def listing(request):
    """Route /store of the app

        Args:
                request (object): Django's request

        Returns:
                HttpResponse: Django's httpresponse
        """
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    album = ["<li>{}</li>".format(album) for album in albums]
    return HttpResponse("<h1>Store</h1><ul>{}</ul>".format("\n".join(album)))


def detail(request, album_id):
    """View detail of the app

        Args:
                request (object): Django's request

        Returns:
                HttpResponse: Django's httpresponse
        """
    return HttpResponse('detail {}'.format(album_id))
    # return HttpResponse("Le nom de l'album est {}".format(album["name"]))


def search(request):
    """Route /search by query of the app

        Args:
                request (object): Django's request

        Returns:
                HttpResponse: Django's httpresponse
        """

    return HttpResponse("search")
