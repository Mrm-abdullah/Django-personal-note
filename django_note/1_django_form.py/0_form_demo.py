# forms.py

""" 
from django import forms

class contactForm(forms.Form):
    email = forms.Emailfield(label= "Your email", initial='abc@g.com', disabled=True, validators=[validators.MaxLengthValidator(30)]) #= anb-30 & 34
    number = forms.CharField(max_length=100, label= "Your number")
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20, error_messages={'reuired' : 'Enter Your Password'})
    textarea = forms.CharField(widget=forms.Textarea(attrs={'rows' : 4, 'cols' : 40}))
    checkbox = forms.CharField(widget=forms.CheckboxInput)
    file = forms.CharField(widget=forms.FileInput())
    word = forms.CharField(help_text="describe about word")
    Ram = forms.ImageField(min_value=4, max_value=12)
    ssd = forms.DecimalField(min_value=1, max_value=50, max_digits=3, decimal_places=2)
    youtube = forms.BooleanField(label='subcribe the youtube')

    def clean(self): # duit pass akoi kia dekhar jonno
        cleaned_data = super().clean()
        password_match = self.cleaned_data['password']
        re_password_match = self.cleaned_data['re_password']
        if password_match != re_password_match:
            raise forms.ValidationError('password does not match')

    def clean_password(self): # mon moto vaidtion korar jonno
        password_validation = self.cleaned_data['password']
        if len(password_validation)<4:
            raise forms.ValidationError('Enter ypor correct password')
        return password_validation
"""
# email = forms.Emailfield(initial="abn@gmail.com ") # initial value, ja user poriborton korte parbe.
# {{form.email.value}} #== initial value ki ace ta dekhar jonno. html a.


# ------------- view-----------------#

""" 
from django.shortcuts import render
from .forms import contactForm
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    if request.method == "POST" or request.method == "post":
        form = contactForm(request.POST)
        if form.is_valid():
            print(form)
            print(form.cleaned_data)
            return HttpResponseRedirect('/url/')
    else:
        form = contactForm(auto_id='best_%s', label_suffix=' $') # auto_id='True/False'
        form.order_fields(field_order=['email', 'password', 'number']) # ordering korar jonno ==== ANB- 29
    return render(request,'index.html', {'form':form})

"""
# ---------html ------------#
""" 
<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{form}}
    {{form.as_p}}
    {{form.as_ul}} 
    <hr>

    {{form.email.label_tag}} # akta field paoyar jonno
    {{form.email}} <br>
    <hr>

    {% for x in form.hidden_fields %} 
    {{ hidden }}
    {% for x in form.visible_fields %} 
    {% for x in form %} 
    {{x.label_tag}}
    {{x}} <br>
    {{x.errors|striptags}} <br>
    {% endfor %}

    <button type="submit" class="btn btn-primary">Submit</button>
</form> """