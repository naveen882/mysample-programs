"""

usage : sudo docker cp 7a85d1a623a3:/tmp/ac . && python proctoring.py "/tmp/ac" 2 3 4 5

"""
import os,sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'hpro.settings'

from app1.models import Proctoring


file_path = sys.argv[1]
user_id = sys.argv[2]
tenant_id = sys.argv[3]
created_by = sys.argv[4]
duration = sys.argv[4]



if file_path is not None and user_id is not None  and tenant_id is not None:
	pt = Proctoring()
	pt.file_path = file_path
	pt.user_id = user_id 
	pt.tenant_id = tenant_id
	pt.duration = duration
	if created_by is not None:
		pt.created_by = created_by
	pt.save(using='db16')
