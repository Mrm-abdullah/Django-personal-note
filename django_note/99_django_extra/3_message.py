# --------------- view ------------------#
""" 
from django.contrib import messages

class ContactView(FormView):
    form_class=ContactForm
    template_name='contact.html'
    # success_url='/'
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Form successfully submitted!')
        messages.info(self.request, 'Form successfully submitted!')
        return super().form_valid(form)
"""

# ------------- html ----------------#
""" 
 {% for message in messages %}
  <div class="alert alert-{{message.tags}} alert-dismissible fade show" role="alert">
    {{message}}
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
  {% endfor %} """