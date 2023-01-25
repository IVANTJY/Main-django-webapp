from django.db import models

# Create your models here.


# declare a new model with a name "GeeksModel"
class RegisteredUser(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    phoneNum = models.CharField(max_length = 20, null = True, blank = True)
    password = models.CharField(max_length=30)
    
    
# class GeeksModel(models.Model):
#     title = models.CharField(max_length = 200)
#     content = models.TextField(max_length = 200, null = True, blank = True)
#     views = models.IntegerField()
#     url = models.URLField(max_length = 200)
#     image = models.ImageField()


# class RegisteredUser(models.Model):
#     name = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name

# class Machines(models.Model):
#     todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)
#     complete = models.BooleanField()
    
#     def __str__(self):
#         return self.text