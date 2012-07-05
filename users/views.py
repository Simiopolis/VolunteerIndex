from django.shortcuts import render_to_response
from users.models import User
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
	user_list = User.objects.all()
	return render_to_response('users/index.html', {'user_list': user_list})

def names(request, user_id):
	try:
		user = User.objects.get(id=user_id)
	except User.DoesNotExist:
		raise Http404
	return HttpResponse("You're looking at user {0}, whose name is {1}."
			.format(str(user.id), str(user.first_name)))
