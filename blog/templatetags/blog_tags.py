from django import template
from blog.models import Post
from blog.models import Category
register = template.Library() 


@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='posts')
def function():
    posts = Post .objects.filter(status=1)
    return posts



@register.filter
def snippet(value,arg=20):
    return value[:arg] + '...'


@register.inclusion_tag('blog/blog_popular_posts.html', name='popularposts')
def latest_post():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts':posts}



@register.inclusion_tag('blog/blog_post_categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}
    
    
    





























    
    
    
    # categories = {'iot ': 1 ,'programing':2}
    
    # for name,count in categories.items():
    #     print(name,count)