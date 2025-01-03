# ------------------ view ------------#

# from django.views import View
# aiquest
""" 
class ProductView(View):
    def get(self, request):
     gentspants = Product.objects.filter(category='GP')
     contex={
          'gentspants': gentspants,
     }
     return render(request, 'Shop/home.html', contex)
# path('', views.ProductView.as_view(), name='home'),
"""
"""
class ProductdetailView(View):
    def get(self, request, pk):
     product = Product.objects.get(pk=pk)
     contex={
          'product': gentproductspants,
     }
     return render(request, 'Shop/productdetail.html', contex)
# path('product-detail/<int:pk>', views.ProductdetailView.as_view(), name='product-detail'),
"""
#menual filter view
""" 
class LehengaView(View):
     def get(self, request, data=None):
          if data == None:
               lehenggas = Product.objects.filter(category='L')
          elif data == 'hello' or data == 'hi':
               lehenggas = Product.objects.filter(category='L').filter(brand=data)
          elif data == 'bellow':
               lehenggas = Product.objects.filter(category='L').filter(discountprice__lt=550)
          elif data == 'above':
               lehenggas = Product.objects.filter(category='L').filter(discountprice__gt=550)
          contex = {
               'lehenggas':lehenggas, 
          }
          return render(request, 'Shop/lehenga.html', contex)

    # path('lehengaview/', views.LehengaView.as_view(), name='LehengaView'),
    # path('lehengaview/<slug:data>', views.LehengaView.as_view(), name='Lehengaitem'),
"""
##########
"""    
class ContactView(View):
    form_class=contactForm
    template_name  = 'index.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form} )
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form} )
 """

# ------------------ forms.py ------------#
""" 
from django import forms
from .models import Members

class contactForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = '__all__'
class contactFormTwo(forms.ModelForm):
    class Meta:
        model = Members
        fields = '__all__'
 """

# ------------------ urls ------------#
""" from django.urls import path
from . import views
from .forms import contactFormTwo

app_name = 'account'
urlpatterns = [
    path('', views.ContactView.as_view(), name='home'),
    path('h/', views.ContactView.as_view(form_class=contactFormTwo, template_name  = 'indexx.html'), name='home'),
]
 """