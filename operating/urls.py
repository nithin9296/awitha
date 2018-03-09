from django.conf.urls import url



from .views import  npmargin_detail_view, login_page, ChartData, npmargin_view, signup

urlpatterns = [
    #url(r'^$', npmarginListView.as_view(), name='npmargin_changelist'),
    #url(r'^$', HomeView.as_view(), name='home'),
    url(r'^npmargin/$', npmargin_view),
    #url(r'^compare/$', npmargin_compare),
    url(r'^login/$', login_page),
    url(r'^signup/$', signup, name='signup'),

    #url(r'^add/$', npmarginListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', npmargin_detail_view),
    url(r'^api/chart/data/$', ChartData.as_view(), name='api-data'),
    #url(r'^operating/(?P<pk>\d+)/$', npmarginDetailView.as_view()),
   ]

