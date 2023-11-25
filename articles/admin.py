from django.contrib import admin

from .models import Article, Tag, Scope


class ScopeAdmin(admin.TabularInline):
    model = Scope
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeAdmin]

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass