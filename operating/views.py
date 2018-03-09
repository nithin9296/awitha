from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from .forms import CompanyNetPercentageForm, LoginForm, SignUpForm
from django.contrib.auth import authenticate, login
from .models import npmargin, CompanyNetPercentage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, F
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "operating/home.html", {})


#@csrf_exempt

# Create your views here.

# class npmarginListView(ListView):
# 	model 				= npmargin
# 	context_object_name = 'netprofitmargin'


# class npmarginCreateView(CreateView):
# 	model 				= npmargin
# 	fields				= ('industry', 'npy2015', 'npy2016', 'npy2017')
# 	sucess_url			= reverse_lazy('npmargin_changelist')

# class npmarginUpdateView(UpdateView):
# 	model 				= npmargin
# 	fields				= ('industry', 'npy2015', 'npy2016', 'npy2017')
# 	sucess_url			= reverse_lazy('npmargin_changelist')


# def npmargin_view(request):
# 	if request.method == "POST":
# 		form = CompanyNetPercentageForm(request.POST)

# 		if form.is_valid():
# 			form.save()
# 			selected_industry = form.cleaned_data.get("industry")
# 			selected_user	= form.cleaned_data.get("user")
# 			query_results = npmargin.objects.filter(industry__industry_name=selected_industry)
# 			company_query = CompanyNetPercentage.objects.filter(user=selected_user)
# 			context = {
# 					'query_results': query_results,
# 					'company_query' : company_query
# 			}
# 			return render(request, "operating/detail.html", context)
# 	else:
# 		form = CompanyNetPercentageForm()
# 	return render(request, "operating/form.html",{'form': form})


# class npmarginListView(LoginRequiredMixin, ListView):
# 	def get_queryset(self):
# 		return CompanyNetPercentage.objects.filter(user=self.request.user)

def npmargin_view(request):
	if request.method == "POST":
		form = CompanyNetPercentageForm(request.POST)

		if form.is_valid():
			form.save()
			selected_industry = form.cleaned_data.get("industry")
			selected_user = form.cleaned_data.get("user")

			request.session['selected_industry'] = selected_industry
			request.session['selected_user'] = selected_user



			context = {
					'selected_industry': selected_industry,
					'selected_user': selected_user
			}
 
			return render(request, "charts.html", {})
	else:
		form = CompanyNetPercentageForm()
	return render(request, "operating/form.html",{'form': form})



class ChartData(APIView):

	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):

		selected_industry = request.session.get('selected_industry')
		selected_user = request.session.get('selected_user')
		#selected_industry: request.GET.get('selected_industry')
		#selected_user: request.GET.get('selected_user')

		industry_results = npmargin.objects.filter(industry__industry_name=selected_industry)
		np2015 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(np2015=Sum('npy2015'))['np2015'])
		np2016 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(np2016=Sum('npy2016'))['np2016'])
		np2017 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(np2017=Sum('npy2017'))['np2017'])


		np2015i = (npmargin.objects.filter(industry__industry_name=selected_industry)
									.aggregate(np2015i=Sum('npy2015'))['np2015i'])

		np2016i = (npmargin.objects.filter(industry__industry_name=selected_industry)
									.aggregate(np2016i=Sum('npy2016'))['np2016i'])

		np2017i = (npmargin.objects.filter(industry__industry_name=selected_industry)
									.aggregate(np2017i=Sum('npy2017'))['np2017i'])

				

		labels = ["2015", "2016", "2017", ]
		default_items_c = [np2015, np2016, np2017]
		default_items_i = [np2015i, np2016i, np2017i]

		data = {
				"labels" : labels,
				"default_c" : default_items_c,
				"default_i" : default_items_i,
				}
		return Response(data)


# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'operating/charts.html', {})
	



# class ChartData(APIView):
   
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         qs_count = trialbalance2017.objects.all().count()
        
#         current_asset = (trialbalance2017.objects
#                         .filter(description__in=['cash', 'debtors', 'inventory'])
#                         .aggregate(
#                             current_asset=Sum('debit')
#                             )['current_asset']
#                     )
    
#         current_liab = (trialbalance2017.objects
#                         .filter(description__in=['creditors', 'loans'])
#                         .aggregate(
#                             current_liab=Sum('credit')
#                             )['current_liab']
#                     )
#         current_assets = current_asset - current_liab 
#         labels = ["Users", "current_assets", "current_asset", "current_liab", ]
#         default_items = [qs_count, current_assets, current_asset, current_liab,]
        
        
#         data = {
#                 "labels" : labels,
#                 "default" : default_items,
#         } 
#         return Response(data)









def npmargin_detail_view(request, pk=None, *args, **kwags):
	qs = npmargin.objects.filter(industry=pk)
	context = {
		'object' : qs
	}
	return render(request, "operating/detail.html", context)



def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'operating/signup.html', {'form': form})




def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	print("User logged in")
	#print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		print (user)
		#print(request.user.is_authenticated())
		if user is not None:
			#print(request.user.is_authenticated())
			login(request, user)
			context['form'] = LoginForm()
			return redirect("/operating")
		else:
			print("Error")

	return render(request, "auth/login.html", context)


# def register_page(request):
# 	form = LoginForm(request.POST or None)
# 	if form.is_valid():
# 		print(form.cleaned_data)
# 	return render(request, "auth/login.html", {})
	

















# 






















# class npmarginListView(ListView):
# 	queryset = npmargin.objects.all()
# 	template_name = "operating/list.html"

# 	def get_queryset(self, *args, **kwargs):
# 		request = self.request
# 		return npmargin.objects.all()


# class npmarginDetailView(DetailView):
# 	template_name = "operating/detail.html"

# 	def get_object(self, *args, **kwargs):
# 		request = self.request
# 		pk = self.kwargs.get('pk')
# 		instance = npmargin.objects.get_by_id(pk)
# 		if instance is None:
# 			raise Http404("Product doesn't exist")
# 		return instance
