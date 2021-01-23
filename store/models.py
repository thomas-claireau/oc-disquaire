"""Models of Store's app

	Class:
		Artist
		Contact
		Album
		Booking
    """
from django.db import models


class Artist(models.Model):
    """Model Artist of the store's app

        Args:
                models (Object): Django's model

        Returns:
                String: Name of contact
        """
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    """Model Contact of the store's app

        Args:
                models (Object): Django's model

        Returns:
                String: Name of contact
        """
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    """Model Album of the store's app

        Args:
                models (Object): Django's model

        Returns:
                String: Title of album
        """
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist, related_name='albums')

    def __str__(self):
        return self.title


class Booking(models.Model):
    """Model Booking of the store's app

        Args:
                models (Object): Django's model

        Returns:
                String: Name of contact
        """
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name
