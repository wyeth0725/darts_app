from django import forms

class register_form(forms.Form):
    user_name = forms.CharField(label="user name")