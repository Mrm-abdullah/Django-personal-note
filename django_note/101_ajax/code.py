# view
""" 
from django.db.models import Q
from django.http import JsonResponse

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('showcart')

def plus_cart(request):
    if request.method == 'GET':
      prod_id = request.GET['prod_id']
      c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
      
      c.quantity +=1
      c.save()
      amount = 0.0
      shipping_amount = 100.0
      cart_product = [p for p in Cart.objects.all() if p.user==request.user]
      for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount  
            totalamount = amount + shipping_amount
      data = {
         'quantity': c.quantity,
         'amount': amount,
         'totalamount': totalamount
      }
      return JsonResponse(data)

def show_cart(request):
   if request.user.is_authenticated:
      user = request.user
      cart = Cart.objects.filter(user=user)
      amount = 0.0
      shipping_amount = 100.0
      total = 0.0
      cart_product = [p for p in Cart.objects.all() if p.user==user]
      if cart_product:
         for p in cart_product:
            tempamount = (p.quantity * p.product.discountprice)
            amount += tempamount  
            totalamount = amount + shipping_amount
         return render(request, 'Shop/addtocart.html', {'carts':cart, 'totalamount':totalamount,'amount':amount })
      else:
         return render(request, 'Shop/emptycart.html')

def remove_cart(request):
    if request.method == 'GET':
      prod_id = request.GET['prod_id']
      c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
      c.delete()
      amount = 0
      shipping_amount = 100
      cart_product = [p for p in Cart.objects.all() if p.user==request.user]
      for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount  
            totalamount = amount + shipping_amount
      data = {
         'amount': amount,
         'totalamount': totalamount
      }
      return JsonResponse(data)


"""
# url 
""" 
    path('pluscart/', views.plus_cart),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('removecart/', views.remove_cart),
"""