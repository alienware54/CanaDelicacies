from django import forms
from canaapp.models import Reservation, ImageModel


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'
