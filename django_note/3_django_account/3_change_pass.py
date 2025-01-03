# ---------------- view ----------------#
""" 
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash

def change_password(request):
    if request.method=="POST":
        form= PasswordChangeForm(data=request.POST, user=request.user)  
        if form.is_valid():
            # form.save()
            update_session_auth_hash(request, form.user)  
            messages.success(request, " Password has successfully Changed")
            return redirect('/')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html',{'form':form})
"""
# without old pass
# ---------------- view ----------------#
""" 
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash

def change_password(request):
    if request.method=="POST":
        form= SetPasswordForm(data=request.POST, user=request.user)  
        if form.is_valid():
            # form.save()
            update_session_auth_hash(request, form.user)  
            messages.success(request, " Password has successfully Changed")
            return redirect('/')
    else:
        form=SetPasswordForm(user=request.user)
    return render(request, 'change_pass.html',{'form':form})

"""
#             user change form
"""  
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm, SetPasswordForm, UserChangeForm    -----full dekho anb-42

form = UserChangeForm(instance = request.user)
"""

###########################################################################################
################################# abn course | django ar code kora #########################
###########################################################################################

# forms
""" 
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

#Password Change
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus': True, 'class':'form-control'}))

    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())


    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new password', 'class':'form-control'}))

#password reset 
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))

#set password form
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    
    new_password2 = forms.CharField(label=_('Confirm new password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))
 """

# views 
"""

"""
# url
""" 
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.contrib.auth import views as auth_views


    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='Shop/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='Shop/passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='Shop/password_reset.html', form_class=MyPasswordResetForm), name='password-reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Shop/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Shop/password_reset_complete.html'), name='password_reset_complete'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Shop/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
"""

# setting
""" 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # static ar nice

# akdom nice

#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ('mrmabdullah2024@gmail.com')
EMAIL_HOST_PASSWORD = ('hcujhgnlzxtgndrl')
"""

# goto gmail search two varification / app password