import datetime

from django.db import models
from django.shortcuts import render, redirect

from ..models.customer import Customer
from ..models.products import Products


class Order(models.Model):
	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.IntegerField()
	address = models.CharField(max_length=50, default='', blank=True)
	phone = models.CharField(max_length=50, default='', blank=True)
	date = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)

	def placeOrder(self):
		self.save()

	@staticmethod
	def get_orders_by_customer(customer_id):
		return Order.objects.filter(customer=customer_id).order_by('-date')

class Cart():
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )