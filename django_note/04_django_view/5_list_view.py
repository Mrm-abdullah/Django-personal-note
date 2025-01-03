#   kono ajta model ar object guloke contex akare diye de/

# ----------------- view ----------#
""" from .models import post, Subject, Class_in
from django.views.generic import ListView

class PostListView(ListView):
    template_name='index.html'

    # model = post
    queryset=post.objects.filter(user=1)

    # queryset=post.objects.all()
    context_object_name='posts'
    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        # posts=context.get('object_list')
        # context['posts']= posts
        context['msg']= 'this is post list'
        # context['subjects']= Subject.objects.all()
        # context['classes']= Class_in.objects.all()
        return context """

# ---------------- urls -------------------#
""" from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('',views.PostListView.as_view(),name="postlist"),

] """

# --------------html --------------#
""" {{msg}} <br>
{% comment %} {% for p in object_list %} {% endcomment %} 
{% for p in posts %}
{{p.title}} by {{p.user.username}} <br>
{% comment %} <img src="/media/{{p.image}}" alt=""> {% endcomment %}

<hr>
{% endfor %}
 """