# import libraries(modules)
from django.contrib import admin
# import created model
from .models import Articles

# Register your models here.
admin.site.register(Articles)

