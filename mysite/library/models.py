from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from datetime import date
from PIL import Image
from django.conf import settings

# ------------Stovyklavietės------------
class Camp(models.Model):
    name = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite poilsiavietės pavadinimą')
    summary = models.TextField('Aprašymas', max_length=1000, help_text='Trumpas stovyklavietės aprašymas', null=True)

    class Meta:
        verbose_name = 'Stovyklavietė'
        verbose_name_plural = 'Stovyklavietės'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Poilsiavietės - detalės', args=[str(self.id)])

# ------------Vaikų Stovyklos------------

class ChildrenCamp(models.Model):
    name = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite vaikų stovyklos pavadinimą')
    summary = models.TextField('Aprašymas', max_length=1000, help_text='Trumpas stovyklos aprašymas', null=True)
    dateFrom = models.DateField('Nuo', null=True)
    dateTo = models.DateField('Iki', null=True)
    capacity = models.IntegerField("Grupės dydis", help_text='Pasirinkite grupės dydį', null=True)

    class Meta:
        verbose_name = 'Vaikų stovykla'
        verbose_name_plural = 'Vaikų stovyklos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vaiku_stovyklos - detalės', args=[str(self.id)])

# ------------Suaugusiuju Stovyklos------------

class AdultCamp(models.Model):
    name = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite vaikų stovyklos pavadinimą')
    summary = models.TextField('Aprašymas', max_length=1000, help_text='Trumpas stovyklos aprašymas', null=True)
    dateFrom = models.DateField('Nuo', null=True)
    dateTo = models.DateField('Iki', null=True)
    capacity = models.IntegerField("Grupės dydis", help_text='Pasirinkite grupės dydį', null=True)

    class Meta:
        verbose_name = 'Suaugusiųjų stovykla'
        verbose_name_plural = 'Suaugusiųjų stovyklos'

# ----------------------------------------------

class CampInstance(models.Model):
    id = models.AutoField(primary_key=True, help_text='Poilsiavietės ID')
    camp = models.ForeignKey('Camp', on_delete=models.SET_NULL, null=True) 
    due_back = models.DateField('Rezervuota nuo', null=True, blank=True)
    unavailable = models.DateField('Rezervuota iki', null=True, blank=True)
    consumer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('t', 'Tvarkoma'),
        ('g', 'Galima rezervuoti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='g',
        help_text='Galima rezervuoti',
    )

    class Meta:
        ordering = ['due_back']
        verbose_name = 'Prieinamumas'
        verbose_name_plural = 'Prieinamumai'

    def __str__(self):
        return f'{self.id} ({self.camp.name})'
    
class CampReview(models.Model):
    camp = models.ForeignKey('camp', on_delete=models.SET_NULL, null=True, blank=True, related_name="comment")
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Atsiliepimas', max_length=2000)
    
    class Meta:
        verbose_name = "Atsiliepimas"
        verbose_name_plural = 'Atsiliepimai'
        ordering = ['-date_created']

class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.nuotrauka.path)
        if img.height > 225 or img.width > 225:
            output_size = (225, 225)
            img.thumbnail(output_size)
            img.save(self.nuotrauka.path)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    campsite = models.ForeignKey(Camp, on_delete=models.CASCADE)
    camp_instance = models.ForeignKey(CampInstance, on_delete=models.SET_NULL, null=True)
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}, {self.check_in}, {self.check_out}'

    

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

