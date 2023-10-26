from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Existing imports...

class UserProfile(models.Model):
    #...
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) # One to one relationship with User model   

class FileUpload(models.Model):
    #...
    file = models.FileField(upload_to='uploads/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'jpg', 'jpeg', 'png'])])

class Banking(models.Model):
    #...
    transactions = models.JSONField(default=dict)    

# Creating a new instance of User model
user = User.objects.create_user('ninjaai', password='Sober323')

# Creating a UserProfile instance associated with the created User instance
UserProfile.objects.create(user=user)

# Existing model classes...
