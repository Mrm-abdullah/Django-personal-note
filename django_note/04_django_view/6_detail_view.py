# kono akta object ar details show koranor jonno

# -------------- view ----------------#
""" 
from django.views.generic import DetailView
class PostDetailView(DetailView):
    model=post
    template_name='indexx.html'
    # context_object_name = 'item' """

# ---------------- urls -------------#
""" from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('',views.PostListView.as_view(),name="postlist"),
    path('postdetail/<int:pk>/',views.PostDetailView.as_view(),name="postdetail"),

] """

# ---------------- html ------------------#
""" <a href="/postdetail/{{p.id}}/"> ...Details</a> """

""" 
<h1> post detail <h1>

Title = {{object.title}}<br />
Subject= {% for s in object.subject.all %}
{{s.name}},
{% endfor %} <br />
Class= {% for s in object.class_in.all %}
{{s.name}},
{% endfor %} <br />
category={{object.category}} <br />
 """