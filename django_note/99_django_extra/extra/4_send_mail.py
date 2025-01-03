# ------------- email -----------------------#
""" Enable IMAP
https://myaccount.google.com/lesssecureapps """

# ------------- setting -----------------------#
""" 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hmdfahad49@gmail.com'
EMAIL_HOST_PASSWORD = 'lonelyfahad'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'OTF Team <hmdfahad49@gmail.com>' """

# ------------- view vul-----------------------#
""" 
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def registration(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            # user=form.save(commit=False)
#             user.is_active=False
#             user.save()
            current_site=get_current_site(request)
            mail_subject='Activate Your Account'
            message=render_to_string('account.html',{
                'user':user,
                'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': default_token_generator.make_token(user),
            })
            send_mail=form.cleaned_data.get('email')
            email=EmailMessage(mail_subject,message, to=[send_mail])
            email.send()
            messages.success(request,'Successfully created account')
#             messages.info(request,'Activate Your account from the mail you provided')
            return redirect('home:login')
    else:
        form=SignUpForm()
    return render(request, 'signup.html',{'form':form}) """

# ------------- html -----------------------#
""" 
{% autoescape off %}  
Hi {{ user.username }},  
Please click on the link to confirm your registration,
http://{{ domain }}
{% comment %} {% url 'activate' uidb64=uid token=token %} {% endcomment %}
If you think, it's not you, then just ignore this email.  
{% endautoescape %} """