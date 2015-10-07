# Create your views here.
from django.contrib.auth import authenticate
from django.http import HttpResponse,HttpResponseForbidden
import json
import os
from django.contrib.auth.models import User
from .models import Candidates,Candidate_education_profiles,Candidate_work_profiles,Candidate_location_preferences,Candidate_preferences,Attachments,Files,Candidate_full_texts,Candidate_salarys,Candidate_social_network_details
from app2.models import *
import logging
from django.core import serializers
from django.http import JsonResponse
import redis
import logging
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import datetime


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def login(request):
   try:
      data = json.loads(request.body)
      username = data['username']
      password = data['password']
      user = authenticate(username=username, password=password)
      print request.session
      print request
      print dir(request.session)
      print request.session.keys()
      print "hi" in request.session
      print request.session["hi"]

      try:
         if "hi" not in request.session:
            request.session['hi']="hi1"
            print request.session['hi']
      except Exception as e:
         print e
      if user is not None:
         if user.is_active:
           return HttpResponse("Authorized")
         else:
           return HttpResponseForbidden("User disabled")
      else:
          return HttpResponseForbidden("The username and password were incorrect.")
   except:
      raise

def get_files(request):
   try:
      path = request.GET.get('path', '')
      out = os.listdir(path)
      return HttpResponse(out)
   except:
      raise

def list_users(request):
   try:
      status = request.GET.get('status', None)
      if status != None:
         users = User.objects.filter(is_active=status)
      else:
         users = User.objects.all()
      user_list = [user.username for user in users]
      return HttpResponse(user_list)
   except:
      raise

def redis_connect():
	r = redis.StrictRedis(host='10.0.3.7', port=6379,socket_timeout=10) #make this configurable later
	return r


def save_candidate(request,m_id=None):
	try:
		c=Candidates(version=1,notes='12',importance=1,technology_text='ss django',bulk_custom_field_string='123',no_of_attachments=1,is_alive=1,created_by=1,is_deleted=1,guid='12',is_black_listed=0,is_partial_duplicate=0,black_list_mode=0,soft_delete_type=0,is_utilized=0,type_of_candidate=0)
		c.save()
		return HttpResponse(c.id)
	except Exception as e:
		print e		

def db1save(request):
	try:
		c=Candidates(version=1,notes='12',importance=1,technology_text='ss django',bulk_custom_field_string='123',no_of_attachments=1,is_alive=1,created_by=1,is_deleted=1,guid='12',is_black_listed=0,is_partial_duplicate=0,black_list_mode=0,soft_delete_type=0,is_utilized=0,type_of_candidate=0)
		c.save()
		return HttpResponse(c.id)
	except Exception as e:
		print e		


def db2save(request):
	try:
		#candidate_full_texts.full_clean()
		c1 = candidate_full_texts(created_by=1)
		c1.save()
		return HttpResponse(c1.id)
	except Exception as e:
		print e		

def app(request):
	return HttpResponse("hello world")



print "==========================================="


def get_candidate_details(xauth_token):
	try:
		r =redis_connect()
		xauth_token += '_AppServer'
		return (r.get(xauth_token),r.ttl(xauth_token))
	except:
		logger.error("Error while getting token details from redis server")
		return None
		

def custom_generic_serializer(obj):
	return serializers.serialize('json', [obj])


def json_post(request, model, mandatory_params=[],other_db = None):
	response = {'message' : 'Incorrect Json'}
	try:
		json_request = json.loads(request.body)
		print json_request
		json_keys_set = set(json_request.keys())
		if set(mandatory_params).issubset(json_keys_set): #if mandatory fields are in the json request then continue
			obj = model()
			#for key in models_fields_set & json_keys_set:
			for key in model._meta.get_all_field_names():
				if key in json_request:
					setattr(obj, key, json_request[key])
			obj.save()
			response['data'] = custom_generic_serializer(obj)
			if other_db is not None:
				obj.pk=None
				#candidate.save(using='db2',force_insert=True) #candidate table should exist with same name ,model name doesnt matter in this case
				obj.save(using=other_db,force_insert=True) #candidate table should exist with same name ,model name doesnt matter in this case
				response['data1'] = custom_generic_serializer(obj)
			response['message'] = 'Success'
		else:
			data = "Missing json parameters are "
			for k in set(mandatory_params).difference(json_request):#missing items in request
				data += "," + str(k)
			response['message'] = 'Unsuccessfull. ' + data
	except Exception as e:
		response['message'] = 'Exception'
		logging.exception("Exception"+str(e))
	return response


