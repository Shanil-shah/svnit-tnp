# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 09:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CGPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('5', 'Fifth'), ('6', 'Sixth'), ('7', 'Seventh'), ('8', 'Eighth'), ('9', 'Ninth'), ('10', 'Tenth')], max_length=1)),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='EducationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=31, unique=True)),
                ('ssc', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ssc_result_type', models.CharField(choices=[('CGPA', 'CGPA'), ('PERCENTAGE', '%')], default='PERCENTAGE', max_length=10)),
                ('hsc', models.DecimalField(decimal_places=2, max_digits=4)),
                ('hsc_result_type', models.CharField(choices=[('CGPA', 'CGPA'), ('PERCENTAGE', '%')], default='PERCENTAGE', max_length=10)),
                ('ssc_passing_year', models.CharField(blank=True, max_length=4, null=True)),
                ('extrance_exam_score', models.IntegerField(blank=True, null=True)),
                ('entrance_exam', models.CharField(choices=[('JEE_MAIN', 'JEE Mains'), ('SAT', 'SAT'), ('JEE_ADV', 'JEE Advanced')], default='JEE_MAIN', max_length=8)),
                ('current_backlogs', models.IntegerField(default=0)),
                ('total_backlogs', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='education_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('caste_category', models.CharField(choices=[('OBC', 'OBC'), ('GEN', 'General/Open'), ('SC', 'SC'), ('ST', 'ST')], default='GEN', max_length=3)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('current_address', models.TextField(blank=True, max_length=5000, null=True)),
                ('current_residence_city', models.CharField(blank=True, max_length=255, null=True)),
                ('current_residence_state', models.CharField(blank=True, max_length=255, null=True)),
                ('premanent_address', models.TextField(blank=True, max_length=5000, null=True)),
                ('permanent_residence_city', models.CharField(blank=True, max_length=255, null=True)),
                ('permanent_residence_state', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personal_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cgpa',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cgpa', to='consent.EducationDetail'),
        ),
    ]
