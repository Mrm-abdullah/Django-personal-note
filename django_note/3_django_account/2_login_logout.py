# login logout last anb ##########################
""" 
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
# html
""" 
{% for fm in form %}
<div class="form-group mb-3">
    {{fm.label_tag}}{{fm}} <small class="text-danger">{{fm.errors|striptags}}</small>
</div>
{% endfor %}

{% if form.non_field_errors %}
{% for error in form.non_field_errors %}
<p class='alert alert-danger'>{{error}}</p>
{% endfor %}
{% endif %}
"""

# ----------------------  menual login ------------------#
#views.py
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate 

def customerlogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST' or request.method == 'post':
            username = request.POST.get('username')
            password = request.POST.get('password')
            customer = authenticate(request, username=username, password=password)
            if customer is not None:
                login(request, customer)
                return HttpResponse('you are login successfully')
            else:
                return HttpResponse('404')
    return render(request, 'account/login.html')
"""
# ---------------------- auto login ------------------#
#views.py
""" 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
def loginuser(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                # return redirect('homeview')
                return render(request, 'index.html')
            else:
                messages.error(request, 'Invalid Username or password')
    else:
        form=AuthenticationForm()
    return render(request, 'login.html',{'form':form})
"""
            # logout
"""
def logoutuser(request):
    logout(request)
    messages.success(request, "successfully logged out!")
    # return redirect('homeview')
    return render(request, 'index.html')
"""
            # Auto logout
"""
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]
SESSION_EXPIRE_SECONDS = 300 # 5 minutes
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_TIMEOUT_REDIRECT = 'account:logout'
"""

# login.html
""" 
{% if form.non_field_errors %}
{% for x in form.non_field_errors %} 
<p> {{x}} </p>
{% endfor %}
{% endif %}

<form action="" method="post" enctype="multipart/form-data">
{% csrf_token %}
{% for x in form %} 
{{x.label_tag}}
{{x}} <br><br>
{% endfor %}
<button type="submit">Login</button>
</form>
"""
                      # login logout html menu start
""" 
<ul> 
  {% if user.is_authenticated %}
    <li class="nav-item dropdown">
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
        <a class="dropdown-item" href="/logout/">Logout</a>
        </div>
    </li>
    {% else %}
    <li class="nav-item">
        <a class="btn btn-primary ml-2" href="/login/">Login</a>
    </li>
    {% endif %}
</ul>
"""