# ------------ model -------------#
from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.
class Members(models.Model):
    email = models.CharField(max_length=255)
    number = models.CharField(max_length=11)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.number

""" 
class Subject(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_total_post(self):
        return self.subject_set.all().count()
    def get_post_list(self):
        return self.subject_set.all()
class Class_in(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
"""

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
    user = models.OneToOneField(User,on_delete=models.CASCADE, blank=True, null= True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null= True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default=title)
    email = models.EmailField()
    no = models.IntegerField()
    details = models.TextField()
    avalable = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY )
    created_at = models.DateTimeField( default=now )
    image = models.ImageField(default='images/default.png', upload_to='images')
    medium=MultiSelectField(max_length=100, max_choices=5, choices=MEDIUM, default='bangla')
"""

"""    
    subject = models.ManyToManyField(Subject, related_name='subject_set')
    class_in = models.ManyToManyField(Class_in, related_name='class_set')
"""
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

# --------------------- form --------------#

""" from django import forms
from django.forms import widgets
from .models import  post

class contactForm(forms.ModelForm):
    class Meta:
        model = post
        exclude = ['user', 'slug', 'id', 'created_at', ]
        widgets={
            'class_in': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            }),
            'subject': forms.CheckboxSelectMultiple(attrs={
                'multiple': True,
            })
        }
"""

# --------------------- view --------------#
""" from django.shortcuts import render
from .forms import contactForm
# Create your views here.
def home(request):
    if request.method == "POST" or request.method == "post":
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            sub = form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in = form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
    else:
        form = contactForm()
    return render(request,'index.html', {'form':form})
"""
# ------------ admin ---------------#
"""
from django.contrib import admin
from .models import Members, post, Subject, Class_in

# Register your models here.
admin.site.register(Members)
admin.site.register(post)
admin.site.register(Subject)
admin.site.register(Class_in)
"""