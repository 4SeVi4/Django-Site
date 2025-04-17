from django.contrib import admin
from .models import Category, Article, ArticleImage

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'main_page')
    list_filter = ('category', 'main_page')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ArticleImageInline]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
