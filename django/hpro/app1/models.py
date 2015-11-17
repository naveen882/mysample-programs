from django.db import models
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import fields


#class UserProfile(models.Model):
#	user = models.ForeignKey(User)
#	created_date = models.DateTimeField(auto_now_add=True, db_index=True)
#	first_name = models.CharField(max_length=255)
#	last_name = models.CharField(max_length=255)
#	role = models.CharField(max_length=255)
#
#	class Meta:
#		db_table='up'
#		app_label = 'app1'



class Candidates(models.Model):
	version = models.IntegerField()
	current_employer_id = models.IntegerField(null=True)
	current_employer_text = models.CharField(max_length=100,null=True)
	current_location_id = models.IntegerField(null=True)
	date_of_birth = models.DateTimeField(null=True)
	final_degree_id = models.IntegerField(null=True)
	final_degree_text = models.CharField(max_length=100,null=True)
	final_department_id = models.IntegerField(null=True)
	final_department_text = models.CharField(max_length=70,null=True)
	gender = models.IntegerField(null=True)
	is_fresher = models.NullBooleanField() #models.SmallIntegerField(null=True) is small Int
	current_location_text = models.CharField(max_length=75,null=True)
	marital_status = models.IntegerField(null=True)
	opening_status_id = models.IntegerField(null=True)
	status_id = models.IntegerField(null=True)
	total_experience = models.IntegerField(null=True)
	notes = models.TextField()
	relevant_experience = models.IntegerField(null=True)
	expertise_id1 = models.IntegerField(null=True)
	expertise_text = models.CharField(max_length=50,null=True)
	expertise_id2 = models.IntegerField(null=True)
	hierarchy_id = models.IntegerField(null=True)
	hierarchy_text = models.CharField(max_length=50,null=True)
	university_id = models.IntegerField(null=True)
	university_text = models.CharField(max_length=100,null=True)
	email1 = models.CharField(max_length=100,null=True)
	email2 = models.CharField(max_length=100,null=True)
	first_name = models.CharField(max_length=75,null=True)
	importance = models.IntegerField()
	last_name = models.CharField(max_length=75,null=True)
	middle_name = models.CharField(max_length=75,null=True)
	mobile1 = models.CharField(max_length=75,null=True)
	phone_office = models.CharField(max_length=100,null=True)
	phone_residence = models.CharField(max_length=100,null=True)
	sensitivity = models.IntegerField(null=True)
	salutation = models.IntegerField(null=True)
	college_id = models.IntegerField(null=True)
	college_text = models.CharField(max_length=255,null=True)
	resume_grade_id = models.IntegerField(null=True)
	no_of_attachments = models.IntegerField()
	experience_updated_on = models.DateTimeField(null=True)
	technology_text = models.TextField()
	current_ctc = models.CharField(max_length=255,null=True)
	user_id = models.IntegerField(null=True)
	candidate_name = models.CharField(max_length=255,null=True)
	brownie_point_total = models.IntegerField(null=True)
	sourcer = models.IntegerField(null=True)
	sourcer_log = models.CharField(max_length=2000,null=True)
	crm_status_date = models.DateTimeField(null=True)
	address1 = models.CharField(max_length=255,null=True)
	address2 = models.CharField(max_length=255,null=True)
	address3 = models.CharField(max_length=255,null=True)
	notice_period = models.IntegerField(null=True)
	skill_id = models.IntegerField(null=True)
	current_source_id = models.IntegerField(null=True)
	sourcer_modified_date = models.DateTimeField(null=True)
	tenant_id = models.IntegerField(null=True)
	published_on = models.DateTimeField(null=True)
	published_by = models.IntegerField(null=True)
	is_active = models.NullBooleanField(default=1)
	is_draft = models.NullBooleanField()
	is_archived = models.NullBooleanField()
	true_false2 = models.NullBooleanField()
	true_false1 = models.NullBooleanField()
	integer2 = models.IntegerField(null=True)
	integer1 = models.IntegerField(null=True)
	text4 = models.CharField(max_length=1000,null=True)
	text3 = models.CharField(max_length=1000,null=True)
	text2 = models.CharField(max_length=1000,null=True)
	text1 = models.CharField(max_length=1000,null=True)
	is_alive = models.BooleanField(default=1)
	created_by = models.IntegerField()
	created_on = models.DateTimeField( auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	is_deleted = models.BooleanField(default=0)
	guid = models.CharField(max_length=40)
	candidateoriginalsourceinfo_id = models.IntegerField(null=True)
	candidatepreference_id = models.IntegerField(null=True)
	#candidatesourceinfo_id = models.IntegerField(null=True)
	percentage_or_cgp = models.FloatField(null=True) ##pending double DEFAULT NULL,
	is_percentage = models.NullBooleanField()
	original_candidate_id = models.IntegerField(null=True)
	pan_card = models.CharField(max_length=20,null=True)
	passport = models.CharField(max_length=10,null=True)
	percentage_of_duplication = models.IntegerField(null=True)
	candidateresumefulltext_id = models.IntegerField(null=True)
	candidatefulltext_id = models.IntegerField(null=True)
	country_code = models.CharField(max_length=10,null=True)
	bulk_custom_field_string = models.TextField()#longtext,
	is_black_listed = models.BooleanField(default=0)
	duplicate_or_blacklist_comment = models.CharField(max_length=5000,null=True)
	original_source_info_modified = models.DateTimeField(null=True)
	duplication_comment = models.CharField(max_length=5000,null=True)
	is_set_resume_status_to_crm = models.NullBooleanField()
	is_rejected = models.NullBooleanField()
	is_partial_duplicate = models.BooleanField(default=0)
	black_list_mode = models.IntegerField(default=0)
	soft_delete_type = models.IntegerField(default=0)
	candidate_photo_file_id = models.IntegerField(null=True)
	is_hirepro_vendor_candidate = models.NullBooleanField()
	is_utilized = models.BooleanField()
	audio_file_name = models.CharField(max_length=255,null=True)
	text5 = models.CharField(max_length=50,null=True)
	integer3 = models.IntegerField(null=True)
	integer4 = models.IntegerField(null=True)
	integer5 = models.IntegerField(null=True)
	password = models.CharField(max_length=255,null=True)
	owner_id = models.IntegerField(null=True)
	usn = models.CharField(max_length=45,null=True)
	country = models.IntegerField(null=True)
	nationality = models.IntegerField(null=True)
	familydetail_id = models.IntegerField(null=True)
	type_of_candidate = models.IntegerField(default=0)
	original_source_id = models.IntegerField(default=0)
	source_modified_by = models.IntegerField(null=True)
	source_modified_on = models.DateTimeField(null=True)
	originated_from = models.IntegerField(default=0)
	level_id = models.IntegerField(null=True)
	role_Id = models.IntegerField(null=True)
	mentor = models.IntegerField(null=True)
	buddies = models.CharField(max_length=100,null=True)
	bu_id = models.IntegerField(null=True)
	current_activity = models.IntegerField(null=True)
	activity_status = models.IntegerField(null=True)
	candidate_user_id = models.IntegerField(null=True)
	candidatestaffingprofile_id = models.IntegerField(null=True)
	current_experience = models.IntegerField(null=True)
	bpo_experience = models.IntegerField(null=True)
	date_custom_field1 = models.DateTimeField(null=True)
	date_custom_field2 = models.DateTimeField(null=True)
	text_area1 = models.CharField(max_length=3000,null=True)
	text_area2 = models.CharField(max_length=3000,null=True)
	text_area3 = models.CharField(max_length=3000,null=True)
	text_area4 = models.CharField(max_length=3000,null=True)
	candidate_photo_path = models.CharField(max_length=500,null=True)
	#uuid = models.CharField(max_length=32,null=True)
	#uid = models.CharField(max_length=32,null=True)
  #PRIMARY KEY (`id`),
  #KEY `candidatefulltext_id` (`candidatefulltext_id`),
  #KEY `email1` (`email1`),
  #KEY `tenant_id` (`tenant_id`)
#) #ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 |

	class Meta:
		db_table='candidates'

class Candidate_education_profiles(models.Model):
	college_id = models.IntegerField(null=True)
	college_text = models.CharField(max_length=100,null=True)
	degree_id = models.IntegerField(null=True)
	degree_text = models.CharField(max_length=100,null=True)
	degree_type_id = models.IntegerField(null=True)
	degree_type_text = models.CharField(max_length=50,null=True)
	end_year = models.IntegerField(null=True)
	is_final = models.NullBooleanField(null=True)
	percentage = models.DecimalField(max_digits=3, decimal_places=2,null=True)
	start_year = models.IntegerField(null=True)
	university_id = models.IntegerField(null=True)
	university_text = models.CharField(max_length=100,null=True)
	start_month = models.IntegerField(null=True)
	end_month = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add = True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	#candidate_id = models.IntegerField(null=True)
	education_type = models.IntegerField(default=1)
	is_percentage = models.NullBooleanField()
	institute_type_id = models.IntegerField(null=True)
	candidate = models.ForeignKey(Candidates,null=True)
	#PRIMARY KEY (`id`),
	#KEY `candidate_id` (`candidate_id`)
	#) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1 |


	class Meta:
		db_table='candidate_education_profiles'


class Candidate_work_profiles(models.Model):
	deisignation_id = models.IntegerField(null=True)
	designation_text = models.CharField(max_length=75,null=True)
	employer_id = models.IntegerField(null=True)
	employer_text = models.CharField(max_length=100,null=True)
	location_id = models.IntegerField(null=True)
	location_text = models.CharField(max_length=75,null=True)
	reason_for_leaving = models.TextField(null=True)
	yearly_salary = models.IntegerField(null=True)
	from_month = models.IntegerField(null=True)
	to_month = models.IntegerField(null=True)
	from_year = models.IntegerField(null=True)
	to_year = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	#candidate_id = models.IntegerField(null=True)
	candidate = models.ForeignKey(Candidates,null=True) #db_index=True
	bulk_custom_field_string = models.TextField(null=False)# longtext,
	is_latest = models.NullBooleanField()
	industry = models.IntegerField(null=True)
	expertise = models.IntegerField(null=True)
	sub_expertise = models.IntegerField(null=True)
	sub_expertise2 = models.IntegerField(null=True)
	title = models.CharField(max_length=55,null=True)
	#PRIMARY KEY (`id`),
	#KEY `candidate_id` (`candidate_id`)
	#) ENGINE=InnoDB DEFAULT CHARSET=latin1 |

	class Meta:
		db_table = 'candidate_work_profiles'

class Candidate_location_preferences(models.Model):
	location_id = models.IntegerField()
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	candidatepreference_id = models.IntegerField(null=True)
	location_text = models.CharField(max_length=50,null=True)

	class Meta:
		db_table = 'candidate_location_preferences'


class Candidate_preferences(models.Model):
	#desired_salary_from = models.DecimalField(max_digits=8, decimal_places=2,null=True)
	#desired_salary_to = models.DecimalField(max_digits=8, decimal_places=2,null=True)
	desired_salary_from = models.FloatField(null=True)
	desired_salary_to = models.FloatField(null=True)
	desired_title_id = models.IntegerField(null=True)
	desired_title_text = models.CharField(max_length=50,null=True)
	job_category_id1 = models.IntegerField(null=True)
	job_category_text = models.CharField(max_length=50,null=True)
	notes = models.CharField(max_length=255,null=True)
	other_compensation = models.CharField(max_length=255,null=True)
	is_willing_to_relocate = models.NullBooleanField()
	job_category_id2 = models.IntegerField(null=True)
	job_category_id3 = models.IntegerField(null=True)
	job_category_id4 = models.IntegerField(null=True)
	company_type_id = models.IntegerField(null=True)
	company_type_text = models.CharField(max_length=50,null=True)
	company_sub_type_id = models.IntegerField(null=True)
	company_sub_type_text = models.CharField(max_length=50,null=True)
	notice_period = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)

	class Meta:
		db_table = 'candidate_preferences'

