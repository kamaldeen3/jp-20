from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Student(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='students'
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'