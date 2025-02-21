from django.shortcuts import render, get_object_or_404
from .models import Tag, Project, ProjectImage

# Create your views here.
def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "content.html", {"projects": projects, "tags": tags})

def contact(request):
    return render(request, "contact.html")

def projectDetail(request, id):
    details = get_object_or_404(Project, pk=id)
    return render(request, "projectDetail.html", {"details": details})