# models 
""" 
class Product(models.Model):
    mainimage = models.ImageField(upload_to='products')
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]
 """
# admin.py
""" 
from django.contrib import admin
from store.models import Category, Product
admin.site.register(Category)
admin.site.register(Product)
"""
# view list view
""" 
from django.shortcuts import render
from store.models import Category, Product
from django.views.generic import ListView, DeleteView

# class base list view
class Home(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name='products'
"""
####################### # product- details
# function base detail view
"""     
# item.get_product_url

def product_details(request, pk):
    item = Product.objects.get(id=pk)
    photos = ProductImages.objects.filter(product=item).order_by('-created')
    context = {
        'item': item,
        'photos': photos,
    }
    return render(request, 'store/product.html', context)
"""
# class base detail view
""" 
class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImages.objects.filter(product=self.object.id)
        return context
"""
#######################################################
# slugify
# slug base url ----- https://www.youtube.com/watch?v=FnIRbGLZUeA&list=PLxQ9RfumYrxYfJKbHYmU8f5Zr1fUkUUOF&index=9
""" 
from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductDetail, name='product-detail'),
]
"""
# html---- home
""" 
{% for product in products %}
{% url 'store:product-detail' pk=product.pk %}         
<img src="{{product.mainimage.url}}">
{{product.category}}
{{product.name}}
${{product.price}}

{% if product.old_price %}
    ${{product.old_price}}
{% endif %}
{% endfor %}
"""
# model
""" 
class Product(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_des = models.CharField(max_length=255, verbose_name='Short Descriptions')
    description = models.TextField(max_length=1000, verbose_name='Descriptions')
    image = models.ImageField(upload_to='products', default='demo/demo.jpg', blank=False, null=False)
    price = models.FloatField()
    old_price = models.FloatField(default=0.00, blank=True, null=True)
    is_stock = models.BooleanField(default=True)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

    def get_product_url(self):
        return reverse('store:product-details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
"""
# view 
""" same """