def json_get(request, model, m_id=None):
	response = {'message' : 'Incorrect Json'}
	try:
		if m_id is not None:
			obj = model.objects.filter(pk=m_id)
		else:
			obj = model.objects.all() #to filter by tenant
		response['data'] = serializers.serialize('json', obj)
		response['message'] = 'Success'
	except Exception as e:
		response['message'] = 'Exception'
		logging.exception("Exception"+str(e))
	return response



def get_candidate_json(request, model, m_id=None):
	response = {'message' : 'Incorrect Json'}
	try:
		if m_id is not None:
			cd =  model.objects.get(pk=m_id)
			ce = Candidate_education_profiles.objects.filter(candidate_id=m_id)
			cw = Candidate_work_profiles.objects.filter(candidate_id=m_id)
			response = {'Candidate': model_to_dict(cd)}
			if ce:
				ce = ce.order_by("-id")[0]
			else:
				ce = type('', (object,),{'percentage':None , 'college_text':None})
			if cw :
				cw = cw.order_by("-id")[0]
			else:
				cw = type('', (object,),{'yearly_salary':None})
			#response = {'Candidate': {}}
			response['Candidate'].update({'CandidateEducationProfile' : [model_to_dict(x) for x in Candidate_education_profiles.objects.filter(candidate_id=m_id)]})
			response['Candidate'].update({ 'CandidateWorkProfile' : [model_to_dict(x) for x in Candidate_work_profiles.objects.filter(candidate_id=m_id)]})
			#response['Candidate'].update({'AttachmentCollection': { 'Attachments': [model_to_dict(x) for x in Attachments.objects.filter(source_item_id = m_id)]}}) #more than one attachment
			response['Candidate'].update({'AttachmentCollection': { 'Attachments': []}}) #more than one attachment
			response['Candidate'].update({'Technologies': []})
			response['Candidate'].update({'TechnologiesValue': []})
			response['Candidate'].update({ "Cgp": ce.percentage ,"Collage": ce.college_text,"CollageId": cd.college_id ,"CreatedOn": str(cd.created_on) ,"CurrentExperience": cd.current_experience ,"CurrentSalary": cw.yearly_salary ,"DateOfBirth": str(cd.date_of_birth),"DateTime1": None,"DateTime2": None,"Degree": cd.final_degree_text,"DegreeId": cd.final_degree_id ,"Email": cd.email1,"Email2": cd.email2,"Experience": cd.total_experience,"ExperienceInMonths": 0,"ExperienceInYears": cd.current_experience,"Gender": cd.gender,"Integer1": cd.integer1,"Integer2": cd.integer2,"Integer3": cd.integer3,"Integer4": cd.integer4,"Integer5": cd.integer4,"IsPercentage": True,"Location": cd.current_location_text,"LocationId": cd.current_location_id,"MaritalStatus": cd.marital_status,"Name": str(cd.first_name) + " " + str(cd.last_name) ,"Phone": cd.mobile1,"ResumeGrade": "","Source":cd.sourcer,"SourceId": cd.original_source_id,"SourceType": "" ,"SourceTypeText": "Consultant","TasksList": None,"Text1": cd.text1,"Text2": cd.text2,"TextArea1": None,"TextArea2": None,"TextArea3": None,"TextArea4": None,"TrueFalse1": None,"TrueFalse2": None,"TypeOfCandidateType": cd.type_of_candidate,"CreatedObjectId": cd.created_by,"IsException": False,"IsFailure": False,"ResumeAtachmentId": 737517,"CandidateUpdateOption":0,"CandidateId": cd.id ,"CandidateOriginatedFromText": "None", "CandidatePhotoPath": cd.candidate_photo_path }) #more than one attachment else:
			obj = model.objects.all() #to filter by tenant
	except Exception as e:
		response['message'] = 'Exception'
		logging.exception("Exception in json construct"+str(e))
	return response