class Attachments(models.Model):
	version = models.IntegerField()
	attachment_type_id = models.IntegerField(null=True)
	tenant_id = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	is_deleted = models.BooleanField()
	guid = models.CharField(max_length=40)
	source_item_type = models.CharField(max_length=255,null=True)
	source_item_id = models.IntegerField(null=True)
	target_item_type = models.CharField(max_length=255,null=True)
	target_item_id = models.IntegerField(null=True)#file id

	class Meta:
		db_table = 'attachments'

class Files(models.Model):
	version = models.IntegerField()
	title = models.TextField()
	original_file_name = models.TextField()
	file_type_id = models.IntegerField(null=True)
	file_type_text = models.CharField(max_length=255,null=True)
	file_format_id = models.IntegerField(null=True)
	file_size = models.BigIntegerField()
	is_compressed = models.NullBooleanField()
	is_encrypted = models.NullBooleanField()
	target_path = models.TextField()
	file_created_on = models.DateTimeField(auto_now_add=True)
	file_modified_on = models.DateTimeField(auto_now_add=True)
	tenant_id = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	is_deleted = models.BooleanField()
	guid = models.CharField(max_length=40)
	filecontent_id = models.IntegerField(null=True)

	class Meta:
		db_table = 'files'

class Candidate_full_texts(models.Model):
	candidate_resume_full_text = models.TextField(null=True)
	candidate_id = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	tenant_id = models.IntegerField(null=True)
	rank = models.IntegerField(null=True)

	class Meta:
		db_table = 'candidate_full_texts'

	def clean(self):
		if (self.created_by is None):
			raise ValidationError('Validation Error')

