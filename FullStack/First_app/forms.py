from django import forms
from django.contrib.auth.models import User
from django.core import validators
from First_app import models

def checkforZ(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Start with Z or GET OUT")

class FormName(forms.Form):
    name = forms.CharField(validators= [checkforZ])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput , validators = [validators.MaxLengthValidator(0)])

    #def clean_botcatcher(self):
    #    botcatcher = self.cleaned_data['botcatcher']
    #    if len(botcatcher) > 0 :
    #        raise forms.ValidationError("Gotcha BOT!")

    #    return botcatcher

class FormName1(forms.ModelForm):
    class Meta():
        model = models.Webpage
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = models.UserProfileInfo

        fields = ('portofolio_site','profile_pic')
