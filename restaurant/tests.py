from django.test import TestCase
from .models import *


#add the following method in Menu class
# def __str__(self):
#     return f'{self.title} : {str(self.price)}'

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

    def test_getall(self):

        item = Menu.objects.all()
        serialized_data = [
            {"title": obj.title, "price": obj.price, "inventory": obj.inventory}
            for obj in item
        ]
        expected_data = [
            {"title": obj.title, "price": obj.price, "inventory": obj.inventory}
            for obj in item
        ]
        self.assertEqual(serialized_data, expected_data)
