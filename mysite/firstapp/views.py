from django.shortcuts import render
from .forms import Personform
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home_view(request):
	context ={}

	# create object of form
	form = Personform(request.POST or None, request.FILES or None)
	
	# check if form data is valid
	if form.is_valid():
		# save the form data to model
		form.save()

	context['form']= form
	return render(request, "firstapp/home.html", context)
