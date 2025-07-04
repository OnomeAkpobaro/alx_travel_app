from django.contrib import admin
from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    """Admin interface for Listing model."""
    
    list_display = ['title', 'location', 'price', 'created_by', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at', 'location']
    search_fields = ['title', 'description', 'location']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'location', 'price')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )