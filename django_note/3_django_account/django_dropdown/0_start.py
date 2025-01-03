#----------------- models -------------#
""" 
from django.db import models

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Division(models.Model):
    name=models.CharField(max_length=100)
    country=models.ForeignKey(Country,on_delete=models.CASCADE, related_name='divisions')
    def __str__(self):
        return self.name
class District(models.Model):
    name=models.CharField(max_length=100)
    division=models.ForeignKey(Division,on_delete=models.CASCADE, related_name='districts')
    def __str__(self):
        return self.name
class SubDistrict(models.Model):
    name=models.CharField(max_length=100)
    district=models.ForeignKey(District,on_delete=models.CASCADE, related_name='subdistricts')
    def __str__(self):
        return self.name

# class Address(models.Model):
#     addressOf=models.CharField(max_length=100)
#     country=models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='country_set')
#     division=models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True, related_name='division_set')
#     district=models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='district_set')
#     subdistrict=models.ForeignKey(SubDistrict, on_delete=models.SET_NULL, null=True, blank=True, related_name='subdistrict_set')
#     def __str__(self):
#         return self.addressOf
"""

#----------------- admin -------------#
""" 
from django.contrib import admin
from .models import *
# Register your models here.
# class AddressAdmin(admin.ModelAdmin):    
#     list_display = ['addressOf','country']
#     class Media:
#         js = ("myapp/selectajax.js",)
# admin.site.register(Address,AddressAdmin)
admin.site.register([Country,Division,District,SubDistrict])

 """

#----------------- urls -------------#
""" 
from django.urls import path
from . import views


urlpatterns = [
    path('drop/',views.indexview,name="drop"),

] """
#----------------- view -------------#
""" 
from django.shortcuts import render
from .models import *
import json

# Create your views here.
def indexview(request):
    country=Country.objects.all().order_by('name')
    country_list=list(country.values('name','id'))
    country_list=json.dumps(country_list)

    division=Division.objects.all().order_by('name')
    division_list=list(division.values('name','country_id','id'))
    division_list=json.dumps(division_list)

    district=District.objects.all().order_by('name')
    district_list=list(district.values('name','division_id','id'))
    district_list=json.dumps(district_list)

    subdistrict=SubDistrict.objects.all().order_by('name')
    subdistrict_list=list(subdistrict.values('name','district_id','id'))
    subdistrict_list=json.dumps(subdistrict_list)

    context={
        "country_list":country_list,
        "division_list":division_list,
        "district_list":district_list,
        "subdistrict_list":subdistrict_list,
    }
    return render(request, 'drop.html',context) """

#----------------- html -------------#
""" 

<div class="container" id="app">
    <div class="row">
    <form action="" method="post">
        <div class="col">
            <select class="form-control form-control-sm  mx-2  my-2" v-model="country_selected" @change="loadDiv($event)">
                <option v-for="(p,i) in country" :key="i" :value="p.id">[[p.name]]</option>
            </select>
        </div>
        <div class="col">
            <select class="form-control form-control-sm mx-2  my-2"  v-model="division_selected" @change="loadDis($event)">
             <option v-for="(p,i) in div" :key="i" :value="p.id">[[p.name]]</option>

            </select>
        </div>
        <div class="col">
            <select class="form-control form-control-sm  mx-2  my-2" v-model="district_selected" @change="loadSub($event)">
                <option v-for="(p,i) in dis" :key="i" :value="p.id">[[p.name]]</option>
            </select>
        </div>
        <div class="col">
            <select class="form-control form-control-sm  mx-2 my-2">
                <option v-for="(p,i) in sub" :key="i" :value="p.id">[[p.name]]</option>
            </select>
        </div>
        <button type="submit">Submit</button>
    </form>
    </div>
</div>

    

<script>
    
var app = new Vue({
    el:"#app",
    delimiters: ['[[', ']]'],
    data:{
        country: {{country_list|safe}},
        division: {{division_list|safe}},
        district: {{district_list|safe}},
        subdistrict: {{subdistrict_list|safe}},

        country_selected: "",
        div:[],
        division_selected: "",
        dis:[],
        district_selected: "",
        sub:[],


    },
    mounted: function(){
        console.log("Mounted");  
    },
    methods:{ 
        loadDiv(){
            this.sub=[];
            this.dis=[];
            this.div=[];
            for(let i=0; i< this.division.length; i++){
                if(this.country_selected==this.division[i].country_id){
                    this.div.push({name:this.division[i].name,id:this.division[i].id});
                }
            }
        },
        loadDis(){
            this.sub=[];
            this.dis=[];
            for(let i=0; i< this.district.length; i++){
                if(this.division_selected==this.district[i].division_id){
                    this.dis.push({name:this.district[i].name,id:this.district[i].id});
                }
            }
        },
        loadSub(){
            this.sub=[];
            for(let i=0; i< this.subdistrict.length; i++){
                if(this.district_selected==this.subdistrict[i].district_id){
                    this.sub.push({name:this.subdistrict[i].name,id:this.subdistrict[i].id});
                }
            }
        },

    },
})
</script>
</body>
</html> """