# Generated by Django 3.2.5 on 2021-07-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseCreator',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
