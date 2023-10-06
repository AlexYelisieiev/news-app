from django.contrib import admin
from . import models


class CommentInline(admin.TabularInline):
    model = models.Comment
    extra = 0


class AcrticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]


admin.site.register(models.Article, AcrticleAdmin)
admin.site.register(models.Comment)
