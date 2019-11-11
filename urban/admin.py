from django.contrib import admin
from .models import Editor,Article,Category, Location

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Location)