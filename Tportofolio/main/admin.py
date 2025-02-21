from django.contrib import admin
from .models import Tag, Project, ProjectImage

# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1 

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "link"
    )
    
    inlines = [ProjectImageInline]

    # what can be search
    search_fields = (
        "title",
        "description"
    )

    list_filter = ("tags",)

class tagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Tag, tagAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectImage)
