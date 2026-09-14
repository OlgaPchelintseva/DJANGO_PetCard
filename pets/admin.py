from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'owner', 'is_public')
    list_filter = ('is_public', 'breed')
    search_fields = ('name', 'breed', 'owner__username')
    prepopulated_fields = {'slug': ('breed', 'name')}
    list_editable = ('is_public',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('owner', 'name', 'breed', 'slug')
        }),
        ('Описание и доступ', {
            'fields': ('bio', 'is_public')
        }),
    )