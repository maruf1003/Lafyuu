# Generated by Django 3.2.1 on 2022-03-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0007_alter_order_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Zip_Code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country_Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='Address',
            field=models.ManyToManyField(to='things.Address'),
        ),
    ]
