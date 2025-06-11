# create model
""" from django.db import models

# Create your models here.
class Members(models.Model):
    email = models.CharField(max_length=255)
    number = models.CharField(max_length=11)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.number """

  # view

"""
from django.shortcuts import render
from .models import Members
# Create your views here.
def home(request):
    if request.method == "POST" or request.method == "post":
        email = request.POST['email']
        number = request.POST['number']
        image = request.FILES['image']
        password = request.POST['pass']
        obj = Members(email=email, number=number, password=password)
        obj.save()
    return render(request,'index.html')
 """
# html

""" <<form method="post">
    {% csrf_token %}
    <div class="mb-3">
      <input type="text" name="email" >
    </div>
    <div class="mb-3">
      <input type="text" name="number" >
    </div>
    <div class="mb-3">
      <input type="password" name="pass" >
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form> """
