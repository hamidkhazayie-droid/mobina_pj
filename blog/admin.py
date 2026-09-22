from django.contrib import admin
from  blog.models import Post,Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    date_hierarchy = 'created_date'
    
    empty_value_display = '-empty-'

    fields = ('image','author', 'title', 'content', 'category', 'content_views', 'status', 'published_date')

    list_display = ('title','author', 'content_views', 'status', 'published_date', 'created_date')

    list_filter = ('status','author',)

    # ordering = ['-created_date']    

    search_fields = ['title','content'] 
    
    list_per_page = 20
    
    admin.site.register(Category)