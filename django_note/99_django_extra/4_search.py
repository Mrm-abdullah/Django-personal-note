# --------------------- view -----------#
""" 
from django.db.models import Q
def search(request):
    query=request.POST.get('search','')
    if query:
        queryset=(Q(title__icontains=query)) | (Q(details__icontains=query)) | (Q(medium__icontains=query)) | (Q(category__icontains=query)) | (Q(subject__name__icontains=query)) | (Q(class_in__name__icontains=query))
        results= post.objects.filter(queryset).distinct()
    else:
        results=[]
    context ={
        'results':results
    }
    return render(request, 'search.html',context)
"""
# ------------- html --------------#
""" 
<form method="post" action="/search/" class="form-inline my-2 my-lg-0">
  {% csrf_token %}
  <input class="form-control mr-sm-2" type="search" placeholder="Search" name="search" aria-label="Search" />
  <button class="btn btn-outline-primary my-2 my-sm-0" type="submit">
    Search
  </button>
</form> """


""" 
<h1 class="text-center">All Posts Are given below:</h1>
 {% for p in results %}
 {{p.title}} <br>
 by {{p.user.username}}  <br>
 <hr>
 Details: {{p.details}}
 <a href="/postdetail/{{p.id}}">...Read More</a> 
  
{% endfor %}
 """


###########################################
############     filter     ###############
###########################################

# --------------------- view -----------#
""" 
def filter(request):
    if request.method=="POST":
        subject=request.POST['subject']
        class_in=request.POST['class_in']
        salary_from=request.POST['salary_from']
        salary_to=request.POST['salary_to']
        available=request.POST['available']
        print(subject, class_in)
        if subject or class_in:
            queryset=(Q(subject__name__icontains=subject)) & (Q(class_in__name__icontains=class_in)) 
            results= post.objects.filter(queryset).distinct()
            if available:
                results=results.filter(available=True)
            if salary_from:
                results=results.filter(salary__gte=salary_from)
            if salary_to:
                results=results.filter(salary__lte=salary_to)
        else:
            results=[]

        context ={
        'results':results
        }
        return render(request, 'search.html',context)
"""

""" 
class PostListView(ListView):
    template_name='index.html'
    # model = post
    queryset=post.objects.filter(user=1)
    # queryset=post.objects.all()
    context_object_name='posts'
    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        # posts=context.get('object_list')
        # context['posts']= posts
        context['msg']= 'this is post list'
        context['subjects']= Subject.objects.all()
        context['classes']= Class_in.objects.all()
        return context
"""
# ------------- html --------------#
""" 
<form action="/filter/" method="post">
  {% csrf_token %}
  <div class="input-group mb-3">
    <select class="custom-select" id="inputGroupSelect02" name='subject'>
      <option></option>
      {% for i in subjects %}
      <option value="{{i}}">{{i}}</option>
      {% endfor %}
    </select>
    <div class="input-group-append">
      <label class="input-group-text" for="inputGroupSelect02">Subjects</label>
    </div>
  </div>
  <div>
    <div class="input-group mb-3">
      <select class="custom-select" id="inputGroupSelect02" name='class_in'>
        <option></option>
        {% for i in classes %}
        <option value="{{i}}">{{i}}</option>
        {% endfor %}
      </select>
      <div class="input-group-append">
        <label class="input-group-text" for="inputGroupSelect02">Class</label>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col">
      <div class="form-group">
        <label for="exampleFormControlInput1">Salary From</label>
        <input type="number" class="form-control" name="salary_from" id="exampleFormControlInput1">
      </div>
    </div>
    <div class="col">
      <div class="form-group">
        <label for="exampleFormControlInput1">Salary to</label>
        <input type="number" class="form-control" name="salary_to" id="exampleFormControlInput1">
      </div>
    </div>
  </div>

  <div class="form-group form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1" name="available">
    <label class="form-check-label" for="exampleCheck1">Only Available</label>
  </div>
  <button class="btn btn-primary" type="submit">Filter Posts</button>
</form>
"""
# search.html
""" 
<h1 class="text-center">All Posts Are given below:</h1>
 {% for p in results %}
 {{p.title}} <br>
 by {{p.user.username}}  <br>

 Details: {{p.details}}
 <a href="/postdetail/{{p.id}}">...Read More</a> 
   <hr>
{% endfor %}
"""