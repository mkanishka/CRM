# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 00:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
        ('oppurtunity', '0001_initial'),
        ('common', '0001_initial'),
        ('leads', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_comments', to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='comment',
            name='lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leads', to='leads.Lead'),
        ),
        migrations.AddField(
            model_name='comment',
            name='opportunity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opportunity_comments', to='oppurtunity.Opportunity'),
        ),
        migrations.AddField(
            model_name='comment',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_comments', to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
