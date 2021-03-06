# Generated by Django 2.1.3 on 2018-11-18 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simple_ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
