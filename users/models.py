from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # phone_number = models.CharField(max_length=30,default='78900')
    # institute = models.CharField(max_length=30,default='jin')
    
    def __str__(self):
        return f'{self.user.username} Profile'
      

    def save(self, ** kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
# creating user profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    phone_number=models.IntegerField(default='0')
    institute=models.CharField(max_length=30,default='Not provided')
    degree=models.CharField(max_length=30,default='Not provided')
    Number_of_publications=models.IntegerField(default='0')
    funding=models.IntegerField(max_length=30,default='4 m')
    type_of_funding=models.CharField(max_length=30,default='private')
    Number_of_patents=models.IntegerField(max_length=30,default='nil')
    license=models.CharField(max_length=30,default='nil')
    Project_title = models.CharField(max_length=100,default='No projects have been added')
    Project_details = models.CharField(max_length=100,default='No project details have been added')
    
    def __str__(self):
        return self.user.username