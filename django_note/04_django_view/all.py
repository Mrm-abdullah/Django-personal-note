# html

""" 
<h1> post detail <h1>

Title = {{object.title}}<br />

{% if request.user == object.user %}
<a href="/edit/{{object.id}}/"> Edit</a> <br />
<a href="/delete/{{object.id}}/"> Delete</a> <br />
{% comment %} <a href="/tuition/addphoto/{{object.id}}/"> Addphoto</a> <br />
<a href="/tuition/delete/{{object.id}}/">Delete</a> <br /> {% endcomment %}
{% endif %} 

Subject= {% for s in object.subject.all %}
{{s.name}},
{% endfor %} <br />
Class= {% for s in object.class_in.all %}
{{s.name}},
{% endfor %} <br />
category={{object.category}} <br />

Title={{object.title}} <br />
      by: {{object.user.username}} at: {{object.created_at}} <br /> """

###############################################

""" 
 """