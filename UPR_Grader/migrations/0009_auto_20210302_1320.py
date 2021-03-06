# Generated by Django 3.1.6 on 2021-03-02 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UPR_Grader', '0008_students_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='students',
            name='student_email',
        ),
        migrations.RemoveField(
            model_name='students',
            name='student_first_name',
        ),
        migrations.RemoveField(
            model_name='students',
            name='student_last_name',
        ),
        migrations.RemoveField(
            model_name='students',
            name='student_password',
        ),
        migrations.AddField(
            model_name='students',
            name='student_campus',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students',
            name='student_program',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students',
            name='student_user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
