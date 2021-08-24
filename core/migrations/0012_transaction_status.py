# Generated by Django 3.2.6 on 2021-08-24 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_courier_paypal_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('in', 'In'), ('out', 'Out')], default='in', max_length=20),
        ),
    ]