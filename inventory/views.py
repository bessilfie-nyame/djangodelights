from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import * 
from .forms import *

class HomeView(TemplateView):
    template_name = "inventory/home.html"
    # revenue = 0

    def get_context_data(self):
        context = super().get_context_data()
        context["ingredients"] = Ingredient.objects.all()
        context["menuItem"] = MenuItem.objects.all()
        context["recipe_requirement"] = RecipeRequirement.objects.all()
        context["purchase"] = Purchase.objects.all()

        # HomeView.revenue += Purchase.menu_item.price
        # rev = HomeView.revenue
        # context["revenue"] = rev

        return context

class IngredientsView(ListView):
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


class MenuItemView(ListView):
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


class Purchaseview(ListView):
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




