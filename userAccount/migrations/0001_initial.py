# Generated by Django 3.0 on 2021-07-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modelStrategyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domainStrategy', models.CharField(blank=True, default='Strategy', max_length=20)),
                ('dateStrategy', models.DateTimeField(auto_now_add=True)),
                ('priorityStrategy', models.IntegerField()),
                ('questionsToAddStrategy', models.CharField(max_length=256)),
                ('questionType', models.CharField(blank=True, max_length=20, null=True)),
                ('question_text', models.CharField(blank=True, max_length=200, null=True)),
                ('OptionsOneStrategy', models.CharField(blank=True, max_length=120, null=True)),
                ('OptionsOneValueStrategy', models.IntegerField(blank=True, null=True)),
                ('OptionsTwoStrategy', models.CharField(blank=True, max_length=120, null=True)),
                ('OptionsTwoValueStrategy', models.IntegerField(blank=True, null=True)),
                ('OptionsThreeStrategy', models.CharField(blank=True, max_length=120, null=True)),
                ('OptionsThreeValueStrategy', models.IntegerField(blank=True, null=True)),
                ('OptionsFourStrategy', models.CharField(blank=True, max_length=120, null=True)),
                ('OptionsFourValueStrategy', models.IntegerField(blank=True, null=True)),
                ('OptionsFiveStrategy', models.CharField(blank=True, max_length=120, null=True)),
                ('OptionsFiveValueStrategy', models.IntegerField(blank=True, null=True)),
                ('OptionsSixStrategy', models.CharField(blank=True, max_length=120, null=True)),
                ('OptionsSixValueStrategy', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]