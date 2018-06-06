from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Applicant
from django import forms
import smtplib

#script created and implemented by:
#Joey G, Omar M, Andrew F
def generate_email(parent,first_name,last_name):
	gmail_user = 'mrstarkidontfeelsogood6937@gmail.com'
	gmail_password = 'idontwannago'


	sent_from = gmail_user
	#to = [parent]
	to = ['lamsond@wctech.org']
	subject = 'Warren Tech Application'
	body = 'Your child, ' + first_name + ' ' + last_name + ', has successfully submitted an application'


	email_text = """\
	From: %s
	To: %s
	Subject: %s


	%s
	""" % (sent_from, ", ".join(to), subject, body)


	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()
		
		
		print ('Email sent!')
	except:
		print ('Something went wrong...')


# Create your views here.
class ApplicantForm(forms.ModelForm):
	class Meta:
		model = Applicant
		exclude = ['birth_date', 'student_home_phone', 'parent_cell_1', 'counselor_phone']
		
def apply(request):
	if request.method != "POST":
		form = ApplicantForm()
	else:
		form = ApplicantForm(request.POST)
		if form.is_valid():
			new_applicant = form.save(commit=False)
			new_applicant.birth_date = int(request.POST.get("birth_date"))
			new_applicant.student_home_phone = "1-" + str(request.POST.get("student_areacode")) + "-" + str(request.POST.get("student_exchange")) + "-" + str(request.POST.get("student_last_four"))
			new_applicant.parent_cell_1 = "1-" + str(request.POST.get("parent_areacode")) + "-" + str(request.POST.get("parent_exchange")) + "-" + str(request.POST.get("parent_last_four"))
			new_applicant.counselor_phone = "1-" + str(request.POST.get("counselor_areacode")) + "-" + str(request.POST.get("counselor_exchange")) + "-" + str(request.POST.get("counselor_last_four"))
			new_applicant.save()
			generate_email(request.POST.get("parent_1_email"), request.POST.get("first_name"), request.POST.get("last_name"))
			return HttpResponseRedirect('/confirm/')
	return render(request, 'wcts_app/apply_custom.html', {'form': form})
	#return render(request, 'wcts_app/apply.html', {'form': form})
		
def confirm(request):
	applicant = request.POST.get("first_name");
	return render(request, 'wcts_app/confirm_new.html', {'name':applicant})


