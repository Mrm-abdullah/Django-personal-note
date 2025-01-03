# model
""" 
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to='product_gallery')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)
"""
# view
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
    # item.get_product_url

# def product_details(request, pk):
#     item = Product.objects.get(id=pk)
#     photos = ProductImages.objects.filter(product=item).order_by('-created')
#     context = {
#         'item': item,
#         'photos': photos,
#     }
#     return render(request, 'store/product.html', context)
# url
""" 
from django.contrib import admin
from store.models import Category, Product, ProductImages

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ('mainimage', 'name','category','preview_text','detail_text', 'price','old_price')

admin.site.register(Product, ProductAdmin)
"""

# html

