# Create your views here.
from django.contrib.auth import authenticate
from django.http import HttpResponse,HttpResponseForbidden
import json
import os
from django.contrib.auth.models import User
from .models import Candidates,Candidate_education_profiles,Candidate_work_profiles,Candidate_location_preferences,Candidate_preferences,Attachments,Files,Candidate_full_texts,Candidate_salarys,Candidate_social_network_details,CandidatePreferences,CatalogValues,CandidateLocationPreferences,Technologys,Users,Sources,CandidateOriginalSourceInfos,EntityPropertys,EntityPropertyDefinitions,CandidateScores,TestUsers,TestResults,Sections,QpGroups,Tests
from app2.models import *
import logging
from django.core import serializers
from django.http import JsonResponse
import redis
import logging
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.apps import apps
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
	#r = redis.StrictRedis(host='10.0.3.7', port=6379,socket_timeout=10) #make this configurable later
	r = redis.StrictRedis(host='preproduction.hirepro.in', port=6379,socket_timeout=10) #make this configurable later
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


def convert_date(obj):
	if isinstance(obj, datetime.datetime):
		d1 = str(obj).split(" ")
		return datetime.datetime.strptime(d1[0], '%Y-%m-%d').strftime('%d/%m/%Y')
	return obj
	
	

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



