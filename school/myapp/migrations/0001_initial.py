# Generated by Django 4.2.13 on 2024-05-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('StudentClass', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
