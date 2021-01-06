from django.shortcuts import render
from .models import Project

# Create your views here.
def project_index(request):
    # Perform a query that retrieves all objects in the projects table
    projects = Project.objects.all()
    #create a dictionary context. that is used to send information to our template
    context = {
        'projects': projects
    }
    '''
    context is added as an argument to render(). Any entries in the context dictionary 
    are available in the template, as long as the context argument is passed to render(). 
    You’ll need to create a context dictionary and pass it to render in each view 
    function you create.
    '''
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
