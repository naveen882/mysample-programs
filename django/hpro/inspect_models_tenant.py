{'159': 'db1', '70': 'db3', '228': 'db2'}
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


class BillingPlans(models.Model):
    version = models.IntegerField()
    available_data_base_usage = models.IntegerField(blank=True, null=True)
    available_down_load_size = models.IntegerField(blank=True, null=True)
    cost_per_user = models.IntegerField(blank=True, null=True)
    available_time = models.IntegerField(blank=True, null=True)
    data_base_usage_cost_per_mb = models.IntegerField(blank=True, null=True)
    down_load_size_cost_per_mb = models.IntegerField(blank=True, null=True)
    plan_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'billing_plans'


class BluePrintSplitRatios(models.Model):
    version = models.IntegerField()
    split_ratio = models.IntegerField(blank=True, null=True)
    low = models.IntegerField()
    medium = models.IntegerField()
    high = models.IntegerField()
    is_latest = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'blue_print_split_ratios'


class BrowniePointConfigurations(models.Model):
    version = models.IntegerField()
    brownie_point_currency_ratio = models.FloatField(blank=True, null=True)
    tax_percentage = models.FloatField(blank=True, null=True)
    max_amount_exempted = models.FloatField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'brownie_point_configurations'


class BusinessActionBillingPrices(models.Model):
    version = models.IntegerField()
    business_action_id = models.IntegerField()
    price = models.BigIntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'business_action_billing_prices'


class BusinessActions(models.Model):
    version = models.IntegerField()
    action_name = models.CharField(max_length=255, blank=True, null=True)
    is_billable = models.IntegerField()
    is_metered = models.IntegerField()
    is_logged = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'business_actions'


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
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_pofu_categorizations'


