from django.db import models
from django.contrib.auth.models import User
# one to one
class onetoone(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=50)
    teacher_reg = models.IntegerField()

# many to one
class manytoone(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_reg = models.IntegerField()
    course = models.CharField(max_length=50)

# many to many
class manytomany(models.Model):
    user = models.ManyToManyField(User)
    course_name = models.CharField(max_length=50)
    course_code = models.IntegerField()

    def course_teacher(self):
        return ",".join([str(p) for p in self.user.all()]) 
