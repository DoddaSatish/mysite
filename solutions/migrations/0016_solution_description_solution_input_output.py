# Generated by Django 4.0.4 on 2022-06-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0015_alter_job_notification_posted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='solution',
            name='input_output',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
