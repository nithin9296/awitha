from django.conf.urls import url


from .views import importdata_view,  my_custom_sql

urlpatterns = [
	url(r'^importdata/$', importdata_view),
	url(r'^my_custom_sql/$', my_custom_sql, name = 'my_custom_sql'),

	]