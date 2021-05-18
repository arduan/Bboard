from django import forms
from .views import AdvUser

class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, Label='Адрес электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')


