# ---------- view -------------#
""" from django.views.generic import DeleteView
class PostDeleteView(DeleteView):
    model=post
    template_name="delete.html"
    success_url=reverse_lazy('home:postlist') """

# ---------------- html --------------------#
""" 
{% if request.user == object.user %}
<a href="/delete/{{object.id}}/"> Delete</a> <br />
{% endif %}  """

""" 
<form method="post">
{% csrf_token %}
Are you sure to Delete this post?

<button type="submit">Yes</button>
</form> """

# ---------------- urls --------------- #
""" 
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('',views.PostListView.as_view(),name="postlist"),
    path('postdetail/<int:pk>/',views.PostDetailView.as_view(),name="postdetail"),
    path('edit/<int:pk>/',views.PostEditView.as_view(),name="edit"),
    path('delete/<int:pk>/',views.PostDeleteView.as_view(),name="delete"),

] """