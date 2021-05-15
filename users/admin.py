from django.contrib import admin
from .models import Profile
# imported user profile
from .models import UserProfile

# imported user profile
admin.site.register(Profile)
admin.site.register(UserProfile)
