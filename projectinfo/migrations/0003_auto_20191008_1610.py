# Generated by Django 2.2.6 on 2019-10-08 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectinfo', '0002_auto_20191008_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectinfo',
            old_name='department',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='projectinfo',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='projectinfo',
            old_name='submitted_date',
            new_name='Submitted_Date',
        ),
        migrations.RenameField(
            model_name='projectinfo',
            old_name='title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='projectinfo',
            old_name='year',
            new_name='Year',
        ),
    ]