class Candidate_salarys(models.Model):
	date_created = models.DateTimeField(null=True)
	company_name = models.CharField(max_length=100,null=True)
	basic = models.FloatField(null=True)
	flexible = models.FloatField(null=True)
	pf = models.FloatField(null=True)
	performance_bonus = models.FloatField(null=True)
	gratuity = models.FloatField(null=True)
	super_annuation = models.FloatField(null=True)
	insurance = models.FloatField(null=True)
	medical = models.FloatField(null=True)
	stocks = models.CharField(max_length=255,null=True)
	comments = models.CharField(max_length=255,null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	candidate_id = models.IntegerField(null=True)
	offer_id = models.IntegerField(null=True)
	currency = models.IntegerField(null=True)

	class Meta:
		db_table = 'candidate_salarys'

class Candidate_social_network_details(models.Model):
	version = models.IntegerField()
	face_book_link = models.CharField(max_length=255,null=True)
	face_book_details = models.CharField(max_length=255,null=True)
	twitter_link = models.CharField(max_length=255,null=True)
	twitter_details = models.CharField(max_length=255,null=True)
	linked_in_link = models.CharField(max_length=255,null=True)
	linked_in_details = models.CharField(max_length=255,null=True)
	candidate_id = models.IntegerField()
	tenant_id = models.IntegerField(null=True)
	created_by = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	modified_by = models.IntegerField(null=True)
	modified_on = models.DateTimeField(null=True)
	is_deleted = models.BooleanField()
	guid = models.CharField(max_length=40)

	class Meta:
		db_table = 'candidate_social_network_details'


class CandidatePreferences(models.Model):
    desired_salary_from = models.FloatField(blank=True, null=True)
    desired_salary_to = models.FloatField(blank=True, null=True)
    desired_title_id = models.IntegerField(blank=True, null=True)
    desired_title_text = models.CharField(max_length=50, blank=True, null=True)
    job_category_id1 = models.IntegerField(blank=True, null=True)
    job_category_text = models.CharField(max_length=50, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    other_compensation = models.CharField(max_length=255, blank=True, null=True)
    is_willing_to_relocate = models.IntegerField(blank=True, null=True)
    job_category_id2 = models.IntegerField(blank=True, null=True)
    job_category_id3 = models.IntegerField(blank=True, null=True)
    job_category_id4 = models.IntegerField(blank=True, null=True)
    company_type_id = models.IntegerField(blank=True, null=True)
    company_type_text = models.CharField(max_length=50, blank=True, null=True)
    company_sub_type_id = models.IntegerField(blank=True, null=True)
    company_sub_type_text = models.CharField(max_length=50, blank=True, null=True)
    notice_period = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_preferences'

class CandidateLocationPreferences(models.Model):
    location_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidatepreference_id = models.IntegerField(blank=True, null=True)
    location_text = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_location_preferences'

class CatalogValues(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    catalogmaster_id = models.IntegerField(blank=True, null=True)
    catalogvalue_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_values'


class Technologys(models.Model):
    technology_id = models.IntegerField()
    order_number = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'technologys'


class Users(models.Model):
    version = models.IntegerField()
    login_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=510, blank=True, null=True)
    password_question = models.CharField(max_length=100, blank=True, null=True)
    password_answer = models.CharField(max_length=50, blank=True, null=True)
    is_approved = models.IntegerField()
    last_login_date = models.DateTimeField(blank=True, null=True)
    is_on_line = models.IntegerField()
    is_locked_out = models.IntegerField()
    signature = models.CharField(max_length=255, blank=True, null=True)
    is_system = models.IntegerField()
    email1 = models.CharField(max_length=50, blank=True, null=True)
    email2 = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=75, blank=True, null=True)
    last_name = models.CharField(max_length=75, blank=True, null=True)
    middle_name = models.CharField(max_length=75, blank=True, null=True)
    mobile1 = models.CharField(max_length=20, blank=True, null=True)
    phone_office = models.CharField(max_length=20, blank=True, null=True)
    phone_residence = models.CharField(max_length=20, blank=True, null=True)
    salutation = models.IntegerField()
    password_hash = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.IntegerField()
    type_of_user = models.IntegerField(blank=True, null=True)
    password_question_id = models.IntegerField(blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    current_login_date = models.DateTimeField(blank=True, null=True)
    email_password = models.CharField(max_length=255, blank=True, null=True)
    is_pop3_listener = models.IntegerField(blank=True, null=True)
    is_email_extraction_required = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    is_password_auto_generated = models.IntegerField(blank=True, null=True)
    userprofile_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=75, blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    is_master_vendor_user = models.IntegerField(blank=True, null=True)
    last_password_changed_date = models.DateTimeField(blank=True, null=True)
    browser_details = models.CharField(max_length=45, blank=True, null=True)
    operating_system_details = models.CharField(max_length=45, blank=True, null=True)
    last_login_ip = models.CharField(max_length=45, blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    is_disabled = models.IntegerField()
    login_failed_count = models.IntegerField()
    is_archived = models.IntegerField()
    location_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Sources(models.Model):
    version = models.IntegerField()
    source_name = models.CharField(max_length=75, blank=True, null=True)
    email1 = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    site_url = models.CharField(max_length=55, blank=True, null=True)
    types_of_source = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    no_of_attachments = models.IntegerField(blank=True, null=True)
    published_on = models.DateTimeField(blank=True, null=True)
    published_by = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_draft = models.IntegerField(blank=True, null=True)
    is_archived = models.IntegerField(blank=True, null=True)
    is_alive = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    is_extractor_listener_required = models.IntegerField(blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=55, blank=True, null=True)
    mobile1 = models.CharField(max_length=55, blank=True, null=True)
    phone_office = models.CharField(max_length=55, blank=True, null=True)
    contract_id = models.IntegerField(blank=True, null=True)
    color_code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sources'


class CandidateOriginalSourceInfos(models.Model):
    source_id = models.IntegerField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_original_source_infos'


#==========================Tenant DB============================================
class EntityPropertys(models.Model):
    version = models.IntegerField()
    property_name = models.CharField(max_length=255, blank=True, null=True)
    entity_type = models.IntegerField(blank=True, null=True)
    property_type = models.CharField(max_length=255, blank=True, null=True)
    is_custom_property = models.IntegerField(blank=True, null=True)
    property_code = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    mandatory_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_propertys'
        app_label = '9999'			


class EntityPropertyDefinitions(models.Model):
    property_label = models.CharField(max_length=255, blank=True, null=True)
    property_order = models.IntegerField(blank=True, null=True)
    is_mandatory = models.IntegerField(blank=True, null=True)
    is_catalog = models.IntegerField(blank=True, null=True)
    master_name_if_catalog = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    entityproperty_id = models.IntegerField(blank=True, null=True)
    is_not_visible = models.IntegerField(blank=True, null=True)
    is_visible_in_grid = models.IntegerField(blank=True, null=True)
    is_visible_in_search = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_property_definitions'
        app_label = '9999'			

class Proctoring(models.Model):
    file_path = models.CharField(max_length=1024, blank=True, null=True)
    user_id = models.IntegerField()
    tenant_id = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True,)
    suspicious_flag =  models.BooleanField(default=0)
    review_status = models.BooleanField(default=0)
    duration = models.IntegerField()
    is_deleted =  models.BooleanField(default=0)

class QpGroups(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    instruction_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    questionpaperinfo_id = models.IntegerField(blank=True, null=True)
    sub_category_id = models.IntegerField(blank=True, null=True)
    blueprint_id = models.IntegerField(blank=True, null=True)
    question_tenant_type = models.IntegerField(blank=True, null=True)
    total_questions = models.IntegerField(blank=True, null=True)
    foreign_group_id = models.IntegerField(blank=True, null=True)
    instruction_text = models.CharField(max_length=255, blank=True, null=True)
    group_tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qp_groups'
        app_label = '9999'			


class Sections(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    instruction_id = models.IntegerField(blank=True, null=True)
    sub_category_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    qpgroup_id = models.IntegerField(blank=True, null=True)
    no_of_questions_to_display = models.IntegerField(blank=True, null=True)
    question_type = models.IntegerField(blank=True, null=True)
    sub_topic_id = models.IntegerField(blank=True, null=True)
    is_revised = models.IntegerField()
    foreign_section_id = models.IntegerField(blank=True, null=True)
    instruction_text = models.CharField(max_length=255, blank=True, null=True)
    section_tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sections'
        app_label = '9999'			


class TestResults(models.Model):
    question_id = models.IntegerField()
    answer_string = models.CharField(max_length=7000, blank=True, null=True)
    is_subjective = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    testuser_id = models.IntegerField(blank=True, null=True)
    obtained_marks = models.FloatField(blank=True, null=True)
    time_spent = models.FloatField(blank=True, null=True)
    section_id = models.IntegerField(blank=True, null=True)
    question_tenant_id = models.IntegerField(blank=True, null=True)
    is_statistics_completed = models.IntegerField()
    coding_language_id = models.IntegerField(blank=True, null=True)
    result_status = models.IntegerField(blank=True, null=True)
    code_server_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_results'
        app_label = '9999'			


class TestUsers(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    total_score = models.FloatField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    candidate_regn_id = models.CharField(max_length=255, blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    log_out_time = models.DateTimeField(blank=True, null=True)
    login_id = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_login_info_sent = models.IntegerField()
    normal_distribution = models.FloatField(blank=True, null=True)
    percentile = models.FloatField(blank=True, null=True)
    correct_answers = models.IntegerField(blank=True, null=True)
    in_correct_answers = models.IntegerField(blank=True, null=True)
    un_attended_questions = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    is_password_disabled = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    total_no_of_subjective_questions = models.IntegerField(blank=True, null=True)
    is_partially_evaluated = models.IntegerField(blank=True, null=True)
    enable_last_session = models.IntegerField()
    is_dummy = models.IntegerField(blank=True, null=True)
    is_candidate_registered = models.IntegerField(blank=True, null=True)
    client_system_info = models.CharField(max_length=255, blank=True, null=True)
    is_offline = models.IntegerField()
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    candidate_email = models.CharField(max_length=255, blank=True, null=True)
    reactivated_count = models.IntegerField()
    time_spent = models.FloatField(blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    is_submission_failed = models.IntegerField()
    is_test_user_exported = models.IntegerField(blank=True, null=True)
    current_employer_id = models.IntegerField(blank=True, null=True)
    current_employer_text = models.CharField(max_length=45, blank=True, null=True)
    total_experience = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_users'
        app_label = '9999'			

class CandidateScores(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    correct_anwers = models.IntegerField(blank=True, null=True)
    in_correct_answers = models.IntegerField(blank=True, null=True)
    qn_paper_id = models.CharField(max_length=255, blank=True, null=True)
    qn_paper_code = models.CharField(max_length=255, blank=True, null=True)
    un_attended_questions = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    testuser_id = models.IntegerField(blank=True, null=True)
    candidatescore_id = models.IntegerField(blank=True, null=True)
    total_no_of_subjective_questions = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_scores'
        app_label = '9999'			

class Tests(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255)
    valid_from = models.DateTimeField()
    experience_from = models.IntegerField()
    expertise_id = models.IntegerField(blank=True, null=True)
    technology = models.CharField(max_length=255)
    no_of_candidates = models.IntegerField(blank=True, null=True)
    is_approved = models.IntegerField(blank=True, null=True)
    valid_to = models.DateTimeField()
    test_duration = models.FloatField(blank=True, null=True)
    test_code = models.CharField(max_length=255, blank=True, null=True)
    permissible_late_time = models.IntegerField(blank=True, null=True)
    test_start_time = models.DateTimeField(blank=True, null=True)
    test_end_time = models.DateTimeField(blank=True, null=True)
    is_all_time_permissible = models.IntegerField()
    is_accepted = models.IntegerField(blank=True, null=True)
    no_of_questions_per_page = models.IntegerField(blank=True, null=True)
    about_test = models.TextField(blank=True, null=True)
    purpose_of_test = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    hierarchy_id = models.IntegerField(blank=True, null=True)
    experience_to = models.IntegerField(blank=True, null=True)
    question_paper_id = models.IntegerField(blank=True, null=True)
    correct = models.FloatField(blank=True, null=True)
    in_correct = models.FloatField(blank=True, null=True)
    left_entries = models.FloatField(blank=True, null=True)
    max_marks = models.FloatField(blank=True, null=True)
    instant_evaluation = models.IntegerField()
    mean = models.FloatField(blank=True, null=True)
    standard_deviation = models.FloatField(blank=True, null=True)
    group_wise_timing = models.IntegerField()
    question_randomizing = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    published_on = models.DateTimeField(blank=True, null=True)
    published_by = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_draft = models.IntegerField(blank=True, null=True)
    is_archived = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
    integer2 = models.IntegerField(blank=True, null=True)
    integer1 = models.IntegerField(blank=True, null=True)
    text4 = models.CharField(max_length=50, blank=True, null=True)
    text3 = models.CharField(max_length=50, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    text1 = models.CharField(max_length=50, blank=True, null=True)
    is_alive = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    que_paper_tenantid = models.IntegerField(blank=True, null=True)
    is_test_active = models.IntegerField(blank=True, null=True)
    primary_owner_id = models.IntegerField(blank=True, null=True)
    template_id = models.IntegerField(blank=True, null=True)
    automate_tagging = models.IntegerField(blank=True, null=True)
    selecting_criteria = models.FloatField(blank=True, null=True)
    is_instant_result = models.IntegerField(blank=True, null=True)
    integer3 = models.IntegerField(blank=True, null=True)
    integer4 = models.IntegerField(blank=True, null=True)
    integer5 = models.IntegerField(blank=True, null=True)
    text5 = models.CharField(max_length=50, blank=True, null=True)
    is_online = models.IntegerField(blank=True, null=True)
    is_option_randomize = models.IntegerField()
    is_shuffle_question_order = models.IntegerField()
    blue_print_id = models.IntegerField(blank=True, null=True)
    event_name = models.CharField(max_length=255, blank=True, null=True)
    multiplicity_offline = models.IntegerField(blank=True, null=True)
    multiplicity_online = models.IntegerField(blank=True, null=True)
    is_published = models.IntegerField(blank=True, null=True)
    logo_file_id = models.IntegerField(blank=True, null=True)
    number_of_question_papers = models.IntegerField(blank=True, null=True)
    footer = models.CharField(max_length=255, blank=True, null=True)
    header = models.CharField(max_length=255, blank=True, null=True)
    logo_position = models.IntegerField(blank=True, null=True)
    page_number_position = models.IntegerField(blank=True, null=True)
    end_instruction = models.CharField(max_length=255, blank=True, null=True)
    presentation_file_id = models.IntegerField(blank=True, null=True)
    number_of_attachments = models.IntegerField()
    is_sent_for_approval = models.IntegerField(blank=True, null=True)
    event_details = models.CharField(max_length=255, blank=True, null=True)
    type_of_test = models.IntegerField()
    rejecting_criteria = models.FloatField(blank=True, null=True)
    is_manual_selection_criteria = models.IntegerField()
    type_of_shortlisting_criteria = models.IntegerField(blank=True, null=True)
    config = models.CharField(max_length=2000, blank=True, null=True)
    ip_configuration_text = models.TextField(blank=True, null=True)
    ip_address_config = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tests'
        app_label = '9999'			
