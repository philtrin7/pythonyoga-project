# Generated by Django 3.2.6 on 2021-08-24 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_transaction_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='courier',
            name='fcm_token',
            field=models.TextField(blank=True),
        ),
    ]