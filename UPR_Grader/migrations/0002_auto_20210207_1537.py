# Generated by Django 3.1.6 on 2021-02-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPR_Grader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]