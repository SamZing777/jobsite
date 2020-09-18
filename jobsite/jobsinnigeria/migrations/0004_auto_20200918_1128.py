# Generated by Django 3.1.1 on 2020-09-18 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobsinnigeria', '0003_jobcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(blank=True, default='Lagos', max_length=20, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jobsinnigeria.jobcategory'),
        ),
    ]
