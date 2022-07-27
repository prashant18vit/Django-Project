from typing import Text
from django.db import models
QUESTION_CHOICE = [
        ('options', 'options'),
        ('Text', 'Text'),
    ]

class QuestionsForm(models.Model):

    DOMAIN_NAME = [
        ('Email', 'Email'),
        ('Website', 'Website'),
        ('Skills', 'Skills'),
        ('Customers', 'Customers'),
        ('Competitors', 'Competitors'),
        ('Finance', 'Finance'),
        ('Sales', 'Sales'),
    ]

    PRIOR_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]
    OPTIONS_CHOICE = [
        ('1', ''),
        ('2', '2'),
    ]
    QUESTION_CHOICE = [
        ('1', 'options'),
        ('2', 'Text'),
    ]
    domain = models.CharField(max_length=20, choices=DOMAIN_NAME)
    questionType = models.CharField(max_length = 20,choices=QUESTION_CHOICE)
    ans_text = models.CharField(max_length=200,null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=PRIOR_CHOICES)
    questionsToAdd = models.CharField(max_length=256)
    OptionsOne = models.CharField(max_length=120)
    OptionsOneValue = models.IntegerField()
    OptionsTwo = models.CharField(max_length=120)
    OptionsTwoValue = models.IntegerField()
    OptionsThree = models.CharField(max_length=120, null=True, blank=True)
    OptionsThreeValue = models.IntegerField(null=True, blank=True)
    OptionsFour = models.CharField(max_length=120, null=True, blank=True)
    OptionsFourValue = models.IntegerField(null=True, blank=True)
    OptionsFive = models.CharField(max_length=120, null=True, blank=True)
    OptionsFiveValue = models.IntegerField(null=True, blank=True)
    OptionsSix = models.CharField(max_length=120, null=True, blank=True)
    OptionsSixValue = models.IntegerField(null=True, blank=True)


class modelFinance(models.Model):
    domain = models.CharField(max_length=20, default="Finance", blank=True)
    date = models.DateField(auto_now_add=True)
    priority = models.IntegerField()
    questionsToAdd = models.CharField(max_length=256)
    
    questionType = models.CharField(max_length = 20,choices=QUESTION_CHOICE,null=True, blank=True)
    question_text = models.CharField(max_length=200,null=True, blank=True)
    OptionsOne = models.CharField(max_length=120)
    OptionsOneValue = models.IntegerField()
    OptionsTwo = models.CharField(max_length=120)
    OptionsTwoValue = models.IntegerField()
    OptionsThree = models.CharField(max_length=120, null=True, blank=True)
    OptionsThreeValue = models.IntegerField(null=True, blank=True)
    OptionsFour = models.CharField(max_length=120, null=True, blank=True)
    OptionsFourValue = models.IntegerField(null=True, blank=True)
    OptionsFive = models.CharField(max_length=120, null=True, blank=True)
    OptionsFiveValue = models.IntegerField(null=True, blank=True)
    OptionsSix = models.CharField(max_length=120, null=True, blank=True)
    OptionsSixValue = models.IntegerField(null=True, blank=True)


class modelStrategy(models.Model):
    domainStrategy = models.CharField(
        max_length=20, default="Strategy", blank=True)
    dateStrategy = models.DateField(auto_now_add=True)
    priorityStrategy = models.IntegerField()
    questionsToAddStrategy = models.CharField(max_length=256)
    questionType = models.CharField(max_length = 20,choices=QUESTION_CHOICE,null=True, blank=True)
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


class modelPortfolio(models.Model):
    domain = models.CharField(max_length=20, default="Portfolio", blank=True)
    date = models.DateField(auto_now_add=True)
    priority = models.IntegerField()
    questionsToAdd = models.CharField(max_length=256)
    questionType = models.CharField(max_length = 20,choices=QUESTION_CHOICE,null=True, blank=True)
    question_text = models.CharField(max_length=200,null=True, blank=True)
    OptionsOne = models.CharField(max_length=120, null=True, blank=True)
    OptionsOneValue = models.IntegerField(null=True, blank=True)
    OptionsTwo = models.CharField(max_length=120, null=True, blank=True)
    OptionsTwoValue = models.IntegerField(null=True, blank=True)
    OptionsThree = models.CharField(max_length=120, null=True, blank=True)
    OptionsThreeValue = models.IntegerField(null=True, blank=True)
    OptionsFour = models.CharField(max_length=120, null=True, blank=True)
    OptionsFourValue = models.IntegerField(null=True, blank=True)
    OptionsFive = models.CharField(max_length=120, null=True, blank=True)
    OptionsFiveValue = models.IntegerField(null=True, blank=True)
    OptionsSix = models.CharField(max_length=120, null=True, blank=True)
    OptionsSixValue = models.IntegerField(null=True, blank=True)


class modelSkills(models.Model):
    domain = models.CharField(max_length=20, default="Skills", blank=True)
    date = models.DateField(auto_now_add=True)
    priority = models.IntegerField()
    questionsToAdd = models.CharField(max_length=256)
    questionType = models.CharField(max_length = 20,choices=QUESTION_CHOICE,null=True, blank=True)
    question_text = models.CharField(max_length=200,null=True, blank=True)
    OptionsOne = models.CharField(max_length=120, null=True, blank=True)
    OptionsOneValue = models.IntegerField(null=True, blank=True)
    OptionsTwo = models.CharField(max_length=120, null=True, blank=True)
    OptionsTwoValue = models.IntegerField(null=True, blank=True)
    OptionsThree = models.CharField(max_length=120, null=True, blank=True)
    OptionsThreeValue = models.IntegerField(null=True, blank=True)
    OptionsFour = models.CharField(max_length=120, null=True, blank=True)
    OptionsFourValue = models.IntegerField(null=True, blank=True)
    OptionsFive = models.CharField(max_length=120, null=True, blank=True)
    OptionsFiveValue = models.IntegerField(null=True, blank=True)
    OptionsSix = models.CharField(max_length=120, null=True, blank=True)
    OptionsSixValue = models.IntegerField(null=True, blank=True)


