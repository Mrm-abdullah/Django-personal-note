
######################################################################
                        # default signup
######################################################################
# view
""" ---- anb-39
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    if request.method == "POST" or request.method == "post":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request,'index.html', {'form':form})
 """
# forms.py>>>>>>>>>> 
"""
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


"""
# views.py
"""
from django.shortcuts import render
from django.http import HttpResponse
from account.forms import RegistrationForm

def register(request):
    if request.user.is_authenticated:
        return HttpResponse('you have authenticated')
    else:
        form = RegistrationForm()
        if request.method == 'POST' or request.method == 'post':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                return HttpResponse('youe account has been registered')
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)
"""

                                # menual signup start
# view.py
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST' or request.method == 'post':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            

            if password1==password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already Exists')
                    return redirect('/register/')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already Exists')
                    return redirect('/register/')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,password=password1, username=username)
                    user.save()
                    return redirect('/user_login/')
            else:
                messages.info(request, 'Password not matching')
                return redirect('/register/')
        else:
            return render(request, 'account/registration_form.html')
"""
                                # menual signup close
# html
# message
""" 
{% if messages %}
<ul class="messagelist">{% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message|capfirst }}</li>
{% endfor %}</ul>
{% endif %}
"""
# error
""" 
{% if form.errors %}
{% for field in form %}
{% for err in field.errors %}
<p> {{err}} </p>
{% endfor %}
{% endfor %}
{% endif %}
      
<form>
    {% csrf_token %}
    {% for x in form %} 
    {{x.label_tag}}
    {{x}} <br>
    {% endfor %}
    <br>
    <input type="submit" value='Create an account'>
</form>
"""

#####################################################################################
#####################################################################################
#####################################################################################

# form
""" 
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


# Registration
class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

"""
#  views
""" 
from django.contrib import messages

class CustomerRegistrationView(View):
  def get(self, request):
     form = CustomerRegistrationForm()
     return render(request, 'Shop/customerregistration.html', {'form':form})
  
  def post(self, request):
     form = CustomerRegistrationForm(request.POST)
     if form.is_valid():
        messages.success(request,'Congratulations registration done.')
        form.save()
     return render(request, 'Shop/customerregistration.html', {'form':form})
"""
# url
""" 
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
"""
#  html
""" 
{% if messages %}
{% for message in messages %}
<p {% if message.tags %} class="alert alert-{{message.tags}} mb-5" {% endif %} >{{message}}</p>
{% endfor %}
{% endif %}

{% for fm in form %}
<div class="form-group mb-3">
    {{fm.label_tag}}{{fm}} <small class="text-danger">{{fm.errors|striptags}}</small>
</div>
{% endfor %}

{% if form.non_field_errors %}
{% for error in form.non_field_errors %}
<p class="alert alert-danger my-3">{{error}}</p>
{% endfor %}
{% endif %}
"""