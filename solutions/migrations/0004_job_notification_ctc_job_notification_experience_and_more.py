# Generated by Django 4.0.4 on 2022-06-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0003_rename_job_notifications_job_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_notification',
            name='ctc',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='job_notification',
            name='experience',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='job_notification',
            name='last_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='job_notification',
            name='official_website',
            field=models.CharField(default='', max_length=500),
        ),
    ]
