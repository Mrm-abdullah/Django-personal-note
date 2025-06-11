#                view

""" from django.shortcuts import render
from .models import *
import json

# Create your views here.
def village_Add(request):
    if request.method == "POST" or request.method == "post" and request.user.is_authenticated:
        ward = request.POST['wardforvill']
        ward = int(ward)
        village = request.POST['village']
        village_list = village.split(',')
        if Ward.objects.filter(id=ward).exists():
            ward = Ward.objects.get(id=ward)
            for vill in village_list:
                obj = Village(ward=ward, name=vill)
                obj.save()
        return redirect('account:profile')
 """


#    html

""" 
{% if user.is_authenticated %}
<h1 class="text-center"> This Is DropDown 2ndPage </h1>
<div class="container" id="appp">
    <div class="row">
    <form action="" method="post">
        {% csrf_token %}
        <div class="col">
            <select name="country" class="form-control form-control-sm  mx-2  my-2" >
                <option v-for="(p,i) in country" :key="i" :value="p.id">[[p.name]]</option>
            </select>
            
        </div>
        <div class="col">
            <input type="text" name="divi" >
        </div>
        <button type="submit">Submit</button>
    </form>
    </div>
</div>
{% endif %}
    
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

<script>
var app = new Vue({
    el:"#appp",
    delimiters: ['[[', ']]'],
    data:{
        country: {{country_list|safe}},
    },
    mounted: function(){

        console.log("Mounted");  
    },
    methods:{ 
        loadDiv(){
            this.div=[];
            for(let i=0; i< this.division.length; i++){
                if(this.country_selected==this.division[i].country_id){
                    this.div.push({name:this.division[i].name,id:this.division[i].id});
                }
            }
        },
    },
})
</script> """

########################################################################
######################## auto subcategory add start ####################
########################################################################
 # view
""" 
if request.method == "POST" or request.method == "post" and request.user.is_authenticated:
        start = request.POST['start']
        start = int(start)
        if 128249 == start:
            country = Country.objects.all().order_by('id')
            print(len(country))
            divi = "1,2,3,4,5,6,7,8,9"
            divi_list = divi.split(',')
            count = 1
            for coun in country:
                coun_id = coun.id
                if Country.objects.filter(id=coun_id).exists():
                    countri = Country.objects.get(id=coun_id)
                    for divissio in divi_list:
                        pass
                        obj = Division(country=countri, name=divissio)
                        obj.save()
                    if count%50==0:
                        time.sleep(3)
                        print(count,'ti compleat')
                        count = count +1
        return redirect('drop')
 """

# html
""" 
{% if user.is_authenticated %}
<h1 class="text-center"> This Is DropDown </h1>
<div class="container" id="appp">
    <div class="row">
    <form action="" method="post">
        {% csrf_token %}
        <div class="col">
            <input type="text" name="start" >
        </div>
        <button type="submit">Submit</button>
    </form>
    </div>
</div>
{% endif %} """

########################################################################
########################## auto subcategory add end  ###################
########################################################################