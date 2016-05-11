from django.contrib import admin

from .models import Company, People, Jobs

admin.site.register(Company)
admin.site.register(People)
admin.site.register(Jobs)