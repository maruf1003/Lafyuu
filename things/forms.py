from django import forms

# bu frontEnd uchun html forma
class SubscribeForm(forms.Form):
    email = forms.EmailField()
