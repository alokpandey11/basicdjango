# import the standard Django Model
# from built-in library
from django.db import models
  
# declare a new model with a name "GeeksModel"
class PersonModel(models.Model):
 
    # fields of the model
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name
