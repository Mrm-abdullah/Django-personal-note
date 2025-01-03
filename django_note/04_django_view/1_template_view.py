# ----------------- view -------#
""" 
from django.views.generic import TemplateView

class templateView(TemplateView):
    template_name= 'course/succ.html'

class HomeView(TemplateView):
    template_name= 'index.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['msg']="Welcome to our website"
        context['msg2']="Welcome to our website Again"
        return context
"""


# ----------------- urls -------#
""" from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'account'
urlpatterns = [
    path('',views.HomeView.as_view(), name="homeview"),
    # path('',TemplateView.as_view(template_name='index.html'), name="homeview"),

]
"""