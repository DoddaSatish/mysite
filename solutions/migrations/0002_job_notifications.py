# Generated by Django 4.0.4 on 2022-06-01 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_notifications',
            fields=[
                ('id', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('eligibility', models.CharField(max_length=200)),
                ('qualification', models.TextField()),
                ('job_description', models.TextField()),
                ('job_locations', models.CharField(max_length=1000)),
                ('apply_link', models.CharField(max_length=500)),
            ],
        ),
    ]
