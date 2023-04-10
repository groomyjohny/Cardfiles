from django.db import models

char_max_length = 200

class Composers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=char_max_length)


class Genres(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=char_max_length)


class AuthorsOfText(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=char_max_length)


class Performers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=char_max_length)


class Records(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=char_max_length)


class Artworks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=char_max_length)
    id_composers = models.ForeignKey




