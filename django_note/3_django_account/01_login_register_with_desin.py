# forms.py
""" 
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


#Registration
class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}


#Login
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control' }))

    password = forms.CharField(label=_('Password'),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current_password','class':'form-control' }))

# login url


from .forms import LoginForm
from django.contrib.auth import views as auth_views

    path('accounts/login/',auth_views.LoginView.as_view(template_name='Shop/login.html', authentication_form=LoginForm) , name='login'),
#logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),


LOGIN_REDIRECT_URL = '/profile/' # settings a dao
"""

# VIEWS 
""" 

class CustomerRegistrationView(View):
  def get(self,request):
     form = CustomerRegistrationForm()
     return render(request, 'Shop/customerregistration.html', {'form':form})
  
  def post(self,request):
     form = CustomerRegistrationForm(request.POST)
     if form.is_valid():
        messages.success(request,'Congratulations registration done.')
        form.save()
     return render(request, 'Shop/customerregistration.html', {'form':form})
"""
# hml
""" 
<form action="" method="post" novalidate class="shadow p-5">
    {% if messages %}
    {% for message in messages %}
    <p {% if message.tags %} class="alert alert-{{message.tags}} mb-5" {% endif %} >{{message}}</p>
    {% endfor %}
    {% endif %}

    {% csrf_token %}
    {% for fm in form %}
    <div class="form-group mb-3">
        {{fm.label_tag}}{{fm}} <small class="text-danger">{{fm.errors|striptags}}</small>
    </div>
    {% endfor %}
    <br>
    <input type="submit" class="btn btn-primary" value="Submit">
    <br>
    <div class="text-center text-primary fw-bold"><small>Existing User ? <a href="{% url 'login' %}"
                class="text-danger">Login Now</a> </small></div>
    {% if form.non_field_errors %}
    {% for error in form.non_field_errors %}
    <p class="alert alert-danger my-3">{{error}}</p>
    {% endfor %}
    {% endif %}
</form>
"""
