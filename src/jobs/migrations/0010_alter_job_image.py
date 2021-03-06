# Generated by Django 3.2.4 on 2021-06-22 21:17

from django.db import migrations
import django_resized.forms
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_alter_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='jobs/default.jpg', force_format=None, keep_meta=True, quality=0, size=[500, 300], upload_to=jobs.models.image_upload),
        ),
    ]