def get_candidate_json(request, model, m_id,t_id):
	response = {'message' : 'Incorrect Json'}
	try:
		cd =  model.objects.get(pk=m_id)
		ce = Candidate_education_profiles.objects.filter(candidate_id=m_id)
		cw = Candidate_work_profiles.objects.filter(candidate_id=m_id)
		cl = CandidateLocationPreferences.objects.filter(candidatepreference_id=cd.candidatepreference_id)
		cv = CatalogValues.objects.filter(pk__in=[c.location_id for c in cl])
		cval = {val.id:val.value for val in cv}
		at = Attachments.objects.filter(source_item_id = m_id)
		f = [{"AttachmentId" : a.id, "FileName": fl.title, "FileSize": fl.file_size, "GetTypeOfAttachment": '0', "IsCreatedAlready": "false", "IsDeletedAttachment": a.is_deleted, "TargetItemId":a.target_item_id , "TargetItemType": "9" , "TypeOfAttachment": 0 }  for a in at for fl in Files.objects.filter(pk=a.target_item_id)] 


		user = type('', (object,),{'first_name':None})
		src =  type('', (object,),{'source_name':None})
		role =  type('', (object,),{'value':None})
		co =  type('', (object,),{'comments':None})

		if cd.sourcer is not None:
			user = Users.objects.get(pk=cd.sourcer)
		if cd.original_source_id is not None:
			src = Sources.objects.get(pk=cd.original_source_id)
		if cd.hierarchy_id is not None and cd.hierarchy_id != 0:
			role = CatalogValues.objects.get(pk=cd.hierarchy_id)
		if cd.candidateoriginalsourceinfo_id is not None:
			co = CandidateOriginalSourceInfos.objects.get(pk=cd.candidateoriginalsourceinfo_id)

		cust_properties = {'integer1': cd.integer1,'integer2':cd.integer2,'integer3':cd.integer3,'integer4':cd.integer4,'integer5':cd.integer5}
		cust_properties_txt = {'integer1': cd.integer1,'integer2':cd.integer2,'integer3':cd.integer3,'integer4':cd.integer4,'integer5':cd.integer5}
		for cust_val in cust_properties.keys():
			en_p = EntityPropertys.objects.using('db4').filter(is_custom_property=1,entity_type=2,property_name=cust_val)  
			epd = EntityPropertyDefinitions.objects.using('db4').filter(entityproperty_id__in=[ ep.id for ep in en_p],is_catalog=1,tenant_id=t_id)
			if epd:
				if cust_properties[cust_val] is not None and cust_properties[cust_val] != 0:
					cv = CatalogValues.objects.get(pk=cust_properties[cust_val])
					cust_properties_txt[cust_val] = cv.value

		
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
		#response['Candidate'].update({'CandidateEducationProfile' : [model_to_dict(x) for x in Candidate_education_profiles.objects.filter(candidate_id=m_id)]})
		response['Candidate'].update({'CandidateEducationProfile' : [{"CandidateEducationProfileId": ce.id,"CollegeId": ce.college_id,"CollegeText": ce.college_text  ,"DegreeId": ce.degree_id,"DegreeText": ce.degree_text,"DegreeTypeId": ce.degree_type_id,"DegreeTypeText": ce.degree_type_text,"EndMonth": ce.end_month ,"EndYear": ce.end_year,"EndYearText": "--","IsFinal": ce.is_final,"IsPercentage": ce.is_percentage,"Percentage": ce.percentage,"StartMonth": ce.start_month,"StartYear": ce.start_year ,"UniversityId" : ce.university_id ,"UniversityText": ce.university_text} for ce in Candidate_education_profiles.objects.filter(candidate_id=m_id)]})
		#response['Candidate'].update({ 'CandidateWorkProfile' : [model_to_dict(x) for x in Candidate_work_profiles.objects.filter(candidate_id=m_id)]})
		response['Candidate'].update({ 'CandidateWorkProfile' : [{"CandidateCustomFieldTypes": None, "CandidateWorkProfileId": cw.id,"DeisignationId": cw.deisignation_id ,"DesignationText": cw.designation_text,"EmployerId": cw.employer_id ,"EmployerText": cw.employer_text ,"FromMonth": cw.from_month,"FromYear": cw.from_year,"Id": cw.to_year,"LocationId": cw.location_id,"LocationText": cw.location_text,"ReasonForLeaving": cw.reason_for_leaving,"ToMonth": cw.to_month,"ToYear": cw.to_year,"YearlySalary": cw.yearly_salary} for cw in Candidate_work_profiles.objects.filter(candidate_id=m_id)]})
		response['Candidate'].update({ 'CandidatePreference' : {"AddedLocationPreferences": None,"DesiredSalaryFrom": cp.desired_salary_from,"DesiredSalaryTo": cp.desired_salary_to,"IsWillingToRelocate": cp.is_willing_to_relocate,"NoticePeriod":cp.notice_period, "LocationPreferenceValue": cval.values(),"LocationPreferences" : cval.keys(),"Notes": cp.notes} for cp in CandidatePreferences.objects.filter(pk=cd.candidatepreference_id)})
		#response['Candidate'].update({'AttachmentCollection': { 'Attachments': [model_to_dict(x) for x in Attachments.objects.filter(source_item_id = m_id)]}}) #more than one attachment
		response['Candidate'].update({'AttachmentCollection': { 'Attachments': f}}) #more than one attachment
		response['Candidate'].update({'Technologies': [{"OrderNumber": tech.id, "TechnologyId":tech.technology_id} for tech  in Technologys.objects.filter(candidate_id=cd.id)]})
		response['Candidate'].update({'TechnologiesValue': [cd.technology_text]})
		response['Candidate'].update({ "Cgp": ce.percentage ,"Collage": ce.college_text,"CollageId": cd.college_id ,"CreatedOn": str(cd.created_on) ,"CurrentExperience": cd.current_experience ,"CurrentSalary": cd.current_ctc ,"DateOfBirth": convert_date(cd.date_of_birth),"DateTime1": convert_date(cd.date_custom_field1),"DateTime2": convert_date(cd.date_custom_field2),"Degree": cd.final_degree_text,"DegreeId": cd.final_degree_id ,"Email": cd.email1,"Email2": cd.email2,"Experience": cd.total_experience,"ExperienceInMonths": 0,"ExperienceInYears": "1","Gender": cd.gender,"Integer1": cust_properties['integer1'],"Integer2": cust_properties['integer2'],"Integer3": cust_properties['integer3'],"Integer4": cust_properties['integer4'],"Integer5":cust_properties['integer5'] ,"IsPercentage": True,"Location": cd.current_location_text,"LocationId": cd.current_location_id,"MaritalStatus": cd.marital_status,"Name": str(cd.first_name) + " " + str(cd.last_name) ,"Phone": cd.mobile1,"ResumeGrade": "","Source":src.source_name, "SourceChangeComments": co.comments,"SourceId": cd.original_source_id,"SourceType": "" ,"SourceTypeText": "Consultant","TasksList": None,"Text1": cd.text1,"Text2": cd.text2,"TextArea1": None,"TextArea2": None,"TextArea3": None,"TextArea4": None,"TrueFalse1": cd.true_false1,"TrueFalse2": cd.true_false2,"TypeOfCandidateType": cd.type_of_candidate,"CreatedObjectId": cd.created_by,"IsException": False,"IsFailure": False,"ResumeAtachmentId": 737517,"CandidateUpdateOption":0,"CandidateId": cd.id ,"CandidateOriginatedFromText": "None", "CandidatePhotoPath": cd.candidate_photo_path,"PhoneOffice":cd.phone_office,"Address1" : cd.address1 , "Address2": cd.address2 ,"Address3": cd.address3,"PanNo" : cd.pan_card,"PassportNo":cd.passport , "Organization":cd.current_employer_text,"OrganizationId":cd.current_employer_id,"SourcerText":user.first_name,"CountryText": "India" ,"NationalityText":"Indian","Expertise": cd.expertise_text,"Designation": role.value,"Notes": cd.notes ,"Text3":cd.text3,"Text4":cd.text4,"Text5":cd.text5 ,"TextArea1" :cd.text_area1,"TextArea2" :cd.text_area2,"TextArea3" :cd.text_area3,"TextArea4" :cd.text_area4,"CanidatePhotoFileId":cd.candidate_photo_file_id,"CountryCode":cd.country_code, "Integer1Text" : cust_properties_txt['integer1'],"Integer2Text" : cust_properties_txt['integer2'],"Integer3Text" : cust_properties_txt['integer3'],"Integer4Text" : cust_properties_txt['integer4'],"Integer5Text" : cust_properties_txt['integer5']}) 
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
							token = (user_tenant_id,user_id)
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
				response_data = get_candidate_json(request,Candidates,m_id,token[0])
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

