from django import forms
from .models import Profilis, CampReview, Reservation, Camp
from django.contrib.auth.models import User
from django.forms import DateInput



class ReservationForm(forms.ModelForm):
    campsite = forms.ModelChoiceField(label='Stovyklavietės', queryset=Camp.objects.all())
    check_in = forms.DateField(label='Registracija nuo:', widget=DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(label='Registracija iki:', widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Reservation
        fields = ['campsite', 'check_in', 'check_out']
        widgets = {'user': forms.HiddenInput()}


class CampReviewForm(forms.ModelForm):
    class Meta:
        model = CampReview
        fields = ('content', 'camp', 'reviewer')
        widgets = {'camp': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['nuotrauka']

class ScoreForm(forms.Form):
    points = forms.IntegerField(label='Taškai', min_value=0, max_value=120)


