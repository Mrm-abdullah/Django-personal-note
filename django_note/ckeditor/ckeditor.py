# pip install django-ckeditor

# Add 'ckeditor' to your INSTALLED_APPS setting.

# python manage.py collectstatic


# model
""" 

from ckeditor.fields import RichTextField

class Ckeditor(models.Model):
    name = models.CharField(max_length=50)
    des = RichTextField()
    

    def __str__(self):
        return self.name
"""
# view
""" 
def Home(request):
    editor = Ckeditor.objects.all()
    contex={
        'editor' : editor,
    }
    return render(request,'index.html', contex)
"""

# html

""" 
    <form action="" method="post" enctype="multipart/form-data">
        {{form.media}}
    </form>
    
    {{editor}}
    {% for editor in editor %}
    <h1>{{editor.name}}</h1>
    <span> {{editor.des|safe}} </span>
    {% endfor %}
"""