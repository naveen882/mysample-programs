from django.shortcuts import render
from django.http import HttpResponse,HttpResponseForbidden
import json
from django.http import JsonResponse

from .models import Proctoring_Info
from .models import Tenant_Credentials

# Create your views here.

def get_proctoring_file_path(request, tenant_id, candidate_id, test_id):
	response = {}
	response['status'] = 'OK'
	data = {}
	data["filePath"] = "tenants/" + tenant_id + "/candidates/" + candidate_id + "/tests/" + test_id
	response['data'] = data
	print JsonResponse(response)
	return HttpResponse(JsonResponse(response), content_type="application/json")

def proctoring_done(request,tenant_id,candidate_id,test_id ):
	response = {}
	status_code = 201
	#print "GOT Request"
	if request.method == 'POST':
		try:
			#print "GOT POST!!"
			print tenant_id,candidate_id, test_id
			req_body = json.loads(request.body)
			req_data = req_body.get('data',None)
			if req_data is not None:
				file_path = req_data.get('filePath',None)
				duration = req_data.get('duration',None)
			else:
				file_path =''
				duration = 0

			pt = Proctoring_Info()
			pt.file_path = file_path
			pt.tenant_id = int(tenant_id)
			pt.candidate_id= int(candidate_id)
			pt.test_id = int(test_id)
			pt.duration = duration
			pt.save(using='db16')

			response['status'] = 'OK'
			response['data'] = "successfully updated the model"
			response.pop('message','')
		except Exception as e:
			print e
			response['status'] = 'KO'
			response['data'] = ''
			response['message'] = 'Exception!!'
	else:
		response['status'] = 'KO'
		response['data'] = ''
		response['message'] = "Invalid request Method. Use POST"
		status_code = 200
	resp = HttpResponse(JsonResponse(response),content_type="application/json",status=status_code)
	if status_code == 201:
		resp['Location'] = "app1/api/v1/recordedFilePath/" + tenant_id + "/" + candidate_id + "/" + test_id
	return resp



def get_recording_file_path(request,tenant_id, candidate_id, test_id):
	response = {}
	print "Recording File Path for tenant(%s) candidate(%s) test(%s)" % (tenant_id,candidate_id, test_id)
	try:
		proctoring_data = Proctoring_Info.objects.using('db16').filter(tenant_id = tenant_id).filter(candidate_id = candidate_id).filter(test_id = test_id)
		#print len(proctoring_data) 
		#print proctoring_data
		if len(proctoring_data):
			response['status'] = 'OK'
			proctoring_files = [r.file_path for r in proctoring_data]
			response['data'] = proctoring_files
			response.pop('message','')
		else:
			response['status'] = 'KO'
			response['data'] = ''
			error = {}
			error['errorCode'] = 404
			error['errorDescription'] = 'No recording done for the given tenant/candidate/testIds!!'
			response['error'] = error
	except Exception as e:
		print e
	return HttpResponse(JsonResponse(response),content_type="application/json")

def update_proctoring_info(request, tenant_id, candidate_id, test_id):
	response = {}
	print "Updating the info for tenant(%s) candidate(%s) test(%s)" % (tenant_id,candidate_id, test_id)
	if request.method != 'PUT':	
		response['status'] = 'KO'
		response['data'] = ''
		error = {}
		error['errorCode'] = 405
		error['errorDescription'] = 'This API only works over the HTTP method PUT'
		response['error'] = error
	else:
		req_body = json.loads(request.body)	
		print req_body
		req_data = req_body.get('data',None)
		print req_data

		response['status'] = 'KO'
		response['data'] = ''
		error = {}
		error['errorCode'] = 422
		error['errorDescription'] = 'Missing param(s). One/More of filePath/reviewStatus/suspiciousFlag/isDeleted/duration is required for updation'
		response['error'] = error
		if req_data is not None:
			duration = req_data.get('duration',None)
			suspicious_flag = req_data.get('suspiciousFlag',None)
			review_status = req_data.get('reviewStatus',None)
			is_deleted = req_data.get('isDeleted',None)
			file_path = req_data.get('filePath',None)
			print file_path, is_deleted,suspicious_flag,review_status, duration

			if file_path or is_deleted or review_status or suspicious_flag or duration:
				try:
					pt = Proctoring_Info.objects.using('db16').get(tenant_id = tenant_id, candidate_id = candidate_id,test_id = test_id)
					if file_path :
						pt.file_path = file_path
					if is_deleted is not None:
						pt.is_deleted = is_deleted
						# Ensure when is_deleted is set, file_path is also not passed!!
					if review_status :
						pt.review_status = review_status
					if suspicious_flag:
						pt.suspicious_flag = suspicious_flag
					if duration:
						pt.duration = int(duration)
					print "Updated the RECORD!!"
					#pt.save(using='db16')
					pt.save()
					response['status'] = 'OK'
					response['data'] = "Updated the info successfully!!" 
					response.pop('error','')
				except Proctoring_Info.DoesNotExist:
					error['errorCode'] = 404
					error['errorDescription'] = 'No recording done for the given tenant/candidate/testIds!!'
					response['error'] = error
				except Proctoring_Info.MultipleObjectsReturned:
					error['errorCode'] = 500
					error['errorDescription'] = 'For the same tenant/candidate/testIds multiple records exist!'
					response['error'] = error
	return HttpResponse(JsonResponse(response),content_type="application/json")

def get_credentials_for_tenant(request, tenant_id):
	response = {}
	error = {}
	print "Fetching the Recording Server credentials for (%s)" % (tenant_id)
	try:
		credRecSet = Tenant_Credentials.objects.using('db16').get(tenant_id = tenant_id)
		print credRecSet.userName
		print credRecSet.password
		data = {}
		data["email"] = credRecSet.userName
		data["password"] = credRecSet.password
		response['data'] = data
		response['status'] = 'OK'
	except Tenant_Credentials.DoesNotExist:
		response['status'] = 'KO'
		error['errorCode'] = 404
		error['errorDescription'] = 'The given tenant does not exist!!' 
		response['error'] = error
	except Tenant_Credentials.MultipleObjectsReturned:
		response['status'] = 'KO'
		error['errorCode'] = 500
		error['errorDescription'] = 'The given tenant does not exist!!' 
		response['error'] = error
	print JsonResponse(response)
	return HttpResponse(JsonResponse(response), content_type="application/json")
