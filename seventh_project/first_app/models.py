from django.db import models

class StudentModel(models.Model):
    Roll = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Father_name = models.CharField(max_length=30)
    Address = models.TextField()
    
    
    def __str__(self):
        return f"{self.Name}:{self.Roll}"