#@is_login()
def candidate_assesment(request,c_id=None, test_id=None, token=None):
	response_data = {'message': 'unsuccessfull.Token may have expired'}
	category_dict = {}	
	subcategory_dict = {}	
	tests_dict= {}
	app_models = apps.get_app_config('app1').get_models()
	for modl in app_models:
		modl._meta.app_label = '9999'
	if token is None: #to change this later
		try:
			if request.method == 'GET':
				cd = Candidates.objects.get(pk=c_id)
				response_data['Candidate'] = {"id":cd.id,"first_name": cd.first_name,"last_name":cd.last_name,"email1":cd.email1}
				response_data['message'] = 'Success'
				#select id from test_users where candidate_id=544480 and test_id=2242)
				testid_arr = TestUsers.objects.filter(candidate_id=c_id,status=1).order_by('-login_time')
				testids = [ test.test_id  for test in testid_arr]
				tests = Tests.objects.filter(pk__in=testids)
				tests_dict = {t.id:t.name for t in tests}
				if test_id is None:
					testids=[]
					#testusers = TestUsers.objects.get(candidate_id=544480,test_id=2242)
					testuser_id = testid_arr[0].id
					testuser_percentage = testid_arr[0].percentage
					current_test = Tests.objects.get(pk=testid_arr[0].test_id)
					current_test_details = {"name" : current_test.name,"testid" : current_test.id}
				else:
					testusers = TestUsers.objects.get(candidate_id=c_id,test_id=test_id,status=1)
					current_test = Tests.objects.get(pk=testusers.test_id)
					current_test_details = {"name" : current_test.name,"testid" : current_test.id}
					testuser_id = testusers.id
					testuser_percentage = testusers.percentage
					#testusers = TestUsers.objects.get(candidate_id=c_id,test_id=test_id,status=1)
					#testresults = TestResults.objects.filter(testuser_id = testusers.id)
				cd_score = CandidateScores.objects.filter(testuser_id=testuser_id,candidatescore_id__isnull=True) #categoryscores
				for cat_sc in cd_score:
					category_id = QpGroups.objects.filter(pk=cat_sc.group_id).values_list('category_id','name')
					group_name =  category_id[0][1]
					ctval = CatalogValues.objects.filter(pk=category_id[0][0]).values_list('value',flat=True)
					#print "category name "
					#print ctval
					#category_dict.update({str(category_id[0][0]):[str(ctval),cat_sc.score]})#format: {category_id: [category_name,category_score]
					category_dict.update({str(category_id[0][0]):{"category_name" : str(ctval),"category_score": cat_sc.score}})#format: {category_id: [category_name,category_score]
					#print "category score "
					#print cat_sc.score
					sub_cat_score = CandidateScores.objects.filter(candidatescore_id=cat_sc.id) #subcategoryscore
					for scs in sub_cat_score:
						subcategory_id = Sections.objects.filter(pk=scs.group_id).values_list('sub_category_id',flat=True)
						subctval = CatalogValues.objects.filter(pk=subcategory_id).values_list('value',flat=True)
						#print "Subcategory subcategory name"
						#print subctval
						#print "Subcategory score "
						#print scs.score
						subcategory_dict.update({str(subcategory_id):{"sub_catageory_name": str(subctval), "sub_category_score" : scs.score,"category_id": category_id[0][0]}}) #format: {subcategory_id: [subcategory_name,subcategory_score,categoryid]
				response_data['test_scores'] = {'categories': category_dict}
				response_data['test_scores'].update({'subcategories': subcategory_dict})
				response_data['percentage'] = testuser_percentage
				response_data['all_tests'] = tests_dict
				response_data['current_test_details'] = current_test_details
				response_data['cut_of'] = ["10","20","30","40","50","60","70","80","90","100"]
				response_data['fitment'] = ["10","20","30","40","50","60","70","80","90","100"]
		except Exception as e:
			logging.exception("Exception in candidate_create" +str(e))
			response_data['data'] = {}
			response_data['message'] = 'Exception'
	return HttpResponse(json.dumps(response_data,cls=DateTimeEncoder), content_type="application/json")

