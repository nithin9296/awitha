from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from .forms import CompanyNetPercentageForm, LoginForm, SignUpForm, trialbalanceForm
from django.contrib.auth import authenticate, login
from .models import npmargin, CompanyNetPercentage, trialbalance
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, F
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import django_excel as excel
import pyexcel
from pyexcel  import get_sheet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "operating/home.html", {})


def options(request):
	return render(request, "operating/options_page.html", {})


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
@login_required
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
 
			return render(request, "charts2.html", {})
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
									 .aggregate(np2015=Sum('netmargin_percentage_2015'))['np2015'])
		np2016 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(np2016=Sum('netmargin_percentage_2016'))['np2016'])
		np2017 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(np2017=Sum('netmargin_percentage_2017'))['np2017'])
		gp2017 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(gp2017=Sum('gross_profit_margin_2017'))['gp2017'])
		gp2016 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(gp2016=Sum('gross_profit_margin_2016'))['gp2016'])
		gp2015 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(gp2015=Sum('gross_profit_margin_2015'))['gp2015'])
		de2015 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(de2015=Sum('debtequity_ratio_2015'))['de2015'])
		de2016 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(de2016=Sum('debtequity_ratio_2016'))['de2016'])
		de2017 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(de2017=Sum('debtequity_ratio_2017'))['de2017'])
		np2015i = (npmargin.objects.filter(industry__industry_name=selected_industry)
									.aggregate(np2015i=Sum('netmargin_percentage_2015'))['np2015i'])

		np2016i = (npmargin.objects.filter(industry__industry_name=selected_industry)
									.aggregate(np2016i=Sum('netmargin_percentage_2016'))['np2016i'])

		np2017i = (npmargin.objects.filter(industry__industry_name=selected_industry)
									.aggregate(np2017i=Sum('netmargin_percentage_2017'))['np2017i'])

		sales_2017 = (trialbalance.objects.filter(classification__in=['sales']).aggregate(sales_2017=Sum('credit_2017'))['sales_2017'])
		cgs_2017 = (trialbalance.objects.filter(classification__in=['costofgoodsold']).aggregate(cgs_2017=Sum('debit_2017'))['cgs_2017'])
		gross_profit_2017 = sales_2017 - cgs_2017
		gross_profit_margin_2017  = gross_profit_2017 / sales_2017

		sales_2016 = (trialbalance.objects.filter(classification__in=['sales']).aggregate(sales_2016=Sum('credit_2016'))['sales_2016'])
		cgs_2016 = (trialbalance.objects.filter(classification__in=['costofgoodsold']).aggregate(cgs_2016=Sum('debit_2016'))['cgs_2016'])
		gross_profit_2016 = sales_2016 - cgs_2016
		gross_profit_margin_2016  = gross_profit_2016 / sales_2016

		sales_2015 = (trialbalance.objects.filter(classification__in=['sales']).aggregate(sales_2015=Sum('credit_2015'))['sales_2015'])
		cgs_2015 = (trialbalance.objects.filter(classification__in=['costofgoodsold']).aggregate(cgs_2015=Sum('debit_2015'))['cgs_2015'])
		gross_profit_2015 = sales_2015 - cgs_2015
		gross_profit_margin_2015  = gross_profit_2015 / sales_2015

		debt_cy = (trialbalance.objects.filter(classification__in=['debt']).aggregate(debt_cy=Sum('credit_cy'))['debt_cy'])
		equity_cy = (trialbalance.objects.filter(classification__in=['equity']).aggregate(equity_cy=Sum('credit_cy'))['equity_cy'])
		debtequity_ratio_cy  = debt_cy / equity_cy

		debt_py = (trialbalance.objects.filter(classification__in=['debt']).aggregate(debt_py=Sum('credit_py'))['debt_py'])
		equity_py = (trialbalance.objects.filter(classification__in=['equity']).aggregate(equity_py=Sum('credit_py'))['equity_py'])
		debtequity_ratio_py  = debt_py / equity_py

				

		labels = ["2015", "2016", "2017", ]
		default_items_c = [np2015, np2016, np2017]
		default_items_i = [np2015i, np2016i, np2017i]
		default_items_gp = [gross_profit_margin_cy, gross_profit_margin_py]
		default_items_de = [debtequity_ratio_cy, debtequity_ratio_py]

		data = {
				"labels" : labels,
				"default_c" : default_items_c,
				"default_i" : default_items_i,
				"default_gp" : default_items_gp,
				"default_de" : default_items_de,
				}
		return Response(data)


