from .models import Garage
from django import forms

class GarageForm(forms.ModelForm):
    class Meta:
        model = Garage
        fields='__all__'
        labels = { "name": "Item Name:", "description": "Describe Item:", "price": "Price:", "itemPicture": "Picture:"}