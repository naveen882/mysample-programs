from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from models import UserProfile
from django.contrib.auth.models import User
from django.utils import simplejson
from django.contrib.auth import authenticate, login
import logging as log

def reg_index(request):
	return render_to_response('registration/index.html',
                               context_instance=RequestContext(request, {}))

def log_in(request):
	return render_to_response('registration/login.html',
                               context_instance=RequestContext(request, {}))

def logon(request):
	response_dict = {}
	qd = request.POST
	email = qd.__getitem__('email')
	password = qd.__getitem__('password')
	user = authenticate(username=email, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			up = UserProfile.objects.get(user=user)
			if up.role == "role1":
				response_dict['role'] = "Welcome role1 user"
				print "Welcome role1 user"
				message = "Welcome role1 user"
			elif up.role == "role2":
				response_dict['role'] = "Welcome role2 user"
				print "Welcome role2 user"
				message = "Welcome role2 user"
			else :
				response_dict['role'] = "Unknown role"
				print "Unknown role"
				message = "Unknown role"
			return render_to_response('registration/main.html',
								   context_instance=RequestContext(request, {'response_dict' : message}))
		else:
			print "Account disabled"
			response_dict ['message'] = "Account disabled"
	else:
		print "Username/Password incorrect"
		response_dict ['message'] = "Username/Password incorrect"
	return render_to_response('registration/login.html',
						   context_instance=RequestContext(request, response_dict))
		

def send(request):
	try:
		response_dict = {}
		if request.method == 'GET':
			qd = request.GET
		elif request.method == 'POST':
			qd = request.POST
		firstname = qd.__getitem__('firstname')
		lastname = qd.__getitem__('lastname')
		password = qd.__getitem__('password')
		role = qd.__getitem__('role')
		email = qd.__getitem__('email')

		user_exist = User.objects.filter(username=email)
		if not user_exist:
			user= User()	
			user.username = email
			user.set_password(password)
			user.save()
			up = UserProfile()
			up.user= user
			up.first_name = firstname 
			up.last_name = lastname
			up.role = role
			up.save()
			response_dict['status'] = 0
			response_dict['message'] = "Registration successfull"
			print "Registration successfull"
		else:
			response_dict['status'] = 1
			print "Username already exist"
			response_dict['message'] = "Username already exist"
	except Exception as e:
		response_dict['status'] = 2
		import logging
		logging.exception("Exception")
	return HttpResponse(simplejson.dumps(response_dict), content_type='application/javascript')
		
def list(request):
	response_dict = {}
	up = UserProfile.objects.all()
	return render_to_response('registration/list.html',
						   context_instance=RequestContext(request, {'up':up}))

def update(request):
	try:
		response_dict = {}
		qd = request.POST
		firstname = qd.__getitem__('firstname')
		lastname = qd.__getitem__('lastname')
		rid = qd.__getitem__('rid')

		up = UserProfile.objects.get(pk=rid)
		up.first_name = firstname 
		up.last_name = lastname
		up.save()
		response_dict['status'] = 0
		print "Update successfull"
		response_dict['message'] = "Update successfull"
	except Exception as e:
		response_dict['status'] = 1
		print "Update unsuccessfull"
		response_dict['message'] = "Update unsuccessfull"
		import logging
		logging.exception("Exception")
	return HttpResponse(simplejson.dumps(response_dict), content_type='application/javascript')

def delete(request):
	try:
		response_dict = {}
		qd = request.POST
		rid = qd.__getitem__('rid')

		up = UserProfile.objects.get(pk=rid)
		up.delete()
		up.user.delete()
		response_dict['status'] = 0
		print "Delete successfull"
		response_dict['message'] = "Delete successfull"
	except Exception as e:
		response_dict['status'] = 1
		print "Delete unsuccessfull"
		response_dict['message'] = "Delete unsuccessfull"
	return HttpResponse(simplejson.dumps(response_dict), content_type='application/javascript')

def get_user(request):
	try:
		response_dict = {}
		qd = request.POST
		firstname = qd.__getitem__('firstname')
		lastname = qd.__getitem__('lastname')
		up = UserProfile.objects.get(first_name=firstname,last_name=lastname)
		print up.id
		#return HttpResponse(up.id)
		return render_to_response('registration/get_user.html',
							   context_instance=RequestContext(request, {'up':up}))
	except:
		print "User not found"
