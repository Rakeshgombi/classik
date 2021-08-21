# Generated by Django 3.2.5 on 2021-07-28 12:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_course_coursecreator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseStudent',
            field=models.ManyToManyField(blank=True, related_name='Disciples', to=settings.AUTH_USER_MODEL),
        ),
    ]
