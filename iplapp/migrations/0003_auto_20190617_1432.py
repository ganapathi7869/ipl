# Generated by Django 2.2.2 on 2019-06-17 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplapp', '0002_auto_20190617_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='venue',
            field=models.CharField(max_length=100),
        ),
    ]