from django.db import models

# Create your models here.
class Proctoring_Info(models.Model):
    tenant_id = models.IntegerField()
    candidate_id = models.IntegerField()
    test_id = models.IntegerField()
    file_path = models.CharField(max_length=1024, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,)
    suspicious_flag =  models.BooleanField(default=0)
    review_status = models.BooleanField(default=0)
    duration = models.IntegerField()
    is_deleted =  models.BooleanField(default=0)

    class Meta:
	db_table = 'proctering_info_map'
"""
    class Meta:
	app_label = '9999'
"""
class Tenant_Credentials(models.Model):
	# can't be blank is the default
	tenant_id = models.IntegerField(unique=True);
	userName = models.CharField(max_length=256);
	password = models.CharField(max_length=256);
	class Meta:
		db_table = 'proc_tenant_credentials'
