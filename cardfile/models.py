from django.db import models
from django.db.models import CASCADE

char_max_length = 200


class Composers(models.Model):
    name = models.CharField(max_length=char_max_length)


class Genres(models.Model):
    name = models.CharField(max_length=char_max_length)


class AuthorsOfText(models.Model):
    name = models.CharField(max_length=char_max_length)


class Performers(models.Model):
    name = models.CharField(max_length=char_max_length)


class Artworks(models.Model):
    name = models.CharField(max_length=char_max_length)
    id_composers = models.ManyToManyField(Composers, blank=True, null=True)
    id_genres = models.ManyToManyField(Genres, blank=True, null=True)
    id_authors_of_text = models.ManyToManyField(AuthorsOfText, blank=True, null=True)


class Performances(models.Model):
    id_performances = models.IntegerField
    id_artworks = models.ForeignKey(Artworks, on_delete=models.CASCADE)
    id_performers = models.ManyToManyField(Performers)


class Records(models.Model):
    name = models.CharField(max_length=char_max_length)
    id_performers = models.ManyToManyField(Performances)

