# Generated by Django 3.1.5 on 2023-04-06 16:25

import applications.online_cms.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0002_student_hall_id'),
        ('online_cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(auto_now=True)),
                ('submit_date', models.DateTimeField()),
                ('assignment_name', models.CharField(max_length=100)),
                ('doc', models.FileField(blank=True, null=True, upload_to=applications.online_cms.models.assignment_file_name)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(auto_now=True)),
                ('document_name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=100)),
                ('doc', models.FileField(blank=True, null=True, upload_to=applications.online_cms.models.content_file_name)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.course')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAssignment1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(auto_now=True)),
                ('course_code', models.CharField(max_length=100)),
                ('doc', models.FileField(blank=True, null=True, upload_to=applications.online_cms.models.assignment_submit_name)),
                ('score', models.IntegerField(null=True)),
                ('feedback', models.CharField(max_length=100, null=True)),
                ('assign_name', models.CharField(max_length=100)),
                ('assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_cms.courseassignment')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.AlterField(
            model_name='coursedocuments',
            name='document_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='StudentAssignment',
        ),
    ]
