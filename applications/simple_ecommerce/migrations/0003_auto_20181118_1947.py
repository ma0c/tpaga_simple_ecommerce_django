# Generated by Django 2.1.3 on 2018-11-18 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_ecommerce', '0002_auto_20181118_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_cost',
            new_name='total_value',
        ),
    ]