# from django.contrib.auth.hashers import check_password
# from django.shortcuts import HttpResponseRedirect, redirect, render
# from store.models.category import Category
# from store.models.customer import Customer
# from store.models.products import Products


# # Create your views here.
# # home view
# class Index():
      
#     def post(self, request):
#         product = request.POST.get('product')
#         remove = request.POST.get('remove')
#         cart = request.session.get('cart')
#         if cart:
#             quantity = cart.get(product)
#             if quantity:
#                 if remove:
#                     if quantity <= 1:
#                         cart.pop(product)
#                     else:
#                         cart[product] = quantity-1
#                 else:
#                     cart[product] = quantity+1
  
#             else:
#                 cart[product] = 1
#         else:
#             cart = {}
#             cart[product] = 1
  
#         request.session['cart'] = cart
#         print('cart', request.session['cart'])
#         return redirect('homepage')
  
#     def get(self, request):
#         # print()
#         return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
  
  
# def store(request):
#     cart = request.session.get('cart')
#     if not cart:
#         request.session['cart'] = {}
#     products = None
#     categories = Category.get_all_categories()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Products.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Products.get_all_products()
  
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
  
#     print('you are : ', request.session.get('email'))
#     return render(request, 'index.html', data)


# # login view
# class Login():
#     return_url = None
  
#     def get(self, request):
#         Login.return_url = request.GET.get('return_url')
#         return render(request, 'login.html')
  
#     def post(self, request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 request.session['customer'] = customer.id
  
#                 if Login.return_url:
#                     return HttpResponseRedirect(Login.return_url)
#                 else:
#                     Login.return_url = None
#                     return redirect('homepage')
#             else:
#                 error_message = 'Invalid !!'
#         else:
#             error_message = 'Invalid !!'
  
#         print(email, password)
#         return render(request, 'login.html', {'error': error_message})
  
  
# def logout(request):
#     request.session.clear()
#     return redirect('login')


# from django.contrib.auth.hashers import make_password
# # signup view
# from django.shortcuts import redirect, render
# from django.views import View
# from store.models.customer import Customer


# class Signup (View):
# 	def get(self, request):
# 		return render(request, 'signup.html')

# 	def post(self, request):
# 		postData = request.POST
# 		first_name = postData.get('firstname')
# 		last_name = postData.get('lastname')
# 		phone = postData.get('phone')
# 		email = postData.get('email')
# 		password = postData.get('password')
# 		# validation
# 		value = {
# 			'first_name': first_name,
# 			'last_name': last_name,
# 			'phone': phone,
# 			'email': email
# 		}
# 		error_message = None

# 		customer = Customer(first_name=first_name,
# 							last_name=last_name,
# 							phone=phone,
# 							email=email,
# 							password=password)
# 		error_message = self.validateCustomer(customer)

# 		if not error_message:
# 			print(first_name, last_name, phone, email, password)
# 			customer.password = make_password(customer.password)
# 			customer.register()
# 			return redirect('homepage')
# 		else:
# 			data = {
# 				'error': error_message,
# 				'values': value
# 			}
# 			return render(request, 'signup.html', data)

# 	def validateCustomer(self, customer):
# 		error_message = None
# 		if (not customer.first_name):
# 			error_message = "Please Enter your First Name !!"
# 		elif len(customer.first_name) < 3:
# 			error_message = 'First Name must be 3 char long or more'
# 		elif not customer.last_name:
# 			error_message = 'Please Enter your Last Name'
# 		elif len(customer.last_name) < 3:
# 			error_message = 'Last Name must be 3 char long or more'
# 		elif not customer.phone:
# 			error_message = 'Enter your Phone Number'
# 		elif len(customer.phone) < 10:
# 			error_message = 'Phone Number must be 11 char Long'
# 		elif len(customer.password) < 5:
# 			error_message = 'Password must be 5 char long'
# 		elif len(customer.email) < 5:
# 			error_message = 'Email must be 5 char long'
# 		elif customer.isExists():
# 			error_message = 'Email Address Already Registered..'
# 		# saving
# 		return error_message
