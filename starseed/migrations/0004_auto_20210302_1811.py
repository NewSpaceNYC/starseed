# Generated by Django 3.1.7 on 2021-03-02 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starseed', '0003_auto_20210302_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
