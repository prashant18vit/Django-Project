# Generated by Django 3.0 on 2021-07-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminAccount', '0003_modelfinance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelfinance',
            name='domain',
            field=models.CharField(blank=True, default='Finance', max_length=20),
        ),
    ]