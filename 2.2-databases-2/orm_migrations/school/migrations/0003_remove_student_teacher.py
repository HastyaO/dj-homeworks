# Generated by Django 4.2.1 on 2023-12-20 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_student_group_alter_student_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
