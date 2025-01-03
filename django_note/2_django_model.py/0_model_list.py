# from django.db import models
# from django.utils.timezone import now
# from PIL import Image #--------------- > image edit
# from django.utils.text import slugify
# from multiselectfield import MultiSelectField
# from django.contrib.auth.models import User

# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# @login_required
# @method_decorator(login_required, name='dispatch')
"""
class post(models.Model):
    CATEGORY = (
        ('teacher','teacher'),
        ('student','student'),
    )
    MEDIUM=(
        ('bangla','bangla'),
        ('English','English'),
        ('Urdu','Urdu'),
        ('Hindi','Hindi'),
        ('Arabic','Arabic'),
    )
    id = models.AutoField(primary_key=True)
    alt = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100)
    homeimage = HomeImg.objects.filter(is_active=True).order_by('-id').first()
    slug = models.CharField(max_length=100, default=title)
    email = models.EmailField()
    salary = models.FloatField()
    no = models.IntegerField()
    details = models.TextField()
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY )
    created_at = models.DateTimeField( default=now )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null= True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null= True)
    user = models.ManyToManyField(User)
    image = models.ImageField(default='default.png', upload_to='images')
    medium=MultiSelectField(max_length=100, max_choices=5, choices=MEDIUM, default='bangla')
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discountprice
"""

# -------- slugify, image edit ----------#
""" 
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail (output_size)
            img.save(self.image.path)
"""

# 2nd backend.py

""" 
from django.utils.text import slugify
import random
import string

# 1. Genarate a random string and presurve for later
# 2. If new slug match with existing slug then add that random string with the slug and return new_slug

def custom_slugify(the_title):
    new_chked_title = slugify(the_title)

    from home.models import Contents
    if Contents.objects.filter(slug=new_chked_title).first():
        random_string = ''.join(random.choices(string.ascii_letters, k=5))
        new_chked_title = f"{new_chked_title}-{random_string}"
        return new_chked_title

    return new_chked_title

from .backend import custom_slugify
def save(self, *args, **kwargs):
        self.slug = custom_slugify(self.title)  # Generate slug based on the 'title' field
        super().save(*args, **kwargs)
"""
#  --------view >for post show----------#
""" def home(request):
    posts = post.objects.all()
    return render(request,'index.html', {'postt': posts}) """

#  --------html >or post show----------#
"""
{% for p in postt %}
{{p.title}} <br>
<img src="{{p.image.url}}" alt=""> <br>
<img src="/media/{{p.image}}" alt=""> <br>
{% endfor %}
"""

# python -m pip install Pillow
# pip install django-multiselectfield
# setting >>> app
""" multiselectfield """
# return f"{self.user.username}'s profile"


""" 
    item_already_in_cart = False
    if request.user.is_authenticated:
       item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
    return render(request, 'Shop/productdetail.html',{'product': product, 'item_already_in_cart':item_already_in_cart})
"""

# import random

#         similar_product = Product.objects.filter(category=product.category)
#         similar_product_sample = random.sample(list(similar_product),4)

        # products = Product.objects.all().order_by('-id')
        # banners = Banner.objects.filter(is_active=True).order_by('-id')[0:3]