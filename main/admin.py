from django.contrib import admin
from .models import SiteModel,EntryModel,OldEntryModel
# Register your models here.

admin.site.register(SiteModel)
admin.site.register(EntryModel)
admin.site.register(OldEntryModel)