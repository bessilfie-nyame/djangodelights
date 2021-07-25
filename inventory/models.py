from django.db import models
import datetime

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
    unit = models.CharField(max_length=15)
    unit_price = models.FloatField()

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    # @property
    # def price(self):
    #     return self.price

    def __str__(self):
        return self.title + ": " + str(self.price)

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.date.today)

    # def __str__(self):
    #     return f"{self.menu_item.title}: {self.menu_item.price} puchased at {self.timestamp}"
