#   category.py

""" 
from django import template
from store.models import Category

register = template.Library()


@register.filter
def category(user):
    if user.is_authenticated:
        cat = Category.objects.filter(parent=None)
        return cat
"""

 # html

""" 
{% load category %}

{% for cat in request.user|category %}
{% if not cat.children.all %}
<li class="item-lead"><a href="#">{{cat.name}}</a></li>
{% else %}
<li class="item-lead"><a href="#">{{cat.name}}</a>
    <ul>
        {% for subcategory in cat.children.all %}
        <li>
            <a href="#">{{subcategory.name}}</a>
        </li>
        {% endfor %}
    </ul>
</li>
{% endif %}
{% endfor %}
"""
 ###########################################################################
 ###########################################################################
 # model
""" 
 class MyLogo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'logo')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)

class MyFavicon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'logo')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)
"""
# template tags => logoinfo
""" 
from django import template
from home.models import MyLogo, MyFavicon
register = template.Library()

@register.filter
def logo(request):
    if request:
        logo = MyLogo.objects.filter(is_active=True).order_by('-id').first()
        return logo.image.url

    else:
        logo = MyLogo.objects.filter(is_active=True).order_by('-id').first()
        return logo.image.url

@register.filter
def favicon(user):
    if user.is_authenticated:
        logo = MyFavicon.objects.filter( is_active=True).order_by('-id').first()
        return logo.image.url
"""
# html
""" 
{% load logoInfo %}
{{ request.user | favicon }}
{% static '{{request.user|favicon}}' %}
{{ request.user | logo }}
"""