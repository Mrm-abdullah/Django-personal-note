# view 

""" 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def dHome(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html')
    else:
        return redirect('account:login')


# demo

def emo_404(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/404.html')
    else:
        return redirect('account:login')

def Demo_blank(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/blank.html')
    else:
        return redirect('account:login')

def Demo_button(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/button.html')
    else:
        return redirect('account:login')

def Demo_chart(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/chart.html')
    else:
        return redirect('account:login')

def Demo_element(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/element.html')
    else:
        return redirect('account:login')

def Demo_form(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/form.html')
    else:
        return redirect('account:login')

def Demo_signin(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/signin.html')
    else:
        return redirect('account:login')

def Demo_signup(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/signup.html')
    else:
        return redirect('account:login')

def Demo_table(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/table.html')
    else:
        return redirect('account:login')

def Demo_typography(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/typography.html')
    else:
        return redirect('account:login')

def Demo_widget(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/demo/widget.html')
    else:
        return redirect('account:login')


 """



 #######################################     Url       #############################################

""" 

from . import views
from django.urls import path

app_name = 'dashboard'
urlpatterns = [
    path('dashboard/', views.dHome, name='dhome'),

    path('404/', views.emo_404, name='de404'),
    path('blank/', views.Demo_blank, name='deblank'),
    path('button/', views.Demo_button, name='debutton'),
    path('chart/', views.Demo_chart, name='dechart'),
    path('element/', views.Demo_element, name='deelement'),
    path('form/', views.Demo_form, name='deform'),
    path('signin/', views.Demo_signin, name='designin'),
    path('signup/', views.Demo_signup, name='designup'),
    path('table/', views.Demo_table, name='detable'),
    path('typography/', views.Demo_typography, name='detypography'),
    path('widget/', views.Demo_widget, name='dewidget'),
]
  """