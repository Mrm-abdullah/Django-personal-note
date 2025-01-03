# ---------- view -------------#
""" from django.views.generic import UpdateView
from django.urls import reverse_lazy

class PostEditView(UpdateView):
    model=post
    form_class=contactForm
    template_name='inde.html'
    def get_success_url(self):
        id= self.object.id
        return reverse_lazy('home:postdetail', kwargs={'pk':id}) """

# ---------------- html --------------------#
""" 
{% if request.user == object.user %}
<a href="/edit/{{object.id}}/"> Edit</a> <br />
{% endif %}  """

""" 
<form  method="post" enctype="multipart/form-data">
{% csrf_token %}
{{form}}
<button type="submit">Submit</button>
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

] """




###################### update advance

""" 

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Logo_Edit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= MyLogo
    fields = ['image']
    template_name='dashboard/editimage.html'
    def get_success_url(self):
        id= self.object.id
        return reverse_lazy('dashboard:edit_logo', kwargs={'pk':id})
    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('account:login')
        else:
            return redirect('account:profile')

 """