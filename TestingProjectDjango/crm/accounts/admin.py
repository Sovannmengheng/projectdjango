from django.contrib import admin
from.models import *

# Register your models here.

admin.site.register(Customer)

admin.site.register(ImageType)
admin.site.register(Image)

admin.site.register(Menu)
admin.site.register(MenuDetail)