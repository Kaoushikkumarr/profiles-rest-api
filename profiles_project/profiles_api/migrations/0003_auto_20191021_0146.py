# Generated by Django 2.2 on 2019-10-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilefeeditem',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
