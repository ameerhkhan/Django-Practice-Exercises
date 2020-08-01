from django.shortcuts import render
from projects.models import Project

# Create your views here.

def project_index(request): # @4.0
    # query --> A command that allows you to create, retrieve, update or delete objects(rows) in your database.
    
    projects = Project.objects.all() # query to get all objects in the table i.e projects.
    
    context = {                 # The context dictionary is used to send information to our template
        'projects': projects    # We assign our queryset of all projects to entry named 'projects'
    }                           # Every view function we create needs to have a context dictionary.

    return render(request, 'project_index.html', context) # render basically takes in the request, template and the queries made in context dictionary.


def project_detail(request, pk): # @4.1
    project = Project.objects.get(pk=pk) # This query retrieves the project with primary key(pk) equal to that in the function argument.

    context = {
        'project': project
    }

    return render(request, 'project_detail.html', context)





