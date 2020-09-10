from django.db import models

# Create your models here.
# @6.0
class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)    # assgns a current date and time when this instance is created.
    last_modified = models.DateTimeField(auto_now=True)     # assigns current date and time whenever an instance is last saved. basically every edit.
    categories = models.ManyToManyField('Category', related_name='posts') # Many categories to many posts. Allows us to create a relationship between the two tables.

    # The ManytoManyField takes two arguments. The first is the model with which the relationship is,
    # The second allows us to to access the relationship from a Category object even though we haven't added that field.
    # By adding related_name to posts we can access category.posts to give us a list of posts in a certain category.


# The third and final model we need to add is Comment.
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE) # relational field similar to many to many
                            # but instead defines a many to one relationship. So that many comments can be
                            # associated to a single post.
    
    # The ForeignKey field takes two arguments. The first is the other model in the relatioship, in this case
    # Post. The second tells Django what to do when a post is deleted. If a post is deleted we don't want
    # its comments hanging around. We, therfore, want to delete them as well. hence, on_delete=models.CASCADE.



    