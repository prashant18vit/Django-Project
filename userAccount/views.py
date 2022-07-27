import re
from typing import Counter
from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from adminAccount.models import modelStrategy
from django.http import JsonResponse, request
from django.views.generic import View,TemplateView
from .models import modelStrategyAnswer,modelAnswer
from adminAccount.models import *
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def regestraionUser(request):
    # form = UserCreationForm()
    # context = {
    #     "form":form
    # }
    # return render(request,"userRegestration.html",context=context)

    # print("this")
    # if request.method == "POST":
    #     saveans = modelAnswer()
    #     saveans.questionsToAddStrategy = request.POST.get("Question")
    #     saveans.OptionsStrategy = request.POST.get('1_Option_ans')
    #     # saveans.OptionsTwoStrategy = request.POST.get('2_Option_ans')
    #     # saveans.OptionsThreeStrategy = request.POST.get('3_Option_ans')
    #     # saveans.OptionsFourStrategy = request.POST.get('4_Option_ans')
    #     # saveans.OptionsFiveStrategy = request.POST.get('5_Option_ans')
    #     # saveans.OptionsSixStrategy = request.POST.get('6_Option_ans')
    #     saveans.save()
    #     print("THIS IS POST",saveans.OptionsStrategy)
    return HttpResponse("<h1>Registration</h1>")    

# class loginUser(View):

    # def get(self, *args, **kwargs):
    #     # print(kwargs)
        
    #     upper = kwargs.get('num_ques')
    #     lower = upper - 1
    #     post = list(modelStrategy.objects.values()[lower:upper])
    #     posts_size = len(modelStrategy.objects.all()) +1
    #     max_size = True if upper >= posts_size else False

        
#         return JsonResponse({'data':post , "max_size":max_size},safe=False)
# listQues =[]
# listans =[]
# mainList = []

# def chnageQuesStra(request):
#     if request.method == "POST":
#         saveans = modelAnswer()
#         saveans.questionsToAddStrategy = request.POST.get("Question")
#         saveans.OptionsStrategy = request.POST.get('optionval')
#         print(saveans.OptionsStrategy)
#         # saveans.save()

#     mod = modelStrategy.objects.all()
#     paginator = Paginator(mod,1)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page =1

#     try:
#         questions = paginator.page(page)

#     except(EmptyPage,InvalidPage):
#         questions = paginator.page(paginator.num_pages)
    
#     context = {
#         "mod":mod,
#         "questions":questions,

#     }
#     return render(request,'Questions.html',context=context)
    
def OtpUser(request):
    return render(request, "userOTP.html")


def Subscription(request):
    return render(request, "subscription.html")


def AdminRedirect(request):
    return redirect(request, "adminLogin.html")
# def saveans(request):

#     if request.method == "POST":
#         saveans = modelAnswer()
#         saveans.questionsToAddStrategy = request.POST.get("Question")
#         saveans.OptionsStrategy = request.POST.get('option')
#         print("HHHHHHHHHHHH",saveans.OptionsStrategy)


#         # check_ques = modelAnswer.objects.filter(questionsToAddStrategy= str).first()
#         # print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",check_ques)
#         # saveans.OptionsTwoStrategy = request.POST.get('2_Option_ans')
#         # saveans.OptionsThreeStrategy = request.POST.get('3_Option_ans')
#         # saveans.OptionsFourStrategy = request.POST.get('4_Option_ans')
#         # saveans.OptionsFiveStrategy = request.POST.get('5_Option_ans')
#         # saveans.OptionsSixStrategy = request.POST.get('6_Option_ans')
#         saveans.save()
#         print("THIS IS POST",saveans.OptionsStrategy)
#         return redirect("chnageQuesStra")
#     return redirect("chnageQuesStra")

def question(request):
    question = modelStrategy.objects.all()
    questionport = modelPortfolio.objects.all()
    questionskill = modelSkills.objects.all()
    questionsales = modelSales.objects.all()
    questioncost = modelCustomers.objects.all()
    questioncompi = modelCompetitors.objects.all()
    questionfin = modelFinance.objects.all()
    arrques = request.POST.get("question")
    arrans = request.POST.get("ans")
    arrval = request.POST.get("val")
    arrdomain = request.POST.get("dom")
    print("DOMAIN",arrdomain)
    # farrayques = arrques.split(",")
    print("before if")
    if arrval != None:
        print("this is if  ")
        listques = arrques.split(",")
        listans = arrans.split(",")
        listval = arrval.split(",")
        listdom = arrdomain.split(",")
        if request.method == "POST":
            print("her post")
            
            print("this is ",len(listval))
            Counter = 0
            if len(listval) != 0 or len(listval)!= None :    
                for i in range(0,len(listval)):
                    print("i -- ",listques[i])
                    questfield = listques[i]
                    if listans[i] == None:
                        listans[i] = ""
                    if listval[i] == None:
                        listval[i] == ""
                        
                    if listval[i] == None or listval[i] == "":
                        pass
                    else:
                        optionfield = str(listans[i])
                        ValueField = str(listval[i])
                        domainfield = str(listdom)
                        saveans = modelAnswer()

                        saveans.questionsToAddStrategy = questfield 
                        saveans.OptionsStrategy = optionfield 
                        saveans.OptionsValueStrategy = ValueField 
                        saveans.domainStrategy = domainfield
                        saveans.save()
                        Counter = Counter + 1
                        print(arrval)
    
        else:
            question = modelStrategy.objects.all()
            questionskill = modelSkills.objects.all()
            questionsales = modelSales.objects.all()
            questioncost = modelCustomers.objects.all()
            questioncompi = modelCompetitors.objects.all()
            questionfin = modelFinance.objects.all()
            context = {


            "question":question,
            "questionport":questionport,
            "questionsales":questionsales,
            "questionskill":questionskill,
            "questioncompi":questioncompi,
            "questioncost":questioncost,
            "questionfin":questionfin,
            }
            return render(request,"question_1.html",context=context)
    context = {
        "question":question,
            "questionport":questionport,
            "questionsales":questionsales,
            "questionskill":questionskill,
            "questioncompi":questioncompi,
            "questioncost":questioncost,
            }
    return render(request,"question_1.html",context=context)