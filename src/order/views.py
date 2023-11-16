from typing import Any
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView, DeleteView
#from references import models

User = get_user_model()

def order_detail(request, pk):
    obj = models.Order.objects.get(pk=pk)
    context={"obj":obj, "verb":"Detail"}
    return render(request, 
                  template_name="order/order_detail.html",
                  context=context,
                  )

def order_list(request):
    obj_list = models.Order.objects.all()
    context={"object_list":obj_list, "verb":"List"}
    return render(request, 
                  template_name="order/order_list.html",
                  context=context,
                  )

def order_create(request):
    
    if request.method == "GET":
        template_name = "order/order_create.html"
        form = forms.OrderForm()
        context={"verb":"Create", "form":form}
    elif request.method == "POST":
        template_name = "order/order_create.html"
        user_pk = request.POST.get("user")
        #name = request.POST.get("name")
        #description = request.POST.get("description")
        #print(name, description)
        form = forms.OrderForm()
        summ = request.POST.get("summ")
        #order_currency_pk = request.POST.get("order_currency")
        obj = models.Order.objects.create(user=User.objects.get(pk=user_pk),
            summ=summ,
            )
        return HttpResponseRedirect(f"/order/{obj}/")
    else :
        raise Exception("Wrong Method")
    return render(request, 
                  template_name=template_name,
                  context=context,
                  )
    
def order_update(request, pk):
    
    if request.method == "GET":
        template_name = "order/order_update.html"
        obj = models.Order.objects.get(pk=pk)
        all_users = User.objects.all()
        all_currencies = models.Currency.objects.all()
        context={
            "obj": obj , 
            "verb":"Update",
            "all_users": all_users,
            "all_currencies": all_currencies
            }

    elif request.method == "POST":
        user_pk = request.POST.get("user")
        summ = request.POST.get("summ")
        order_currency_pk = request.POST.get("order_currency")
        print(user_pk, summ, order_currency_pk)
        obj = models.Order.objects.update(
            user=User.objects.get(pk=user_pk),
            summ=summ,
            order_currency=models.Currency.objects.get(pk=order_currency_pk)
        )
        all_users = User.objects.all()
        all_currencies = models.Currency.objects.all()
        context={
            "obj": obj , 
            "verb":"Update",
            "all_users": all_users,
            "all_currencies": all_currencies
            }
        print(obj)
        return HttpResponseRedirect(f"/order/{ obj }")
    else :
        raise Exception("Wrong Method")
    return render(request, 
                  template_name=template_name,
                  context=context,
                  )

class OrderUpdate(UpdateView):
    template_name = "order/order_update.html"
    model = models.Order
    form_class = forms.OrderModelForm

    def get_success_url(self):
        return  f"/order/success/"
    
class OrderDetail(DetailView):
    template_name="order/order_detail.html"
    model = models.Order
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['verb']='Detail'
        return context
    
class OrderSuccess(TemplateView):
    template_name = "order/order_success.html"    

class OrderList(ListView):
    template_name = "order/order_list.html"
    model = models.Order
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['verb']='List'
        return context
    
class OrderCreate(CreateView):
    template_name = "order/order_create.html"
    model = models.Order
    form_class = forms.OrderModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['verb']='Create'
        return context

class OrderDelete(DeleteView):
    template_name = "order/order_delete.html"
    model = models.Order
    success_url = "/order/list/"