# Generated by Django 4.0.4 on 2022-06-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0006_alter_job_notification_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_notification',
            name='img',
            field=models.CharField(default='', max_length=500),
        ),
    ]
