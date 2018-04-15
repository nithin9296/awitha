from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin, ImportExportActionModelAdmin



# Register your models here.
from .models import npmargin, Industry, Region, UserName, CompanyNetPercentage, ObjectViewed, feedback


admin.site.register(Region)
admin.site.register(UserName)
admin.site.register(CompanyNetPercentage)
admin.site.register(ObjectViewed)
admin.site.register(feedback)


class Industryresource(resources.ModelResource):

	class Meta:
		model = Industry



class npmarginresource(resources.ModelResource):

	class Meta:
		model = npmargin



class Industryadmin(ImportExportModelAdmin):
	resource_class = Industryresource
	


class npmarginadmin(ImportExportModelAdmin):
	resource_class = npmarginresource


admin.site.register(Industry, Industryadmin)
admin.site.register(npmargin, npmarginadmin)