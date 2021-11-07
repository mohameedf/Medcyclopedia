from medcyclopedia.models import Article, Category, Drug, DrugClass, Tag
from django.contrib import admin

# Register your models here.
admin.site.register(Drug)
admin.site.register(Tag)
admin.site.register(DrugClass)
admin.site.register(Article)
admin.site.register(Category)
