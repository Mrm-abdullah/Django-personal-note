# model
""" 
class UserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    bacth_no = models.IntegerField()
    textarea = models.CharField(max_length=500)
    password = models.CharField(max_length=50)
    re_password = models.CharField(max_length=50)
    checkbox = models.CharField(max_length=20)
    payment = models.DecimalField(max_digits=5, decimal_places=2)
    django = models.BooleanField()
"""
################ view
""" 
from .forms import Lean_Form, RegistrationForm
from django.http import HttpResponseRedirect

def Form_Show(request):
    if request.method == "POST" or request.method == "post":
        frm = Lean_Form(request.POST)
        if frm.is_valid():
            first_name = frm.cleaned_data ['first_name']
            last_name = frm.cleaned_data ['last_name']
            email = frm.cleaned_data ['email']
            bacth_no = frm.cleaned_data ['bacth_no']
            textarea =frm.cleaned_data ['textarea']
            password = frm.cleaned_data ['password']
            re_password = frm.cleaned_data ['re_password']
            checkbox = frm.cleaned_data ['checkbox']
            payment = frm.cleaned_data ['payment']
            django = frm.cleaned_data ['django']
            data = UserInfo(first_name=first_name, last_name=last_name, email=email,bacth_no=bacth_no,textarea=textarea,password=password, re_password=re_password,checkbox=checkbox,payment=payment,django=django)
            data.save()
            return HttpResponseRedirect('/form-succ/')
    else:
        frm = Lean_Form()
    return render(request,'course/form.html', {'form':frm})
"""
######### html
""" 
<form action="" method="POST" enctype="multipart/form-data>
    {% csrf_token %}
    {% for x in form %} 
    {{x.label_tag}} <br>
    {{x}} <br>
    {{x.errors|striptags}} <br>
    {% endfor %}
    <input type="submit" value="submit">
</form>
"""