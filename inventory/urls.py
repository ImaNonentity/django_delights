from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.log_out, name="logout"),
    path('register', views.register_request, name="register"),
    path('', views.HomeView.as_view(), name='home'),
    path('ingredients/', views.IngredientsView.as_view(), name='ingredients'),
    path('ingredients/new', views.AddIngredientView.as_view(), name='add_ingredient'),
    path('ingredients/<pk>/update', views.UpdateIngredientView.as_view(), name='update_ingredient'),
    path('ingredients/<pk>/delete', views.DeleteIngredientView.as_view(), name='delete_ingredient'),
    path('menu', views.MenuView.as_view(), name='menu'),
    path('menu/new', views.AddMenuItemView.as_view(), name='add_menu_item'),
    path('menu/<pk>/delete', views.DeleteMenuItemView.as_view(), name='delete_menu_item'),
    path('reciperequirement/new', views.NewRecipeRequirementView.as_view(), name='add_recipe_requirement'),
    path('purchase', views.PurchaseView.as_view(), name='purchase'),
    path('purchase/new', views.NewPurchaseView.as_view(), name='add_purchase'),
    path('purchase/<pk>/delete', views.DeletePurchaseView.as_view(), name='delete_purchase'),
    path('reports', views.ReportView.as_view(), name='reports'),

]