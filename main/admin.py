from django.contrib import admin
from .models import SiteModel,EntryModel
# Register your models here.

admin.site.register(SiteModel)
admin.site.register(EntryModel)