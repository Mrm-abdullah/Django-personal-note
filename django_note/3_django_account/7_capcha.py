""" 
pip install django-simple-captcha Pillow
"""
# main url
# path('captcha/', include('captcha.urls')),

# setting
""" 
  INSTALLED_APPS = [
    ...
    'captcha',
]

CAPTCHA_FONT_SIZE = 30
CAPTCHA_LENGTH = 6
CAPTCHA_IMAGE_SIZE = (120, 40)
"""

# ধাপ ২:
""" 
python manage.py makemigrations captcha
python manage.py migrate
 
"""
# ধাপ ২: view
""" 
from django.shortcuts import render
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore

def your_view(request):
    if request.method == 'POST':
        captcha_key = request.POST.get('captcha_1', '')
        captcha_value = request.POST.get('captcha_0', '')
        if CaptchaStore.objects.filter(response=captcha_value, hashkey=captcha_key).exists():
            # ক্যাপচা সঠিক
            # আপনার প্রয়োজনীয় লজিক এখানে সম্পাদন করুন
            return render(request, 'success.html')
        else:
            # ক্যাপচা ভুল
            error_message = 'Invalid captcha. Please try again.'
            return render(request, 'your_template.html', {'error_message': error_message})
    else:
        new_captcha = CaptchaStore.generate_key()
        captcha_image = captcha_image_url(new_captcha)
        return render(request, 'your_template.html', {'captcha_image': captcha_image, 'captcha_key': new_captcha})
  """
# ধাপ ৩: URL কনফিগারেশন

""" 
from captcha.views import captcha_refresh

urlpatterns = [
    # অন্যান্য URL
    path('captcha/refresh/', captcha_refresh, name='captcha_refresh'),
]
 """
# ধাপ ৪: forms.py

""" 
from captcha.fields import CaptchaField
class YourForm(forms.Form):
    captcha = CaptchaField()
 """
# ধাপ ৫: template

""" 
<form>
  {% csrf_token %}
  {{ form.as_p }}
  <img src="{{ captcha.image_url }}" alt="captcha">
  <input type="text" name="captcha_0">
  <input type="hidden" name="captcha_1" value="{{ captcha.key }}">
  <button type="submit">Submit</button>
</form>

"""
""" <form method="post" action="">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
 """