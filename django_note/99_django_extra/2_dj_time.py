# from datetime import datetime
# def home(request):
#     d = datetime.now()
#     return render(request,'home/index.html',{'dt' : d })

#  <h1> {{dt}} </h1>
#  <h1> {{dt|date:'SHORT_DATE_FORMATE'}}</h1>
#  <h1> {{dt|date:'DATE_FORMATE'}}</h1>
#  <h1> {{dt|date:'TIME_FORMATE'}}</h1>
#  {{dt|date:'d m y'}} <br>

# ---------- real time show -----------#



# ---------- naturaltime -----------------#
# setting >app
""" 
    'django.contrib.humanize',
"""

# ======= html 
""" 
 <h1> {{dt}} </h1>
 <h1> {{dt|date:'SHORT_DATE_FORMATE'}}</h1>
 <h1> {{dt|date:'DATE_FORMATE'}}</h1>
 <h1> {{dt|date:'TIME_FORMATE'}}</h1>
 {{dt|date:'d m y'}} <br>
"""

""" 
{% load humanize %}

Title={{object.title}} <br />
by: {{object.user.username}} at: {{object.created_at| naturaltime}} <br />
"""
# ------------- post detail html -----------------#
""" 
Title={{object.title}} <br />
by: {{object.user.username}} at: {{object.created_at}} <br />
"""
""" 
<li class="nav-item">
    <a class="nav-link" href="">{% now "h:i A" %}</a>
</li>
<li class="nav-item">
    <a class="nav-link" href="">{% now " D jS F Y" %}</a>
</li>
"""