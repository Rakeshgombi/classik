# Generated by Django 3.2.5 on 2021-07-28 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_alter_course_coursestudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseCreator',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