class ChartData_op2(APIView):

	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):

		selected_industry = request.session.get('selected_industry')
		selected_user = request.session.get('selected_user')
		#selected_industry: request.GET.get('selected_industry')
		#selected_user: request.GET.get('selected_user')

		industry_results = npmargin.objects.filter(industry__industry_name=selected_industry)
		np2015 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(np2015=Sum('netmargin_percentage_2015'))['np2015'])
		np2016 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(np2016=Sum('netmargin_percentage_2016'))['np2016'])
		np2017 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(np2017=Sum('netmargin_percentage_2017'))['np2017'])
		gp2017 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(gp2017=Sum('gross_profit_margin_2017'))['gp2017'])
		gp2016 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(gp2016=Sum('gross_profit_margin_2016'))['gp2016'])
		gp2015 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(gp2015=Sum('gross_profit_margin_2015'))['gp2015'])
		de2015 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(de2015=Sum('debtequity_ratio_2015'))['de2015'])
		de2016 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(de2016=Sum('debtequity_ratio_2016'))['de2016'])
		de2017 = (CompanyNetPercentage.objects.filter(user=selected_user)
									 .aggregate(de2017=Sum('debtequity_ratio_2017'))['de2017'])
		np2015i = (npmargin.objects.filter(industry__industry_name=selected_industry)
									.aggregate(np2015i=Sum('netmargin_percentage_2015'))['np2015i'])

		np2016i = (npmargin.objects.filter(industry__industry_name=selected_industry)
									.aggregate(np2016i=Sum('netmargin_percentage_2016'))['np2016i'])

		np2017i = (npmargin.objects.filter(industry__industry_name=selected_industry)
									.aggregate(np2017i=Sum('netmargin_percentage_2017'))['np2017i'])

		gp2017i = (npmargin.objects.filter(industry__industry_name=selected_industry)
									.aggregate(np2017i=Sum('netmargin_percentage_2017'))['np2017i'])
				

		labels = ["2015", "2016", "2017", ]
		default_items_c = [np2015, np2016, np2017]
		default_items_i = [np2015i, np2016i, np2017i]
		default_items_gp = [gp2015, gp2016, gp2017]
		default_items_de = [de2015, de2016, de2017]

		data = {
				"labels" : labels,
				"default_c" : default_items_c,
				"default_i" : default_items_i,
				"default_gp" : default_items_gp,
				"default_de" : default_items_de,
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
			return redirect("/operating/options")
		else:
			print("Error")

	return render(request, "auth/login.html", context)



def logout_view(request):
    logout(request)


# def register_page(request):
# 	form = LoginForm(request.POST or None)
# 	if form.is_valid():	
# 		print(form.cleaned_data)
# 	return render(request, "auth/login.html", {})
	

@login_required
def trialbalanceanalysis(request):
	if request.method == "POST":
		form = trialbalanceForm(request.POST, request.FILES)
		if form.is_valid():
			request.FILES['trialbalancefile'].save_book_to_database(
				models=[trialbalance],
				initializer=[None],
				mapdicts=[
					['user', 'region', 'industry', 'glcode', 'gldescription', 'classification', 'subclassification', 'debit_2017', 'credit_2017', 'debit_2016', 'credit_2016', 'debit_2015', 'credit_2015' ]]
			)
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
			return HttpResponseBadRequest()
	else:
		form = trialbalanceForm()
		return render( request,'operating/prelim_analysis.html', {'form': form})

# def handson_table(request):
#     return excel.make_response_from_tables(
#         [trialbalance], 'handsontable.html')


# def embed_handson_table(request):
#     """
#     Renders two table in a handsontable
#     """
#     content = excel.pe.save_book_as(
#         models=[trialbalance],
#         dest_file_type='handsontable.html',
#         dest_embed=True)
#     content.seek(0)
#     return render(
#         request,
#         'custom-handson-table.html',
#         {
#             'handsontable_content': content.read()
#         })


# def embed_handson_table_from_a_single_table(request):
#     """
#     Renders one table in a handsontable
#     """
#     content = excel.pe.save_as(
#         model=trialbalance,
#         dest_file_type='handsontable.html',
#         dest_embed=True)
#     content.seek(0)
#     return render(
#         request,
#         'custom-handson-table.html',
#         {
#             'handsontable_content': content.read()
#         })





@login_required
def rationop1(request):
	sales_cy = (trialbalance.objects.filter(classification__in=['sales']).aggregate(sales_cy=Sum('credit_cy'))['sales_cy'])
	cgs_cy = (trialbalance.objects.filter(classification__in=['costofgoodsold']).aggregate(cgs_cy=Sum('debit_cy'))['cgs_cy'])
	gross_profit_cy = sales_cy - cgs_cy
	gross_profit_margin_cy  = gross_profit_cy / sales_cy

	sales_py = (trialbalance.objects.filter(classification__in=['sales']).aggregate(sales_py=Sum('credit_py'))['sales_py'])
	cgs_py = (trialbalance.objects.filter(classification__in=['costofgoodsold']).aggregate(cgs_py=Sum('debit_cy'))['cgs_py'])
	gross_profit_py = sales_py - cgs_py
	gross_profit_margin_py  = gross_profit_py / sales_py

	debt_cy = (trialbalance.objects.filter(classification__in=['debt']).aggregate(debt_cy=Sum('credit_cy'))['debt_cy'])
	equity_cy = (trialbalance.objects.filter(classification__in=['equity']).aggregate(cgs_cy=Sum('credit_cy'))['equity_cy'])
	debtequity_ratio_cy  = debt_cy / equity_cy

	debt_py = (trialbalance.objects.filter(classification__in=['debt']).aggregate(sales_py=Sum('credit_py'))['debt_py'])
	equity_py = (trialbalance.objects.filter(classification__in=['equity']).aggregate(cgs_py=Sum('debit_cy'))['equity_py'])
	debtequity_ratio_py  = debt_py / equity_py	



	

	context = {
		"gross_profit_margin_cy" : gross_profit_margin_cy,
		"gross_profit_margin_py" : gross_profit_margin_py,
		"debtequity_ratio_cy" : debtequity_ratio_cy,
		"debtequity_ratio_py" : debtequity_ratio_py
	}

	return render(request, 'operating/rationop1.html', context)







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



