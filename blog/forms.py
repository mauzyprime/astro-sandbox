from django import forms

class HomeForm(forms.Form):
	x = forms.charfield(label='Your Query', max_length=100)