class ChatMessages(models.Model):
    message = models.CharField(max_length=255, blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    session_id = models.CharField(db_column='session__id', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_messages'


class ChatSessions(models.Model):
    version = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    ipaddress = models.CharField(max_length=255, blank=True, null=True)
    is_first_request = models.IntegerField()
    sent_time = models.DateTimeField(blank=True, null=True)
    recieved_time = models.DateTimeField(blank=True, null=True)
    support_user_id = models.IntegerField(blank=True, null=True)
    session_alive = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    anonymous_id = models.IntegerField(blank=True, null=True)
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
        db_table = 'chat_sessions'


class DatabaseMappings(models.Model):
    id = models.IntegerField(primary_key=True)
    db_name = models.CharField(max_length=45)
    db_user = models.CharField(max_length=45)
    db_pwd = models.CharField(max_length=45)
    db_port = models.IntegerField(blank=True, null=True)
    db_host = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'database_mappings'


class EntitiesPropertys(models.Model):
    version = models.IntegerField()
    property_name = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=255, blank=True, null=True)
    is_custom_field = models.IntegerField(blank=True, null=True)
    is_catalog_field = models.IntegerField(blank=True, null=True)
    catalog_master_name = models.CharField(max_length=255, blank=True, null=True)
    is_mandatory = models.IntegerField(blank=True, null=True)
    minimum_length = models.IntegerField(blank=True, null=True)
    maximum_length = models.IntegerField(blank=True, null=True)
    is_default_tenant_property = models.IntegerField()
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
    entityinfo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entities_propertys'


class EntityGridPropertyDefns(models.Model):
    property_order = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    entitygridproperty_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_grid_property_defns'


class EntityGridPropertys(models.Model):
    version = models.IntegerField()
    module_name = models.CharField(max_length=255, blank=True, null=True)
    grid_name = models.CharField(max_length=255, blank=True, null=True)
    entityproperty_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    is_static = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_grid_propertys'


class EntityInfos(models.Model):
    version = models.IntegerField()
    entity_name = models.CharField(max_length=255, blank=True, null=True)
    type_string = models.CharField(max_length=255, blank=True, null=True)
    module_id = models.IntegerField(blank=True, null=True)
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
        db_table = 'entity_infos'


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


class EntityPropertyWeightages(models.Model):
    version = models.IntegerField()
    weightage = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    tenant_id = models.IntegerField(blank=True, null=True)
    formentitymap_id = models.IntegerField(blank=True, null=True)
    parent_property_id = models.IntegerField(db_column='parent_property_Id', blank=True, null=True)  # Field name made lowercase.
    profile_label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_property_weightages'


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


class FormEntityMaps(models.Model):
    version = models.IntegerField()
    entity_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    entity_property = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    formentitymap_id = models.IntegerField(blank=True, null=True)
    weightage = models.IntegerField(blank=True, null=True)
    entity_catalog = models.CharField(max_length=100, blank=True, null=True)
    control_type = models.IntegerField(blank=True, null=True)
    validation_type = models.IntegerField(blank=True, null=True)
    group_value = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_entity_maps'


class FormEntityMapsTemp(models.Model):
    version = models.IntegerField()
    entity_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    entity_property = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    formentitymap_id = models.IntegerField(blank=True, null=True)
    weightage = models.IntegerField(blank=True, null=True)
    entity_catalog = models.CharField(max_length=100, blank=True, null=True)
    control_type = models.IntegerField(blank=True, null=True)
    validation_type = models.IntegerField(blank=True, null=True)
    group_value = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_entity_maps_temp'


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
    approver_user_id = models.IntegerField(blank=True, null=True)
    approval_sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'job_approval_levels'


class MasterConfigurationEvents(models.Model):
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

    class Meta:
        managed = False
        db_table = 'master_configuration_events'


class MasterConfigurations(models.Model):
    version = models.IntegerField()
    decompressed_file = models.CharField(max_length=255, blank=True, null=True)
    mail_server = models.CharField(max_length=255, blank=True, null=True)
    optional_mail_server = models.CharField(max_length=255, blank=True, null=True)
    file_repository = models.CharField(max_length=255, blank=True, null=True)
    no_of_days_to_keep_events_in_database = models.IntegerField(blank=True, null=True)
    send_mail_to_user = models.IntegerField(blank=True, null=True)
    self_service_url = models.CharField(max_length=255, blank=True, null=True)
    self_service_mail_template = models.CharField(max_length=255, blank=True, null=True)
    direct_mail_users = models.TextField(blank=True, null=True)
    send_sent_mail_copy_to_outlook = models.IntegerField(blank=True, null=True)
    refer_job_mail_template = models.CharField(max_length=255, blank=True, null=True)
    content_attachment_storage_mode = models.IntegerField(blank=True, null=True)
    activity_attachment_storage_mode = models.IntegerField(blank=True, null=True)
    other_attachment_storage_mode = models.IntegerField(blank=True, null=True)
    daily_report_recepients = models.TextField(blank=True, null=True)
    is_job_approve_enabled = models.IntegerField()
    active_validity_period = models.IntegerField(blank=True, null=True)
    alive_validity_period = models.IntegerField(blank=True, null=True)
    candidate_sourcer_expiry_days = models.IntegerField(blank=True, null=True)
    pop3_mail_server = models.CharField(max_length=255, blank=True, null=True)
    pop3_mail_server_port = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    duplication_rule_text = models.TextField(blank=True, null=True)
    notification_sender_email_id = models.CharField(max_length=255, blank=True, null=True)
    resume_repository = models.CharField(max_length=255, blank=True, null=True)
    event_log_directory = models.CharField(max_length=255, blank=True, null=True)
    notification_sender_email_password = models.CharField(max_length=45, blank=True, null=True)
    employee_referral_to_email_password = models.CharField(max_length=45, blank=True, null=True)
    employee_referral_to_email = models.CharField(max_length=45, blank=True, null=True)
    internal_employee_referral_email_domain = models.CharField(max_length=45, blank=True, null=True)
    is_action_to_be_taken_after_source_expiry = models.IntegerField(blank=True, null=True)
    on_duplication_found_action = models.IntegerField(blank=True, null=True)
    assessment_template_id = models.IntegerField(blank=True, null=True)
    is_position_manager_enabled = models.IntegerField(blank=True, null=True)
    is_job_posting_detail_enabled = models.IntegerField(blank=True, null=True)
    ctc_approver1 = models.IntegerField(blank=True, null=True)
    ctc_approver2 = models.IntegerField(blank=True, null=True)
    is_hopping_resume_status_enabled = models.IntegerField(blank=True, null=True)
    job_primary_owner = models.IntegerField(blank=True, null=True)
    is_candidate_job_matching_engine_enabled = models.IntegerField(blank=True, null=True)
    is_ctc_approval_enabled = models.IntegerField(blank=True, null=True)
    is_candidates_rejected = models.IntegerField(blank=True, null=True)
    duplication_check_period = models.IntegerField(blank=True, null=True)
    is_reject_candidate_on_app_status_rejected = models.IntegerField()
    export_candidate_properties_text = models.TextField(blank=True, null=True)
    is_partial_duplicate_by_admin = models.IntegerField(blank=True, null=True)
    is_black_list_candidate_required = models.IntegerField(blank=True, null=True)
    duplication_rule_weightage = models.TextField(blank=True, null=True)
    is_ssl_mailserver = models.IntegerField(db_column='is_Ssl_Mailserver', blank=True, null=True)  # Field name made lowercase.
    is_close_job_on_all_positions_filled = models.IntegerField(blank=True, null=True)
    is_offer_manager_enabled = models.IntegerField()
    password_expiry_limit_in_days = models.IntegerField(blank=True, null=True)
    is_employee_create_enabled = models.IntegerField(blank=True, null=True)
    is_status_notification_for_employee_referral_enabled = models.IntegerField(blank=True, null=True)
    is_bulk_interview_time_optional = models.IntegerField()
    pofu_status_id = models.IntegerField(blank=True, null=True)
    position_tag_status_id = models.IntegerField(blank=True, null=True)
    forecast_settings = models.CharField(max_length=255, blank=True, null=True)
    rejected_candidate_visibility = models.CharField(max_length=755, blank=True, null=True)
    vendor_billing_verifier = models.IntegerField(blank=True, null=True)
    is_show_source_as_hirepro = models.IntegerField(blank=True, null=True)
    vendor_account_help_desk_email_id = models.CharField(max_length=55, blank=True, null=True)
    campus_hiring_enabled = models.IntegerField(blank=True, null=True)
    resume_stage_settings_for_source_expiry = models.TextField(blank=True, null=True)
    question_reusage_statistics = models.IntegerField(blank=True, null=True)
    default_entity_config = models.CharField(max_length=500, blank=True, null=True)
    is_salary_structure_customizable = models.IntegerField()
    date_of_joining_notification_to_business_user = models.TextField(blank=True, null=True)
    mail_server_port = models.IntegerField(blank=True, null=True)
    is_campus_candidates_approve_enabled = models.IntegerField()
    is_new_campus_hiring_enabled = models.IntegerField()
    is_question_approver_flow_enabled = models.IntegerField()
    is_auto_job_tag_employee_referral = models.IntegerField(blank=True, null=True)
    mail_server_user_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_configurations'


class MenuItems(models.Model):
    version = models.IntegerField()
    menu_name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    module_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_items'


class ModuleBillingPrices(models.Model):
    version = models.IntegerField()
    module_id = models.IntegerField()
    price = models.BigIntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'module_billing_prices'


class ModuleGridConfigurations(models.Model):
    version = models.IntegerField()
    module = models.IntegerField(blank=True, null=True)
    grid_method_name = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'module_grid_configurations'


class ModuleGridEnabledPropertys(models.Model):
    grid_property = models.CharField(max_length=255, blank=True, null=True)
    label_name = models.CharField(max_length=255, blank=True, null=True)
    property_order = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    modulegridconfiguration_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_grid_enabled_propertys'


class OfferApprovalLevels(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    approver_user_id = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    approval_sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'offer_approval_levels'


class OnLineUsers(models.Model):
    version = models.IntegerField()
    support_user_id = models.IntegerField(blank=True, null=True)
    last_request_time = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'on_line_users'


class PortedCandidateInfos(models.Model):
    version = models.IntegerField()
    last_ported_id = models.IntegerField()
    last_ported_time = models.DateTimeField(blank=True, null=True)
    candidate_count = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'ported_candidate_infos'


class Presentations(models.Model):
    version = models.IntegerField()
    layout = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=255, blank=True, null=True)
    logo1 = models.CharField(max_length=255, blank=True, null=True)
    logo2 = models.CharField(max_length=255, blank=True, null=True)
    slogan_text = models.CharField(max_length=255, blank=True, null=True)
    slogan_image = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    background_image = models.CharField(max_length=255, blank=True, null=True)
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
        db_table = 'presentations'


class QueryCategoryConfigurations(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    version = models.IntegerField()
    category_id = models.IntegerField()
    user_ids = models.CharField(max_length=255, blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'query_category_configurations'


class StaffingAutomationRules(models.Model):
    version = models.IntegerField()
    move_candidate_to_next_activity = models.IntegerField(blank=True, null=True)
    send_credentials_to_candidate = models.IntegerField(blank=True, null=True)
    tag_activity_task_to_candidate = models.IntegerField(blank=True, null=True)
    send_welcome_mail_to_candidate = models.IntegerField(blank=True, null=True)
    tag_candidate_to_activity = models.IntegerField(blank=True, null=True)
    tag_content_to_candidate = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40, blank=True, null=True)
    enable_activity_rule_engine = models.IntegerField(blank=True, null=True)
    enable_task_rule_engine = models.IntegerField(blank=True, null=True)
    enable_content_rule_engine = models.IntegerField(blank=True, null=True)
    complete_activity_on_complete_all_tasks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_automation_rules'


class TenantContracts(models.Model):
    version = models.IntegerField()
    tenant_id = models.IntegerField()
    no_of_modules = models.IntegerField(blank=True, null=True)
    initial_price = models.BigIntegerField(blank=True, null=True)
    validity_period = models.IntegerField(blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField(blank=True, null=True)
    invoice_period = models.IntegerField(blank=True, null=True)
    billing_plan_id = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'tenant_contracts'


class TenantEntityAverageSizes(models.Model):
    version = models.IntegerField()
    tenant_id = models.IntegerField()
    entity_name = models.CharField(max_length=255, blank=True, null=True)
    avg_row_size = models.FloatField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'tenant_entity_average_sizes'


class TenantEntityDefs(models.Model):
    property_id = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    is_visible = models.IntegerField(blank=True, null=True)
    validation_rule_name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    is_custom_catalog = models.IntegerField()
    catalog_master_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    tenantentityfield_id = models.IntegerField(blank=True, null=True)
    is_visible_in_grid = models.IntegerField(blank=True, null=True)
    is_visible_in_search = models.IntegerField(blank=True, null=True)
    is_required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tenant_entity_defs'


class TenantEntityFields(models.Model):
    version = models.IntegerField()
    tenant_id = models.IntegerField(blank=True, null=True)
    entity_info_id = models.IntegerField(blank=True, null=True)
    entity = models.CharField(max_length=255, blank=True, null=True)
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
        db_table = 'tenant_entity_fields'


class TenantInvoices(models.Model):
    version = models.IntegerField()
    tenant_id = models.IntegerField()
    from_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField(blank=True, null=True)
    total_amount = models.FloatField()
    no_of_new_candidates = models.IntegerField()
    no_of_new_sources = models.IntegerField()
    db_usage = models.FloatField()
    down_load_size = models.FloatField()
    total_no_of_users = models.IntegerField()
    new_users_created = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'tenant_invoices'


class TenantLoggings(models.Model):
    action_name = models.CharField(max_length=255, blank=True, null=True)
    request_time = models.DateTimeField(blank=True, null=True)
    response_time = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tenant_id = models.IntegerField()
    response_size = models.FloatField()
    created_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_loggings'


class TenantValidations(models.Model):
    version = models.IntegerField()
    validator = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    tenantentitydef_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_validations'


class Tenants(models.Model):
    version = models.IntegerField()
    tenant_name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    domain_model = models.IntegerField(blank=True, null=True)
    splash_screen = models.TextField(blank=True, null=True)
    welcome_text = models.CharField(max_length=255, blank=True, null=True)
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
    presentation_id = models.IntegerField(blank=True, null=True)
    tenant_type = models.IntegerField(blank=True, null=True)
    industry_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    text5 = models.CharField(max_length=50, blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(blank=True, null=True)
    integer4 = models.IntegerField(blank=True, null=True)
    integer5 = models.IntegerField(blank=True, null=True)
    tenant_rank_id = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    is_clms_enabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenants'


class TenantsMenuItems(models.Model):
    html_content = models.TextField(blank=True, null=True)
    menu_item_id = models.IntegerField(blank=True, null=True)
    is_public = models.IntegerField()
    sequence = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)
    menu_name = models.CharField(max_length=245, blank=True, null=True)
    url = models.CharField(max_length=245, blank=True, null=True)
    module_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenants_menu_items'


class TenantsModules(models.Model):
    is_visible = models.IntegerField()
    module_id = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    tenant_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenants_modules'


class Validations(models.Model):
    version = models.IntegerField()
    validator = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    created_on = models.DateTimeField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    guid = models.CharField(max_length=40)
    entitiesproperty_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validations'