def is_login():
	def evaluate(f):
		def param_eval(request,m_id=None,token=None):
			#res = get_candidate_details('9fd14ca4-f65a-4913-b27d-27eee1004598') #get the value from xuth thoken
			res = get_candidate_details(token) #get the value from xuth thoken
			if res:
				if res[0] is not None and res[1] > 0: #valid token condition ,token exist and ttl is > 0
					ttl = res[1]
					token = (res[0], res[1])  #('userid-tenantid' ,ttl)
					user_details = token[0].split("-")
					from django.apps import apps
					if len(user_details) > 1:
						user_id = int(user_details[0])
						user_tenant_id = user_details[1]
					app_models = apps.get_app_config('app1').get_models()
					for modl in app_models:
						modl._meta.app_label = user_tenant_id
					if user_id is not None and ttl > 0: 
						return f(request,m_id,token)
			return f(request,m_id) #redis connection error or token expired
		return param_eval
	return evaluate


class DateTimeEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime.datetime):
			#encoded_object = list(obj.timetuple())[0:6]
			encoded_object = str(obj)
		else:
			encoded_object =json.JSONEncoder.default(self, obj)
		return encoded_object

@is_login()
def candidate_create(request, m_id=None, token=None):
	response_data = {'message': 'unsuccessfull.Token may have expired'}
	if token is not  None:
		try:
			require_params = ['version' , 'notes' , 'importance' ,'no_of_attachments' , 'technology_text' , 'created_by' , 'bulk_custom_field_string'  , 'is_utilized' , 'is_deleted']
			if request.method == 'POST':
				response_data = json_post(request,Candidates,require_params,'db2')
			elif request.method == 'GET':
				try:
					ttl = token[1]
				except Exception as e:
					print e
				response_data = get_candidate_json(request,Candidates,m_id)
				print response_data
		except Exception as e:
			logging.exception("Exception in candidate_create" +str(e))
			response_data['message'] = 'Exception'
	return HttpResponse(json.dumps(response_data,cls=DateTimeEncoder), content_type="application/json")


@is_login()
def candidate_educationprofiles_create(request,m_id=None,token=None):
	response_data = {'message': 'unsuccessfull'}
	if token is not None:
		try:
			require_params = ['created_by']
			if request.method == 'POST':
				response_data = json_post(request,Candidate_education_profiles,require_params)
			elif request.method == 'GET':
				ttl = token[1]
				user_details = token[0].split("-")
				if len(user_details) > 1:
					user_id = int(user_details[0])
					user_tenant_id = int(user_details[1])
					if user_id is not None and ttl > 0: 
							response_data = json_get(request,Candidate_education_profiles,m_id)
		except Exception as e:
			response_dict['message'] = 'Exception'
		return HttpResponse(JsonResponse(response_data), content_type="application/json")

@is_login()
def candidate_work_profiles(request,m_id=None,token=None):
	response_data = {'message': 'unsuccessfull'}
	if token is not None:
		try:
			require_params = ['created_by']
			if request.method == 'POST':
				response_data = json_post(request,Candidate_work_profiles,require_params)
			elif request.method == 'GET':
				ttl = token[1]
				user_details = token[0].split("-")
				if len(user_details) > 1:
					user_id = int(user_details[0])
					user_tenant_id = int(user_details[1])
					if user_id is not None and ttl > 0: 
						response_data = json_get(request,Candidate_work_profiles,m_id)
		except Exception as e:
			response_dict['message'] = 'Exception'
		return HttpResponse(JsonResponse(response_data), content_type="application/json")

@is_login()
def candidate_location_preferences(request,m_id=None,token=None):
	response_data = {'message': 'unsuccessfull'}
	if token is not None:
		try:
			require_params = ['location_id','created_by']
			if request.method == 'POST':
				response_data = json_post(request,Candidate_location_preferences,require_params)
			elif request.method == 'GET':
				ttl = token[1]
				user_details = token[0].split("-")
				if len(user_details) > 1:
					user_id = int(user_details[0])
					user_tenant_id = int(user_details[1])
					if user_id is not None and ttl > 0: 
						response_data = json_get(request,Candidate_location_preferences,m_id)
		except Exception as e:
			response_dict['message'] = 'Exception'
	return HttpResponse(JsonResponse(response_data), content_type="application/json")

