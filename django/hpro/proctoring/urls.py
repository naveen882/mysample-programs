from django.conf.urls import include, url
from . import views
urlpatterns = [
	#Interaction with Recording Server
	# 4 APIs.
	#   i) get the (ABSOLUTE) path where to store the recording for the given tenantId/candidateId/testId
	#  ii) notify recording status(success/failure) for the given tenantId/candidateId/testId
	# iii) retrieve the path of the recording file given the tenantId/candidateId/testId
	#  iv) API for updating suspicious_flag, review_status, and is_deleted and other fields like filePath
	 url(r'^api/v1/filePathFor/(?P<tenant_id>\d+)/(?P<candidate_id>\d+)/(?P<test_id>\d+)',views.get_proctoring_file_path),
	 url(r'^api/v1/status/(?P<tenant_id>\d+)/(?P<candidate_id>\d+)/(?P<test_id>\d+)'   ,views.proctoring_done),
	 url(r'^api/v1/recordedFilePath/(?P<tenant_id>\d+)/(?P<candidate_id>\d+)/(?P<test_id>\d+)'  ,views.get_recording_file_path),
	 url(r'^api/v1/infoFor/(?P<tenant_id>\d+)/(?P<candidate_id>\d+)/(?P<test_id>\d+)'  ,views.update_proctoring_info),
	# Exposing django api to outside world over http!! Live with it for now.
	 url(r'^api/v1/credentials/(?P<tenant_id>\d+)'  ,views.get_credentials_for_tenant),
]
