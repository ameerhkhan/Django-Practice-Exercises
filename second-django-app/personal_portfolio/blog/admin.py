from django.contrib import admin
from blog.models import Post, Category, Comment          # import what you would like to register.s
# Register your models here.
# @6.1

# The following classes are used to customize what is shown on the admin pages.
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass


# The following lines register the models with the admin classes.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

