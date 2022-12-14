# Generated by Django 3.0 on 2021-07-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminAccount', '0010_auto_20210723_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcompetitors',
            name='questionType',
            field=models.CharField(blank=True, choices=[('options', 'options'), ('Text', 'Text')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='modelcustomers',
            name='questionType',
            field=models.CharField(blank=True, choices=[('options', 'options'), ('Text', 'Text')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='modelfinance',
            name='questionType',
            field=models.CharField(blank=True, choices=[('options', 'options'), ('Text', 'Text')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='modelmarketing',
            name='questionType',
            field=models.CharField(blank=True, choices=[('options', 'options'), ('Text', 'Text')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='modelportfolio',
            name='questionType',
            field=models.CharField(blank=True, choices=[('options', 'options'), ('Text', 'Text')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='modelsales',
            name='questionType',
            field=models.CharField(blank=True, choices=[('options', 'options'), ('Text', 'Text')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='modelskills',
            name='questionType',
            field=models.CharField(blank=True, choices=[('options', 'options'), ('Text', 'Text')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='modelstrategy',
            name='questionType',
            field=models.CharField(blank=True, choices=[('options', 'options'), ('Text', 'Text')], max_length=20, null=True),
        ),
    ]
