# Generated by Django 4.2.1 on 2023-11-01 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_jg', '0004_alter_job_giver_details_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_avl_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_first_name', models.CharField(blank=True, max_length=40, null=True)),
                ('form_last_name', models.CharField(blank=True, max_length=40, null=True)),
                ('job_image', models.ImageField(upload_to='static/images/')),
                ('form_email', models.CharField(blank=True, max_length=10, null=True)),
                ('form_job_title', models.CharField(blank=True, max_length=40, null=True)),
                ('form_phno', models.CharField(blank=True, max_length=40, null=True)),
                ('form_country', models.CharField(blank=True, max_length=40, null=True)),
                ('form_job_desc', models.CharField(blank=True, max_length=40, null=True)),
                ('form_job_skills', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]