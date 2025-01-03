# variable 
# =========== view
""" 
def home(request):
    return render(request,'home/index.html')

def home(request):
    return render(request,'home/index.html',{'nm' :'Abdullah' }) #html a {{nm}}

def home(request):   #poyojone abu noman basar 17
    students_list = students.objects.order_by('name')
    diction = {'students' : students_list}
    return render(request,'home/index.html',context=diction)
"""
# ============= variable html 
""" 
html a {{nm}}
"""
#####     filter html file a ======= google 50 ta filter ace practice koro
""" 
<h1>{{c | upper}}</h1>
<h1>{{c | lower}}</h1>
<h1>{{c | capfirst}}</h1>
<h1>{{c | length}}</h1>
"""
#========= date time
""" 
from datetime import datetime
def home(request):
    d = datetime.now()
    return render(request,'home/index.html',{'dt' : d })
"""
# ======= html 
""" 
 <h1> {{dt}} </h1>
 <h1> {{dt|date:'SHORT_DATE_FORMATE'}}</h1>
 <h1> {{dt|date:'DATE_FORMATE'}}</h1>
 <h1> {{dt|date:'TIME_FORMATE'}}</h1>
 {{dt|date:'d m y'}} <br>
 """
 #####     template tags
#  ===== html 
# if tag===
""" 
{% if dt %}
{{dt}}
{% elif dt%}
<h1>{{dt}}</h1>
{% else %}
ncncncn
{% endif %}
"""
# for tag
""" 
def home(request):
    d = ['a', 'b', 'c', 'd']
    return render(request,'home/index.html',{'dt' : d })


{{forloop.revcounter}}         #filter ar jonno
{{forloop.first}}              #filter ar jonno
{{forloop.last}}               #filter ar jonno

{% for x in dt %} {{forloop.counter}}              #filter ar jonno
{{x}} <br>
{% endfor %} 

{% for x in data reversed %}            #filter ar jonno

"""
##############   template base,html
# load static for>>> html template>>> call images and css
"""
{% load static %}
<img src=" /static/..... " >
<img src=" {% static 'image.png' %} " >
<link rel="stylesheet" href=" {% static 'css/style.css' %}">
"""

# ---------------------------------common likha ba extends -------------------#
"""
{% extends 'common_code/base.html' %}
{% block title %}{% endblock title %}
"""
#---------------- url tag ----------
"""
<li class="nav-item">
    <a class="nav-link active" aria-current="page" href="/">Home</a>
    <a class="nav-link active" aria-current="page" href="{% url 'home' %}">Home</a>
</li>
<li class="nav-item">
    <a class="nav-link" href="/studymart/">studu mart</a>
    <a class="nav-link" href="{% url 'studymart' %}">studu mart</a>
    <a class="nav-link" href="{% url 'home:studymart' %}">studu mart</a>
</li>
"""
# dtl

# {% block body %}{% endblock body %}

# {% extends 'base.html' %}
# {% block title %}{% endblock title %}
# {% block body %}{% endblock body %}

# <head>
#     {% load static %}