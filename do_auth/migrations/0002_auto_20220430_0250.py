# Generated by Django 3.2.12 on 2022-04-30 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('do_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firm',
            name='info',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='licence',
            name='info',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
