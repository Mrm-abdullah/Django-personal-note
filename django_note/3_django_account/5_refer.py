# referrel MOdel
""" 
from django.db import models
from django.contrib.auth.models import User

class Referral(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='referral')
    referral_code = models.CharField(max_length=10, unique=True)
    referred_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')
    referred_users = models.ManyToManyField(User, blank=True, related_name='referred_by')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.referral_code
"""
# reffer view
""" 
def Reffer_Registration(request, pk):
    idd = pk
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if Referral.objects.filter(referral_code=idd).exists():
            refferBy = Referral.objects.get(referral_code=idd)
        context = {
            'refferBy': refferBy,
        }
        return render(request, 'account/registation.html', context)

# register start
def Registration(request):
    if request.user.is_authenticated:
        return redirect('account:profile')
    else:
        if request.method == 'POST' or request.method == 'post':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                referred_by = request.POST['referred_by']
                if Referral.objects.filter(referral_code=referred_by).exists():
                    referred_by = Referral.objects.get(referral_code=referred_by)
                    user = form.save()

                    userr = User.objects.get(username=user)
                    refer_by = User.objects.get(id=referred_by.user_id)
                    referral = Referral(user=userr, referred_by=refer_by, referral_code=100000+userr.id)
                    referral.save()
                    referred_by.referred_users.add(userr)
                    return redirect('account:login')
                else:
                    messages.info(request, 'refer code invalid')
                    return redirect('account:registration')
        else:
            form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'account/registation.html', context)
    
 """
# refer url
""" 
from . import views
from django.urls import path

app_name = 'account'
urlpatterns = [
    path('registration/', views.Registration, name='registration'),
    path('refer/<int:pk>/', views.Reffer_Registration),
]
 """