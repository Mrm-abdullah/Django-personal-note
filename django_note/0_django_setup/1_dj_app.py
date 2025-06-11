# active env + go project folder
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
# views.py>>>>>>>>> funtion
""" 
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('ami ak bisal boka vai')

def home(request):
    z = 30+34
    return HttpResponse(z)
"""


# views.py>>>>>>>>> class
"""
from django.views import View
class jekononam(View):
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
    path('', include('app name.urls')),
]
"""

# app/urls.py>>>>>>>>> function
""" 
from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('', views.home, name='home'),
]
"""

# app/urls.py>>>>>>>>> class
"""
path('class/', views.jekononam.as_view(), name='home'),
"""

#  app url a
""" 

from django.conf.urls.static import static
from django.conf import settings


+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""