# Generated by Django 3.1.5 on 2021-01-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(max_length=264),
        ),
    ]
