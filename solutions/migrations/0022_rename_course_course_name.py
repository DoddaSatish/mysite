# Generated by Django 4.0.4 on 2022-06-07 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0021_alter_quiz_script'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course',
            new_name='name',
        ),
    ]
