# Generated by Django 3.1.1 on 2020-11-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20201107_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
