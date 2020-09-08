# @4.3

from django.urls import path
from . import views

# root folder indicated via ""
urlpatterns = [
    path("", views.project_index, name="project_index"),            # the root url of our projects app is hooked up to project_index view.
    path("<int:pk>/", views.project_detail, name="project_detail"), # since we require a pk hence that is also passed in this path so as to diplay the correct project.
]


