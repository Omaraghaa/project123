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
    phone_number=models.CharField(max_length=30,default='0490453309')
    institute=models.CharField(max_length=30,default='kjc')
    degree=models.CharField(max_length=30,default='ms')
    publications=models.CharField(max_length=30,default='2')
    funding=models.CharField(max_length=30,default='4 m')
    type_of_funding=models.CharField(max_length=30,default='private')
    patent=models.CharField(max_length=30,default='nil')
    license=models.CharField(max_length=30,default='nil')
    
    
    def __str__(self):
        return self.user.username