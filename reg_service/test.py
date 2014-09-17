import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'reg_service.settings'
from reg_service import settings
sys.path.append('/tmp/reg_service')
from django.test import Client

#inserting testusername in the DB
c = Client(enforce_csrf_checks=False)
response = c.post('/registration/send/', {'firstname': 'test', 'lastname' : '_test','password': 'test123', 'role': 'role1','email': 'testemail@test.com'})
print response.status_code


#inserting duplicate username in the DB
response = c.post('/registration/send/', {'firstname': 'test', 'lastname' : '_test','password': 'test123', 'role': 'role1','email': 'testemail@test.com'})
print response.status_code

#Check wrong email id
response = c.post('/registration/logon/', {'email': 'testemail@test.com1', 'password': 'test123'})
print response.status_code

#check correct email id
response = c.post('/registration/logon/', {'email': 'testemail@test.com', 'password': 'test123'})
print response.status_code

#List all users 
response = c.post('/registration/list/', {})
print response.status_code

#get user details
response = c.post('/registration/get_user/', {'firstname': 'test', 'lastname' : '_test'})
uid =int(response.content.rstrip())

#Update user 
response = c.post('/registration/update/', {'firstname': 'test', 'lastname' : 'test_','rid':uid})
print response.status_code

#Delete user 
response = c.post('/registration/delete/', {'rid':uid})
print response.status_code
