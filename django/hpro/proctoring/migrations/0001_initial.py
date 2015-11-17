# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proctoring_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tenant_id', models.IntegerField()),
                ('candidate_id', models.IntegerField()),
                ('test_id', models.IntegerField()),
                ('file_path', models.CharField(max_length=1024, null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('suspicious_flag', models.BooleanField(default=0)),
                ('review_status', models.BooleanField(default=0)),
                ('duration', models.IntegerField()),
                ('is_deleted', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'proctering_info_map',
            },
        ),
    ]
