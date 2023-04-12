from django.db import models
from django.db.models import CASCADE

char_max_length = 200


class Composer(models.Model):
    name = models.CharField(max_length=char_max_length)


class Genre(models.Model):
    name = models.CharField(max_length=char_max_length)


class AuthorOfText(models.Model):
    name = models.CharField(max_length=char_max_length)


class Performer(models.Model):
    name = models.CharField(max_length=char_max_length)


class Artwork(models.Model):
    name = models.CharField(max_length=char_max_length)
    composers = models.ManyToManyField(Composer, blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True, null=True)
    authors_of_text = models.ManyToManyField(AuthorOfText, blank=True, null=True)


class Performance(models.Model):
    artworks = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    performers = models.ManyToManyField(Performer)


class Record(models.Model):
    name = models.CharField(max_length=char_max_length)
    performers = models.ManyToManyField(Performance)