class modelCustomers(models.Model):
    domain = models.CharField(max_length=20, default="Customers", blank=True)
    date = models.DateField(auto_now_add=True)
    priority = models.IntegerField()
    questionsToAdd = models.CharField(max_length=256)
    questionType = models.CharField(max_length = 20,choices=QUESTION_CHOICE,null=True, blank=True)
    question_text = models.CharField(max_length=200,null=True, blank=True)
    OptionsOne = models.CharField(max_length=120, null=True, blank=True)
    OptionsOneValue = models.IntegerField(null=True, blank=True)
    OptionsTwo = models.CharField(max_length=120,null=True, blank=True)
    OptionsTwoValue = models.IntegerField(null=True, blank=True)
    OptionsThree = models.CharField(max_length=120, null=True, blank=True)
    OptionsThreeValue = models.IntegerField(null=True, blank=True)
    OptionsFour = models.CharField(max_length=120, null=True, blank=True)
    OptionsFourValue = models.IntegerField(null=True, blank=True)
    OptionsFive = models.CharField(max_length=120, null=True, blank=True)
    OptionsFiveValue = models.IntegerField(null=True, blank=True)
    OptionsSix = models.CharField(max_length=120, null=True, blank=True)
    OptionsSixValue = models.IntegerField(null=True, blank=True)


class modelCompetitors(models.Model):
    domain = models.CharField(max_length=20, default="Competitors", blank=True)
    date = models.DateField(auto_now_add=True)
    priority = models.IntegerField()
    questionsToAdd = models.CharField(max_length=256)
    questionType = models.CharField(max_length = 20,choices=QUESTION_CHOICE,null=True, blank=True)
    question_text = models.CharField(max_length=200,null=True, blank=True)
    OptionsOne = models.CharField(max_length=120, null=True, blank=True)
    OptionsOneValue = models.IntegerField( null=True, blank=True)
    OptionsTwo = models.CharField(max_length=120, null=True, blank=True)
    OptionsTwoValue = models.IntegerField(null=True, blank=True)
    OptionsThree = models.CharField(max_length=120, null=True, blank=True)
    OptionsThreeValue = models.IntegerField(null=True, blank=True)
    OptionsFour = models.CharField(max_length=120, null=True, blank=True)
    OptionsFourValue = models.IntegerField(null=True, blank=True)
    OptionsFive = models.CharField(max_length=120, null=True, blank=True)
    OptionsFiveValue = models.IntegerField(null=True, blank=True)
    OptionsSix = models.CharField(max_length=120, null=True, blank=True)
    OptionsSixValue = models.IntegerField(null=True, blank=True)


class modelSales(models.Model):
    domain = models.CharField(max_length=20, default="Sales", blank=True)
    date = models.DateField(auto_now_add=True)
    priority = models.IntegerField()
    questionsToAdd = models.CharField(max_length=256)
    questionType = models.CharField(max_length = 20,choices=QUESTION_CHOICE,null=True, blank=True)
    question_text = models.CharField(max_length=200,null=True, blank=True)
    OptionsOne = models.CharField(max_length=120, null=True, blank=True)
    OptionsOneValue = models.IntegerField( null=True, blank=True)
    OptionsTwo = models.CharField(max_length=120, null=True, blank=True)
    OptionsTwoValue = models.IntegerField( null=True, blank=True)
    OptionsThree = models.CharField(max_length=120, null=True, blank=True)
    OptionsThreeValue = models.IntegerField(null=True, blank=True)
    OptionsFour = models.CharField(max_length=120, null=True, blank=True)
    OptionsFourValue = models.IntegerField(null=True, blank=True)
    OptionsFive = models.CharField(max_length=120, null=True, blank=True)
    OptionsFiveValue = models.IntegerField(null=True, blank=True)
    OptionsSix = models.CharField(max_length=120, null=True, blank=True)
    OptionsSixValue = models.IntegerField(null=True, blank=True)


class modelMarketing(models.Model):
    domain = models.CharField(max_length=20, default="Marketing", blank=True)
    date = models.DateField(auto_now_add=True)
    priority = models.IntegerField()
    questionsToAdd = models.CharField(max_length=256, null=True, blank=True)
    questionType = models.CharField(max_length = 20,choices=QUESTION_CHOICE,null=True, blank=True)
    question_text = models.CharField(max_length=200,null=True, blank=True)
    OptionsOne = models.CharField(max_length=120, null=True, blank=True)
    OptionsOneValue = models.IntegerField(null=True, blank=True)
    OptionsTwo = models.CharField(max_length=120, null=True, blank=True)
    OptionsTwoValue = models.IntegerField( null=True, blank=True)
    OptionsThree = models.CharField(max_length=120, null=True, blank=True)
    OptionsThreeValue = models.IntegerField(null=True, blank=True)
    OptionsFour = models.CharField(max_length=120, null=True, blank=True)
    OptionsFourValue = models.IntegerField(null=True, blank=True)
    OptionsFive = models.CharField(max_length=120, null=True, blank=True)
    OptionsFiveValue = models.IntegerField(null=True, blank=True)
    OptionsSix = models.CharField(max_length=120, null=True, blank=True)
    OptionsSixValue = models.IntegerField(null=True, blank=True)
