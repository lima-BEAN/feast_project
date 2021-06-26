from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
class Eater(models.Model):
    # first name, last name, email, password are all inheritied from User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=False)
    question_1 = models.CharField(max_length=200, null=False)
    answer_1 = models.CharField(max_length=200, null=False)
    question_2 = models.CharField(max_length=200, null=False)
    answer_2 = models.CharField(max_length=200, null=False)
    is_provider = models.BooleanField(null=False)
    # TODO: associate kitchen with provider if provider
    def __str__(self):
        return self.username
   
class Provider(Eater):
    def __str__(self):
        return self.username
"""

class Kitchen(models.Model):
 #   WORKING_DAYS = (
 #       ('Monday', 'Monday'), 
 #       ('Tuesday',  'Tuesday'),
 #       ('Wednesday', 'Wednesday'),
 #       ('Thursday', 'Thursday'),
 #       ('Friday', 'Friday'),
 #       ('Saturday', 'Saturday'),
 #       ('Sunday', 'Sunday'),
 #       )

    name = models.CharField(max_length=50, null=False)
#    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    open_time = models.TimeField(null=False)
    close_time = models.TimeField(null=False)
#    image = models.ImageField(upload_to='img', null=False)
    # TODO: working_days field 
    # TODO: Menu 

    def __str__(self):
        return self.name

"""
class Menu(models.Model):
    pass

class Food(models.Model):
    pass
"""
