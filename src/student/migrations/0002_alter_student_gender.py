# Generated by Django 5.1 on 2024-09-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('H', 'Homme'), ('F', 'Femme'), ('O', 'Autre')], default='H', max_length=1, verbose_name='Genre'),
        ),
    ]
