from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.


def adminHome(request):
    form = formAdmin(request.POST)
    if form.is_valid():
        QuestionsAdded = form.save(commit=False)
        form.save()
        return redirect("adminHome")
    else:
        questionsForm = QuestionsForm.objects.all()
        return render(request, "adminHome.html", context={'form': form, "questionsForm": questionsForm})


def AdminLogin(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, "adminLogin.html", context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            print("authenticated", user)
            if user is not None:
                login(request, user)
                return redirect('questions')

        else:
            context = {
                "form": form
            }
            return render(request, "adminLogin.html", context=context)


def adminRegistration(request):
    if request.method == "GET":
        form = UserCreationForm()
        context = {
            "form": form,
        }
        return render(request, "adminRegistration.html", context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect("adminLogin")
        else:
            context = {
                "form": form,
            }
            return render(request, "adminRegistration.html", context=context)


def addQuestions(request):
    form = formAdmin(request.POST)
    if form.is_valid():

        form.save(commit=False)
        form.save()
        return redirect("adminHome")
    else:
        return render(request, "index.html", context={'form': form})


def delete_ques(request, id):
    QuestionsForm.objects.get(pk=id).delete()
    return redirect('adminHome')


def updateQues(request, id):
    update = QuestionsForm.objects.get(pk=id)
    update_ques_form = formAdmin(instance=update)
    # update
    # save
    if request.method == 'POST':
        update_ques_form = formAdmin(request.POST, instance=update)
        if update_ques_form.is_valid():
            update_ques_form.save()
            return redirect('adminHome')
    questionsForm = QuestionsForm.objects.all()
    return render(request, "update.html", context={'update_ques_form': update_ques_form, "questionsForm": questionsForm})


def questionsDashboard(request):
    # form = QuestionsForm.objects.all()
    # totalQuestions = form.count()
    FormFinance = modelFinance.objects.all()
    totalFinQues = FormFinance.count()
    FormStrategy = modelStrategy.objects.all()
    totalStrategy = FormStrategy.count()
    FormPortfolio = modelPortfolio.objects.all()
    totaPortfolio = FormPortfolio.count()
    FormSkills = modelSkills.objects.all()
    totalSkills = FormSkills.count()
    FormCustomers = modelCustomers.objects.all()
    totalCustomers = FormCustomers.count()
    FormCompetitors = modelCompetitors.objects.all()
    totalCompetitors = FormCompetitors.count()
    FormSales = modelSales.objects.all()
    totalSales = FormSales.count()
    FormMarketing = modelMarketing.objects.all()
    totalMarketing = FormMarketing.count()
    totalQuestions = totalMarketing + totalCompetitors + totalCustomers + \
        totalFinQues + totalSales + totalSkills + totalStrategy + totaPortfolio
    context = {
        "totalQuestions": totalQuestions,
        "totalFinQues": totalFinQues,
        "totalStrategy": totalStrategy,
        "totalMarketing": totalMarketing,
        "totalSales": totalSales,
        "totalCompetitors": totalCompetitors,
        "totalCustomers": totalCustomers,
        "totalSkills": totalSkills,
        "totaPortfolio": totaPortfolio,

    }

    return render(request, "QuestionsDashbord.html", context=context)


# def viewFinance(request):
#     formFin = formFinance(request.POST)
#     if formFin.is_valid():

#         formFin.save(commit=False)
#         formFin.save()
#         return redirect("financeHome")
#     else:
#         return render(request, "financeTemplate.html", context={'formFin': formFin})


def financeHome(request):
    formFin = formFinance(request.POST)
    if formFin.is_valid():
        QuestionsAdded = formFin.save(commit=False)
        formFin.save()
        return redirect("financeHome")
    else:
        FormFinance = modelFinance.objects.all()
        return render(request, "financeTemplate.html", context={'formFin': formFin, "FormFinance": FormFinance})


def delete_ques_fin(request, id):
    modelFinance.objects.get(pk=id).delete()
    return redirect('financeHome')


def updatefin(request, id):
    update = modelFinance.objects.get(pk=id)
    update_ques_form = formFinance(instance=update)
    # update
    # save
    if request.method == 'POST':
        update_ques_form = formFinance(request.POST, instance=update)
        if update_ques_form.is_valid():
            update_ques_form.save()
            return redirect('financeHome')
    questionsForm = modelFinance.objects.all()
    return render(request, "updatefinance.html", context={'update_ques_form': update_ques_form, "questionsForm": questionsForm})


# def viewStrategy(request):
#     formStr = formStrategy(request.POST)
#     if formStr.is_valid():

#         formStr.save(commit=False)
#         formStr.save()
#         return redirect("financeHome")
#     else:
#         return render(request, "financeTemplate.html", context={'formStr': formStr})


def StrategyHome(request):
    formStr = formStrategy(request.POST)
    if formStr.is_valid():
        QuestionsAdded = formStr.save(commit=False)
        formStr.save()
        return redirect("StrategyHome")
    else:
        FormStrategy = modelStrategy.objects.all()
        return render(request, "strategyTemplate.html", context={'formStr': formStr, "FormStrategy": FormStrategy})


def delete_ques_stra(request, id):
    modelStrategy.objects.get(pk=id).delete()
    return redirect('StrategyHome')


def updatestra(request, id):
    update = modelStrategy.objects.get(pk=id)
    update_ques_form = formStrategy(instance=update)
    # update
    # save
    if request.method == 'POST':
        update_ques_form = formStrategy(request.POST, instance=update)
        if update_ques_form.is_valid():
            update_ques_form.save()
            return redirect('StrategyHome')
    questionsForm = modelStrategy.objects.all()
    return render(request, "updateStrategy.html", context={'update_ques_form': update_ques_form, "questionsForm": questionsForm})


def PortfolioHome(request):
    form = formPortfolio(request.POST)
    if form.is_valid():
        QuestionsAdded = form.save(commit=False)
        form.save()
        return redirect("PortfolioHome")
    else:
        FormModel = modelPortfolio.objects.all()
        return render(request, "portfolio.html", context={'form': form, "FormModel": FormModel})


def updateportfolio(request, id):
    update = modelPortfolio.objects.get(pk=id)
    update_ques_form = formPortfolio(instance=update)
    # update
    # save
    if request.method == 'POST':
        update_ques_form = formPortfolio(request.POST, instance=update)
        if update_ques_form.is_valid():
            update_ques_form.save()
            return redirect('PortfolioHome')
    questionsForm = modelPortfolio.objects.all()
    return render(request, "updateportfolio.html", context={'update_ques_form': update_ques_form, "questionsForm": questionsForm})


def delete_ques_portfo(request, id):
    modelPortfolio.objects.get(pk=id).delete()
    return redirect('PortfolioHome')


def SkillsHome(request):
    form = formSkills(request.POST)
    if form.is_valid():
        QuestionsAdded = form.save(commit=False)
        form.save()
        return redirect("SkillsHome")
    else:
        FormModel = modelSkills.objects.all()
        return render(request, "skills.html", context={'form': form, "FormModel": FormModel})


def delete_ques_skills(request, id):
    modelSkills.objects.get(pk=id).delete()
    return redirect('SkillsHome')


def updateskills(request, id):
    update = modelSkills.objects.get(pk=id)
    update_ques_form = formSkills(instance=update)
    # update
    # save
    if request.method == 'POST':
        update_ques_form = formSkills(request.POST, instance=update)
        if update_ques_form.is_valid():
            update_ques_form.save()
            return redirect('SkillsHome')
    questionsForm = modelSkills.objects.all()
    return render(request, "updateskills.html", context={'update_ques_form': update_ques_form, "questionsForm": questionsForm})


def CustomersHome(request):
    form = formCustomers(request.POST)
    if form.is_valid():
        QuestionsAdded = form.save(commit=False)
        form.save()
        return redirect("CustomersHome")
    else:
        FormModel = modelCustomers.objects.all()
        return render(request, "customers.html", context={'form': form, "FormModel": FormModel})


def delete_ques_custom(request, id):
    modelCustomers.objects.get(pk=id).delete()
    return redirect('CustomersHome')


def updatecustomers(request, id):
    update = modelCustomers.objects.get(pk=id)
    update_ques_form = formCustomers(instance=update)
    # update
    # save
    if request.method == 'POST':
        update_ques_form = formCustomers(request.POST, instance=update)
        if update_ques_form.is_valid():
            update_ques_form.save()
            return redirect('CustomersHome')
    questionsForm = modelCustomers.objects.all()
    return render(request, "updatecustomers.html", context={'update_ques_form': update_ques_form, "questionsForm": questionsForm})


def CompetitorsHome(request):
    form = formCompetitors(request.POST)
    if form.is_valid():
        QuestionsAdded = form.save(commit=False)
        form.save()
        return redirect("CompetitorsHome")
    else:
        FormModel = modelCompetitors.objects.all()
        return render(request, "competitors.html", context={'form': form, "FormModel": FormModel})


def delete_ques_competi(request, id):
    modelCompetitors.objects.get(pk=id).delete()
    return redirect('CompetitorsHome')


def updatecompetitors(request, id):
    update = modelCompetitors.objects.get(pk=id)
    update_ques_form = formCompetitors(instance=update)
    # update
    # save
    if request.method == 'POST':
        update_ques_form = formCompetitors(request.POST, instance=update)
        if update_ques_form.is_valid():
            update_ques_form.save()
            return redirect('CompetitorsHome')
    questionsForm = modelCompetitors.objects.all()
    return render(request, "updatecompetitiors.html", context={'update_ques_form': update_ques_form, "questionsForm": questionsForm})


def SalesHome(request):
    form = formSales(request.POST)
    if form.is_valid():
        QuestionsAdded = form.save(commit=False)
        form.save()
        return redirect("SalesHome")
    else:
        FormModel = modelSales.objects.all()
        return render(request, "sales.html", context={'form': form, "FormModel": FormModel})


def delete_ques_sales(request, id):
    modelSales.objects.get(pk=id).delete()
    return redirect('SalesHome')


def updatesales(request, id):
    update = modelSales.objects.get(pk=id)
    update_ques_form = formSales(instance=update)
    # update
    # save
    if request.method == 'POST':
        update_ques_form = formSales(request.POST, instance=update)
        if update_ques_form.is_valid():
            update_ques_form.save()
            return redirect('SalesHome')
    questionsForm = modelSales.objects.all()
    return render(request, "updateskills.html", context={'update_ques_form': update_ques_form, "questionsForm": questionsForm})


def MarketingHome(request):
    form = formMarketing(request.POST)
    if form.is_valid():
        QuestionsAdded = form.save(commit=False)
        form.save()
        return redirect("MarketingHome")
    else:
        FormModel = modelMarketing.objects.all()
        return render(request, "marketing.html", context={'form': form, "FormModel": FormModel})


def updatemarketing(request, id):
    update = modelMarketing.objects.get(pk=id)
    update_ques_form = formMarketing(instance=update)
    # update
    # save
    if request.method == 'POST':
        update_ques_form = formMarketing(request.POST, instance=update)
        if update_ques_form.is_valid():
            update_ques_form.save()
            return redirect('MarketingHome')
    questionsForm = modelMarketing.objects.all()
    return render(request, "updatemarketing.html", context={'update_ques_form': update_ques_form, "questionsForm": questionsForm})


def delete_ques_marketing(request, id):
    modelMarketing.objects.get(pk=id).delete()
    return redirect('MarketingHome')


def scrap(request):
    return render(request, 'scrap.html')

def Form(request):
    form = FormQues()
    print("NO",form)
    context = {
        "form":form
    }
    return render(request,"form.html",context=context)