#forms.py in app named enroll
from django import forms
from .models import Major

MAJOR_LIST = []
num = len(Major.objects.all())
for i in range(1, num):
	maj = Major.objects.get(pk=i)
	MAJOR_LIST.append((maj.shop_code, maj.shop_name))

MAJOR_TUPLE = tuple(MAJOR_LIST)

class EnrollmentForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	first_choice = forms.ChoiceField(choices = MAJOR_TUPLE)
	second_choice = forms.ChoiceField(choices = MAJOR_TUPLE)
	third_choice = forms.ChoiceField(choices = MAJOR_TUPLE)

