# Generated by Django 3.0 on 2021-07-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminAccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsform',
            name='domain',
            field=models.CharField(choices=[('Email', 'Email'), ('Website', 'Website'), ('Skills', 'Skills'), ('Customers', 'Customers'), ('Competitors', 'Competitors'), ('Finance', 'Finance'), ('Sales', 'Sales')], max_length=20),
        ),
    ]
