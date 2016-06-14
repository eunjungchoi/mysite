from django.contrib import admin

# Register your models here.
from hangout.models import *


admin.site.register(Place)
admin.site.register(PlacePhoto)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Visit)
