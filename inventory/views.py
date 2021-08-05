from django.db.models.base import Model
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
 
from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import * 
from .forms import *


class HomeView(TemplateView):
    template_name = "inventory/home.html"

def login_view(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username,
                        password=password)
    if user is not None:
      login(request, user)

      return redirect("home")
    else:
      return HttpResponse("invalid credentials")
  return render(request, "registration/login.html", context)

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

def logout_request(request):
  logout(request)
  return redirect("home")

class IngredientsView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["ingredients"] = Ingredient.objects.all()

        return context

class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = "inventory/add_ingredient.html"

class IngredientUpdate(UpdateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = "inventory/ingredient_update.html"

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html" 
    success_url = "/ingredients/"


class MenuItemView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu.html"
 
class MenuItemCreate(CreateView):
    model = MenuItem
    form_class = MenuCreateForm
    template_name = "inventory/add_menu.html"


class RecipeCreate(CreateView):
    model = RecipeRequirement
    form_class = RecipeCreateForm
    template_name = "inventory/add_recipe_requirements.html"


class Purchaseview(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchases.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["purchases"] = Purchase.objects.all()

        return context

class PurchaseCreate(CreateView):
    model = Purchase
    form_class = PurchaseCreateForm
    template_name = "inventory/record_purchase.html"


class ProfitRevenue(TemplateView):
    template_name = "inventory/profit_revenue.html"

    def get_context_data(self):
        context = super().get_context_data()
        ingredients = Ingredient.objects.all()
        menu_items = MenuItem.objects.all()
        
        cost = self.calculate_cost(ingredients)
        revenue = self.calculate_revenue(menu_items)
        profit = self.calculate_profit(revenue, cost)

        context['profit'] = profit
        context['revenue'] = revenue

        return context

    @staticmethod
    def calculate_cost(items):
        cost = 0   
        for item in items:
            cost += item.unit_price
        return cost

    @staticmethod
    def calculate_revenue(items):
        revenue = 0   
        for item in items:
            revenue += item.price
        return revenue

    @staticmethod
    def calculate_profit(revenue, cost):
        return revenue - cost



