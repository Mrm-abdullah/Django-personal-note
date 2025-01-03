#  wallet model
""" 
class Payment_Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rechareamount')
    amount = models.IntegerField( null=True, blank=True)
    sender_number = models.CharField( max_length=16,null=True, blank=True)
    bank_name = models.ForeignKey(Bank_Name, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_id = models.CharField(max_length=20, null=True, blank=True)
    succes_requ = models.BooleanField(default=False)
    succes_payment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.succes_payment:
            wallet = User_Profile.objects.get(user=self.user)
            wallet.balance += self.amount
            wallet.save()
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.user.username}'s request"


from django.db.models.signals import post_save
from django.dispatch import receiver
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    full_name = models.CharField( max_length=150, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        User_Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
 """
# wallet request view
""" 
def Payment_request_1(request):
    if request.user.is_authenticated:
        if request.method == 'POST' or request.method == 'post':
            user = request.user
            amount = request.POST['reamount']
            amount = Payment_Request(user=user,amount=amount)
            amount.save()
            requ_id = Payment_Request.objects.filter(user=user).order_by('-id').first()
            return redirect('account:recherge2',pk=requ_id.pk)
        else:
            reammount = Recharge_Routine.objects.all().order_by('amount')
            contex={
            'reammount': reammount,
            }
            return render(request,'account/recharge.html', contex)
    else:
        return redirect('account:login')

def Payment_request_2(request, pk):
    if request.user.is_authenticated:
        profile = get_object_or_404(Payment_Request, pk=pk)
        bank = Bank_Name.objects.all()
        logo = MyLogo.objects.filter(is_active=True).order_by('-id').first()

        if request.method == 'POST':
            profile.sender_number = request.POST['sender_number']
            profiles = request.POST['bank_name']
            profilee = int(profiles)
            banks = Bank_Name.objects.get(id=profilee)
            profile.bank_name = banks
            profile.save()
            return redirect('account:recherge3', pk=profile.pk)
        contex={
            'profile': profile,
            'bank': bank,
            'logo': logo,
        }
        return render(request, 'account/recherge2.html',contex)
    else:
        return redirect('account:login')

def Payment_request_3(request, pk):
    if request.user.is_authenticated:
        profile = get_object_or_404(Payment_Request, pk=pk)
        bankinfo = Bank_Info.objects.filter(is_active=True, bank_name=profile.bank_name)
        logo = MyLogo.objects.filter(is_active=True).order_by('-id').first()
        
        if request.method == 'POST':
            profile.transaction_id = request.POST['transaction_id']
            profile.succes_requ = True
            profile.save()
            return redirect('account:profile')
        contex={
            'profile': profile,
            'logo': logo,
            'bankinfo': bankinfo,
        }
        return render(request, 'account/recherge3.html',contex)
    else:
        return redirect('account:login')
 """
# wallet url
""" 
from . import views
from django.urls import path

app_name = 'account'
urlpatterns = [
    path('recherge1/',views.Payment_request_1,name="recherge1"),
    path('recherge2/<int:pk>/',views.Payment_request_2,name="recherge2"),
    path('recherge3/<int:pk>/',views.Payment_request_3,name="recherge3"),
]
"""
# admin.py
""" 
from django.contrib import admin
from django.db import models
from .models import Payment_Request,User_Profile

class Payment_admin(admin.ModelAdmin):
    list_display = ('id', 'user','amount', 'sender_number', 'bank_name', 'transaction_id', 'succes_requ', 'succes_payment')
    list_filter = ('succes_payment',)
    actions = ['approve_requests']

    def approve_requests(self, request, queryset):
        queryset.update(succes_payment=True)

admin.site.register(User_Profile)
admin.site.register(Payment_Request,Payment_admin)
 """

