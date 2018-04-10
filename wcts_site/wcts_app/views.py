from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Applicant
from django import forms

# Create your views here.
class ApplicantForm(forms.ModelForm):
	class Meta:
		model = Applicant
		fields = '__all__'
		
def apply(request):
	if request.method != "POST":
		form = ApplicantForm()
	else:
		form = ApplicantForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/confirm/')
	return render(request, 'wcts_app/apply_custom.html', {'form': form})
	#return render(request, 'wcts_app/apply.html', {'form': form})
		
def confirm(request):
	return render(request, 'wcts_app/confirm.html', {'':''})