@is_login()
def candidate_preferences(request,m_id=None,token=None):
	response_data = {'message': 'unsuccessfull'}
	if token is not None:
		try:
			require_params = ['created_by']
			if request.method == 'POST':
				response_data = json_post(request,Candidate_preferences,require_params,'db2')
			elif request.method == 'GET':
				ttl = token[1]
				user_details = token[0].split("-")
				if len(user_details) > 1:
					user_id = int(user_details[0])
					user_tenant_id = int(user_details[1])
					if user_id is not None and ttl > 0: 
						response_data = json_get(request,Candidate_preferences,m_id)
		except Exception as e:
			response_dict['message'] = 'Exception'
	return HttpResponse(JsonResponse(response_data), content_type="application/json")

@is_login()
def attachments(request,m_id=None,token=None):
	response_data = {'message': 'unsuccessfull'}
	if token is not None:
		try:
			require_params = ['version', 'created_by','is_deleted', 'guid']
			if request.method == 'POST':
				response_data = json_post(request,Attachments,require_params)
			elif request.method == 'GET':
				ttl = token[1]
				user_details = token[0].split("-")
				if len(user_details) > 1:
					user_id = int(user_details[0])
					user_tenant_id = int(user_details[1])
					if user_id is not None and ttl > 0: 
						response_data = json_get(request,Attachments,m_id)
		except Exception as e:
			response_dict['message'] = 'Exception'
	return HttpResponse(JsonResponse(response_data), content_type="application/json")

@is_login()
def files(request,m_id=None,token=None):
	response_data = {'message': 'unsuccessfull'}
	if token is not None:
		try:
			require_params = ['version', 'title' ,'created_by','original_file_name','file_size','target_path','is_deleted','guid']
			if request.method == 'POST':
				response_data = json_post(request,Files,require_params)
			elif request.method == 'GET':
				ttl = token[1]
				user_details = token[0].split("-")
				if len(user_details) > 1:
					user_id = int(user_details[0])
					user_tenant_id = int(user_details[1])
					if user_id is not None and ttl > 0: 
						response_data = json_get(request,Files,m_id)
		except Exception as e:
			response_dict['message'] = 'Exception'
	return HttpResponse(JsonResponse(response_data), content_type="application/json")


@is_login()
def candidate_full_texts(request,m_id=None,token=None):
	response_data = {'message': 'unsuccessfull'}
	if token is not None:
		try:
			require_params = ['created_by']
			if request.method == 'POST':
				response_data = json_post(request,Candidate_full_texts,require_params)
			elif request.method == 'GET':
				ttl = token[1]
				user_details = token[0].split("-")
				if len(user_details) > 1:
					user_id = int(user_details[0])
					user_tenant_id = int(user_details[1])
					if user_id is not None and ttl > 0: 
						response_data = json_get(request,Candidate_full_texts,m_id)
		except Exception as e:
			response_dict['message'] = 'Exception'
	return HttpResponse(JsonResponse(response_data), content_type="application/json")

@is_login()
def candidate_salarys(request,m_id=None,token=None):
	response_data = {'message': 'unsuccessfull'}
	if token is not None:
		try:
			require_params = ['created_by']
			if request.method == 'POST':
				response_data = json_post(request,Candidate_salarys,require_params)
			elif request.method == 'GET':
				ttl = token[1]
				user_details = token[0].split("-")
				if len(user_details) > 1:
					user_id = int(user_details[0])
					user_tenant_id = int(user_details[1])
					if user_id is not None and ttl > 0: 
						response_data = json_get(request,Candidate_salarys,m_id)
		except Exception as e:
			response_dict['message'] = 'Exception'
	return HttpResponse(JsonResponse(response_data), content_type="application/json")

@is_login()
def candidate_social_network_details(request,m_id=None,token=None):
	response_data = {'message': 'unsuccessfull'}
	if token is not None:
		try:
			require_params = ['version', 'candidate_id' ,'created_by','is_deleted']
			if request.method == 'POST':
				response_data = json_post(request,Candidate_social_network_details,require_params)
			elif request.method == 'GET':
				ttl = token[1]
				user_details = token[0].split("-")
				if len(user_details) > 1:
					user_id = int(user_details[0])
					user_tenant_id = int(user_details[1])
					if user_id is not None and ttl > 0: 
						response_data = json_get(request,Candidate_social_network_details,m_id)
		except Exception as e:
			response_dict['message'] = 'Exception'
	return HttpResponse(JsonResponse(response_data), content_type="application/json")
