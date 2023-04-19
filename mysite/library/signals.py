from django.db.models.signals import post_save  
from django.contrib.auth.models import User    
from django.dispatch import receiver           
from .models import Profilis

# Sukūrus vartotoją automatiškai sukuriamas ir profilis.
@receiver(post_save, sender=User) # jeigu išsaugojamas User objektas, inicijuojama f-ja po dekoratoriumi
def create_profile(sender, instance, created, **kwargs): # instance yra ką tik sukurtas User objektas.
    if created:
        Profilis.objects.create(user=instance)
        print('KWARGS: ', kwargs)


# Pakoregavus vartotoją, išsaugomas ir profilis
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profilis.save()