from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("account/", include("django.contrib.auth.urls"),
    name='login'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout", views.logout_request, name="logout"),
    path('ingredients/', views.IngredientsView.as_view(), 
    name='ingredients'),
    path('ingredient/new', views.IngredientCreate.as_view(),
    name='create_ingredient'),
    path('ingredient/<pk>/update/', views.IngredientUpdate.as_view(),
    name='update_ingredient'),
    path('ingredient/<pk>/delete/', views.IngredientDelete.as_view(),
    name='delete_ingredient'),
    path('menu/', views.MenuItemView.as_view(),
    name='menu'),
    path('purchase/', views.Purchaseview.as_view(),
    name='purchase'),
    path('menu/new', views.MenuItemCreate.as_view(),
    name='create_menu'),
    path('recipe/new', views.RecipeCreate.as_view(),
    name='create_recipe'),
    path('purchase/new', views.PurchaseCreate.as_view(),
    name='create_purchase'),
    path('report', views.ProfitRevenue.as_view(),
    name='revenue_profit')
]