# Generated by Django 4.2.5 on 2023-10-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_name', models.CharField(max_length=30)),
                ('ad_pwd', models.CharField(max_length=50)),
            ],
        ),
    ]