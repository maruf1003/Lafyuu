# Generated by Django 3.2.1 on 2022-03-17 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]
