from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
        required=True,
    )

    shipping_email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True,
    )

    shipping_address1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address1'}),
        required=True,
    )

    shipping_address2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address2'}),
        required=False
    )

    shipping_city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
        required=True,
    )

    shipping_state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
        required=False,
    )

    shipping_zipcode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZipCode'}),
        required=False,
    )

    shipping_country = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
        required=True,
    )

    class Meta:
        model = ShippingAddress
        fields =[
            'shipping_full_name',
            'shipping_email',
            'shipping_address1',
            'shipping_address2',
            'shipping_city',
            'shipping_state',
            'shipping_zipcode',
            'shipping_country',
        ]

        exclude = ['user',]
