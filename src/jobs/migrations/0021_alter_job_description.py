# Generated by Django 3.2.4 on 2021-07-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_rename_post_comment_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
