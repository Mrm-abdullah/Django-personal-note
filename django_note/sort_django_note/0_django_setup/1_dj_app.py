# create a django app
""" 
django-admin startapp (app name)
python manage.py startapp (app name)
"""

# INSTALLED_APPS setting.py
""" 
INSTALLED_APPS = [
    ...
    'app name',
    'members.apps.MembersConfig'
]
"""

#---------------------------------view -----------------------------#

                # return redirect('/result/'+passw)
                # return redirect('account:recherge3', pk=profile.pk)

# views.py>>>>>>>>> class
"""
from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        return render(request,'home/index.html')
"""


#--------------------app urls --------------------#

# create app>urls.py and
# link koro main>urls ar sathe add path
""" 
from django.urls import path, include 
urlpatterns = [
    ...
    path('', include('account.urls')),
]
"""

# app/urls.py>>>>>>>>> class
"""
from account  import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]
"""
