# Generated by Django 3.1.6 on 2021-03-02 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPR_Grader', '0010_auto_20210302_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='student_gpa',
            field=models.CharField(default=0.0, max_length=4),
        ),
        migrations.AddField(
            model_name='students',
            name='student_major_gpa',
            field=models.CharField(default=0.0, max_length=4),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_campus',
            field=models.CharField(default='Mayaguez', max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_program',
            field=models.CharField(default='ICOM', max_length=20),
        ),
    ]
