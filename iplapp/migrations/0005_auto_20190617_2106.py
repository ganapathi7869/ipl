# Generated by Django 2.2.2 on 2019-06-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplapp', '0004_deliveries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveries',
            name='dismissal_kind',
            field=models.CharField(max_length=30, null=True),
        ),
    ]