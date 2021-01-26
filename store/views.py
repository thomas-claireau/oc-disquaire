"""Views of the Store's app

    Functions:
            index
            listing
            detail
            search
    """

from django.shortcuts import render
from store.models import Album


def index(request):
    """Initial route (/) of the app

        Args:
                request (object): Django's request

        Returns:
                HttpResponse: Django's response
        """
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    context = {"albums": albums}

    return render(request, "store/index.html", context)


def listing(request):
    """Route /store of the app

        Args:
                request (object): Django's request

        Returns:
                HttpResponse: Django's response
        """
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    context = {"albums": albums}
    return render(request, "store/listing.html", context)


def detail(request, album_id):
    """View detail of the app

        Args:
                request (object): Django's request
                album_id (int): Id of album

        Returns:
                HttpResponse: Django's response
        """
    album = Album.objects.get(pk=album_id)

    context = {
        "album_title": album.title,
        "thumbnail": album.picture,
        "artists_name": ", ".join([artist.name for artist in album.artists.all()]),
    }

    return render(request, "store/detail.html", context)


def search(request):
    """Route /search by query of the app

        Args:
                request (object): Django's request

        Returns:
                HttpResponse: Django's response
        """

    query = request.GET.get('query')

    albums = Album.objects.filter(title__icontains=query)

    if not albums:
        albums = Album.objects.filter(artists__name__icontains=query)

    context = {"albums": albums}
    return render(request, "store/search.html", context)
