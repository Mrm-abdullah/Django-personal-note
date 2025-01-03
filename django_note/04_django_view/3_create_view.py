# view 
""" 
class Add_Logos( LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model= MyLogo
    fields = ['image']
    template_name='dashboard/editimage.html'
    def get_success_url(self):
        id= self.object.id
        return reverse_lazy('dashboard:add_logo')
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.is_active = True
        return super().form_valid(form)
    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('account:login')
        else:
            return redirect('account:profile')
 """