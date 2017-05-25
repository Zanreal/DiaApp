# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    """Category Model."""
    name = models.CharField(u'Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(u'Beschreibung', blank=True)

    class Meta:
        verbose_name = u'Kategorie'
        verbose_name_plural = u'Kategorien'

    def __unicode__(self):
        return self.name

class Insulin(models.Model):
    WERT_GUT = 1
    WERT_MITTEL = 2
    WERT_SCHLECHT = 3
    WERTE = (
        (WERT_GUT, u'Gut'),
        (WERT_MITTEL, u'Mittel'),
        (WERT_SCHLECHT, u'Schlecht')
    )
    """Insulin Model."""
    title = models.TextField(u'Titel', max_length=255)
    blutwert = models.IntegerField(u'Blutwert')
    slug = models.SlugField(unique=True)
    #datum = models.DateField(U'Datum', auto_now=True)
    #uhrzeit = models.TimeField(u'Uhrzeit', auto_now=True)
    restinsulin = models.IntegerField(u'Restinsulin')
    kohlenhydrate = models.IntegerField(u'Kohlenhydrate')
    vorschlagInsulin = models.IntegerField(u'Vorschlag wie viel Einheiten Insulin')
    kommentar = models.TextField(u'Kommentar',max_length=200)

    werteinschaetzung = models.SmallIntegerField(u'Wert Einschätzung', choices=WERTE, default=WERT_MITTEL)
    category = models.ManyToManyField(Category, verbose_name=u'Kategorien')
    author = models.ForeignKey(User, verbose_name=u'Author')
    date_created = models.DateTimeField(editable=True, auto_now=True)

    class Meta:
        verbose_name= u'Insulin Einheit'
        verbose_name_plural = u'Insuline Einheiten'
        ordering = ['-date_created']

    def __unicode__(self):
        return self.title
