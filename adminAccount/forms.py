from userAccount.models import FormQues
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import *


class formAdmin(ModelForm):
    class Meta:
        model = QuestionsForm
        fields = ["domain","questionType", "priority", "questionsToAdd",
                  "OptionsOne", "OptionsOneValue", "OptionsTwo", "OptionsTwoValue", "OptionsThree", "OptionsThreeValue", "OptionsFour", "OptionsFourValue", "OptionsFive", "OptionsFiveValue", "OptionsSix", "OptionsSixValue"]


class formFinance(ModelForm):
    class Meta:
        model = modelFinance
        fields = ["priority", "questionsToAdd", "questionType","question_text",
                  "OptionsOne", "OptionsOneValue", "OptionsTwo", "OptionsTwoValue", "OptionsThree", "OptionsThreeValue", "OptionsFour", "OptionsFourValue", "OptionsFive", "OptionsFiveValue", "OptionsSix", "OptionsSixValue"]


class formStrategy(ModelForm):
    class Meta:
        model = modelStrategy
        fields = ["priorityStrategy", "questionsToAddStrategy","questionType","question_text", 
                  "OptionsOneStrategy", "OptionsOneValueStrategy", "OptionsTwoStrategy", "OptionsTwoValueStrategy", "OptionsThreeStrategy", "OptionsThreeValueStrategy", "OptionsFourStrategy", "OptionsFourValueStrategy", "OptionsFiveStrategy", "OptionsFiveValueStrategy", "OptionsSixStrategy", "OptionsSixValueStrategy"]


class formPortfolio(ModelForm):
    class Meta:
        model = modelPortfolio
        fields = ["priority", "questionsToAdd", "questionType","question_text",
                  "OptionsOne", "OptionsOneValue", "OptionsTwo", "OptionsTwoValue", "OptionsThree", "OptionsThreeValue", "OptionsFour", "OptionsFourValue", "OptionsFive", "OptionsFiveValue", "OptionsSix", "OptionsSixValue"]


class formSkills(ModelForm):
    class Meta:
        model = modelSkills
        fields = ["priority", "questionsToAdd", "questionType","question_text",
                  "OptionsOne", "OptionsOneValue", "OptionsTwo", "OptionsTwoValue", "OptionsThree", "OptionsThreeValue", "OptionsFour", "OptionsFourValue", "OptionsFive", "OptionsFiveValue", "OptionsSix", "OptionsSixValue"]


class formCustomers(ModelForm):
    class Meta:
        model = modelCustomers
        fields = ["priority", "questionsToAdd", "questionType","question_text",
                  "OptionsOne", "OptionsOneValue", "OptionsTwo", "OptionsTwoValue", "OptionsThree", "OptionsThreeValue", "OptionsFour", "OptionsFourValue", "OptionsFive", "OptionsFiveValue", "OptionsSix", "OptionsSixValue"]


class formCompetitors(ModelForm):
    class Meta:
        model = modelCompetitors
        fields = ["priority", "questionsToAdd", "questionType","question_text",
                  "OptionsOne", "OptionsOneValue", "OptionsTwo", "OptionsTwoValue", "OptionsThree", "OptionsThreeValue", "OptionsFour", "OptionsFourValue", "OptionsFive", "OptionsFiveValue", "OptionsSix", "OptionsSixValue"]


class formSales(ModelForm):
    class Meta:
        model = modelSales
        fields = ["priority", "questionsToAdd", "questionType","question_text",
                  "OptionsOne", "OptionsOneValue", "OptionsTwo", "OptionsTwoValue", "OptionsThree", "OptionsThreeValue", "OptionsFour", "OptionsFourValue", "OptionsFive", "OptionsFiveValue", "OptionsSix", "OptionsSixValue"]


class formMarketing(ModelForm):
    class Meta:
        model = modelMarketing
        fields = ["priority", "questionsToAdd","questionType","question_text", 
                  "OptionsOne", "OptionsOneValue", "OptionsTwo", "OptionsTwoValue", "OptionsThree", "OptionsThreeValue", "OptionsFour", "OptionsFourValue", "OptionsFive", "OptionsFiveValue", "OptionsSix", "OptionsSixValue"]
class formMarketing(FormQues):
    class Meta:
        model = FormQues
        fields = ["Option"]