from django.contrib import admin
from import_export import resources
#from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import Post


admin.site.register(Post)

class PostResource(resources.ModelResource):
	
	class Meta:
		model = Post
		
#class PostAdmin(ImportExportModelAdmin):
	#pass
	