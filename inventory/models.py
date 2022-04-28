from turtle import title

from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    unit_price = models.FloatField(default=0)

    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
        return f"""
        name={self.name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.unit_price}
        """


class MenuItem(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)

    @staticmethod  # may break smth
    def get_absolute_url():
        return "/menu"

    def is_available(self):
        return all(_.is_enough() for _ in self.reciperequirement_set.all())

    def __str__(self):
        return f"title={self.title}; price={self.price}"


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return"/purchase"

    def __str__(self):
        return f"menu_item=[{self.menu_item}]; time={self.timestamp}"


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient: Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)


    def get_absolute_url(self):
        return "/menu"

    def is_enough(self):
        return self.quantity <= self.ingredient.quantity

    def __str__(self):
        return f"menu_item=[{self.menu_item}]; ingredient={self.ingredient.name}; qty={self.quantity}"


