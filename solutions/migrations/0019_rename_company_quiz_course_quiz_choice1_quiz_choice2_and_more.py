# Generated by Django 4.0.4 on 2022-06-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0018_course_quiz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='company',
            new_name='course',
        ),
        migrations.AddField(
            model_name='quiz',
            name='choice1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='quiz',
            name='choice2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='quiz',
            name='choice3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='quiz',
            name='choice4',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='quiz',
            name='correct_choice',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='quiz',
            name='script',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.CharField(default='', max_length=4000),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='is_script',
            field=models.BooleanField(default=False),
        ),
    ]