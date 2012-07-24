from django.shortcuts import render_to_response, redirect
from users.models import User
from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from django.template import RequestContext

# Create your views here.

def site_index(request):
	return render_to_response('website/site_index.html', {}, context_instance=RequestContext(request))


def search(request):
	c = {}
	c.update(csrf(request))
	users = []

	if request.method == 'POST':
		if request.POST['f_name']:
			f_name = request.POST['f_name']
			users_list = User.objects.filter(first_name=f_name)
			if users_list.exists():
				for i in users_list:
					users.append(i)
	c['users'] = users
	return render_to_response('website/search.html', c)
