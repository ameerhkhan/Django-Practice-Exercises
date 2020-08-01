from django.db import models

# Create your models here.
class Project(models.Model): # @3.0
    title = models.CharField(max_length=100)       # Used for small strings and specifies maximum length.
    description = models.TextField()               # similar to CharField() but without any cap on words.
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")      # holds a string but must point to a file path name.
