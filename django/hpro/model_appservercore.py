{'159': 'db1', '158': 'db15', '219': 'db11', '115': 'db10', '131': 'db14', '70': 'db3', '574': 'db2', '9999': 'db16', '18': 'db8', '1': 'db1', '183': 'db9', '3': 'db12'}
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Academics(models.Model):
    branch_id = models.IntegerField(blank=True, null=True)
    degree_id = models.IntegerField(blank=True, null=True)
    cut_off_from = models.FloatField(blank=True, null=True)
    cut_off_to = models.FloatField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    eligibilitycriteria = models.ForeignKey('EligibilityCriterias', blank=True, null=True)
    num_of_hiring = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=45, blank=True, null=True)
    is_percentage = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'academics'


class ActionEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link_to_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    target_id = models.IntegerField(blank=True, null=True)
    link_to_id_type = models.CharField(max_length=255, blank=True, null=True)
    target_id_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'action_events'


class Actions(models.Model):
    version = models.IntegerField()
    action_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    module_id = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    depend_on_action_id = models.IntegerField(blank=True, null=True)
    action_label = models.CharField(max_length=255)
    action_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions'


class ActivityCoordinators(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    staffingactivity = models.ForeignKey('StaffingActivitys', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_coordinators'


class ActivityGroups(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    staffingactivity = models.ForeignKey('StaffingActivitys', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_groups'


class ActivityStatusCallbackConfig(models.Model):
    version = models.IntegerField()
    title = models.CharField(max_length=250, blank=True, null=True)
    activity_id = models.IntegerField(blank=True, null=True)
    type_of_candidate = models.IntegerField(blank=True, null=True)
    entity_type = models.IntegerField(blank=True, null=True)
    entity_id = models.IntegerField(blank=True, null=True)
    activity_status_action = models.IntegerField(blank=True, null=True)
    activity_completed_status = models.IntegerField(blank=True, null=True)
    next_action_valule = models.CharField(max_length=250, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_status_callback_config'


class Activitys(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    time_limit = models.IntegerField(blank=True, null=True)
    activity_owner = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activitys'


class AnswerChoices(models.Model):
    choice = models.CharField(max_length=1, blank=True, null=True)
    answer = models.CharField(max_length=2048, blank=True, null=True)
    html_string = models.TextField(blank=True, null=True)
    no_of_attachments = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    marks = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer_choices'


class Answers(models.Model):
    correct_answer = models.CharField(max_length=7000, blank=True, null=True)
    html_string = models.TextField(blank=True, null=True)
    no_of_attachments = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class AppPreferences(models.Model):
    version = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=45)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_preferences'


class ApplicantEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_events'


class ApplicantReports(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    current_organization = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    previous_status = models.CharField(max_length=255, blank=True, null=True)
    current_status = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    applicant_report_type = models.IntegerField(blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_reports'


class ApplicantStatusItems(models.Model):
    version = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    applican_status_date = models.DateTimeField(blank=True, null=True)
    no_of_attachments = models.IntegerField()
    is_private = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    applicantstatus_id = models.IntegerField(blank=True, null=True)
    applicant_status_reason_id = models.IntegerField(blank=True, null=True)
    applicant_status_reason_text = models.CharField(max_length=1000, blank=True, null=True)
    is_feedback_exists = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_status_items'


class ApplicantStatusReasons(models.Model):
    status_reason_value = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    resumestatus_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_status_reasons'


class ApplicantStatusReports(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    previous_status = models.CharField(max_length=255, blank=True, null=True)
    current_status = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_status_reports'


class ApplicantStatuss(models.Model):
    current_status_id = models.IntegerField()
    forwarded_date = models.DateTimeField(blank=True, null=True)
    candidate_spoc = models.IntegerField(blank=True, null=True)
    resume_type_id = models.IntegerField(blank=True, null=True)
    rotated_by = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    offer_id = models.IntegerField(blank=True, null=True)
    interviewrequest_id = models.IntegerField(blank=True, null=True)
    position_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    applicant_status_manager_id = models.IntegerField(blank=True, null=True)
    recruitevent_id = models.IntegerField(blank=True, null=True)
    current_status_reason_id = models.IntegerField(blank=True, null=True)
    applicant_status_reason_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField()
    master_job_requisition_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_statuss'


class ApplicantTestInfos(models.Model):
    test_id = models.IntegerField()
    applicant_status_item_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_test_infos'


class ApplicantsBySources(models.Model):
    version = models.IntegerField()
    source_id = models.IntegerField()
    candidate_id = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField()
    is_deleted = models.IntegerField(blank=True, null=True)
    guid = models.CharField(max_length=45)
    job_id = models.IntegerField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicants_by_sources'


class ApprovalConfigurations(models.Model):
    version = models.IntegerField()
    entity_type_id = models.IntegerField()
    level = models.IntegerField(blank=True, null=True)
    notification_prefrence_id = models.IntegerField(blank=True, null=True)
    operation_id = models.IntegerField(blank=True, null=True)
    types_of_approval_configuration = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    entity_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'approval_configurations'


class ApprovalEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    entity_id = models.IntegerField(blank=True, null=True)
    entity_type_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approval_events'


class Approvers(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    approvalconfiguration_id = models.IntegerField(blank=True, null=True)
    approver_department = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approvers'


class AssessedFeedbacks(models.Model):
    candidate_id = models.IntegerField()
    skill_id = models.IntegerField()
    marks = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    configassessmentfeedback_id = models.IntegerField(blank=True, null=True)
    is_applicable = models.TextField(blank=True, null=True)  # This field type is a guess.
    applicant_status_item_id = models.IntegerField(db_column='applicant_status_item_Id')  # Field name made lowercase.
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assessed_feedbacks'


class AssessmentApprovalConfigurations(models.Model):
    question_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_approval_configurations'


class AssessmentLines(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'assessment_lines'


class AssessmentLogs(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    question_paper_id = models.IntegerField(blank=True, null=True)
    blue_print_id = models.IntegerField(blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_logs'


class AssessmentTemplates(models.Model):
    assessment_template_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_vendor_screening_template = models.IntegerField(blank=True, null=True)
    is_archived = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'assessment_templates'


class AssignedTaskActors(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_group_id = models.IntegerField(blank=True, null=True)
    task_actor_type = models.IntegerField(blank=True, null=True)
    assignedtask = models.ForeignKey('AssignedTasks', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assigned_task_actors'


class AssignedTaskHistorys(models.Model):
    status = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    assignedtask = models.ForeignKey('AssignedTasks', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assigned_task_historys'


class AssignedTasks(models.Model):
    version = models.IntegerField()
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    assignee_user = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    is_visible_to_candidate = models.IntegerField(blank=True, null=True)
    reporter_department = models.IntegerField(blank=True, null=True)
    approver_department = models.IntegerField(blank=True, null=True)
    assignee_department = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    activity_id = models.IntegerField(blank=True, null=True)
    candidate_group = models.IntegerField(blank=True, null=True)
    form_id = models.IntegerField(blank=True, null=True)
    filled_form_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    reported_date = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    approver_user = models.IntegerField(blank=True, null=True)
    reporter_user = models.IntegerField(blank=True, null=True)
    reporter_group = models.IntegerField(blank=True, null=True)
    approver_group = models.IntegerField(blank=True, null=True)
    assignee_group = models.IntegerField(blank=True, null=True)
    is_auto_approved = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assigned_tasks'


class Attachments(models.Model):
    version = models.IntegerField()
    attachment_type_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    source_item_type = models.CharField(max_length=255, blank=True, null=True)
    source_item_id = models.IntegerField(blank=True, null=True)
    target_item_type = models.CharField(max_length=255, blank=True, null=True)
    target_item_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments'


class AuthorizationCredentials(models.Model):
    version = models.IntegerField()
    role_name = models.CharField(max_length=255, blank=True, null=True)
    action_id = models.IntegerField()
    tenant_alias = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authorization_credentials'


class Bfsicandidates(models.Model):
    candidate_id = models.IntegerField(primary_key=True)
    driving_licence = models.CharField(max_length=255, blank=True, null=True)
    is_apply_driving_licence = models.IntegerField(blank=True, null=True)
    vehicle_type = models.CharField(max_length=255, blank=True, null=True)
    is_apply_pancard = models.IntegerField(blank=True, null=True)
    is_apply_passport = models.IntegerField(blank=True, null=True)
    number_of_offers = models.IntegerField(blank=True, null=True)
    land_mark_of_current_address = models.CharField(max_length=255, blank=True, null=True)
    land_mark_of_permanent_address = models.CharField(max_length=255, blank=True, null=True)
    cast_id = models.IntegerField(blank=True, null=True)
    cast_text = models.CharField(max_length=255, blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    category_text = models.CharField(max_length=255, blank=True, null=True)
    religion_id = models.IntegerField(blank=True, null=True)
    religion_text = models.CharField(max_length=255, blank=True, null=True)
    familydetail_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bfsicandidates'


class BluePrints(models.Model):
    version = models.IntegerField()
    blue_print_name = models.CharField(max_length=45, blank=True, null=True)
    total_questions = models.IntegerField(blank=True, null=True)
    questions_pattern = models.IntegerField(blank=True, null=True)
    split_ratio = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
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
    foreign_blue_print_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blue_prints'


class BrowniePointRedemptions(models.Model):
    version = models.IntegerField()
    redemption_type = models.IntegerField()
    referral_contact_type = models.IntegerField(blank=True, null=True)
    referral_contact_id = models.IntegerField()
    cash_amount = models.IntegerField()
    gift_catalog_id = models.IntegerField()
    equivalent_brownie_points = models.IntegerField()
    redemption_status = models.IntegerField()
    tds_amount = models.IntegerField()
    name_on_cheque = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'brownie_point_redemptions'


class BrowniePoints(models.Model):
    applicant_status = models.CharField(max_length=50)
    point = models.IntegerField()
    calculated_point = models.IntegerField()
    code = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brownie_points'


class BulkInterviewers(models.Model):
    interviewer = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    bulkinterview_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulk_interviewers'


class BulkInterviews(models.Model):
    version = models.IntegerField()
    interview_stage = models.IntegerField(blank=True, null=True)
    interview_round = models.IntegerField(blank=True, null=True)
    interview_address = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    batch_size = models.IntegerField(blank=True, null=True)
    interviews_before_break = models.IntegerField(blank=True, null=True)
    break_duration = models.IntegerField(blank=True, null=True)
    first_batch_start_time = models.DateTimeField(blank=True, null=True)
    final_batch_end_time = models.DateTimeField(blank=True, null=True)
    interview_days = models.CharField(max_length=255, blank=True, null=True)
    is_interview_scheduled = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    day_of_interview = models.IntegerField(blank=True, null=True)
    last_interviewed_batch = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    is_time_un_scheduled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulk_interviews'


class BusinessPlans(models.Model):
    version = models.IntegerField()
    financial_year = models.IntegerField()
    quarter = models.CharField(max_length=255, blank=True, null=True)
    business_unit_id = models.IntegerField()
    year_plan = models.FloatField()
    quarter_plan = models.FloatField()
    business_unit_name = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'business_plans'


class BusinessUnits(models.Model):
    version = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    geography = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    company_id = models.IntegerField(blank=True, null=True)
    businessunit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_units'


class CallLogReports(models.Model):
    description = models.TextField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'call_log_reports'


class CampusApprovalConfigurations(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    job_role_id = models.IntegerField(blank=True, null=True)
    business_unit_id = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_approval_configurations'


class CampusCalendars(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField(blank=True, null=True)
    detail = models.CharField(max_length=1024, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campusinformation = models.ForeignKey('CampusInformations', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_calendars'


class CampusCollegeTypes(models.Model):
    college_type_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campusinformation = models.ForeignKey('CampusInformations', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_college_types'


class CampusContactInfos(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)
    contact_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    photo_file_path = models.CharField(max_length=256, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campusinformation = models.ForeignKey('CampusInformations', blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_contact_infos'


class CampusCourseCurriculums(models.Model):
    course_ids = models.CharField(max_length=256, blank=True, null=True)
    academic_index = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campuscourse = models.ForeignKey('CampusCourses', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_course_curriculums'


class CampusCourses(models.Model):
    degree_id = models.IntegerField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    academic_format = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campusinformation = models.ForeignKey('CampusInformations', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_courses'


class CampusCriterias(models.Model):
    campus_id = models.IntegerField(blank=True, null=True)
    year_of_passing = models.IntegerField(blank=True, null=True)
    eligibility_criteria_id = models.IntegerField(blank=True, null=True)
    salary_package_id = models.IntegerField(blank=True, null=True)
    hiring_number = models.IntegerField(blank=True, null=True)
    is_prior_experience = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    month_of_passing = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_criterias'


class CampusEntranceCriterias(models.Model):
    degree_id = models.IntegerField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    entrance_exam = models.IntegerField(blank=True, null=True)
    opening_rank = models.IntegerField(blank=True, null=True)
    closing_rank = models.IntegerField(blank=True, null=True)
    criteria = models.CharField(max_length=1024, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campusinformation = models.ForeignKey('CampusInformations', blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_entrance_criterias'


class CampusEventActivityComments(models.Model):
    comment = models.CharField(max_length=1000, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campuseventactivity = models.ForeignKey('CampusEventActivitys', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_event_activity_comments'


class CampusEventActivitys(models.Model):
    activity_type_id = models.IntegerField(blank=True, null=True)
    date_from = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruitevent = models.ForeignKey('RecruitEvents', blank=True, null=True)
    completed_on = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    started_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_event_activitys'


class CampusEventCandidates(models.Model):
    recruit_event_id = models.IntegerField(blank=True, null=True)
    campus_candidate_id = models.IntegerField(blank=True, null=True)
    corporate_candidate_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    campus_tenant_id = models.IntegerField(blank=True, null=True)
    corporate_tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_event_candidates'


class CampusGroups(models.Model):
    version = models.IntegerField()
    source_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    source_tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_groups'


class CampusImages(models.Model):
    type = models.IntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=256, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campusinformation = models.ForeignKey('CampusInformations', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_images'


class CampusInformations(models.Model):
    version = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    year_of_establishment = models.IntegerField(blank=True, null=True)
    campus_overview = models.CharField(max_length=2048, blank=True, null=True)
    university_id = models.IntegerField(blank=True, null=True)
    campus_type = models.IntegerField(blank=True, null=True)
    campus_id = models.IntegerField()
    campus_diversity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_informations'


class CampusInfrastructures(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    infrastructure_type_id = models.IntegerField(blank=True, null=True)
    infrastructure_detail_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=1024, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campusinformation = models.ForeignKey(CampusInformations, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_infrastructures'


class CampusInternshipDetails(models.Model):
    degree_id = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    duration_type = models.IntegerField(blank=True, null=True)
    from_date_month = models.DateTimeField(blank=True, null=True)
    to_date_month = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campusinformation = models.ForeignKey(CampusInformations, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_internship_details'


class CampusInterviewers(models.Model):
    interviewer = models.IntegerField(blank=True, null=True)
    interviewer_comments = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_interviewed = models.IntegerField()
    applicantstatusitem_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_interviewers'


class CampusOffers(models.Model):
    company_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_offers'


class CampusPlacementTrends(models.Model):
    year = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    industry_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    branches_allowed = models.CharField(max_length=50, blank=True, null=True)
    degrees_allowed = models.CharField(max_length=50, blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    degree_id = models.IntegerField(blank=True, null=True)
    salary_offered_from = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_offered_to = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    comment = models.CharField(max_length=1024, blank=True, null=True)
    hiring_type = models.IntegerField(blank=True, null=True)
    placement_number = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    percentage_from = models.FloatField(blank=True, null=True)
    percentage_to = models.FloatField(blank=True, null=True)
    is_percentage = models.IntegerField(blank=True, null=True)
    visit_date_from = models.DateTimeField(blank=True, null=True)
    visit_date_to = models.DateTimeField(blank=True, null=True)
    num_of_offers = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campusinformation = models.ForeignKey(CampusInformations, blank=True, null=True)
    currency = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_placement_trends'


class CampusRankings(models.Model):
    year = models.IntegerField(blank=True, null=True)
    ranking_agency = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=1024, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    campusinformation = models.ForeignKey(CampusInformations, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_rankings'


class Campuss(models.Model):
    source_id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campuss'


class CandidateActivitys(models.Model):
    version = models.IntegerField()
    candidate_id = models.IntegerField(blank=True, null=True)
    activity_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_activitys'


class CandidateBuddys(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_buddys'


class CandidateCompanyPreferences(models.Model):
    company_id = models.IntegerField(blank=True, null=True)
    priority_id = models.IntegerField(blank=True, null=True)
    priority_text = models.CharField(max_length=30, blank=True, null=True)
    company_text = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidatepreference_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_company_preferences'


class CandidateEditPropertyInfos(models.Model):
    type_of_object = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)
    property_name = models.CharField(max_length=255, blank=True, null=True)
    edited_value = models.CharField(max_length=255, blank=True, null=True)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    is_removed = models.IntegerField(blank=True, null=True)
    collection_index = models.IntegerField(blank=True, null=True)
    property_type = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidateeditrequest_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_edit_property_infos'


class CandidateEditRequests(models.Model):
    version = models.IntegerField()
    candidate_id = models.IntegerField()
    status_id = models.IntegerField(blank=True, null=True)
    reason_of_rejection = models.TextField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
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
    candidateuploadresume_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_edit_requests'


class CandidateEducationProfiles(models.Model):
    college_id = models.IntegerField(blank=True, null=True)
    college_text = models.CharField(max_length=100, blank=True, null=True)
    degree_id = models.IntegerField(blank=True, null=True)
    degree_text = models.CharField(max_length=100, blank=True, null=True)
    degree_type_id = models.IntegerField(blank=True, null=True)
    degree_type_text = models.CharField(max_length=50, blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    is_final = models.IntegerField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    university_id = models.IntegerField(blank=True, null=True)
    university_text = models.CharField(max_length=100, blank=True, null=True)
    start_month = models.IntegerField(blank=True, null=True)
    end_month = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    education_type = models.IntegerField()
    is_percentage = models.IntegerField(blank=True, null=True)
    institute_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_education_profiles'


class CandidateEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_events'


class CandidateFullTexts(models.Model):
    candidate_resume_full_text = models.TextField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_full_texts'


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


class CandidatePofuCategorizations(models.Model):
    version = models.IntegerField()
    category = models.CharField(max_length=255, blank=True, null=True)
    no_of_calls = models.IntegerField()
    no_of_days = models.IntegerField()
    tenant_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'candidate_pofu_categorizations'


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


class CandidateProjectProfiles(models.Model):
    company_id = models.IntegerField(blank=True, null=True)
    company_text = models.CharField(max_length=100, blank=True, null=True)
    datetime_ended = models.DateTimeField(blank=True, null=True)
    datetime_started = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    role_text = models.CharField(max_length=50, blank=True, null=True)
    technology_text = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidateworkprofile_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_project_profiles'


class CandidateRegisters(models.Model):
    security_code = models.CharField(max_length=255, blank=True, null=True)
    is_registered = models.IntegerField(blank=True, null=True)
    sent_time = models.DateTimeField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_registers'


class CandidateResumeFulltexts(models.Model):
    resume_content = models.TextField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    document_extension = models.CharField(max_length=255, blank=True, null=True)
    save_stamp = models.DateTimeField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_resume_fulltexts'


class CandidateSalarys(models.Model):
    date_created = models.DateTimeField(blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    basic = models.FloatField(blank=True, null=True)
    flexible = models.FloatField(blank=True, null=True)
    pf = models.FloatField(blank=True, null=True)
    performance_bonus = models.FloatField(blank=True, null=True)
    gratuity = models.FloatField(blank=True, null=True)
    super_annuation = models.FloatField(blank=True, null=True)
    insurance = models.FloatField(blank=True, null=True)
    medical = models.FloatField(blank=True, null=True)
    stocks = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    offer_id = models.IntegerField(blank=True, null=True)
    currency = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_salarys'


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


class CandidateSemesterWiseDetails(models.Model):
    semester_id = models.IntegerField(blank=True, null=True)
    percentage_or_cgp = models.FloatField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidateeducationprofile_id = models.IntegerField(blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    start_month = models.IntegerField(blank=True, null=True)
    end_month = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_semester_wise_details'


class CandidateSocialNetworkDetails(models.Model):
    version = models.IntegerField()
    face_book_link = models.CharField(max_length=255, blank=True, null=True)
    face_book_details = models.CharField(max_length=255, blank=True, null=True)
    twitter_link = models.CharField(max_length=255, blank=True, null=True)
    twitter_details = models.CharField(max_length=255, blank=True, null=True)
    linked_in_link = models.CharField(max_length=255, blank=True, null=True)
    linked_in_details = models.CharField(max_length=255, blank=True, null=True)
    candidate_id = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'candidate_social_network_details'


class CandidateSourceInfos(models.Model):
    source_id = models.IntegerField()
    expiry_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_source_infos'


class CandidateSpocs(models.Model):
    version = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    user_id = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_spocs'


class CandidateStaffingProfiles(models.Model):
    actual_joining_date = models.DateTimeField(blank=True, null=True)
    expected_joining_date = models.DateTimeField(blank=True, null=True)
    history_info = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    criticality = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    status_modified_on = models.DateTimeField(blank=True, null=True)
    is_calls_assigned = models.IntegerField(blank=True, null=True)
    call_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_staffing_profiles'


class CandidateStatuss(models.Model):
    candidate_satus_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_statuss'


class CandidateUploadResumes(models.Model):
    file_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_upload_resumes'


class CandidateWorkProfiles(models.Model):
    deisignation_id = models.IntegerField(blank=True, null=True)
    designation_text = models.CharField(max_length=75, blank=True, null=True)
    employer_id = models.IntegerField(blank=True, null=True)
    employer_text = models.CharField(max_length=100, blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    location_text = models.CharField(max_length=75, blank=True, null=True)
    reason_for_leaving = models.TextField(blank=True, null=True)
    yearly_salary = models.IntegerField(blank=True, null=True)
    from_month = models.IntegerField(blank=True, null=True)
    to_month = models.IntegerField(blank=True, null=True)
    from_year = models.IntegerField(blank=True, null=True)
    to_year = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    bulk_custom_field_string = models.TextField(blank=True, null=True)
    is_latest = models.IntegerField(blank=True, null=True)
    industry = models.IntegerField(blank=True, null=True)
    expertise = models.IntegerField(blank=True, null=True)
    sub_expertise = models.IntegerField(blank=True, null=True)
    sub_expertise2 = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_work_profiles'


class Candidates(models.Model):
    version = models.IntegerField()
    current_employer_id = models.IntegerField(blank=True, null=True)
    current_employer_text = models.CharField(max_length=100, blank=True, null=True)
    current_location_id = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    final_degree_id = models.IntegerField(blank=True, null=True)
    final_degree_text = models.CharField(max_length=100, blank=True, null=True)
    final_department_id = models.IntegerField(blank=True, null=True)
    final_department_text = models.CharField(max_length=70, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    is_fresher = models.IntegerField(blank=True, null=True)
    current_location_text = models.CharField(max_length=75, blank=True, null=True)
    marital_status = models.IntegerField(blank=True, null=True)
    opening_status_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    total_experience = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    relevant_experience = models.IntegerField(blank=True, null=True)
    expertise_id1 = models.IntegerField(blank=True, null=True)
    expertise_text = models.CharField(max_length=50, blank=True, null=True)
    expertise_id2 = models.IntegerField(blank=True, null=True)
    hierarchy_id = models.IntegerField(blank=True, null=True)
    hierarchy_text = models.CharField(max_length=50, blank=True, null=True)
    university_id = models.IntegerField(blank=True, null=True)
    university_text = models.CharField(max_length=100, blank=True, null=True)
    email1 = models.CharField(max_length=100, blank=True, null=True)
    email2 = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=75, blank=True, null=True)
    importance = models.IntegerField()
    last_name = models.CharField(max_length=75, blank=True, null=True)
    middle_name = models.CharField(max_length=75, blank=True, null=True)
    mobile1 = models.CharField(max_length=75, blank=True, null=True)
    phone_office = models.CharField(max_length=100, blank=True, null=True)
    phone_residence = models.CharField(max_length=100, blank=True, null=True)
    sensitivity = models.IntegerField(blank=True, null=True)
    salutation = models.IntegerField(blank=True, null=True)
    college_id = models.IntegerField(blank=True, null=True)
    college_text = models.CharField(max_length=255, blank=True, null=True)
    resume_grade_id = models.IntegerField(blank=True, null=True)
    no_of_attachments = models.IntegerField()
    experience_updated_on = models.DateTimeField(blank=True, null=True)
    technology_text = models.TextField(blank=True, null=True)
    current_ctc = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    brownie_point_total = models.IntegerField(blank=True, null=True)
    sourcer = models.IntegerField(blank=True, null=True)
    sourcer_log = models.CharField(max_length=2000, blank=True, null=True)
    crm_status_date = models.DateTimeField(blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    notice_period = models.IntegerField(blank=True, null=True)
    skill_id = models.IntegerField(blank=True, null=True)
    current_source_id = models.IntegerField(blank=True, null=True)
    sourcer_modified_date = models.DateTimeField(blank=True, null=True)
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
    text4 = models.CharField(max_length=1000, blank=True, null=True)
    text3 = models.CharField(max_length=1000, blank=True, null=True)
    text2 = models.CharField(max_length=1000, blank=True, null=True)
    text1 = models.CharField(max_length=1000, blank=True, null=True)
    is_alive = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    candidateoriginalsourceinfo_id = models.IntegerField(blank=True, null=True)
    candidatepreference_id = models.IntegerField(blank=True, null=True)
    candidatesourceinfo_id = models.IntegerField(blank=True, null=True)
    percentage_or_cgp = models.FloatField(blank=True, null=True)
    is_percentage = models.IntegerField(blank=True, null=True)
    original_candidate_id = models.IntegerField(blank=True, null=True)
    pan_card = models.CharField(max_length=20, blank=True, null=True)
    passport = models.CharField(max_length=10, blank=True, null=True)
    percentage_of_duplication = models.IntegerField(blank=True, null=True)
    candidateresumefulltext_id = models.IntegerField(blank=True, null=True)
    candidatefulltext_id = models.IntegerField(blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    bulk_custom_field_string = models.TextField(blank=True, null=True)
    is_black_listed = models.IntegerField()
    duplicate_or_blacklist_comment = models.CharField(max_length=5000, blank=True, null=True)
    original_source_info_modified = models.DateTimeField(blank=True, null=True)
    duplication_comment = models.CharField(max_length=5000, blank=True, null=True)
    is_set_resume_status_to_crm = models.IntegerField(blank=True, null=True)
    is_rejected = models.IntegerField(blank=True, null=True)
    is_partial_duplicate = models.IntegerField()
    black_list_mode = models.IntegerField()
    soft_delete_type = models.IntegerField()
    candidate_photo_file_id = models.IntegerField(blank=True, null=True)
    is_hirepro_vendor_candidate = models.IntegerField(blank=True, null=True)
    is_utilized = models.IntegerField()
    audio_file_name = models.CharField(max_length=255, blank=True, null=True)
    text5 = models.CharField(max_length=50, blank=True, null=True)
    integer3 = models.IntegerField(blank=True, null=True)
    integer4 = models.IntegerField(blank=True, null=True)
    integer5 = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    usn = models.CharField(max_length=45, blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    nationality = models.IntegerField(blank=True, null=True)
    familydetail_id = models.IntegerField(blank=True, null=True)
    type_of_candidate = models.IntegerField()
    original_source_id = models.IntegerField()
    source_modified_by = models.IntegerField(blank=True, null=True)
    source_modified_on = models.DateTimeField(blank=True, null=True)
    originated_from = models.IntegerField(blank=True, null=True)
    level_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(db_column='role_Id', blank=True, null=True)  # Field name made lowercase.
    mentor = models.IntegerField(blank=True, null=True)
    buddies = models.CharField(max_length=100, blank=True, null=True)
    bu_id = models.IntegerField(blank=True, null=True)
    current_activity = models.IntegerField(blank=True, null=True)
    activity_status = models.IntegerField(blank=True, null=True)
    candidate_user_id = models.IntegerField(blank=True, null=True)
    candidatestaffingprofile_id = models.IntegerField(blank=True, null=True)
    current_experience = models.IntegerField(blank=True, null=True)
    bpo_experience = models.IntegerField(blank=True, null=True)
    date_custom_field1 = models.DateTimeField(blank=True, null=True)
    date_custom_field2 = models.DateTimeField(blank=True, null=True)
    text_area1 = models.CharField(max_length=3000, blank=True, null=True)
    text_area2 = models.CharField(max_length=3000, blank=True, null=True)
    text_area3 = models.CharField(max_length=3000, blank=True, null=True)
    text_area4 = models.CharField(max_length=500, blank=True, null=True)
    candidate_photo_path = models.CharField(max_length=500, blank=True, null=True)
    uid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidates'


class CatalogGroupMembers(models.Model):
    catalog_value_id = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    cataloggroup_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_group_members'


class CatalogGroups(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    catalog_master_id = models.IntegerField(blank=True, null=True)
    is_direct_binding = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    cataloggroup_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_groups'


class CatalogMappings(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    old_value = models.CharField(max_length=100, blank=True, null=True)
    old_master_id = models.IntegerField(blank=True, null=True)
    old_value_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    new_value = models.CharField(max_length=100, blank=True, null=True)
    new_master_id = models.IntegerField(blank=True, null=True)
    new_value_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_mappings'


class CatalogMasters(models.Model):
    version = models.IntegerField()
    catalog_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_code_applicable = models.IntegerField()
    is_repeating_value = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    catalogmaster_id = models.IntegerField(blank=True, null=True)
    is_system_catalog = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_masters'


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


class CodingQuestionAttachments(models.Model):
    version = models.IntegerField()
    input_file_id = models.IntegerField(blank=True, null=True)
    output_file_id = models.IntegerField(blank=True, null=True)
    is_sample = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    question = models.ForeignKey('Questions', blank=True, null=True)
    weightage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coding_question_attachments'


class CodingQuestionLanguages(models.Model):
    version = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    code_snippet = models.CharField(max_length=5000, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    question = models.ForeignKey('Questions', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coding_question_languages'


class CollegeGroups(models.Model):
    version = models.IntegerField()
    source_id = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=45, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=45)
    collegegroup_id = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'college_groups'


class Colleges(models.Model):
    college_id = models.IntegerField(blank=True, null=True)
    college_text = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruitevent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colleges'


class CommunicationHistorys(models.Model):
    version = models.IntegerField()
    receiver = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    reference_id = models.IntegerField(blank=True, null=True)
    medium_type = models.IntegerField(blank=True, null=True)
    medium = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40, blank=True, null=True)
    communicationhistory_id = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_historys'


class CompanyEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link_to_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    company_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_events'


class CompanyUsers(models.Model):
    version = models.IntegerField()
    company_id = models.IntegerField()
    user_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'company_users'


class Companys(models.Model):
    version = models.IntegerField()
    company_name = models.CharField(max_length=255, blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    main_website = models.CharField(max_length=100, blank=True, null=True)
    job_website = models.CharField(max_length=255, blank=True, null=True)
    industry_id = models.IntegerField(blank=True, null=True)
    dictionary_id = models.IntegerField(blank=True, null=True)
    key_technologies = models.CharField(max_length=255, blank=True, null=True)
    reappear_duration = models.IntegerField(blank=True, null=True)
    email1 = models.CharField(max_length=255, blank=True, null=True)
    email2 = models.CharField(max_length=50, blank=True, null=True)
    mobile1 = models.CharField(max_length=20, blank=True, null=True)
    phone_office = models.CharField(max_length=255, blank=True, null=True)
    phone_other = models.CharField(max_length=20, blank=True, null=True)
    sensitivity = models.IntegerField(blank=True, null=True)
    site_url = models.CharField(max_length=255, blank=True, null=True)
    fax_number = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_till = models.DateTimeField(blank=True, null=True)
    no_of_attachments = models.IntegerField()
    location_id = models.IntegerField(blank=True, null=True)
    location_text = models.CharField(max_length=75, blank=True, null=True)
    organization_type = models.CharField(max_length=255, blank=True, null=True)
    is_source = models.IntegerField()
    organization_type_id = models.IntegerField()
    is_consultant = models.IntegerField(blank=True, null=True)
    is_tenant = models.IntegerField(blank=True, null=True)
    organization_title = models.CharField(max_length=255, blank=True, null=True)
    organization_description = models.TextField(blank=True, null=True)
    primary_owner_id = models.IntegerField(blank=True, null=True)
    resume_validity = models.IntegerField(blank=True, null=True)
    address1 = models.CharField(max_length=1000, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
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
    contract_id = models.IntegerField(blank=True, null=True)
    out_placement_from_date = models.DateTimeField(blank=True, null=True)
    out_placement_to_date = models.DateTimeField(blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    text5 = models.CharField(max_length=50, blank=True, null=True)
    integer3 = models.IntegerField(blank=True, null=True)
    integer4 = models.IntegerField(blank=True, null=True)
    integer5 = models.IntegerField(blank=True, null=True)
    activity_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companys'


class Compliances(models.Model):
    version = models.IntegerField()
    initial_resume_status_id = models.IntegerField(blank=True, null=True)
    final_resume_status_id = models.IntegerField(blank=True, null=True)
    time_limit = models.IntegerField()
    name = models.CharField(max_length=255)
    tenant_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'compliances'


class ConfigAssessmentFeedbacks(models.Model):
    job_id = models.IntegerField()
    status_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    assessmenttemplate_id = models.IntegerField(blank=True, null=True)
    is_rating_required = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    recruit_event_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_assessment_feedbacks'


class Consultants(models.Model):
    source_id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField(blank=True, null=True)
    is_agreement_signed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consultants'


class ContractDetails(models.Model):
    experience_level_id = models.IntegerField(blank=True, null=True)
    retainer = models.FloatField(blank=True, null=True)
    billing = models.FloatField(blank=True, null=True)
    billing_amount = models.FloatField(blank=True, null=True)
    transition_time = models.IntegerField(blank=True, null=True)
    resume_validity = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    contract_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_details'


class ContractEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link_to_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    contract_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_events'


class Contracts(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=75, blank=True, null=True)
    default_resume_validity = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
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
    retainer = models.FloatField(blank=True, null=True)
    transition_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contracts'


class CtcStructures(models.Model):
    version = models.IntegerField()
    provident_fund_percent = models.FloatField(blank=True, null=True)
    super_annuation_fund_percent = models.FloatField(blank=True, null=True)
    hra_percent = models.FloatField(blank=True, null=True)
    car_lease = models.FloatField(blank=True, null=True)
    car_insurance_and_tax = models.FloatField(blank=True, null=True)
    car_repair_and_maintenance = models.FloatField(blank=True, null=True)
    car_petrol_expense = models.FloatField(blank=True, null=True)
    lta = models.FloatField(blank=True, null=True)
    medical_reimbursement = models.FloatField(blank=True, null=True)
    telephone_expense = models.FloatField(blank=True, null=True)
    gift_voucher = models.FloatField(blank=True, null=True)
    conveyance_allowance = models.FloatField(blank=True, null=True)
    food_coupon = models.FloatField(blank=True, null=True)
    other_allowance = models.FloatField(blank=True, null=True)
    level_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    tenant_id = models.IntegerField(blank=True, null=True)
    salary_structure_template_file_id = models.IntegerField(blank=True, null=True)
    offer_template_file_id = models.IntegerField(blank=True, null=True)
    component_ain_percent = models.FloatField(blank=True, null=True)
    component_bin_percent = models.FloatField(blank=True, null=True)
    custom_field_a1_percent = models.FloatField(blank=True, null=True)
    custom_field_a2_percent = models.FloatField(blank=True, null=True)
    custom_field_a3_flat = models.FloatField(blank=True, null=True)
    custom_field_a4_flat = models.FloatField(blank=True, null=True)
    custom_field_a5_flat = models.FloatField(blank=True, null=True)
    custom_field_b1_percent = models.FloatField(blank=True, null=True)
    custom_field_b2_percent = models.FloatField(blank=True, null=True)
    custom_field_b3_flat = models.FloatField(blank=True, null=True)
    custom_field_b4_flat = models.FloatField(blank=True, null=True)
    custom_field_b5_flat = models.FloatField(blank=True, null=True)
    custom_field_a1_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a2_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a3_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a4_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a5_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_b1_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_b2_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_b3_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_b4_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_b5_label = models.CharField(max_length=45, blank=True, null=True)
    basic_salary_percent = models.FloatField()
    offered_amount_left_in_alabel = models.CharField(max_length=45, blank=True, null=True)
    offered_amount_left_in_blabel = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a6_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a7_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a8_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a9_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a10_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a11_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a12_label = models.CharField(max_length=45, blank=True, null=True)
    custom_field_a8_flat = models.FloatField(blank=True, null=True)
    custom_field_a9_flat = models.FloatField(blank=True, null=True)
    custom_field_a10_flat = models.FloatField(blank=True, null=True)
    custom_field_a11_flat = models.FloatField(blank=True, null=True)
    custom_field_a12_flat = models.FloatField(blank=True, null=True)
    custom_field_a6_percent = models.FloatField(blank=True, null=True)
    custom_field_a7_percent = models.FloatField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    custom_field_a13_flat = models.FloatField(blank=True, null=True)
    custom_field_a13_label = models.CharField(max_length=255, blank=True, null=True)
    custom_field_a14_flat = models.FloatField(blank=True, null=True)
    custom_field_a14_label = models.CharField(max_length=255, blank=True, null=True)
    custom_field_b6_flat = models.FloatField(blank=True, null=True)
    custom_field_b6_label = models.CharField(max_length=255, blank=True, null=True)
    custom_field_b7_flat = models.FloatField(blank=True, null=True)
    custom_field_b7_label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctc_structures'


class CustomerBusinessUnits(models.Model):
    tenant_id = models.IntegerField(blank=True, null=True)
    businessunit_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_business_units'


class CustomerCustomEntityFieldsDefss(models.Model):
    version = models.IntegerField()
    property_name = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    entity_name = models.CharField(max_length=255, blank=True, null=True)
    is_visible = models.IntegerField(blank=True, null=True)
    is_required = models.IntegerField(blank=True, null=True)
    is_visible_in_grid = models.IntegerField(blank=True, null=True)
    is_visible_in_search = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'customer_custom_entity_fields_defss'


class CustomerCustomEntityFieldss(models.Model):
    version = models.IntegerField()
    integer1 = models.IntegerField(blank=True, null=True)
    integer2 = models.IntegerField(blank=True, null=True)
    integer3 = models.IntegerField(blank=True, null=True)
    integer4 = models.IntegerField(blank=True, null=True)
    string1 = models.CharField(max_length=255, blank=True, null=True)
    string2 = models.CharField(max_length=255, blank=True, null=True)
    string3 = models.CharField(max_length=255, blank=True, null=True)
    string4 = models.CharField(max_length=255, blank=True, null=True)
    date_time1 = models.DateTimeField(blank=True, null=True)
    date_time2 = models.DateTimeField(blank=True, null=True)
    boolean1 = models.IntegerField(blank=True, null=True)
    boolean2 = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'customer_custom_entity_fieldss'


class CustomerVendorContracts(models.Model):
    version = models.IntegerField()
    vendor_id = models.IntegerField(blank=True, null=True)
    customer_tenant_id = models.IntegerField(blank=True, null=True)
    expiry_date_to = models.DateTimeField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
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
    contract_id = models.IntegerField(blank=True, null=True)
    expiry_date_from = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_vendor_contracts'


class Customers(models.Model):
    version = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    company_id = models.IntegerField(blank=True, null=True)
    type_of_customer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class DailyBusinessReports(models.Model):
    version = models.IntegerField()
    candidate_id = models.IntegerField()
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    billing_amount = models.CharField(max_length=255, blank=True, null=True)
    day = models.CharField(max_length=255, blank=True, null=True)
    email_id = models.CharField(max_length=255, blank=True, null=True)
    status_id = models.CharField(max_length=255)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=38)

    class Meta:
        managed = False
        db_table = 'daily_business_reports'


class DashBoardCandidatesJoiningReports(models.Model):
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    job_name = models.CharField(max_length=255, blank=True, null=True)
    joining_date = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dash_board_candidates_joining_reports'


class DashBoardRequisitionStatusReports(models.Model):
    selected_name = models.CharField(max_length=255, blank=True, null=True)
    selected_count = models.IntegerField(blank=True, null=True)
    joined_count = models.IntegerField(blank=True, null=True)
    to_forward_name = models.CharField(max_length=255, blank=True, null=True)
    to_forward_count = models.IntegerField(blank=True, null=True)
    matching_name = models.CharField(max_length=255, blank=True, null=True)
    matching_count = models.IntegerField(blank=True, null=True)
    joined_name = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    job_name = models.CharField(max_length=255, blank=True, null=True)
    number_of_openings = models.IntegerField(blank=True, null=True)
    forwarded_name = models.CharField(max_length=255, blank=True, null=True)
    forwarded_count = models.IntegerField(blank=True, null=True)
    number_of_openings_name = models.CharField(max_length=255, blank=True, null=True)
    is_yesterday_status = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    shortlisted_name = models.CharField(max_length=255, blank=True, null=True)
    shortlisted_count = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dash_board_requisition_status_reports'


class DashboardArticleDesignationDepartments(models.Model):
    designation_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    dashboardarticle_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_article_designation_departments'


class DashboardArticles(models.Model):
    version = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    order_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
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
    summary = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_articles'


class DefaultActionss(models.Model):
    module_id = models.IntegerField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    role_name = models.CharField(max_length=45, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    guid = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'default_actionss'


class Departments(models.Model):
    version = models.IntegerField()
    email1 = models.CharField(max_length=50, blank=True, null=True)
    email2 = models.CharField(max_length=50, blank=True, null=True)
    mobile1 = models.CharField(max_length=20, blank=True, null=True)
    phone_office = models.CharField(max_length=20, blank=True, null=True)
    phone_other = models.CharField(max_length=20, blank=True, null=True)
    fax_number = models.CharField(max_length=20, blank=True, null=True)
    department_name = models.CharField(max_length=255, blank=True, null=True)
    site_url = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
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
    company_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    email3 = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=75, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    mobile2 = models.CharField(max_length=20, blank=True, null=True)
    phone_residence = models.CharField(max_length=20, blank=True, null=True)
    preferred_name = models.CharField(max_length=50, blank=True, null=True)
    sensitivity = models.IntegerField(blank=True, null=True)
    salutation = models.IntegerField(blank=True, null=True)
    is_person = models.IntegerField(blank=True, null=True)
    assistant = models.CharField(max_length=75, blank=True, null=True)
    assistant_phone = models.CharField(max_length=20, blank=True, null=True)
    importance = models.IntegerField(blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
    integer2 = models.IntegerField(blank=True, null=True)
    integer1 = models.IntegerField(blank=True, null=True)
    text4 = models.CharField(max_length=50, blank=True, null=True)
    text3 = models.CharField(max_length=50, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    text1 = models.CharField(max_length=50, blank=True, null=True)
    street1 = models.CharField(max_length=255, blank=True, null=True)
    city1_text = models.CharField(max_length=50, blank=True, null=True)
    city1_id = models.IntegerField(blank=True, null=True)
    state1_text = models.CharField(max_length=50, blank=True, null=True)
    country1_text = models.CharField(max_length=50, blank=True, null=True)
    pincode1 = models.CharField(max_length=10, blank=True, null=True)
    state1_id = models.IntegerField(blank=True, null=True)
    country1_id = models.IntegerField(blank=True, null=True)
    street3 = models.CharField(max_length=255, blank=True, null=True)
    city3_text = models.CharField(max_length=50, blank=True, null=True)
    state3_text = models.CharField(max_length=50, blank=True, null=True)
    country3_text = models.CharField(max_length=50, blank=True, null=True)
    pincode3 = models.CharField(max_length=10, blank=True, null=True)
    state3_id = models.IntegerField(blank=True, null=True)
    city3_id = models.IntegerField(blank=True, null=True)
    country3_id = models.IntegerField(blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    city2_text = models.CharField(max_length=50, blank=True, null=True)
    state2_text = models.CharField(max_length=50, blank=True, null=True)
    country2_text = models.CharField(max_length=50, blank=True, null=True)
    pincode2 = models.CharField(max_length=10, blank=True, null=True)
    state2_id = models.IntegerField(blank=True, null=True)
    city2_id = models.IntegerField(blank=True, null=True)
    country2_id = models.IntegerField(blank=True, null=True)
    location = models.IntegerField(blank=True, null=True)
    spoc = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    offered_date = models.DateTimeField(blank=True, null=True)
    joined_date = models.DateTimeField(blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    is_onboarding_department = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class DirectApplicants(models.Model):
    source_id = models.IntegerField(primary_key=True)
    is_default_direct_applicant = models.IntegerField(blank=True, null=True)
    direct_applicant_email_id = models.CharField(max_length=45, blank=True, null=True)
    direct_applicant_email_password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direct_applicants'


class DisableCatalogss(models.Model):
    tenant_id = models.IntegerField(blank=True, null=True)
    catalog_value_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_duplicated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'disable_catalogss'


class Domains(models.Model):
    domain_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domains'


class Dtproperties(models.Model):
    id = models.AutoField()
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.TextField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class DuplicateCandidates(models.Model):
    duplicate_candidate_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate = models.ForeignKey(Candidates, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'duplicate_candidates'


class EditedAnswerChoices(models.Model):
    choice = models.CharField(max_length=1, blank=True, null=True)
    answer = models.CharField(max_length=4000, blank=True, null=True)
    html_string = models.TextField(blank=True, null=True)
    no_of_attachments = models.IntegerField(blank=True, null=True)
    marks = models.FloatField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    editedquestion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edited_answer_choices'


class EditedAnswers(models.Model):
    correct_answer = models.CharField(max_length=4000, blank=True, null=True)
    html_string = models.TextField(blank=True, null=True)
    no_of_attachments = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    editedquestion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edited_answers'


class EditedQuestionAttachments(models.Model):
    version = models.IntegerField()
    file_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    editedquestion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edited_question_attachments'


class EditedQuestionNoteAttachments(models.Model):
    version = models.IntegerField()
    file_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    editedquestion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edited_question_note_attachments'


class EditedQuestions(models.Model):
    version = models.IntegerField()
    question_type = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    sub_categories_id = models.IntegerField(blank=True, null=True)
    sub_topic_id = models.IntegerField(blank=True, null=True)
    difficulty_level = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    source_text = models.CharField(max_length=1024, blank=True, null=True)
    question_str = models.CharField(max_length=4000, blank=True, null=True)
    html_string = models.TextField(blank=True, null=True)
    question_reuse = models.IntegerField()
    is_qa_pending = models.IntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    instruction_id = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    no_of_attachments = models.IntegerField()
    question_label = models.CharField(max_length=255, blank=True, null=True)
    preview_id = models.IntegerField(blank=True, null=True)
    is_survey_question = models.IntegerField()
    total_attempt = models.IntegerField()
    correct = models.IntegerField()
    in_correct = models.IntegerField()
    un_attempted = models.IntegerField()
    is_revised = models.IntegerField()
    is_psychometric = models.IntegerField()
    hirepro_question_id = models.IntegerField(blank=True, null=True)
    author = models.IntegerField(blank=True, null=True)
    question_originality = models.IntegerField()
    question_flag = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
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
    guid = models.CharField(max_length=64)
    editedquestion_id = models.IntegerField(blank=True, null=True)
    original_question_id = models.IntegerField(blank=True, null=True)
    original_question_child_id = models.IntegerField(blank=True, null=True)
    sub_topic_unit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edited_questions'


class EffortPipeLineReports(models.Model):
    version = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    job_code_id = models.IntegerField(blank=True, null=True)
    job_code_text = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    source_name = models.CharField(max_length=255, blank=True, null=True)
    business_unit_id = models.IntegerField(blank=True, null=True)
    sub_business_unit_id = models.IntegerField(blank=True, null=True)
    business_unit_text = models.CharField(max_length=255, blank=True, null=True)
    sub_business_unit_text = models.CharField(max_length=255, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    status_text = models.CharField(max_length=255, blank=True, null=True)
    anchor_id = models.IntegerField(blank=True, null=True)
    total_cvuploaded = models.IntegerField(blank=True, null=True)
    cvscreened_shortlisted = models.IntegerField(blank=True, null=True)
    cvscreened_rejected = models.IntegerField(blank=True, null=True)
    qualified_for_technical_screening = models.IntegerField(blank=True, null=True)
    technical_screening_shortlisted = models.IntegerField(blank=True, null=True)
    technical_screening_rejected = models.IntegerField(blank=True, null=True)
    technical_interview_shortlisted = models.IntegerField(blank=True, null=True)
    technical_interview_rejected = models.IntegerField(blank=True, null=True)
    second_interview_shortlisted = models.IntegerField(blank=True, null=True)
    second_interview_rejected = models.IntegerField(blank=True, null=True)
    final_interview_shortlisted = models.IntegerField(blank=True, null=True)
    final_interview_rejected = models.IntegerField(blank=True, null=True)
    hrinterview_shortlisted = models.IntegerField(blank=True, null=True)
    hrinterview_rejected = models.IntegerField(blank=True, null=True)
    qualified_for_offer = models.IntegerField(blank=True, null=True)
    fitment_in_process = models.IntegerField(blank=True, null=True)
    offer_with_drawn = models.IntegerField(blank=True, null=True)
    offer_released = models.IntegerField(blank=True, null=True)
    joined = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    qualified_for_technical_interview = models.IntegerField(blank=True, null=True)
    qualified_for_second_interview = models.IntegerField(blank=True, null=True)
    qualified_for_final_interview = models.IntegerField(blank=True, null=True)
    qualified_for_hrinterview = models.IntegerField(blank=True, null=True)
    anchor_name = models.CharField(max_length=45, blank=True, null=True)
    primary_owner_id = models.IntegerField(blank=True, null=True)
    primary_owner_name = models.CharField(max_length=45, blank=True, null=True)
    job_name = models.CharField(max_length=255, blank=True, null=True)
    offer_accepted = models.IntegerField(blank=True, null=True)
    pipeline_in_cv_screened = models.IntegerField(blank=True, null=True)
    pipeline_in_technical_screening = models.IntegerField(blank=True, null=True)
    pipeline_in_technical_interivew = models.IntegerField(blank=True, null=True)
    pipeline_in_second_interview = models.IntegerField(blank=True, null=True)
    pipeline_in_final_interview = models.IntegerField(blank=True, null=True)
    pipeline_in_hr_interview = models.IntegerField(blank=True, null=True)
    pipeline_in_offer = models.IntegerField(blank=True, null=True)
    job_created_date = models.DateTimeField(blank=True, null=True)
    third_interview_shortlisted = models.IntegerField(blank=True, null=True)
    third_interview_rejected = models.IntegerField(blank=True, null=True)
    pipeline_in_third_interview = models.IntegerField(blank=True, null=True)
    fourth_interview_shortlisted = models.IntegerField(blank=True, null=True)
    fourth_interview_rejected = models.IntegerField(blank=True, null=True)
    pipeline_in_fourth_interview = models.IntegerField(blank=True, null=True)
    fifth_interview_shortlisted = models.IntegerField(blank=True, null=True)
    fifth_interview_rejected = models.IntegerField(blank=True, null=True)
    pipeline_in_fifth_interview = models.IntegerField(blank=True, null=True)
    sixth_interview_shortlisted = models.IntegerField(blank=True, null=True)
    sixth_interview_rejected = models.IntegerField(blank=True, null=True)
    pipeline_in_sixth_interview = models.IntegerField(blank=True, null=True)
    qualified_for_third_interview = models.IntegerField(blank=True, null=True)
    qualified_for_fourth_interview = models.IntegerField(blank=True, null=True)
    qualified_for_fifth_interview = models.IntegerField(blank=True, null=True)
    qualified_for_sixth_interview = models.IntegerField(blank=True, null=True)
    request_date = models.DateTimeField(blank=True, null=True)
    hirepro_source_id = models.IntegerField(blank=True, null=True)
    is_archived = models.IntegerField(blank=True, null=True)
    self_service_type = models.IntegerField(blank=True, null=True)
    is_source_wise = models.IntegerField()
    types_of_source = models.IntegerField(blank=True, null=True)
    integer1 = models.IntegerField(blank=True, null=True)
    integer2 = models.IntegerField(blank=True, null=True)
    integer3 = models.IntegerField(blank=True, null=True)
    integer4 = models.IntegerField(blank=True, null=True)
    integer5 = models.IntegerField(blank=True, null=True)
    text1 = models.CharField(max_length=2000, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    text3 = models.CharField(max_length=50, blank=True, null=True)
    text4 = models.CharField(max_length=50, blank=True, null=True)
    text5 = models.CharField(max_length=50, blank=True, null=True)
    date_time1 = models.DateTimeField(blank=True, null=True)
    date_time2 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'effort_pipe_line_reports'


class EligibilityCriteriaSkills(models.Model):
    skill_id = models.IntegerField(blank=True, null=True)
    skill_level = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    eligibilitycriteria = models.ForeignKey('EligibilityCriterias', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eligibility_criteria_skills'


class EligibilityCriterias(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    is_utilized = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    from_expirence_in_months = models.IntegerField(blank=True, null=True)
    to_expirence_in_months = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    is_auto_checked_ec = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eligibility_criterias'


class EmployeeEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link_to_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    employee_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_events'


class EmployeeLevels(models.Model):
    version = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    average_cost = models.FloatField()
    average_productivity_ratio = models.FloatField()
    gacost = models.FloatField()
    hierarchy = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'employee_levels'


class EmployeePhaseInfos(models.Model):
    version = models.IntegerField()
    phase_due_date = models.DateTimeField(blank=True, null=True)
    phase_id = models.IntegerField(blank=True, null=True)
    phase_completion_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    onboardingcandidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_phase_infos'


class EmployeeReferralLogs(models.Model):
    version = models.IntegerField()
    candidate_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    candidate_originated_from = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    is_tagged = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'employee_referral_logs'


class Employees(models.Model):
    version = models.IntegerField()
    email1 = models.CharField(max_length=50, blank=True, null=True)
    email2 = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=75, blank=True, null=True)
    last_name = models.CharField(max_length=75, blank=True, null=True)
    middle_name = models.CharField(max_length=75, blank=True, null=True)
    mobile1 = models.CharField(max_length=20, blank=True, null=True)
    phone_office = models.CharField(max_length=20, blank=True, null=True)
    phone_residence = models.CharField(max_length=20, blank=True, null=True)
    salutation = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    employee_referrals_id = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    is_employee_referral = models.IntegerField(blank=True, null=True)
    employee_status = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    published_on = models.DateTimeField(blank=True, null=True)
    published_by = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_draft = models.IntegerField(blank=True, null=True)
    is_archived = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
    is_alive = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    employee_id = models.IntegerField(blank=True, null=True)
    employee_level_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    businessunit_id = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=75, blank=True, null=True)
    interviewer_id = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)
    onboarding_candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class EntityAttachments(models.Model):
    version = models.IntegerField()
    attachment_type = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    entity_type = models.IntegerField(blank=True, null=True)
    entity_id = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_attachments'


class EventLocations(models.Model):
    venue_location_id = models.IntegerField(blank=True, null=True)
    venue_location_text = models.CharField(max_length=45, blank=True, null=True)
    job_location_id = models.IntegerField(blank=True, null=True)
    job_location_text = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruitevent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_locations'


class Events(models.Model):
    version = models.IntegerField()
    event_type = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    link_to_type = models.CharField(max_length=255, blank=True, null=True)
    link_to_id = models.IntegerField(blank=True, null=True)
    target_type = models.CharField(max_length=255, blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    actor_type = models.CharField(max_length=255, blank=True, null=True)
    actor_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class ExperienceRanges(models.Model):
    version = models.IntegerField()
    experience_start = models.IntegerField(blank=True, null=True)
    experience_end = models.IntegerField(blank=True, null=True)
    experience_label = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'experience_ranges'


class ExternalHrOwners(models.Model):
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_hr_owners'


class ExtractorListeners(models.Model):
    version = models.IntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    email_password = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    source_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extractor_listeners'


class FamilyDetails(models.Model):
    head_of_family = models.IntegerField(blank=True, null=True)
    hofprofession = models.CharField(max_length=255, blank=True, null=True)
    total_house_income = models.DecimalField(max_digits=19, decimal_places=5, blank=True, null=True)
    annual_income = models.DecimalField(max_digits=19, decimal_places=5, blank=True, null=True)
    dependents = models.IntegerField(blank=True, null=True)
    siblings = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'family_details'


class FeedBackForms(models.Model):
    max_score = models.IntegerField()
    client_expectation = models.CharField(max_length=2500, blank=True, null=True)
    job_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    feed_back_forms_attachment_id = models.IntegerField(blank=True, null=True)
    interview_round = models.CharField(max_length=200, blank=True, null=True)
    interview_name = models.CharField(max_length=200, blank=True, null=True)
    is_interviewer_feed_back_not_visible = models.IntegerField(blank=True, null=True)
    assessment_template_id = models.IntegerField()
    stage_id = models.IntegerField()
    is_rating_required = models.IntegerField(blank=True, null=True)
    interview_mode = models.IntegerField(blank=True, null=True)
    is_automation_process_needed = models.IntegerField(blank=True, null=True)
    recruit_event_id = models.IntegerField(blank=True, null=True)
    conflict_config = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'feed_back_forms'


class FileContents(models.Model):
    file_content = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_contents'


class FileLists(models.Model):
    version = models.IntegerField()
    resume_source_id = models.IntegerField(blank=True, null=True)
    initial_file_path = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    mail_id = models.IntegerField()
    log = models.CharField(max_length=255, blank=True, null=True)
    original_file_id = models.IntegerField(blank=True, null=True)
    html_file_id = models.IntegerField(blank=True, null=True)
    xml_file_id = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField()
    teared_file_id = models.IntegerField(blank=True, null=True)
    is_indexed = models.IntegerField(blank=True, null=True)
    is_skills_extracted = models.IntegerField(blank=True, null=True)
    object_status = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    candidate_source_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_lists'


class Files(models.Model):
    version = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    original_file_name = models.TextField(blank=True, null=True)
    file_type_id = models.IntegerField(blank=True, null=True)
    file_type_text = models.CharField(max_length=255, blank=True, null=True)
    file_format_id = models.IntegerField(blank=True, null=True)
    file_size = models.BigIntegerField()
    is_compressed = models.IntegerField(blank=True, null=True)
    is_encrypted = models.IntegerField(blank=True, null=True)
    target_path = models.TextField(blank=True, null=True)
    file_created_on = models.DateTimeField()
    file_modified_on = models.DateTimeField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    filecontent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class FilledFormContents(models.Model):
    control_id = models.IntegerField(blank=True, null=True)
    control_value = models.TextField(blank=True, null=True)
    form_control_type = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    filledform = models.ForeignKey('FilledForms', blank=True, null=True)
    form_entity_map_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filled_form_contents'


class FilledForms(models.Model):
    version = models.IntegerField()
    form_filled_by = models.IntegerField(blank=True, null=True)
    form_id = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'filled_forms'


class FixedRtcChildQuestions(models.Model):
    question_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    rtcrandomizedquestion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_rtc_child_questions'


class Folders(models.Model):
    version = models.IntegerField()
    folder_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    folder_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'folders'


class FormControlGroups(models.Model):
    form_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_control_groups'


class FormControls(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    is_mandatory = models.IntegerField(blank=True, null=True)
    max_length = models.IntegerField(blank=True, null=True)
    catalog_master_name = models.CharField(max_length=255, blank=True, null=True)
    group_control_values = models.CharField(max_length=255, blank=True, null=True)
    sequence_id = models.IntegerField(blank=True, null=True)
    validation_type = models.IntegerField(blank=True, null=True)
    form_control_type = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    form = models.ForeignKey('Forms', blank=True, null=True)
    form_entity_map_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    settings = models.CharField(max_length=255, blank=True, null=True)
    tool_tip = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_controls'


class FormValidationRules(models.Model):
    control_id = models.IntegerField(blank=True, null=True)
    validation_rule = models.IntegerField(blank=True, null=True)
    validation_data = models.TextField(blank=True, null=True)
    dependent_rule_id = models.IntegerField(blank=True, null=True)
    formvalidation_id = models.IntegerField(blank=True, null=True)
    dependent_action = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_validation_rules'


class FormValidations(models.Model):
    version = models.IntegerField()
    form_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_validations'


class Forms(models.Model):
    version = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    hirepro_form_id = models.IntegerField(blank=True, null=True)
    validation_failure_message = models.TextField(blank=True, null=True)
    validation_failure_action = models.IntegerField(blank=True, null=True)
    is_required_validation = models.IntegerField(blank=True, null=True)
    is_need_to_pass_all_validations = models.IntegerField(blank=True, null=True)
    header = models.TextField(blank=True, null=True)
    footer = models.TextField(blank=True, null=True)
    type_of_form = models.IntegerField(blank=True, null=True)
    disclaimer = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forms'


class GiftCatalogs(models.Model):
    version = models.IntegerField()
    item_code = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField()
    shiping_charge = models.IntegerField()
    category = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    file_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gift_catalogs'


class Groups(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    department_id = models.IntegerField(blank=True, null=True)
    total_members = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class HelpDeskParticipants(models.Model):
    tenant_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    query_participant_type = models.IntegerField(blank=True, null=True)
    helpdesk = models.ForeignKey('HelpDesks', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'help_desk_participants'


class HelpDesks(models.Model):
    version = models.IntegerField()
    help_desk_status = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    sender = models.IntegerField(blank=True, null=True)
    receiver = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    sender_department = models.IntegerField(blank=True, null=True)
    receiver_department = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    reference_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    helpdesk = models.ForeignKey('self', blank=True, null=True)
    criticality = models.IntegerField(blank=True, null=True)
    sub_query_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'help_desks'


class HireproQuestionLogs(models.Model):
    hirepro_question_id = models.IntegerField(blank=True, null=True)
    destination_tenant_id = models.IntegerField(blank=True, null=True)
    destination_question_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    guid = models.CharField(max_length=40)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hirepro_question_logs'


class HiringForecastByWeeks(models.Model):
    week = models.IntegerField()
    demand = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    hiringforecast_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hiring_forecast_by_weeks'


class HiringForecasts(models.Model):
    version = models.IntegerField()
    location_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField()
    sub_department_id = models.IntegerField(blank=True, null=True)
    skill_category_id = models.IntegerField(blank=True, null=True)
    competency_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField()
    quarter = models.IntegerField()
    demand = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hiring_forecasts'


class InternalHrOwners(models.Model):
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    owner_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internal_hr_owners'


class InternalOwners(models.Model):
    owner_type = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internal_owners'


class InterviewCandidates(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    bulk_interviewer_id = models.IntegerField(blank=True, null=True)
    interview_time = models.DateTimeField(blank=True, null=True)
    candidate_status = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    bulkinterview_id = models.IntegerField(blank=True, null=True)
    applicant_status_id = models.IntegerField(blank=True, null=True)
    interviewrequest_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interview_candidates'


class InterviewFilledFeedbackForms(models.Model):
    interviewer_dicision = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=8000, blank=True, null=True)
    feedback_reason = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    interviewrequest = models.ForeignKey('InterviewRequests', blank=True, null=True)
    interviewed_time = models.DateTimeField(blank=True, null=True)
    interview_duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interview_filled_feedback_forms'


class InterviewInterviwers(models.Model):
    interviewer = models.IntegerField(blank=True, null=True)
    interview_time = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    interviewrequest = models.ForeignKey('InterviewRequests', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interview_interviwers'


class InterviewPanels(models.Model):
    version = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    panel_name = models.CharField(max_length=45, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=45)
    interviewpanel_id = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interview_panels'


class InterviewRequests(models.Model):
    interviewer_id = models.IntegerField(blank=True, null=True)
    interview_time = models.DateTimeField(blank=True, null=True)
    interview_type = models.IntegerField()
    interveiwee_score = models.FloatField(blank=True, null=True)
    is_interviewed = models.IntegerField(blank=True, null=True)
    interviewed_time = models.DateTimeField(blank=True, null=True)
    interview_duration = models.IntegerField(blank=True, null=True)
    stage_id = models.IntegerField(blank=True, null=True)
    client_decision_status = models.IntegerField(blank=True, null=True)
    interviewer_comment = models.CharField(max_length=8000, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    venue_detail = models.CharField(max_length=2500, blank=True, null=True)
    feed_back_form_id = models.IntegerField()
    applicantstatus_id = models.IntegerField(blank=True, null=True)
    is_reschedule_requested = models.IntegerField(blank=True, null=True)
    interview_mode_id = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    tech_screening = models.IntegerField()
    feedback_reason = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField()
    reschedule_request_comment = models.CharField(max_length=2500, blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interview_requests'


class InterviewerFeedbacks(models.Model):
    applicant_status_id = models.IntegerField()
    interviewer_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    interviewfilledfeedbackform = models.ForeignKey(InterviewFilledFeedbackForms, blank=True, null=True)
    interview_request_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interviewer_feedbacks'


class Interviewers(models.Model):
    status = models.IntegerField(blank=True, null=True)
    is_qualified_interviewer = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interviewers'


class Issues(models.Model):
    issue_subject_id = models.IntegerField()
    issue_type_id = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    resolution_type_id = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'


class JobApprovalLevels(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_approval_levels'


class JobApprovers(models.Model):
    is_approved = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    approver_level_id = models.IntegerField()
    job_approver_status = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    is_current_approver = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'job_approvers'


class JobAssessmentTemplates(models.Model):
    assessment_template_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_assessment_templates'


class JobBusinessUnits(models.Model):
    bu_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_business_units'


class JobCampusConfigEvents(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    campus_id = models.IntegerField(blank=True, null=True)
    campus_group_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True, null=True)
    recruit_event_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    jobcampusconfigevent = models.ForeignKey('self', blank=True, null=True)
    masterjobrequisition = models.ForeignKey('MasterJobRequisitions', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_campus_config_events'


class JobCampusCriterias(models.Model):
    eligibility_criteria_id = models.IntegerField(blank=True, null=True)
    salary_package_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    jobcampusconfigevent = models.ForeignKey(JobCampusConfigEvents, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_campus_criterias'


class JobCategorys(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_categorys'


class JobCodeAssessmentTemplates(models.Model):
    assessment_template_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    jobcode_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_code_assessment_templates'


class JobCodeCompetencys(models.Model):
    competency_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    jobcode_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_code_competencys'


class JobCodePoints(models.Model):
    version = models.IntegerField()
    hierarchy_id = models.IntegerField()
    skill_category_id = models.IntegerField()
    points = models.FloatField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'job_code_points'


class JobCodes(models.Model):
    version = models.IntegerField()
    code = models.CharField(max_length=255, blank=True, null=True)
    requirement_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    sub_department_id = models.IntegerField(blank=True, null=True)
    experience_range_id = models.IntegerField(blank=True, null=True)
    skill_category_id = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    no_of_attachments = models.IntegerField(blank=True, null=True)
    experience_from = models.IntegerField(blank=True, null=True)
    experience_to = models.IntegerField(blank=True, null=True)
    hierarchy_id = models.IntegerField(blank=True, null=True)
    job_code_point_id = models.IntegerField(blank=True, null=True)
    published_on = models.DateTimeField(blank=True, null=True)
    published_by = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_alive = models.IntegerField(blank=True, null=True)
    is_draft = models.IntegerField(blank=True, null=True)
    is_archived = models.IntegerField(blank=True, null=True)
    salary_start = models.FloatField(blank=True, null=True)
    salary_end = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_codes'


class JobCompetencys(models.Model):
    competency_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_competencys'


class JobDelays(models.Model):
    delay_from = models.DateTimeField(blank=True, null=True)
    delay_to = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=400, blank=True, null=True)
    is_not_required = models.IntegerField()
    delay_category_id = models.IntegerField(blank=True, null=True)
    no_of_attachments = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_delays'


class JobEducationDetails(models.Model):
    degree_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_education_details'


class JobEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_events'


class JobFullTexts(models.Model):
    jobsearch_fulltext = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_full_texts'


class JobInterviewers(models.Model):
    interviewer_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_interviewers'


class JobLocations(models.Model):
    location_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_locations'


class JobPositions(models.Model):
    req_code = models.CharField(max_length=255)
    date_open = models.DateTimeField(blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    job_position_status_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    is_freezed = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    offered_date = models.DateTimeField(blank=True, null=True)
    joined_date = models.DateTimeField(blank=True, null=True)
    date_dropped = models.DateTimeField(blank=True, null=True)
    offer_accepted_date = models.DateTimeField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    is_position_joined = models.IntegerField(blank=True, null=True)
    is_position_joined_or_dropped = models.IntegerField(blank=True, null=True)
    planned_date_of_joining = models.DateTimeField(blank=True, null=True)
    is_internal_conversion = models.IntegerField()
    type_of_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_positions'


class JobPostings(models.Model):
    duplicate_template = models.IntegerField(blank=True, null=True)
    maximum_no_of_resumes = models.IntegerField(blank=True, null=True)
    posting_date = models.DateTimeField(blank=True, null=True)
    open_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    points = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    screening_template = models.IntegerField(blank=True, null=True)
    no_of_duplicates = models.IntegerField(blank=True, null=True)
    no_of_resumes_sourced = models.IntegerField(blank=True, null=True)
    posted_by = models.IntegerField(blank=True, null=True)
    self_service_type = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_postings'


class JobRequiredSkills(models.Model):
    skill_id = models.IntegerField(blank=True, null=True)
    priority_id = models.IntegerField(blank=True, null=True)
    mandatory_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_required_skills'


class JobScreeningRules(models.Model):
    priority = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    screeningrule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_screening_rules'


class JobSlas(models.Model):
    job_id = models.IntegerField()
    stage_id = models.IntegerField()
    active_pipeline_count = models.IntegerField(blank=True, null=True)
    good_pipeline_range_from = models.IntegerField(blank=True, null=True)
    good_pipeline_range_to = models.IntegerField(blank=True, null=True)
    avg_pipeline_range_from = models.IntegerField(blank=True, null=True)
    avg_pipeline_range_to = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    ageing_range_from = models.IntegerField(blank=True, null=True)
    ageing_range_to = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_slas'


class Jobs(models.Model):
    version = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    jobs_to_be_filled_within = models.DateTimeField(blank=True, null=True)
    requirements_priority_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    visibility_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    location_text = models.CharField(max_length=75, blank=True, null=True)
    salary_start = models.FloatField(blank=True, null=True)
    salary_end = models.FloatField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    experience_start = models.IntegerField(blank=True, null=True)
    experience_end = models.IntegerField(blank=True, null=True)
    technology_text = models.TextField(blank=True, null=True)
    no_of_openings = models.IntegerField()
    expertise_id = models.IntegerField(blank=True, null=True)
    hierarchy_id = models.IntegerField(blank=True, null=True)
    no_of_attachments = models.IntegerField()
    sensitivity = models.IntegerField(blank=True, null=True)
    primary_internal_hr_owner_id = models.IntegerField()
    primary_external_hr_owner_id = models.IntegerField()
    is_private = models.IntegerField()
    job_title = models.TextField(blank=True, null=True)
    is_company_confidential = models.IntegerField(blank=True, null=True)
    type_of_job = models.IntegerField(blank=True, null=True)
    projected_no_of_closer = models.IntegerField()
    customer_requisition_status = models.IntegerField(blank=True, null=True)
    internal_requisition_status = models.IntegerField(blank=True, null=True)
    avg_billing_amount_per_position = models.FloatField()
    expected_total_billing_amount = models.FloatField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    difficulty_level = models.IntegerField(blank=True, null=True)
    percentage_of_billing_we_do = models.FloatField()
    is_job_approved = models.IntegerField()
    skill_id = models.IntegerField(blank=True, null=True)
    job_open_date = models.DateTimeField(blank=True, null=True)
    job_closed_date = models.DateTimeField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    publish_to_employee_referral = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    job_name = models.CharField(max_length=100)
    jobsearch_text = models.TextField(blank=True, null=True)
    published_on = models.DateTimeField(blank=True, null=True)
    published_by = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_draft = models.IntegerField(blank=True, null=True)
    is_archived = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
    integer2 = models.IntegerField(blank=True, null=True)
    integer1 = models.IntegerField(blank=True, null=True)
    text4 = models.CharField(max_length=100, blank=True, null=True)
    text3 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    text1 = models.CharField(max_length=255, blank=True, null=True)
    is_alive = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    company_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    experience_range_id = models.IntegerField(blank=True, null=True)
    parent_job_thread_id = models.IntegerField(blank=True, null=True)
    is_freezed = models.TextField()  # This field type is a guess.
    jobfulltext_id = models.IntegerField(blank=True, null=True)
    work_mode = models.CharField(max_length=45, blank=True, null=True)
    other_work_mode = models.CharField(max_length=45, blank=True, null=True)
    type_of_organization = models.IntegerField(blank=True, null=True)
    other_interviewer = models.CharField(max_length=100, blank=True, null=True)
    hiring_manager_id = models.IntegerField(blank=True, null=True)
    project_start_date = models.DateTimeField(blank=True, null=True)
    cost_centre = models.CharField(max_length=45, blank=True, null=True)
    is_travel_required = models.TextField(blank=True, null=True)  # This field type is a guess.
    criticality = models.IntegerField(blank=True, null=True)
    is_budgeted = models.TextField(blank=True, null=True)  # This field type is a guess.
    job_code_id = models.IntegerField(blank=True, null=True)
    is_replacement = models.IntegerField(blank=True, null=True)
    replacement_text = models.CharField(max_length=100, blank=True, null=True)
    job_code_other_text = models.CharField(max_length=100, blank=True, null=True)
    job_code_point = models.IntegerField(blank=True, null=True)
    no_of_positions_joined = models.IntegerField(blank=True, null=True)
    no_of_positions_joined_or_dropped = models.IntegerField(blank=True, null=True)
    sub_department_id = models.IntegerField(blank=True, null=True)
    priority_id = models.IntegerField(blank=True, null=True)
    date_custom_field1 = models.DateTimeField(blank=True, null=True)
    date_custom_field2 = models.DateTimeField(blank=True, null=True)
    is_part_time_job = models.IntegerField()
    original_req_id = models.IntegerField(blank=True, null=True)
    is_heads_up_position = models.IntegerField()
    delay_days = models.IntegerField(blank=True, null=True)
    is_utilized = models.IntegerField()
    audio_file_name = models.CharField(max_length=255, blank=True, null=True)
    text5 = models.CharField(max_length=50, blank=True, null=True)
    integer3 = models.IntegerField(blank=True, null=True)
    integer4 = models.IntegerField(blank=True, null=True)
    integer5 = models.IntegerField(blank=True, null=True)
    is_screening_rule_configured = models.IntegerField(blank=True, null=True)
    business_unit_id = models.IntegerField(blank=True, null=True)
    sub_business_unit_id = models.IntegerField(blank=True, null=True)
    is_portal_hot_job = models.IntegerField(blank=True, null=True)
    is_job_posted = models.IntegerField(blank=True, null=True)
    is_job_posting_active = models.IntegerField(blank=True, null=True)
    status_modified_on_delay = models.DateTimeField(blank=True, null=True)
    sub_business_unit_name = models.CharField(max_length=255, blank=True, null=True)
    business_unit_name = models.CharField(max_length=255, blank=True, null=True)
    is_utilized_in_event = models.IntegerField(blank=True, null=True)
    job_approvers_names = models.CharField(max_length=255, blank=True, null=True)
    function_id = models.IntegerField(blank=True, null=True)
    sub_function_id = models.IntegerField(blank=True, null=True)
    search_status_id = models.IntegerField(blank=True, null=True)
    master_job_id = models.IntegerField(blank=True, null=True)
    selection_process_id = models.IntegerField(blank=True, null=True)
    male_diversity = models.IntegerField(blank=True, null=True)
    female_diversity = models.IntegerField(blank=True, null=True)
    years_of_passing = models.CharField(max_length=45, blank=True, null=True)
    is_status_notification = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class LanguageKnowns(models.Model):
    language_id = models.IntegerField()
    proficiency = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language_knowns'


class LanuageBarriers(models.Model):
    language_id = models.IntegerField(blank=True, null=True)
    proficiency = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    eligibilitycriteria = models.ForeignKey(EligibilityCriterias, blank=True, null=True)
    num_of_hiring = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lanuage_barriers'


class LegacyData(models.Model):
    source_id = models.IntegerField(primary_key=True)
    resume_source_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legacy_data'


class ListItems(models.Model):
    is_read = models.IntegerField()
    is_starred = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    list_id = models.IntegerField(blank=True, null=True)
    item_type = models.CharField(max_length=255, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'list_items'


class ListUsers(models.Model):
    user_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    list_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'list_users'


class Lists(models.Model):
    version = models.IntegerField()
    list_name = models.CharField(max_length=50, blank=True, null=True)
    target_type = models.IntegerField(blank=True, null=True)
    is_smart = models.IntegerField()
    search_type = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    smart_condition = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lists'


class LiteCandidate(models.Model):
    version = models.IntegerField()
    candidate_text = models.TextField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=255)
    is_active = models.IntegerField(blank=True, null=True)
    is_draft = models.IntegerField(blank=True, null=True)
    is_archived = models.IntegerField(blank=True, null=True)
    is_alive = models.IntegerField(blank=True, null=True)
    published_on = models.DateTimeField(blank=True, null=True)
    published_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lite_candidate'


class MacroTechnicals(models.Model):
    macro_technical_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'macro_technicals'


class MasterJobRequisitionCriterias(models.Model):
    version = models.IntegerField()
    eligibility_criteria_id = models.IntegerField(blank=True, null=True)
    salary_package_id = models.IntegerField(blank=True, null=True)
    campus_id = models.IntegerField(blank=True, null=True)
    recruit_event_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    campus_group_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    venue = models.TextField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    masterjobrequisition = models.ForeignKey('MasterJobRequisitions', blank=True, null=True)
    ec_positive_status_id = models.IntegerField(blank=True, null=True)
    ec_negetive_status_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_job_requisition_criterias'


class MasterJobRequisitions(models.Model):
    version = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    business_unit_id = models.IntegerField(blank=True, null=True)
    hiring_manager_id = models.IntegerField(blank=True, null=True)
    no_of_males = models.IntegerField(blank=True, null=True)
    no_of_females = models.IntegerField(blank=True, null=True)
    no_of_openings = models.IntegerField(blank=True, null=True)
    year_of_passing_from = models.IntegerField(blank=True, null=True)
    year_of_passing_to = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    masterjob = models.ForeignKey('MasterJobs', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_job_requisitions'


class MasterJobs(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    year_of_passing_from = models.IntegerField(blank=True, null=True)
    year_of_passing_to = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    master_job_status = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
    integer5 = models.IntegerField(blank=True, null=True)
    integer4 = models.IntegerField(blank=True, null=True)
    integer3 = models.IntegerField(blank=True, null=True)
    integer2 = models.IntegerField(blank=True, null=True)
    integer1 = models.IntegerField(blank=True, null=True)
    text5 = models.CharField(max_length=50, blank=True, null=True)
    text4 = models.CharField(max_length=50, blank=True, null=True)
    text3 = models.CharField(max_length=50, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    text1 = models.CharField(max_length=50, blank=True, null=True)
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
    is_utilized_in_event = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_jobs'


class MasterReports(models.Model):
    version = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)
    job_name = models.CharField(max_length=255, blank=True, null=True)
    job_code_id = models.IntegerField(blank=True, null=True)
    position_code = models.CharField(max_length=255, blank=True, null=True)
    business_unit_id = models.IntegerField(blank=True, null=True)
    sub_business_unit_id = models.IntegerField(blank=True, null=True)
    hiring_manager_id = models.IntegerField(blank=True, null=True)
    request_date = models.DateTimeField(blank=True, null=True)
    project_start_date = models.DateTimeField(blank=True, null=True)
    offer_date = models.DateTimeField(blank=True, null=True)
    joining_date = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    ageing = models.IntegerField(blank=True, null=True)
    tareaction_time = models.IntegerField(blank=True, null=True)
    request_to_selected_tat = models.IntegerField(blank=True, null=True)
    selected_to_joining_tat = models.IntegerField(blank=True, null=True)
    request_to_joined_tat = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    req_cancelled_or_on_hold_date = models.DateTimeField(blank=True, null=True)
    ageing_request_to_drop_date = models.IntegerField(blank=True, null=True)
    hiring_manager_text = models.CharField(max_length=45, blank=True, null=True)
    job_code_text = models.CharField(max_length=45, blank=True, null=True)
    business_unit_text = models.CharField(max_length=45, blank=True, null=True)
    sub_business_unit_text = models.CharField(max_length=45, blank=True, null=True)
    position_status_id = models.IntegerField(blank=True, null=True)
    position_status_text = models.CharField(max_length=255, blank=True, null=True)
    offer_accepted_date = models.DateTimeField(blank=True, null=True)
    planned_date_of_joining = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    candidate_name = models.CharField(max_length=50, blank=True, null=True)
    job_status = models.CharField(max_length=50, blank=True, null=True)
    job_text1 = models.CharField(max_length=50, blank=True, null=True)
    job_text2 = models.CharField(max_length=50, blank=True, null=True)
    job_text3 = models.CharField(max_length=50, blank=True, null=True)
    job_text4 = models.CharField(max_length=50, blank=True, null=True)
    job_integer1 = models.IntegerField(blank=True, null=True)
    job_integer2 = models.IntegerField(blank=True, null=True)
    skill_category = models.CharField(max_length=45, blank=True, null=True)
    offer_pending_date = models.DateTimeField(blank=True, null=True)
    position_closed_date = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=45, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    source_type = models.IntegerField(blank=True, null=True)
    matching_to_offer_pending_tat = models.IntegerField(blank=True, null=True)
    offer_pending_to_fitment_approved_tat = models.IntegerField(blank=True, null=True)
    offer_pending_to_selected_tat = models.IntegerField(blank=True, null=True)
    job_date_custom_field1 = models.DateTimeField(blank=True, null=True)
    job_date_custom_field2 = models.DateTimeField(blank=True, null=True)
    recruiter_name = models.CharField(max_length=45, blank=True, null=True)
    heads_up_position = models.IntegerField()
    original_requisition_id = models.IntegerField(blank=True, null=True)
    part_time_job = models.IntegerField()
    cost_centre = models.CharField(max_length=45, blank=True, null=True)
    replacement = models.CharField(max_length=255, blank=True, null=True)
    position_type = models.IntegerField()
    candidate_text1 = models.CharField(max_length=255, blank=True, null=True)
    candidate_text2 = models.CharField(max_length=255, blank=True, null=True)
    candidate_text3 = models.CharField(max_length=255, blank=True, null=True)
    candidate_text4 = models.CharField(max_length=255, blank=True, null=True)
    candidate_integer1 = models.IntegerField(blank=True, null=True)
    candidate_integer2 = models.IntegerField(blank=True, null=True)
    request_to_selected_delay = models.IntegerField(blank=True, null=True)
    selected_to_joining_delay = models.IntegerField(blank=True, null=True)
    request_to_joined_delay = models.IntegerField(blank=True, null=True)
    matching_to_offer_pending_delay = models.IntegerField(blank=True, null=True)
    offer_pending_to_fitment_approved_delay = models.IntegerField(blank=True, null=True)
    offer_pending_to_selected_delay = models.IntegerField(blank=True, null=True)
    position_id = models.IntegerField(blank=True, null=True)
    aging_delay = models.IntegerField(blank=True, null=True)
    tareaction_time_delay = models.IntegerField(blank=True, null=True)
    aging_request_to_drop_date_delay = models.IntegerField(blank=True, null=True)
    job_text5 = models.CharField(max_length=50, blank=True, null=True)
    job_integer3 = models.IntegerField(blank=True, null=True)
    job_integer4 = models.IntegerField(blank=True, null=True)
    job_integer5 = models.IntegerField(blank=True, null=True)
    candidate_text5 = models.CharField(max_length=50, blank=True, null=True)
    candidate_integer3 = models.IntegerField(blank=True, null=True)
    candidate_integer4 = models.IntegerField(blank=True, null=True)
    candidate_integer5 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_reports'


class Mifreports(models.Model):
    version = models.IntegerField()
    candidate_id = models.IntegerField(blank=True, null=True)
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    job_name = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    process = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    alternate_email = models.CharField(max_length=255, blank=True, null=True)
    degree_text = models.CharField(max_length=255, blank=True, null=True)
    highest_qualification = models.CharField(max_length=255, blank=True, null=True)
    degree_type_text = models.CharField(max_length=255, blank=True, null=True)
    stream = models.CharField(max_length=255, blank=True, null=True)
    year_of_passing = models.CharField(max_length=255, blank=True, null=True)
    percentage_of_cgpa = models.FloatField(blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    candidate_created_on = models.DateTimeField(blank=True, null=True)
    source_type = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    stages = models.CharField(max_length=255, blank=True, null=True)
    scores = models.CharField(max_length=255, blank=True, null=True)
    is_archived = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'mifreports'


class Modules(models.Model):
    version = models.IntegerField()
    module_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'modules'


class MonthlyEffortPipeLineReports(models.Model):
    version = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)
    job_name = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    source_name = models.CharField(max_length=255, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    total_cv_sourced = models.IntegerField(blank=True, null=True)
    number_of_first_level_interview = models.IntegerField(blank=True, null=True)
    number_of_first_level_shortlisted = models.IntegerField(blank=True, null=True)
    number_of_final_round_interviews = models.IntegerField(blank=True, null=True)
    number_of_final_round_shortlisted = models.IntegerField(blank=True, null=True)
    number_of_no_shows = models.IntegerField(blank=True, null=True)
    number_of_offer_released = models.IntegerField(blank=True, null=True)
    number_of_offer_accepted = models.IntegerField(blank=True, null=True)
    number_of_joinees = models.IntegerField(blank=True, null=True)
    business_unit_id = models.IntegerField(blank=True, null=True)
    type_of_source = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    hirepro_source_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_effort_pipe_line_reports'


class NonAcademics(models.Model):
    nacategory_id = models.IntegerField(blank=True, null=True)
    nacategory_value_id = models.IntegerField(blank=True, null=True)
    num_of_hiring = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    eligibilitycriteria = models.ForeignKey(EligibilityCriterias, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_academics'


class NonComplianceCandidatess(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    actual_time = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    noncompliancereportoutput_id = models.IntegerField(blank=True, null=True)
    time_exceed = models.IntegerField(blank=True, null=True)
    compliance_date = models.DateTimeField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    type_of_source = models.IntegerField(blank=True, null=True)
    is_active_non_compliance = models.IntegerField(blank=True, null=True)
    applicant_status_date = models.DateTimeField(blank=True, null=True)
    source_name = models.CharField(max_length=256, blank=True, null=True)
    location = models.IntegerField(blank=True, null=True)
    contact_number = models.CharField(max_length=50, blank=True, null=True)
    office_number = models.CharField(max_length=50, blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    location_text = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_compliance_candidatess'


class NonComplianceReportOutputs(models.Model):
    version = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)
    job_name = models.CharField(max_length=255, blank=True, null=True)
    job_primary_owner_id = models.IntegerField(blank=True, null=True)
    job_primary_owner_name = models.CharField(max_length=255, blank=True, null=True)
    compliance_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    job_code_id = models.IntegerField(blank=True, null=True)
    job_code_name = models.CharField(max_length=45, blank=True, null=True)
    hiring_manager_id = models.IntegerField(blank=True, null=True)
    hiring_manager_name = models.CharField(max_length=255, blank=True, null=True)
    unit_id = models.IntegerField(blank=True, null=True)
    unit_name = models.CharField(max_length=255, blank=True, null=True)
    job_location = models.IntegerField(blank=True, null=True)
    job_location_text = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_compliance_report_outputs'


class NotificationActionRoles(models.Model):
    version = models.IntegerField()
    user_role_value_id = models.IntegerField(blank=True, null=True)
    user_role_value_text = models.CharField(max_length=255, blank=True, null=True)
    action_value_id = models.IntegerField(blank=True, null=True)
    action_value_text = models.CharField(max_length=255, blank=True, null=True)
    entity_type = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'notification_action_roles'


class NotificationConfigurations(models.Model):
    version = models.IntegerField()
    notification_id = models.IntegerField(blank=True, null=True)
    notification_target = models.IntegerField(blank=True, null=True)
    notification_type = models.IntegerField(blank=True, null=True)
    is_enabled = models.IntegerField(blank=True, null=True)
    notification_watcher = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    tenant_id = models.IntegerField(blank=True, null=True)
    mail_watcher = models.CharField(max_length=255, blank=True, null=True)
    sms_watcher = models.CharField(max_length=255, blank=True, null=True)
    is_system_notification = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notification_configurations'


class NotificationRecepients(models.Model):
    version = models.IntegerField()
    recepient_name = models.CharField(max_length=255, blank=True, null=True)
    recepient_email = models.CharField(max_length=255, blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    contact_type = models.IntegerField(blank=True, null=True)
    is_ignored = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    notificationscheme_id = models.IntegerField(blank=True, null=True)
    notificationactionrole_id = models.IntegerField(blank=True, null=True)
    is_sms_notification = models.TextField(blank=True, null=True)  # This field type is a guess.
    mobile_number = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_recepients'


class NotificationSchemes(models.Model):
    version = models.IntegerField()
    notification_scheme_name = models.CharField(max_length=255, blank=True, null=True)
    is_enabled = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'notification_schemes'


class OfferApprovers(models.Model):
    is_approved = models.IntegerField()
    user_id = models.IntegerField()
    approver_level_id = models.IntegerField()
    offer_approver_status = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    offer_id = models.IntegerField(blank=True, null=True)
    is_current_approver = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'offer_approvers'


class OfferBillingHistorys(models.Model):
    status = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    offer_id = models.IntegerField(blank=True, null=True)
    hirepro_billing_comment = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_billing_historys'


class OfferEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    offer_id = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_events'


class Offers(models.Model):
    position_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_resignation = models.DateTimeField(blank=True, null=True)
    date_of_relieving = models.DateTimeField(blank=True, null=True)
    date_of_joining = models.DateTimeField(blank=True, null=True)
    base_salary = models.CharField(max_length=255, blank=True, null=True)
    bonus = models.CharField(max_length=255, blank=True, null=True)
    benefits = models.CharField(max_length=255, blank=True, null=True)
    ctc = models.CharField(max_length=255, blank=True, null=True)
    stocks = models.CharField(max_length=255, blank=True, null=True)
    vendor_billing_amount = models.CharField(max_length=255, blank=True, null=True)
    reason_of_abort = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_billing_amount = models.FloatField(blank=True, null=True)
    planned_date_of_joining = models.DateTimeField(blank=True, null=True)
    joining_location = models.IntegerField(blank=True, null=True)
    offer_approval_status = models.IntegerField(blank=True, null=True)
    offer_approval_note = models.CharField(max_length=4000, blank=True, null=True)
    offer_approved_date = models.DateTimeField(blank=True, null=True)
    offer_letter_file_id = models.IntegerField(blank=True, null=True)
    level_id = models.IntegerField(blank=True, null=True)
    offered_ctc = models.FloatField(blank=True, null=True)
    basic_salary = models.FloatField(blank=True, null=True)
    designation_name = models.CharField(max_length=255, blank=True, null=True)
    no_of_attachments = models.IntegerField(blank=True, null=True)
    candidate_source_id = models.IntegerField(blank=True, null=True)
    vendor_contract_level_id = models.IntegerField(blank=True, null=True)
    vendor_billing_percentage = models.FloatField(blank=True, null=True)
    vendor_billing_comment = models.CharField(max_length=255, blank=True, null=True)
    type_of_source = models.IntegerField(blank=True, null=True)
    hirepro_billing_amount = models.FloatField(blank=True, null=True)
    hirepro_billing_comment = models.CharField(max_length=255, blank=True, null=True)
    hirepro_billing_percentage = models.FloatField(blank=True, null=True)
    billing_status = models.IntegerField(blank=True, null=True)
    hirepro_contract_level_id = models.IntegerField(blank=True, null=True)
    position_id = models.IntegerField(blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)
    text1 = models.CharField(max_length=50, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    text3 = models.CharField(max_length=50, blank=True, null=True)
    text4 = models.CharField(max_length=50, blank=True, null=True)
    text5 = models.CharField(max_length=50, blank=True, null=True)
    integer1 = models.IntegerField(blank=True, null=True)
    integer2 = models.IntegerField(blank=True, null=True)
    integer3 = models.IntegerField(blank=True, null=True)
    integer4 = models.IntegerField(blank=True, null=True)
    integer5 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    salarystructurecustomized_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offers'


class OnboardingCandidateAttachments(models.Model):
    version = models.IntegerField()
    attachement_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    onboardingcandidate_id = models.IntegerField(blank=True, null=True)
    file_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onboarding_candidate_attachments'


class OnboardingCandidates(models.Model):
    version = models.IntegerField()
    candidate_id = models.IntegerField(blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    joined_date = models.DateTimeField(blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
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
    candidate_name = models.CharField(max_length=55)
    candidate_user_id = models.IntegerField()
    is_onboarding_process_completed = models.IntegerField()
    activity_completion_date = models.DateTimeField(blank=True, null=True)
    activity_id = models.IntegerField(blank=True, null=True)
    activity_due_date = models.DateTimeField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    org_employee_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onboarding_candidates'


class OnboardingEmployeeTaskAttachments(models.Model):
    version = models.IntegerField()
    onboarding_candidate_attachement_id = models.IntegerField(blank=True, null=True)
    attachement_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    onboardingemployeetask_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onboarding_employee_task_attachments'


class OnboardingEmployeeTasks(models.Model):
    version = models.IntegerField()
    due_date = models.DateTimeField(blank=True, null=True)
    read_only_form_html = models.CharField(max_length=255, blank=True, null=True)
    edit_form_html = models.CharField(max_length=30000, blank=True, null=True)
    task_status = models.IntegerField(blank=True, null=True)
    assignee_user_id = models.IntegerField(blank=True, null=True)
    reporter_user_id = models.IntegerField(blank=True, null=True)
    approver_user_id = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    onboardingcandidate_id = models.IntegerField(blank=True, null=True)
    onboardingtask_id = models.IntegerField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    is_not_applicable = models.IntegerField(blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    employee_remarks = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onboarding_employee_tasks'


class OnboardingEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link_to_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    target_id = models.IntegerField(blank=True, null=True)
    target_id_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onboarding_events'


class OnboardingForms(models.Model):
    version = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    edit_form_html = models.CharField(max_length=30000, blank=True, null=True)
    read_only_form_html = models.CharField(max_length=30000, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'onboarding_forms'


class OnboardingTasks(models.Model):
    version = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    objective_of_task = models.CharField(max_length=1000, blank=True, null=True)
    impact_of_task = models.CharField(max_length=1000, blank=True, null=True)
    onboarding_department = models.IntegerField(blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    designation = models.IntegerField(blank=True, null=True)
    assignee = models.IntegerField(blank=True, null=True)
    reporter = models.IntegerField(blank=True, null=True)
    approver = models.IntegerField(blank=True, null=True)
    time_limit = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
    integer2 = models.IntegerField(blank=True, null=True)
    integer1 = models.IntegerField(blank=True, null=True)
    text4 = models.CharField(max_length=50, blank=True, null=True)
    text3 = models.CharField(max_length=50, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    text1 = models.CharField(max_length=50, blank=True, null=True)
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
    onboardingform_id = models.IntegerField(blank=True, null=True)
    is_attachment_required = models.IntegerField()
    activity_id = models.IntegerField(blank=True, null=True)
    phase_id = models.IntegerField(blank=True, null=True)
    text5 = models.CharField(max_length=50, blank=True, null=True)
    integer3 = models.IntegerField(blank=True, null=True)
    integer4 = models.IntegerField(blank=True, null=True)
    integer5 = models.IntegerField(blank=True, null=True)
    onboardingtask_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onboarding_tasks'


class OnlineSpecificQuestions(models.Model):
    section_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    testuser_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_specific_questions'


class OptionalGroupSets(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    guid = models.CharField(max_length=40)
    questionpaperinfo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'optional_group_sets'


class OptionalGroups(models.Model):
    version = models.IntegerField()
    group_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    guid = models.CharField(max_length=40)
    optionalgroupset_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'optional_groups'


class OwnerContactDetails(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    job = models.ForeignKey(Jobs)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'owner_contact_details'


class Page(models.Model):
    version = models.IntegerField()
    title = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True, null=True)
    layout_type = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    is_current = models.IntegerField(blank=True, null=True)
    guid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'page'


class PaperFrameworks(models.Model):
    client_information = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    max_marks = models.FloatField(blank=True, null=True)
    total_attemt_time = models.IntegerField(blank=True, null=True)
    correct = models.FloatField(blank=True, null=True)
    in_correct = models.FloatField(blank=True, null=True)
    partial_correct = models.FloatField(blank=True, null=True)
    left_entries = models.FloatField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paper_frameworks'


class PaperSetQuestions(models.Model):
    question_id = models.IntegerField()
    order_id = models.IntegerField()
    section_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    paperset_id = models.IntegerField(blank=True, null=True)
    question_tenant_id = models.IntegerField(blank=True, null=True)
    papersetquestion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paper_set_questions'


class PaperSets(models.Model):
    version = models.IntegerField()
    set_code = models.CharField(max_length=255, blank=True, null=True)
    no_of_attachments = models.IntegerField()
    paper_set_answer_string = models.CharField(max_length=255, blank=True, null=True)
    sub_category_answer_string = models.CharField(max_length=480, blank=True, null=True)
    set_preview_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    questionpaperinfo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paper_sets'


class PendingItems(models.Model):
    version = models.IntegerField()
    scheduled_task = models.CharField(max_length=255, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    item_type = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'pending_items'


class PersistOfflineXlsDetails(models.Model):
    xls_file_id = models.CharField(max_length=255)
    serialized_offline_xls_data = models.TextField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persist_offline_xls_details'


class Phasess(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    time_limit = models.IntegerField(blank=True, null=True)
    phase_owner = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    activity_id = models.IntegerField(blank=True, null=True)
    is_published_to_vendor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phasess'


class PhoneCalls(models.Model):
    version = models.IntegerField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=75, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    direction = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
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
    link_to_type = models.CharField(max_length=255, blank=True, null=True)
    link_to_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_calls'


class PofuCallHistorys(models.Model):
    status_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    pofucall_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pofu_call_historys'


class PofuCalls(models.Model):
    assignee = models.IntegerField()
    activity_id = models.IntegerField()
    current_status_id = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    pofu_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pofu_calls'


class Pofus(models.Model):
    version = models.IntegerField()
    call_history = models.TextField(blank=True, null=True)
    applicant_status_id = models.IntegerField()
    candidate_pofu_category_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pofus'


class PortalContractDetails(models.Model):
    cost = models.FloatField(blank=True, null=True)
    contract_start_date = models.DateTimeField(blank=True, null=True)
    contract_expiry_date = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_contract_details'


class PortalLoginInfos(models.Model):
    user_id = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=60, blank=True, null=True)
    user_name = models.CharField(max_length=75, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    portal_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_login_infos'


class PortalReports(models.Model):
    version = models.IntegerField()
    visitors = models.IntegerField()
    apllications = models.IntegerField()
    referrals = models.IntegerField()
    direct_applicants = models.IntegerField()
    job_clicks = models.IntegerField()
    organization_clicks = models.IntegerField()
    job_searches = models.IntegerField()
    report_date = models.DateTimeField()
    referral_lead = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'portal_reports'


class Portals(models.Model):
    source_id = models.IntegerField(primary_key=True)
    company_id = models.IntegerField(blank=True, null=True)
    portalcontractdetail_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portals'


class ProfileWeightageConfigurations(models.Model):
    version = models.IntegerField()
    weightage = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    tenant_id = models.IntegerField(blank=True, null=True)
    profile_weightage_id = models.IntegerField(blank=True, null=True)
    parent_profile_id = models.IntegerField(db_column='parent_profile_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profile_weightage_configurations'


class ProfileWeightages(models.Model):
    version = models.IntegerField()
    weightage = models.IntegerField(blank=True, null=True)
    profile_name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    profileweightage_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_weightages'


class QaPersonnels(models.Model):
    qa_id = models.IntegerField(blank=True, null=True)
    is_qa_completed = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    questionpaperinfo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qa_personnels'


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


class QuartzCronTriggers(models.Model):
    trigger_name = models.CharField(max_length=50)
    trigger_group = models.CharField(max_length=50)
    cron_expression = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quartz_cron_triggers'
        unique_together = (('trigger_name', 'trigger_group'),)


class QuartzJobs(models.Model):
    job_name = models.CharField(max_length=50)
    job_group = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    job_class_name = models.TextField(blank=True, null=True)
    is_durable = models.IntegerField(blank=True, null=True)
    is_volatile = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quartz_jobs'
        unique_together = (('job_name', 'job_group'),)


class QuartzSimpleTriggers(models.Model):
    trigger_name = models.CharField(max_length=50)
    trigger_group = models.CharField(max_length=50)
    repeat_count = models.IntegerField(blank=True, null=True)
    repeat_interval = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quartz_simple_triggers'
        unique_together = (('trigger_name', 'trigger_group'),)


class QuartzTriggers(models.Model):
    trigger_name = models.CharField(max_length=50)
    trigger_group = models.CharField(max_length=50)
    is_volatile = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    next_fire_time = models.DateTimeField(blank=True, null=True)
    prev_fire_time = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    trigger_state = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    job_name = models.CharField(max_length=50)
    job_group = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'quartz_triggers'
        unique_together = (('trigger_name', 'trigger_group'),)


class QuestionApprovers(models.Model):
    question_id = models.IntegerField()
    editor = models.IntegerField()
    edited_date = models.DateTimeField()
    edited_reason = models.CharField(max_length=500)
    approver = models.IntegerField()
    approval_status = models.IntegerField()
    approval_date = models.DateTimeField(blank=True, null=True)
    approver_comment = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    editedquestion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_approvers'


class QuestionAttachments(models.Model):
    version = models.IntegerField()
    file_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    question_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_attachments'


class QuestionFullTexts(models.Model):
    question_search_full_text = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_full_texts'


class QuestionNoteAttachments(models.Model):
    version = models.IntegerField()
    file_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    question_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_note_attachments'


class QuestionPaperCaches(models.Model):
    question_paper_id = models.IntegerField()
    question_paper_json = models.TextField()
    tenant_id = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'question_paper_caches'


class QuestionPaperCompanys(models.Model):
    company_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    questionpaperinfo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_paper_companys'


class QuestionPaperInfos(models.Model):
    version = models.IntegerField()
    question_paper_code = models.CharField(max_length=255, blank=True, null=True)
    qp_information = models.CharField(max_length=1024, blank=True, null=True)
    question_paper_reuse = models.IntegerField()
    difficulty_level = models.IntegerField(blank=True, null=True)
    question_paper_name = models.CharField(max_length=255, blank=True, null=True)
    total_questions = models.IntegerField(blank=True, null=True)
    is_qa_pending = models.IntegerField()
    is_published = models.IntegerField()
    no_of_attachments = models.IntegerField()
    instruction_id = models.IntegerField(blank=True, null=True)
    tag_assessment_line = models.IntegerField(blank=True, null=True)
    qp_category_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    master_answer_string = models.CharField(max_length=2000, blank=True, null=True)
    sub_category_answer_string = models.CharField(max_length=2000, blank=True, null=True)
    preview_id = models.IntegerField(blank=True, null=True)
    is_survey_question_paper = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
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
    question_randomizing = models.IntegerField()
    is_optional_group = models.IntegerField()
    is_clone_qp = models.IntegerField(blank=True, null=True)
    is_online_specific = models.IntegerField()
    blue_print_id = models.IntegerField(blank=True, null=True)
    foreign_question_paper_info_id = models.IntegerField(blank=True, null=True)
    question_paper_type = models.IntegerField()
    is_edited_blue_print_paper = models.IntegerField()
    instruction_text = models.TextField(blank=True, null=True)
    question_paper_info_tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_paper_infos'


class QuestionPaperInstuctionAttachments(models.Model):
    version = models.IntegerField()
    file_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    questionpaperinfo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_paper_instuction_attachments'


class QuestionPaperQuestionInfos(models.Model):
    coding_language_id = models.IntegerField(blank=True, null=True)
    coding_snippet = models.CharField(max_length=3000, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    questionpaperquestion = models.ForeignKey('QuestionPaperQuestions', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_paper_question_infos'


class QuestionPaperQuestions(models.Model):
    section_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    questionpaperinfo_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    source_text = models.CharField(max_length=50, blank=True, null=True)
    question_tenant_id = models.IntegerField(blank=True, null=True)
    evalution_method = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_paper_questions'


class QuestionStatisticss(models.Model):
    total_attempt = models.IntegerField()
    correct = models.IntegerField()
    in_correct = models.IntegerField()
    un_attempted = models.IntegerField()
    facility_value = models.FloatField()
    item_difficulty = models.FloatField()
    no_attend_a = models.IntegerField()
    distractor_index_of_a = models.FloatField()
    no_attend_b = models.IntegerField()
    distractor_index_of_b = models.FloatField()
    no_attend_c = models.IntegerField()
    distractor_index_of_c = models.FloatField()
    no_attend_d = models.IntegerField()
    distractor_index_of_d = models.FloatField()
    exposure_rate = models.IntegerField()
    avg_response_time = models.FloatField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_statisticss'


class Questions(models.Model):
    version = models.IntegerField()
    question_type = models.IntegerField(blank=True, null=True)
    sub_categories_id = models.IntegerField(blank=True, null=True)
    difficulty_level = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    question_str = models.CharField(max_length=7000, blank=True, null=True)
    question_reuse = models.IntegerField()
    is_qa_pending = models.IntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    instruction_id = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    no_of_attachments = models.IntegerField()
    html_string = models.TextField(blank=True, null=True)
    question_label = models.CharField(max_length=255, blank=True, null=True)
    preview_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
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
    guid = models.CharField(max_length=64)
    question_id = models.IntegerField(blank=True, null=True)
    is_survey_question = models.IntegerField()
    total_attempt = models.IntegerField()
    correct = models.IntegerField()
    in_correct = models.IntegerField()
    un_attempted = models.IntegerField()
    source_text = models.CharField(max_length=1024, blank=True, null=True)
    questionfulltext_id = models.IntegerField(blank=True, null=True)
    is_revised = models.IntegerField()
    sub_topic_id = models.IntegerField(blank=True, null=True)
    questionstatistics_id = models.IntegerField(blank=True, null=True)
    foreign_question_id = models.IntegerField(blank=True, null=True)
    foreign_tenant_id = models.IntegerField(blank=True, null=True)
    hirepro_question_id = models.IntegerField(blank=True, null=True)
    author = models.IntegerField(blank=True, null=True)
    question_originality = models.IntegerField()
    question_flag = models.IntegerField()
    is_edited_question_exist = models.IntegerField()
    is_approved_edited_question_exist = models.IntegerField()
    sub_topic_unit_id = models.IntegerField(blank=True, null=True)
    question_title = models.CharField(max_length=255, blank=True, null=True)
    memory_limit = models.CharField(max_length=255, blank=True, null=True)
    time_limit = models.CharField(max_length=255, blank=True, null=True)
    code_size = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class RandomizedQuestions(models.Model):
    version = models.IntegerField()
    question_id = models.IntegerField(blank=True, null=True)
    section_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    testuser_id = models.IntegerField(blank=True, null=True)
    question_tenant_id = models.IntegerField(blank=True, null=True)
    randomizedquestion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'randomized_questions'


class RecruitEventCandidateQnPapers(models.Model):
    qn_paper_id = models.IntegerField(blank=True, null=True)
    qn_paper_code = models.CharField(max_length=255, blank=True, null=True)
    answer_string = models.CharField(max_length=255, blank=True, null=True)
    is_evaluated = models.IntegerField(blank=True, null=True)
    log = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruiteventcandidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruit_event_candidate_qn_papers'


class RecruitEventCandidateScores(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    correct = models.IntegerField(blank=True, null=True)
    in_correct = models.IntegerField(blank=True, null=True)
    qn_paper_id = models.IntegerField(blank=True, null=True)
    qn_paper_code = models.CharField(max_length=255, blank=True, null=True)
    log_error = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruiteventcandidate_id = models.IntegerField(blank=True, null=True)
    recruiteventcandidatescore_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruit_event_candidate_scores'


class RecruitEventCandidates(models.Model):
    total_score = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    candidate_regn_id = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    recruiteventjob_id = models.IntegerField(blank=True, null=True)
    recruitevent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruit_event_candidates'


class RecruitEventConfigTemps(models.Model):
    version = models.IntegerField()
    master_job_id = models.IntegerField()
    requirement_content = models.TextField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'recruit_event_config_temps'


class RecruitEventCriterias(models.Model):
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruitevent = models.ForeignKey('RecruitEvents', blank=True, null=True)
    eligibility_criteria_id = models.IntegerField(blank=True, null=True)
    salary_package_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruit_event_criterias'


class RecruitEventJobTests(models.Model):
    job_id = models.IntegerField(blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruitevent = models.ForeignKey('RecruitEvents', blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_to = models.DateTimeField(blank=True, null=True)
    stage_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruit_event_job_tests'


class RecruitEventJobs(models.Model):
    assessment_line_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruitevent_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruit_event_jobs'


class RecruitEventOwners(models.Model):
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    recruitevent_id = models.IntegerField(blank=True, null=True)
    types_of_coordinator = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruit_event_owners'


class RecruitEventQnPaperSets(models.Model):
    set_id = models.IntegerField(blank=True, null=True)
    set_code = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruiteventqnpaper_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruit_event_qn_paper_sets'


class RecruitEventQnPapers(models.Model):
    question_paper_id = models.IntegerField()
    is_qn_paper_set_generated = models.IntegerField()
    is_excel_file_uploaded = models.IntegerField(blank=True, null=True)
    no_of_excel_file_attachments = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruiteventjob_id = models.IntegerField(blank=True, null=True)
    paperframework_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruit_event_qn_papers'


class RecruitEventResumeStatuss(models.Model):
    resume_status_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    recruitevent = models.ForeignKey('RecruitEvents', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruit_event_resume_statuss'


class RecruitEvents(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255)
    location_id = models.IntegerField(blank=True, null=True)
    date_from = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    primary_owner_id = models.IntegerField()
    location_text = models.CharField(max_length=255, blank=True, null=True)
    no_of_attachments = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type_of_event = models.IntegerField(blank=True, null=True)
    no_of_participants = models.IntegerField(blank=True, null=True)
    event_code = models.CharField(max_length=255, blank=True, null=True)
    last_cand_regn_no = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
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
    job_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    college_venue_id = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=45, blank=True, null=True)
    website = models.CharField(max_length=45, blank=True, null=True)
    domain = models.CharField(max_length=45, blank=True, null=True)
    contact_person = models.CharField(max_length=45, blank=True, null=True)
    qualification = models.CharField(max_length=45, blank=True, null=True)
    eligibility = models.CharField(max_length=45, blank=True, null=True)
    expirience = models.CharField(max_length=45, blank=True, null=True)
    job_description = models.CharField(max_length=45, blank=True, null=True)
    is_confidential = models.IntegerField(blank=True, null=True)
    campus_id = models.IntegerField(blank=True, null=True)
    num_of_tentative_hiring = models.IntegerField(blank=True, null=True)
    campus_date_from = models.DateTimeField(blank=True, null=True)
    corporate_date_from = models.DateTimeField(blank=True, null=True)
    campus_date_to = models.DateTimeField(blank=True, null=True)
    corporate_date_to = models.DateTimeField(blank=True, null=True)
    campus_description = models.CharField(max_length=255, blank=True, null=True)
    corporate_description = models.CharField(max_length=255, blank=True, null=True)
    is_utilized = models.IntegerField()
    anchor_text = models.CharField(max_length=6000, blank=True, null=True)
    college_text = models.CharField(max_length=6000, blank=True, null=True)
    no_of_jobs = models.IntegerField()
    no_of_tests = models.IntegerField()
    master_job_id = models.IntegerField(blank=True, null=True)
    is_tpo_enabled = models.IntegerField()
    is_auto_checked_ec = models.IntegerField()
    is_status_notification = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recruit_events'


class RecruitmentTips(models.Model):
    version = models.IntegerField()
    tip = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=38)

    class Meta:
        managed = False
        db_table = 'recruitment_tips'


class ReferralCollections(models.Model):
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    candidate_email1 = models.CharField(max_length=255, blank=True, null=True)
    candidate_contact_number = models.CharField(max_length=255, blank=True, null=True)
    candidate_experience = models.IntegerField()
    file_id = models.IntegerField()
    resume_expiry_date = models.DateTimeField(blank=True, null=True)
    qastatus = models.IntegerField()
    approved_candidate_id = models.IntegerField(blank=True, null=True)
    candidate_current_employer_text = models.CharField(max_length=255, blank=True, null=True)
    candidate_current_employer_id = models.IntegerField(blank=True, null=True)
    candidate_current_location_id = models.IntegerField(blank=True, null=True)
    candidate_current_location_text = models.CharField(max_length=255, blank=True, null=True)
    is_lead = models.IntegerField()
    is_name_show = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    referral_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referral_collections'


class Referrals(models.Model):
    source_id = models.IntegerField(primary_key=True)
    net_brownie_points = models.IntegerField(blank=True, null=True)
    contract_id = models.IntegerField(blank=True, null=True)
    referral_contact_type = models.CharField(max_length=255, blank=True, null=True)
    referral_contact_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referrals'


class ReportDefinitions(models.Model):
    version = models.IntegerField()
    report_name = models.CharField(max_length=255, blank=True, null=True)
    is_cv_utilization_required = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    is_pre_defined_sla_required = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'report_definitions'


class ReportOutputs(models.Model):
    job_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    definition_id = models.IntegerField()
    status_type = models.IntegerField(blank=True, null=True)
    report_version = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    ratio_text = models.CharField(max_length=45, blank=True, null=True)
    job_code_name = models.CharField(max_length=45, blank=True, null=True)
    job_open_date = models.DateTimeField(blank=True, null=True)
    generated_on = models.DateTimeField(blank=True, null=True)
    hiring_manger_id = models.IntegerField(blank=True, null=True)
    hiring_manager = models.CharField(max_length=50, blank=True, null=True)
    is_deleted_or_archived_job = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'report_outputs'


class ReportStatusDefinitions(models.Model):
    definition_id = models.IntegerField(blank=True, null=True)
    status_type = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    reportdefinition_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_status_definitions'


class RequisitionCriterias(models.Model):
    eligibility_criteria_id = models.IntegerField(blank=True, null=True)
    salary_package_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    masterjobrequisition = models.ForeignKey(MasterJobRequisitions, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisition_criterias'


class ResumeSourcesValues(models.Model):
    version = models.IntegerField()
    mac_number = models.CharField(max_length=25, blank=True, null=True)
    source_detail = models.TextField(blank=True, null=True)
    source_name = models.CharField(max_length=255, blank=True, null=True)
    resume_source_master_id = models.IntegerField()
    last_processed_time = models.DateTimeField(blank=True, null=True)
    source_id = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'resume_sources_values'


class ResumeStatuss(models.Model):
    version = models.IntegerField()
    sequence = models.IntegerField()
    base_name = models.CharField(max_length=255)
    label = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    is_terminated = models.IntegerField()
    is_base = models.IntegerField()
    tenant_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    resumestatus_id = models.IntegerField(blank=True, null=True)
    hopping_status_id = models.IntegerField(blank=True, null=True)
    is_interview = models.IntegerField(blank=True, null=True)
    is_assessment = models.IntegerField(blank=True, null=True)
    is_staffing = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resume_statuss'


class ResumeStatuss2(models.Model):
    id = models.IntegerField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    base_name = models.CharField(max_length=255)
    label = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    is_terminated = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_base = models.TextField(blank=True, null=True)  # This field type is a guess.
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField(blank=True, null=True)  # This field type is a guess.
    guid = models.CharField(max_length=40, blank=True, null=True)
    resumestatus_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resume_statuss2'


class Roles(models.Model):
    version = models.IntegerField()
    role_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    is_system_role = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'roles'


class RtcRandomizedQuestions(models.Model):
    question_id = models.IntegerField()
    question_paper_id = models.IntegerField()
    number_of_questions_to_display = models.IntegerField()
    mode_of_randomization = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    question_tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rtc_randomized_questions'


class SalaryPackageBranchDegrees(models.Model):
    branch_id = models.IntegerField(blank=True, null=True)
    degree_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    salarypackage = models.ForeignKey('SalaryPackages', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary_package_branch_degrees'


class SalaryPackages(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    experience_from = models.IntegerField(blank=True, null=True)
    experience_to = models.IntegerField(blank=True, null=True)
    salary_package_from = models.DecimalField(max_digits=19, decimal_places=5, blank=True, null=True)
    salary_package_to = models.DecimalField(max_digits=19, decimal_places=5, blank=True, null=True)
    fixed_pay = models.DecimalField(max_digits=19, decimal_places=5, blank=True, null=True)
    variable_pay = models.DecimalField(max_digits=19, decimal_places=5, blank=True, null=True)
    joining_bonus = models.DecimalField(max_digits=19, decimal_places=5, blank=True, null=True)
    insurance = models.DecimalField(max_digits=19, decimal_places=5, blank=True, null=True)
    is_utilized = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    stock = models.IntegerField(blank=True, null=True)
    fixed_pay_from = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    fixed_pay_to = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    variable_pay_from = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    variable_pay_to = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    joining_bonus_from = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    joining_bonus_to = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    benefits_from = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    benefits_to = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    gross_pay_from = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    gross_pay_to = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    currency = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary_packages'


class SalaryStructureCustomized(models.Model):
    ctc_structure_id = models.IntegerField(blank=True, null=True)
    provident_fund_percent_amount = models.FloatField(blank=True, null=True)
    super_annuation_fund_percent_amount = models.FloatField(blank=True, null=True)
    hra_percent_amount = models.FloatField()
    component_ain_percent_amount = models.FloatField(blank=True, null=True)
    component_bin_percent_amount = models.FloatField(blank=True, null=True)
    custom_field_a1_percent_amount = models.FloatField(blank=True, null=True)
    custom_field_a2_percent_amount = models.FloatField(blank=True, null=True)
    custom_field_a3_flat = models.FloatField(blank=True, null=True)
    custom_field_a4_flat = models.FloatField(blank=True, null=True)
    custom_field_a5_flat = models.FloatField(blank=True, null=True)
    custom_field_b1_percent_amount = models.FloatField(blank=True, null=True)
    custom_field_b2_percent_amount = models.FloatField(blank=True, null=True)
    custom_field_b3_flat = models.FloatField(blank=True, null=True)
    custom_field_b4_flat = models.FloatField(blank=True, null=True)
    custom_field_b5_flat = models.FloatField(blank=True, null=True)
    basic_salary_percent_amount = models.FloatField()
    custom_field_a6_percent_amount = models.FloatField(blank=True, null=True)
    custom_field_a7_percent_amount = models.FloatField(blank=True, null=True)
    custom_field_a8_flat = models.FloatField(blank=True, null=True)
    custom_field_a9_flat = models.FloatField(blank=True, null=True)
    custom_field_a10_flat = models.FloatField(blank=True, null=True)
    custom_field_a11_flat = models.FloatField(blank=True, null=True)
    custom_field_a12_flat = models.FloatField(blank=True, null=True)
    custom_field_a13_flat = models.FloatField(blank=True, null=True)
    custom_field_a14_flat = models.FloatField(blank=True, null=True)
    custom_field_b6_flat = models.FloatField(blank=True, null=True)
    custom_field_b7_flat = models.FloatField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    component_clabel = models.CharField(max_length=255, blank=True, null=True)
    component_dlabel = models.CharField(max_length=255, blank=True, null=True)
    component_cmonthly = models.FloatField(blank=True, null=True)
    component_dmonthly = models.FloatField(blank=True, null=True)
    component_cyearly = models.FloatField(blank=True, null=True)
    component_dyearly = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary_structure_customized'


class ScreeningRuleGroupValues(models.Model):
    catalog_or_catalog_group_id = models.IntegerField()
    is_catalog_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    screeningrulegroup_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'screening_rule_group_values'


class ScreeningRuleGroups(models.Model):
    screening_property = models.IntegerField(blank=True, null=True)
    weightage = models.FloatField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    screeningrule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'screening_rule_groups'


class ScreeningRules(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_relocate = models.IntegerField(blank=True, null=True)
    relocation_weightage = models.FloatField(blank=True, null=True)
    age_from = models.IntegerField(blank=True, null=True)
    age_to = models.IntegerField(blank=True, null=True)
    age_weightage = models.FloatField(blank=True, null=True)
    experience_from = models.IntegerField(blank=True, null=True)
    experience_to = models.IntegerField(blank=True, null=True)
    experience_weightage = models.FloatField(blank=True, null=True)
    percentage_from = models.FloatField(blank=True, null=True)
    percentage_to = models.FloatField(blank=True, null=True)
    cgpa_from = models.FloatField(blank=True, null=True)
    cgpa_to = models.FloatField(blank=True, null=True)
    percentage_or_cgpa_weightage = models.FloatField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    gender_weightage = models.FloatField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'screening_rules'


class SecondaryInterviewers(models.Model):
    interviewer_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    interviewrequest = models.ForeignKey(InterviewRequests, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secondary_interviewers'


class SecondaryRelationshipManagers(models.Model):
    version = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    user_id = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secondary_relationship_managers'


class SectionQuestionDifficultyLevels(models.Model):
    difficult_level = models.IntegerField(blank=True, null=True)
    no_of_questions = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    section_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section_question_difficulty_levels'


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


class SelectionProcesss(models.Model):
    version = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    resume_status_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    selectionprocess_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'selection_processs'


class SelfRegisterCandidates(models.Model):
    name = models.CharField(max_length=255)
    email1 = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    current_employer_id = models.IntegerField(blank=True, null=True)
    current_employer_text = models.CharField(max_length=255, blank=True, null=True)
    total_experience = models.IntegerField(blank=True, null=True)
    current_location_id = models.IntegerField(blank=True, null=True)
    current_location_text = models.CharField(max_length=255, blank=True, null=True)
    qastatus = models.IntegerField(blank=True, null=True)
    file_id = models.IntegerField()
    approved_candidate_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    customer_custom_entity_fields = models.CharField(max_length=2000, blank=True, null=True)
    candidate_education_details = models.CharField(max_length=2000, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'self_register_candidates'


class SelfServiceConfigs(models.Model):
    is_job_alerts = models.IntegerField()
    is_update_alerts = models.IntegerField()
    query_count = models.IntegerField(blank=True, null=True)
    last_candidate_update_sent_time = models.DateTimeField(blank=True, null=True)
    last_job_alert_sent_time = models.DateTimeField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'self_service_configs'


class SelfServiceLogs(models.Model):
    version = models.IntegerField()
    event_type = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'self_service_logs'


class ServiceEngagements(models.Model):
    engagement_type_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    masterjob = models.ForeignKey(MasterJobs, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_engagements'


class ServiceLevelAgrements(models.Model):
    version = models.IntegerField()
    candidate_threshold_status_id = models.IntegerField(blank=True, null=True)
    internal_slavalue = models.IntegerField()
    external_slavalue = models.IntegerField()
    actual_value = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_level_agrements'


class SkillsAssesseds(models.Model):
    skill_id = models.IntegerField()
    skill_score = models.IntegerField(blank=True, null=True)
    skill_comment = models.CharField(max_length=2000, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    interviewrequest_id = models.IntegerField(blank=True, null=True)
    is_applicable = models.IntegerField(blank=True, null=True)
    interviewfilledfeedbackform_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills_assesseds'


class SkillsToAssesss(models.Model):
    skill_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    skill_max_score = models.IntegerField(blank=True, null=True)
    skill_min_score = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    assessmenttemplate_id = models.IntegerField(blank=True, null=True)
    guidelines = models.CharField(max_length=1024, blank=True, null=True)
    skill_type_id = models.IntegerField(blank=True, null=True)
    is_comments_required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skills_to_assesss'


class SlaMetricss(models.Model):
    version = models.IntegerField()
    sla_name = models.CharField(max_length=255, blank=True, null=True)
    numerator_id = models.IntegerField(blank=True, null=True)
    denominator_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'sla_metricss'


class SmsRequests(models.Model):
    version = models.IntegerField()
    receiver_number = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    entity_type = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    notification_name = models.CharField(max_length=55, blank=True, null=True)
    message_status = models.IntegerField(blank=True, null=True)
    error_status = models.IntegerField(blank=True, null=True)
    message_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_requests'


class SocialSiteOauthInfos(models.Model):
    version = models.IntegerField()
    site_url = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    token_secret = models.CharField(max_length=255, blank=True, null=True)
    varifier = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_site_oauth_infos'


class SourceChangeEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    file_id = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'source_change_events'


class SourceEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link_to_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    source_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'source_events'


class SourceSelfServiceReportOutputs(models.Model):
    version = models.IntegerField()
    job_id = models.IntegerField()
    source_id = models.IntegerField()
    job_name = models.CharField(max_length=255, blank=True, null=True)
    experience_range = models.CharField(max_length=255, blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    total_submittals = models.IntegerField()
    matching = models.IntegerField()
    in_process = models.IntegerField()
    rejected = models.IntegerField()
    selected = models.IntegerField()
    on_hold = models.IntegerField()
    joined = models.IntegerField()
    is_job_closed = models.TextField()  # This field type is a guess.
    company_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.TextField()  # This field type is a guess.
    guid = models.CharField(max_length=40)
    job_code_id = models.IntegerField(blank=True, null=True)
    job_code_text = models.CharField(max_length=45, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'source_self_service_report_outputs'


class SourceUsers(models.Model):
    version = models.IntegerField()
    source_id = models.IntegerField()
    user_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'source_users'


class Sources(models.Model):
    version = models.IntegerField()
    source_name = models.CharField(max_length=255, blank=True, null=True)
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


class StaffingActivityAssigningRules(models.Model):
    version = models.IntegerField()
    activity_id = models.IntegerField()
    sequence = models.IntegerField()
    bu_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    level_id = models.IntegerField(blank=True, null=True)
    privilege = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_activity_assigning_rules'


class StaffingActivitys(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    is_calls_required = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    is_sequenced = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_activitys'


class StaffingAttachments(models.Model):
    version = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, null=True)
    original_file_name = models.CharField(max_length=100, blank=True, null=True)
    file_type = models.CharField(max_length=10, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    target_file_name = models.CharField(max_length=100, blank=True, null=True)
    attachment_type = models.IntegerField(blank=True, null=True)
    source_type = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'staffing_attachments'


class StaffingCandidates(models.Model):
    version = models.IntegerField()
    level_id = models.IntegerField(blank=True, null=True)
    spoc = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    business_unit_id = models.IntegerField(blank=True, null=True)
    actual_joining_date = models.DateTimeField(blank=True, null=True)
    expected_joining_date = models.DateTimeField(blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    resume_path = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    marital_status = models.IntegerField(blank=True, null=True)
    email1 = models.CharField(max_length=255, blank=True, null=True)
    email2 = models.CharField(max_length=255, blank=True, null=True)
    mobile1 = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    aadhar_number = models.CharField(max_length=255, blank=True, null=True)
    pan_number = models.CharField(max_length=255, blank=True, null=True)
    passport_number = models.CharField(max_length=255, blank=True, null=True)
    current_location = models.IntegerField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    nationality = models.IntegerField(blank=True, null=True)
    candidate_user_id = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    history_info = models.CharField(max_length=255, blank=True, null=True)
    current_activity = models.IntegerField(blank=True, null=True)
    activity_status = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    total_experience = models.IntegerField(blank=True, null=True)
    criticality = models.IntegerField(blank=True, null=True)
    skill_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    mentor = models.IntegerField(blank=True, null=True)
    buddies = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    status_modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_candidates'


class StaffingGroupMembers(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    staffinggroup_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_group_members'


class StaffingGroups(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    total_members = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'staffing_groups'


class StaffingPofuCallHistorys(models.Model):
    status_id = models.IntegerField()
    comment = models.CharField(max_length=1000, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    staffingpofucall = models.ForeignKey('StaffingPofuCalls', blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_pofu_call_historys'


class StaffingPofuCalls(models.Model):
    caller = models.IntegerField()
    call_type = models.IntegerField()
    current_status_id = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    staffingpofu = models.ForeignKey('StaffingPofus', blank=True, null=True)
    is_commented = models.IntegerField(blank=True, null=True)
    remarks_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_pofu_calls'


class StaffingPofus(models.Model):
    version = models.IntegerField()
    candidate_id = models.IntegerField()
    staffing_activity_id = models.IntegerField(blank=True, null=True)
    pofu_category_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'staffing_pofus'


class StaffingStatusHistorys(models.Model):
    status_id = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    responsiveness = models.IntegerField(blank=True, null=True)
    observations = models.IntegerField(blank=True, null=True)
    resignation_status = models.IntegerField(blank=True, null=True)
    decline_reason = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    staffingstatus = models.ForeignKey('StaffingStatuss', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_status_historys'


class StaffingStatuss(models.Model):
    version = models.IntegerField()
    current_status_id = models.IntegerField()
    responsiveness = models.IntegerField(blank=True, null=True)
    observations = models.IntegerField(blank=True, null=True)
    resignation_status = models.IntegerField(blank=True, null=True)
    decline_reason = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'staffing_statuss'


class StaffingTasks(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    assignee_department = models.IntegerField(blank=True, null=True)
    reporter_department = models.IntegerField(blank=True, null=True)
    approver_department = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    form_id = models.IntegerField(blank=True, null=True)
    is_visible_to_candidate = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    is_utilized = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    assignee_group = models.IntegerField(blank=True, null=True)
    reporter_group = models.IntegerField(blank=True, null=True)
    approver_group = models.IntegerField(blank=True, null=True)
    is_auto_approved = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_tasks'


class StaffingUserProfiles(models.Model):
    version = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    photo_path = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    linked_in_url = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40, blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_user_profiles'


class Synonyms(models.Model):
    value_synonym = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    catalogvalue_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'synonyms'


class TableInfos(models.Model):
    table_name = models.CharField(primary_key=True, max_length=255)
    table_rows = models.IntegerField(blank=True, null=True)
    reserved = models.CharField(max_length=255, blank=True, null=True)
    table_data = models.CharField(max_length=255, blank=True, null=True)
    index_size = models.CharField(max_length=255, blank=True, null=True)
    unused = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_infos'


class TagItems(models.Model):
    item_name = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    item_type = models.CharField(max_length=255, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag_items'


class Tags(models.Model):
    version = models.IntegerField()
    tag_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'tags'


class TaskConfigurations(models.Model):
    task_id = models.IntegerField(blank=True, null=True)
    bu_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    level_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    activity_id = models.IntegerField(blank=True, null=True)
    privilege = models.IntegerField(blank=True, null=True)
    version = models.IntegerField()
    tenant_id = models.IntegerField()
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    job_role_id = models.IntegerField(blank=True, null=True)
    recruit_event_id = models.IntegerField(blank=True, null=True)
    stage_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    hard_limit_status_id = models.IntegerField(blank=True, null=True)
    hard_limit_stage_id = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=45, blank=True, null=True)
    negative_resume_satus_id = models.IntegerField(blank=True, null=True)
    positive_resume_satus_id = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_configurations'


class TaskDepartmentDesignationInfos(models.Model):
    version = models.IntegerField()
    department_id = models.IntegerField(blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    onboardingtask_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_department_designation_infos'


class Tasks(models.Model):
    version = models.IntegerField()
    task_type_id = models.IntegerField()
    type_of_owner = models.IntegerField(blank=True, null=True)
    estimated_work_hours = models.FloatField(blank=True, null=True)
    status_id = models.IntegerField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.CharField(max_length=255, blank=True, null=True)
    additional_work_hours = models.FloatField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completion_date = models.DateTimeField(blank=True, null=True)
    actual_work_hours = models.FloatField(blank=True, null=True)
    user_id = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
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
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
    integer2 = models.IntegerField(blank=True, null=True)
    integer1 = models.IntegerField(blank=True, null=True)
    text4 = models.CharField(max_length=50, blank=True, null=True)
    text3 = models.CharField(max_length=50, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    text1 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'


class Technologys(models.Model):
    technology_id = models.IntegerField()
    order_number = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    occurrence_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'technologys'


class TemplateObjectTypes(models.Model):
    type_code = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    template_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_object_types'


class TemplateWordReplacers(models.Model):
    version = models.IntegerField()
    template_word_id_field = models.CharField(max_length=255)
    template_word_to_map = models.CharField(max_length=255)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'template_word_replacers'


class Templates(models.Model):
    version = models.IntegerField()
    template_name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_domain = models.IntegerField()
    target_type = models.IntegerField(blank=True, null=True)
    place_owner = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    xml_content = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    file_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'templates'


class TemporaryMailObjects(models.Model):
    version = models.IntegerField()
    bcc = models.CharField(max_length=255, blank=True, null=True)
    cc = models.CharField(max_length=255, blank=True, null=True)
    sender_email_ids = models.CharField(max_length=255, blank=True, null=True)
    is_body_html = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    receiver_email_ids = models.CharField(max_length=255, blank=True, null=True)
    body = models.CharField(max_length=4000, blank=True, null=True)
    sent_count = models.IntegerField(blank=True, null=True)
    failed_date = models.DateTimeField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    display_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporary_mail_objects'


class TestCandidates(models.Model):
    version = models.IntegerField()
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    skillset = models.TextField(blank=True, null=True)
    expertise_id = models.IntegerField(blank=True, null=True)
    hierarchy_id = models.IntegerField(blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    degree_id = models.IntegerField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    college_id = models.IntegerField(blank=True, null=True)
    college_location_id = models.IntegerField(blank=True, null=True)
    current_employer_id = models.IntegerField(blank=True, null=True)
    current_employer_text = models.CharField(max_length=100, blank=True, null=True)
    expertise_text = models.CharField(max_length=50, blank=True, null=True)
    hierarchy_text = models.CharField(max_length=50, blank=True, null=True)
    degree_text = models.CharField(max_length=100, blank=True, null=True)
    branch_text = models.CharField(max_length=100, blank=True, null=True)
    college_text = models.CharField(max_length=100, blank=True, null=True)
    college_location_text = models.CharField(max_length=100, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
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
    testcandidate_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_candidates'


class TestGroupInfos(models.Model):
    version = models.IntegerField()
    group_id = models.IntegerField()
    total_time = models.IntegerField()
    break_time = models.IntegerField()
    questions_to_randomize = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    test_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_group_infos'


class TestOwners(models.Model):
    version = models.IntegerField()
    user_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    test_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_owners'


class TestPapers(models.Model):
    question_paper_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_papers'


class TestQuestionInfos(models.Model):
    question_id = models.IntegerField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    question_tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    test = models.ForeignKey('Tests', blank=True, null=True)
    incorrect_mark = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_question_infos'


class TestResultInfos(models.Model):
    coding_question_attachment_id = models.IntegerField(blank=True, null=True)
    coding_output = models.TextField(blank=True, null=True)
    coding_error_message = models.TextField(blank=True, null=True)
    coding_error_code = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    testresult = models.ForeignKey('TestResults', blank=True, null=True)
    coding_execution_time = models.FloatField(blank=True, null=True)
    coding_memory_usage = models.FloatField(blank=True, null=True)
    coding_obtained_mark = models.FloatField(blank=True, null=True)
    coding_signal = models.IntegerField(blank=True, null=True)
    coding_signal_message = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_result_infos'


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


class TestSectionInfos(models.Model):
    section_id = models.IntegerField(blank=True, null=True)
    mark = models.FloatField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    questions_to_randomize = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_section_infos'


class TestUserGroupInfos(models.Model):
    group_id = models.IntegerField()
    testuser = models.ForeignKey('TestUsers', blank=True, null=True)
    time_spent = models.IntegerField(blank=True, null=True)
    is_selected_optional_group = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_user_group_infos'


class TestUserLoginInfos(models.Model):
    login_time = models.DateTimeField(blank=True, null=True)
    client_system_info = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    testuser_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_user_login_infos'


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


class TimeSheets(models.Model):
    version = models.IntegerField()
    group_activity = models.IntegerField()
    activity = models.IntegerField()
    service_line = models.IntegerField()
    bu = models.IntegerField(blank=True, null=True)
    sbu = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField()
    customer = models.IntegerField(blank=True, null=True)
    requisition = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    date = models.DateTimeField()
    attendance_status = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'time_sheets'


class UniqueRandomizedQuestions(models.Model):
    version = models.IntegerField()
    question_id = models.IntegerField(blank=True, null=True)
    section_id = models.IntegerField(blank=True, null=True)
    question_tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    testuser_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unique_randomized_questions'


class UserActions(models.Model):
    enable = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_actions'


class UserArticles(models.Model):
    version = models.IntegerField()
    article_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    is_enable = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'user_articles'


class UserEvents(models.Model):
    version = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    actor_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    link_to_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    event_type = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_events'


class UserGroups(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_groups'


class UserOwners(models.Model):
    version = models.IntegerField()
    entity_type_id = models.IntegerField()
    user_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    entity_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_owners'


class UserProfiles(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    property_name = models.CharField(max_length=255, blank=True, null=True)
    property_values_string = models.CharField(max_length=255, blank=True, null=True)
    property_values_binary = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profiles'


class UserRoles(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_roles'


class Users(models.Model):
    version = models.IntegerField()
    login_name = models.CharField(max_length=75, blank=True, null=True)
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
    userprofile_id = models.IntegerField(blank=True, null=True)
    is_password_auto_generated = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=75, blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    is_master_vendor_user = models.IntegerField(blank=True, null=True)
    last_password_changed_date = models.DateTimeField(blank=True, null=True)
    operating_system_details = models.CharField(max_length=45, blank=True, null=True)
    browser_details = models.CharField(max_length=245, blank=True, null=True)
    last_login_ip = models.CharField(max_length=45, blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    is_disabled = models.IntegerField(blank=True, null=True)
    login_failed_count = models.IntegerField()
    is_archived = models.IntegerField()
    location_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VendorBillingDetails(models.Model):
    version = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)
    candidate_id = models.IntegerField(blank=True, null=True)
    contract_level_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    billing_amount = models.FloatField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    job_code_id = models.IntegerField(blank=True, null=True)
    offer_date = models.DateTimeField(blank=True, null=True)
    joining_date = models.DateTimeField(blank=True, null=True)
    job_code_text = models.CharField(max_length=45, blank=True, null=True)
    job_name = models.CharField(max_length=45, blank=True, null=True)
    source_name = models.CharField(max_length=45, blank=True, null=True)
    candidate_name = models.CharField(max_length=45, blank=True, null=True)
    ctc = models.FloatField(blank=True, null=True)
    billing_percentage = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    offer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_billing_details'


class VendorConfigurations(models.Model):
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    vendor = models.ForeignKey('Vendors', blank=True, null=True)
    service_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_configurations'


class VendorOwners(models.Model):
    user_id = models.IntegerField()
    source_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_owners'


class VendorUsers(models.Model):
    version = models.IntegerField()
    vendor_id = models.IntegerField()
    user_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'vendor_users'


class Vendors(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    contract_start = models.DateTimeField(blank=True, null=True)
    contract_end = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'vendors'


class Widget(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_default = models.IntegerField()
    default_state = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255)
    order_no = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=38)

    class Meta:
        managed = False
        db_table = 'widget'


class WidgetInstance(models.Model):
    version = models.IntegerField()
    page_id = models.IntegerField()
    widget_id = models.IntegerField()
    column_no = models.IntegerField()
    order_no = models.IntegerField()
    expanded = models.IntegerField()
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=38)

    class Meta:
        managed = False
        db_table = 'widget_instance'


class Widgets(models.Model):
    version = models.IntegerField()
    header = models.CharField(max_length=255, blank=True, null=True)
    widget_type = models.IntegerField(blank=True, null=True)
    hposition = models.IntegerField(blank=True, null=True)
    vposition = models.IntegerField(blank=True, null=True)
    widget_position = models.IntegerField(blank=True, null=True)
    widget_name = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    true_false2 = models.IntegerField(blank=True, null=True)
    true_false1 = models.IntegerField(blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'widgets'
