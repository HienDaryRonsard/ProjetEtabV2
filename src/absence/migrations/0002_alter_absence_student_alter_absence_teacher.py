# Generated by Django 5.1 on 2024-09-02 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absence', '0001_initial'),
        ('student', '0002_alter_student_gender'),
        ('teacher', '0002_alter_teacher_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_address', to='student.student'),
        ),
        migrations.AlterField(
            model_name='absence',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_address', to='teacher.teacher'),
        ),
    ]