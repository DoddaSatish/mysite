# Generated by Django 4.0.4 on 2022-06-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0014_job_notification_posted_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_notification',
            name='posted_on',
            field=models.DateTimeField(null=True),
        ),
    ]