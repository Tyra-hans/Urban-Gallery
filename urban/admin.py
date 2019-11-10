from django.contrib import admin
from .models import Editor,Article,tags, Location

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)
admin.site.register(Location)