from django import forms
from .models import Profilis, CampReview, Reservation, Camp, ContactUs,ChildrenRegistration, ChildrenCamp, AdultCamp, AdultRegistration
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


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']


class ChildrenRegistrationForm(forms.ModelForm):
    children_camp = forms.ModelChoiceField(label='Vaikų stovyklos', queryset=ChildrenCamp.objects.all())
    children_name = forms.CharField(label='Vaiko vardas')
    children_dob = forms.DateField(label='Vaiko gimimo data', widget=forms.DateInput(attrs={'type': 'date'}))
    parent_name = forms.CharField(label='Tėvų arba Globėjų Vardas, Pavardė')
    phone = forms.CharField(label='Kontaktinis telefono numeris')
    email = forms.EmailField(label='El. paštas')
    allergies = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}), label='Alergijos ir kita svarbi informacija apie vaiką')

    class Meta:
        model = ChildrenRegistration
        fields = ['children_camp', 'children_name', 'children_dob', 'parent_name', 'phone', 'email', 'allergies']

class AdultRegistrationForm(forms.ModelForm):
    adult_camp = forms.ModelChoiceField(label='Suaugusiųjų stovyklos', queryset=AdultCamp.objects.all())
    first_name = forms.CharField(label='Vardas')
    last_name = forms.CharField(label='Pavardė')
    phone = forms.CharField(label='Kontaktinis telefono numeris')
    email = forms.EmailField(label='El. paštas')
    info = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}), label='Papildoma informacija')

    class Meta:
        model = AdultRegistration
        fields = ['adult_camp', 'first_name', 'last_name', 'phone', 'email', 'info']


