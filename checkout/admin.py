__author__ = 'gabriele'

from django.contrib import admin
from checkout.models import List, Item, UserProfile
from django.contrib.auth.models import User




class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture', 'location', 'date_joined')
    readonly_fields = ('image_tag',)

class ItemInline(admin.TabularInline):
    model = Item

class ListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ItemInline]

    list_display = ('name', 'pub_date', 'total_check')
    list_filter = ['name']
    search_fields = ['name']
    date_hierarchy = 'pub_date'


admin.site.register(List, ListAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
