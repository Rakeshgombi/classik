# Generated by Django 3.2.5 on 2021-07-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_announcemet_anncreator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcemet',
            name='annTitle',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
