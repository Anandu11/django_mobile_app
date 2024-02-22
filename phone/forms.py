from django import forms
#forms is a Django module for creating HTML forms, 
from phone.models import Mobilemodel


class MobileForm(forms.ModelForm):#This line creates a new form class named MobileForm, which is a subclass of forms.ModelForm
    class Meta:#The Meta class inside MobileForm is used to provide additional information about the form
        model=Mobilemodel
        fields='__all__'#that the form should include fields for all the fields in the Mobilemodel