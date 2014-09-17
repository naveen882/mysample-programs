Steps to run the application are the following,

1.Please untar the the zip in /tmp directory only (else in settings.py you will have to change TEMPLATE_DIRS path)

2.python manage.py syncdb

3.python manage.py runserver

4.Exposed urls are
http://127.0.0.1:8000/registration/reg/
http://127.0.0.1:8000/registration/login/
http://127.0.0.1:8000/registration/list/
http://127.0.0.1:8000/registration/update/
http://127.0.0.1:8000/registration/delete/

5.test.py file contains all the test cases for the above said urls.

6.Also http://127.0.0.1:8000/registration/list/ is the url to add new user, edit and delete operations.


Thanks,
Naveen.
