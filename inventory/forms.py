from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"


class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



