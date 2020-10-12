from .models import CustomerInfo
from django import forms

class CustomerInfoForm(forms.ModelForm):
    # full_name = forms.CharField(label='full name:', max_length=150)
    # email = forms.EmailField()
    # phone_number = forms.CharField(label='phone number:', max_length=20)
    # address = forms.CharField(label='address: ', max_length=150)
    
    class Meta:
        model = CustomerInfo
        fields = '__all__'

    # def clean(self):
    #     cleaned_data = super(CustomerInforForm, self).clean()
    #     # full_name = self.cleaned_data["full_name"]
    #     # phone_number = self.cleaned_data["phone_number"]
    #     return cleaned_data