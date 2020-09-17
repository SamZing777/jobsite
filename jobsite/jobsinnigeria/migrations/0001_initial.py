# Generated by Django 3.1.1 on 2020-09-17 09:03

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('age', models.CharField(choices=[('16', 'Sixteen'), ('17', 'Seventeen'), ('18', 'Eighteen'), ('19', 'Nineteen'), ('20', 'Twenty')], default='16', max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], default='Male', max_length=6)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cv', models.FileField(upload_to='cv')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', autoslug.fields.AutoSlugField(default='', editable=False, populate_from='job_title', unique=True)),
                ('job_description', tinymce.models.HTMLField()),
                ('job_type', models.CharField(blank=True, max_length=250, null=True)),
                ('job_location', models.CharField(blank=True, max_length=250, null=True)),
                ('company_name', models.CharField(blank=True, max_length=250, null=True)),
                ('about_the_company', tinymce.models.HTMLField()),
                ('qualifications', models.CharField(blank=True, max_length=400, null=True)),
                ('competency_title', models.CharField(blank=True, default='competency', max_length=20)),
                ('competency', models.TextField(blank=True, default=None)),
                ('job_requirements', tinymce.models.HTMLField()),
                ('website', models.URLField(blank=True, max_length=250, null=True)),
                ('job_experience', models.CharField(blank=True, max_length=250, null=True)),
                ('published', models.BooleanField(default=True)),
                ('job_qualification', models.CharField(blank=True, default='bsc', max_length=250, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(blank=True, default='Lagos', max_length=20, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jobsinnigeria.category')),
                ('job_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
