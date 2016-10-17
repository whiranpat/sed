# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sedUI', '0003_auto_20161017_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='activity_status',
            field=models.CharField(blank=True, choices=[(b'I', b'Inactive'), (b'A', b'Active')], max_length=1),
        ),
        migrations.AddField(
            model_name='staff',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='phone',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_type',
            field=models.CharField(blank=True, choices=[(b'I', b'Instructor'), (b'C', b'Core Team'), (b'V', b'Volunteer')], max_length=1),
        ),
        migrations.AddField(
            model_name='staff',
            name='state',
            field=models.CharField(blank=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Orgeon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')], max_length=2),
        ),
        migrations.AddField(
            model_name='staff',
            name='street',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='zip_code',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
