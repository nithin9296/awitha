from django.conf.urls import url



from .views import  npmargin_detail_view, login_page, ChartData, ChartData_op2, npmargin_view, signup, trialbalanceanalysis,  rationop1, options, productview, qs_to_local_csv, CSVDownloadView, DataView, about, feedback

urlpatterns = [
    #url(r'^$', npmarginListView.as_view(), name='npmargin_changelist'),
    #url(r'^$', HomeView.as_view(), name='home'),
    url(r'^npmargin/$', npmargin_view),
    #url(r'^compare/$', npmargin_compare),
    url(r'^login/$', login_page),
    url(r'^signup/$', signup, name='signup'),
    url(r'^trialbalanceanalysis/$', trialbalanceanalysis),

    #url(r'^add/$', npmarginListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', npmargin_detail_view),
    url(r'^api/chart/data/$', ChartData.as_view(), name='api-data'),
    url(r'^api/chart/data2/$', ChartData_op2.as_view(), name='api-data2'),
    #url(r'^operating/(?P<pk>\d+)/$', npmarginDetailView.as_view()),
    #url(r'^handson_view/', handson_table, name="handson_view"),
    url(r'^rationop1/$', rationop1),
    url(r'^options/$', options),
    url(r'^about/$', about),
    url(r'^feedback/$', feedback),
    url(r'^productview/$', productview),
    url(r'^qs_to_local_csv/$', qs_to_local_csv),
    url(r'^DataView/$', DataView.as_view()),
   ]

