"""Views of the Store's app

    Functions:
            index
            listing
            detail
            search
    """

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from store.models import Album, Contact, Booking
from .forms import ContactForm, ParagraphErrorList


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
    albums_list = Album.objects.filter(available=True).order_by('-created_at')
    paginator = Paginator(albums_list, 9)
    page = request.GET.get("page")

    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)

    context = {
        "albums": albums,
        "pagination": paginator.num_pages > 1
    }
    return render(request, "store/listing.html", context)


def detail(request, album_id):
    """View detail of the app

        Args:
                request (object): Django's request
                album_id (int): Id of album

        Returns:
                HttpResponse: Django's response
        """
    album = get_object_or_404(Album, pk=album_id)

    context = {
        "album_id": album_id,
        "album_title": album.title,
        "thumbnail": album.picture,
        "artists_name": ", ".join([artist.name for artist in album.artists.all()]),
    }

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST, error_class=ParagraphErrorList)

        if form.is_valid():
            try:
                name = form.cleaned_data['name']
                email = form.cleaned_data["email"]

                contact = Contact.objects.filter(email=email)

                if not contact.exists():
                    contact = Contact.objects.create(
                        email=email,
                        name=name
                    )
                else:
                    contact = contact.first()

                album = get_object_or_404(Album, pk=album_id)
                booking = Booking.objects.create(album=album, contact=contact)

                album.available = False
                album.save()

                context = {
                    "album_title": album.title
                }

                return render(request, "store/merci.html", context)
            except IntegrityError:
                form.errors["internal"] = "Une erreur est survenue"

    context["form"] = form
    context["errors"] = form.errors.items()

    return render(request, "store/detail.html", context)


def search(request):
    """Route /search by query of the app

        Args:
                request (object): Django's request

        Returns:
                HttpResponse: Django's response
        """

    query = request.GET.get('query')
    albums = []

    if query:
        albums = Album.objects.filter(title__icontains=query)

        if not albums:
            albums = Album.objects.filter(artists__name__icontains=query)

    context = {"albums": albums}
    return render(request, "store/search.html", context)