def actionplanning(request,c_id,token=None):
	response_data = {'message': 'unsuccessfull.Token may have expired'}
	if token is None: #to change this later
		response_data['beforeplanning'] = ['Research on the company you are targeting to apply','Connect with alumna network who are working with your target company.Gain understanding of the hiring process from them.','Research on the role and the requirements for a job role','Go through the past assesment papers or assesment requirements of the company']
		response_data['resumeprepration'] = ['Resume is a very important aspect of job aspiration','Spend considerable time in making an impactful reusme','Mention all the projects and volunterring work which you may have done during your course work','Ensure that resume is well formatted','Make a cover letter,as lot of companies as for a cover letter','Your cover letter should clearly indicate your desire and keenness of the job role']
		response_data['watch'] = ['when starting to apply,always try to reach out for references in companies.This increases the chances of getting a job sooner','Dont randomly apply to roles when you dont meet the requirement','Follow up on a regular basis','Dont lose hope if you are not able to make it for a desired company or role']
		response_data['message'] = 'Success'
	return HttpResponse(json.dumps(response_data,cls=DateTimeEncoder), content_type="application/json")

def personaldevelopmenttips(request,c_id,token=None):
	response_data = {'message': 'unsuccessfull.Token may have expired'}
	if token is None: #to change this later
		response_data['read'] = ['Outlier By Malcom Gladwell','7 habits of highly effective people by Stephen Convoy','Emotional Intelligence by Daniel Goleman','SQL for professional By Ross Mistry','Programming with C++John Hubbard']
		response_data['Practise'] = ['Spending time in groups','Doing weekly group activites with friends or family','Learning about the new technologies in the market','Researching about the latest books or updates within and outside your field','SQL hirepro practise Test series 1 to 10','C++ hirepro practise Test series 1 to 10','Data analysis practise Test series 1 to 10','Quantitative ability practise Test series 1 to 10']
		response_data['watch'] = ['https://www.youtube.com/watch?v=Rub-JsjMhWY','https://www.youtube.com/watch?v=7Vtl2WggqOg','https://www.youtube.com/watch?v=e0Q7SIj2y4I','https://www.youtube.com/watch?v=Zl3Z-7HK0ZE']
		response_data['message'] = 'Success'
	return HttpResponse(json.dumps(response_data,cls=DateTimeEncoder), content_type="application/json")

def potentialtargetcompanies(request,c_id,token=None):
	response_data = {'message': 'unsuccessfull.Token may have expired'}
	if token is None: #to change this later
		response_data['list_of_companies'] = {"IT-COMPANIES": ["Infosys","AIG","HP","HirePro","Intel"], "IT-PRODUCT":['Akamai',"AIG","HP","HirePro","Intel"],"Others": ['Akamai',"AIG","HP","HirePro","Intel-India"]}
		response_data['message'] = 'Success'
	return HttpResponse(json.dumps(response_data,cls=DateTimeEncoder), content_type="application/json")
