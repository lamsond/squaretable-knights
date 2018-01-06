#forms.py in app named enroll
from django import forms
from .models import Major

MAJOR_TUPLE = (('AT', 'Automotive Technology'),
	('BT', 'Building Technology'),
	('CP', 'Computer Programming'),
	)

class EnrollmentForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	first_choice = forms.ChoiceField(choices = MAJOR_TUPLE)
	second_choice = forms.ChoiceField(choices = MAJOR_TUPLE)
	third_choice = forms.ChoiceField(choices = MAJOR_TUPLE)

