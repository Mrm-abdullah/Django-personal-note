# anb course
# model
""" 
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
DIVISION_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Khulna','Khulna'),
    ('Barishal','Barishal'),
    ('Chattogram','Chattogram'),
    ('Mymenshing','Mymenshing'),
    ('Sylhet','Sylhet'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    division = models.CharField(choices=DIVISION_CHOICES, max_length=50)
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=50)
    villorroad = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    
    def __str__(self):
        return str(self.id)
 """

# form
""" 
from django import forms
from . models import Customer_Info
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer_Info
        fields = ['name','division','district','thana','villorroad','zipcode']
        
 class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer_Info
        fields = ['name','division','district','thana','villorroad','zipcode']
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'division':forms.Select(attrs={'class':'form-control'}),
            'district':forms.TextInput(attrs={'class':'form-control'}), 
            'thana':forms.TextInput(attrs={'class':'form-control'}), 
            'villorroad':forms.TextInput(attrs={'class':'form-control'}), 
            'zipcode':forms.NumberInput(attrs={'class':'form-control'})
        }
"""

# view
""" 
class ProfileView(View):
    def get(self, request):
      form = CustomerProfileForm
      contex={
          'form':form,
      }
      return render(request, 'Shop/profile.html', contex)
   
    def post(self, request):
          form = CustomerProfileForm(request.POST)
          if form.is_valid():
               usr = request.user
               name = form.cleaned_data['name']
               division = form.cleaned_data['division']
               district = form.cleaned_data['district']
               thana = form.cleaned_data['thana']
               villorroad = form.cleaned_data['villorroad']
               zipcode = form.cleaned_data['zipcode']
               reg = Customer_Info(user=usr,name=name, division=division,district=district, thana=thana, villorroad=villorroad, zipcode=zipcode)
               reg.save()
               messages.success(request, 'Congratulations! Profile Updated Successfully')
          contex={
               'form':form,
          }
          return render(request, 'Shop/profile.html',contex)

 """


# --------------- forms --------------#
"""  111111
from django import forms
from .models import Members

class contactForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = '__all__'
"""