from django.db import models

# Create your models here.

class FootGraph(models.Model):
    per = models.CharField(max_length=120)
    league = models.CharField(max_length=120)
    position = models.CharField(max_length=120)

    def _str_(self):
        return self.per
    

 
