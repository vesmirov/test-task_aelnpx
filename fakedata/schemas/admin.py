from django.contrib import admin

from schemas import models


@admin.register(models.Schema)
class SchemaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'user', 'modified')


@admin.register(models.Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'column_type')
    ordering = ('column_type',)


@admin.register(models.Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created', 'rows', 'status')
    ordering = ('created', 'rows')
