from django.contrib import admin
from test_app.models import contact


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ['name','massage']

admin.site.register(contact, ContactAdmin)