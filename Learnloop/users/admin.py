from django.contrib import admin
from .models import User

# Register your models here.
admin.site.site_header = "Learnloop Admin"
admin.site.register(User)