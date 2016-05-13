from django.contrib import admin

# Register your models here.
from hangout.models import Place, City, Category, Visit


admin.site.register(Place)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Visit)
