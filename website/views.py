from django.shortcuts import render_to_response
from users.models import User
from django.http import HttpResponse, Http404

# Create your views here.

def site_index(request):
	return render_to_response('website/site_index.html', {})

