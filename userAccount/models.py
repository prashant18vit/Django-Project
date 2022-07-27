from django.db import models

# Create your models here.
class modelStrategyAnswer(models.Model):
    domainStrategy = models.CharField(
        max_length=20, default="Strategy", blank=True)
    dateStrategy = models.DateTimeField(auto_now_add=True)
    priorityStrategy = models.IntegerField()
    questionsToAddStrategy = models.CharField(max_length=256)
    questionType = models.CharField(max_length = 20,null=True, blank=True)
    question_text  = models.CharField(max_length=200,null=True, blank=True)
    OptionsOneStrategy = models.CharField(max_length=120, null=True, blank=True)
    OptionsOneValueStrategy = models.IntegerField(null=True, blank=True)
    OptionsTwoStrategy = models.CharField(max_length=120, null=True, blank=True)
    OptionsTwoValueStrategy = models.IntegerField( null=True, blank=True)
    OptionsThreeStrategy = models.CharField(
        max_length=120, null=True, blank=True)
    OptionsThreeValueStrategy = models.IntegerField(null=True, blank=True)
    OptionsFourStrategy = models.CharField(
        max_length=120, null=True, blank=True)
    OptionsFourValueStrategy = models.IntegerField(null=True, blank=True)
    OptionsFiveStrategy = models.CharField(
        max_length=120, null=True, blank=True)
    OptionsFiveValueStrategy = models.IntegerField(null=True, blank=True)
    OptionsSixStrategy = models.CharField(
        max_length=120, null=True, blank=True)
    OptionsSixValueStrategy = models.IntegerField(null=True, blank=True)
class modelAnswer(models.Model):
    domainStrategy = models.CharField(
        max_length=20, default="Strategy", blank=True)
    dateStrategy = models.DateTimeField(auto_now_add=True)
    questionsToAddStrategy = models.CharField(max_length=256)
    questionType = models.CharField(max_length = 20,null=True, blank=True)
    OptionsStrategy = models.CharField(max_length=120, null=True, blank=True)
    OptionsValueStrategy = models.IntegerField(null=True, blank=True)
class modelAnswer1(models.Model):
    domainStrategy = models.CharField(
        max_length=20, default="Strategy", blank=True)
    dateStrategy = models.DateTimeField(auto_now_add=True)
    questionsToAddStrategy = models.CharField(max_length=256)
    questionType = models.CharField(max_length = 20,null=True, blank=True)
    OptionsStrategy = models.CharField(max_length=120, null=True, blank=True)
    OptionsValueStrategy = models.IntegerField(null=True, blank=True)

OPTION = [
    ('option_1',modelStrategyAnswer.OptionsOneStrategy),
    ('option_2',modelStrategyAnswer.OptionsOneStrategy),
    ('option_3',modelStrategyAnswer.OptionsOneStrategy),
    ('option_4',modelStrategyAnswer.OptionsOneStrategy),
    ('option_5',modelStrategyAnswer.OptionsOneStrategy),
    ('option_6',modelStrategyAnswer.OptionsOneStrategy)
]
from django import forms
class FormQues():
    Option = forms.RadioSelect(choices=OPTION)