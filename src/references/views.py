from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


from . import models, forms
# Create your views here.

def currency_detail(request, pk):
    obj = models.Currency.objects.get(pk=pk)
    context={"obj":obj, "verb":"Detail"}
    return render(request, 
                  template_name="/references/currency_detail.html",
                  context=context,
                  )

def currency_list(request):
    obj_list = models.Currency.objects.all()
    context={"object_list":obj_list, "verb":"List"}
    return render(request, 
                  template_name="/references/currency_list.html",
                  context=context,
                  )

def currency_create(request):
    template_name = "/references/currency_create.html"
    if request.method == "GET":
        
        form = forms.CurrencyForm()
        context={"verb":"Create", "form":form}
    elif request.method == "POST":
        form = forms.CurrencyForm(request.POST)
        if form.is_valid():
            obj = form.save_obj()
            return HttpResponseRedirect(f"/references/currency/{ obj.pk }")
        else:
            context={"verb":"Create", "form":form}


    else :
        raise Exception("Wrong Method")
    return render(request, 
                  template_name=template_name,
                  context=context,
                  )
    
def currency_update(request, pk):
    template_name = "/references/currency_update.html"
    if request.method == "GET":
        form = forms.CurrencyModelForm()
        context={"verb":"Update", "form":form}

    elif request.method == "POST":
        form = forms.CurrencyModelForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(f"/references/currency/update/{ obj.pk }")
    else :
        raise Exception("Wrong Method")
    return render(request, 
                  template_name=template_name,
                  context=context,
                  )

class AboutUs(TemplateView):
    template_name = "about_us.html"