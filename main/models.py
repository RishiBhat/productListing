from django.db import models

# Create your models here.



class Portfolio(models.Model):
    name=models.CharField(max_length=500)
    email =models.EmailField(max_length=500)
    city=models.CharField(max_length=400)
    address=models.TextField(default="")
    maritialstatus=models.CharField(max_length=50,
                                    choices = (
                                        ('Married', 'Married'),
                                        ('Unmarried', 'Unmarried'),
                                        ('Engaged', 'Engaged'),
                                    ),)
    contactno= models.PositiveBigIntegerField(default=0)
    image=models.ImageField(upload_to="images/", blank=True)
    biodata=models.FileField(upload_to="files/",blank=True )
    date_time= models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return self.name


