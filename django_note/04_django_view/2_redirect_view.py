# ----------------- view -------#
""" 
from django.views.generic import RedirectView
class exredirect(RedirectView):
    url = 'https://www.youtube.com/'


"""


# ----------------- urls -------#
""" from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'account'
urlpatterns = [
    
    path('redirectView/', RedirectView.as_view(url="/templateView"), name='redirectView'),
    path('exredirectView/', views.exredirect.as_view(), name='exredirectView'),

]
"""