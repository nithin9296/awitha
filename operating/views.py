from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from .forms import CompanyNetPercentageForm, LoginForm, SignUpForm, trialbalanceForm, feedbackform
from django.contrib.auth import authenticate, login
from .models import npmargin, CompanyNetPercentage, trialbalance, ObjectViewed
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
import os
import csv
from django.conf import settings
from django.utils.text import slugify
from operating.utils import get_lookup_fields, qs_to_dataset
from io import StringIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.http import HttpResponse, StreamingHttpResponse
from django.utils.text import slugify
from django.views.generic import View
# from operating.mixins import ObjectViewMixin
from operating.signals import object_viewed_signal
from .utils import convert_to_dataframe
try:
	from io import BytesIO as IO
except ImportError:
	from StringIO import StringIO as IO
import pandas as pd
import xlsxwriter


BASE_DIR = settings.BASE_DIR



class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "operating/home.html", {})


def options(request):
	return render(request, "operating/options_page.html", {})


def about(request):
	return render(request, "operating/about.html", {})


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


# def productview(request):
# 		selected_industry = request.session.get('selected_industry')
# 		selected_user = request.session.get('selected_user')

# 		# industry_results = npmargin.objects.filter(industry__industry_name=selected_industry)
# 		# np2015 = (CompanyNetPercentage.objects.filter(user=selected_user)
# 		# 							 .aggregate(np2015=Sum('netmargin_percentage_2015'))['np2015'])
		
# 		qs = CompanyNetPercentage.objects.filter(user=selected_user)
# 		df = convert_to_dataframe(qs, fields=['gross_profit_margin_2015', 'gross_profit_margin_2016', 'gross_profit_margin_2017',
# 											'debtequity_ratio_2015', 'debtequity_ratio_2016', 'debtequity_ratio_2017'
# 											'netmargin_percentage_2015', 'netmargin_percentage_2016', 'netmargin_percentage_2017'])

# 		json = df.to_json(orient='records')


# 		context = {
# 					"data": json
# 				}

# 		return render (request, 'operating/product.html', context)

def productview(request):
		selected_industry = request.session.get('selected_industry')
		selected_user = request.session.get('selected_user')

		# industry_results = npmargin.objects.filter(industry__industry_name=selected_industry)
		# np2015 = (CompanyNetPercentage.objects.filter(user=selected_user)
		# 							 .aggregate(np2015=Sum('netmargin_percentage_2015'))['np2015'])
		
		qs1 = CompanyNetPercentage.objects.filter(user=selected_user)
		qs2 = CompanyNetPercentage.objects.filter(industry=selected_industry)

		df1 = convert_to_dataframe(qs1, fields=['user', 'gross_profit_margin_2015', 'gross_profit_margin_2016', 'gross_profit_margin_2017',
											'debtequity_ratio_2015', 'debtequity_ratio_2016', 'debtequity_ratio_2017',
											'netmargin_percentage_2015', 'netmargin_percentage_2016', 'netmargin_percentage_2017'])
		df2 = convert_to_dataframe(qs2, fields=['user', 'gross_profit_margin_2015', 'gross_profit_margin_2016', 'gross_profit_margin_2017',
											'debtequity_ratio_2015', 'debtequity_ratio_2016', 'debtequity_ratio_2017', 
											'netmargin_percentage_2015', 'netmargin_percentage_2016', 'netmargin_percentage_2017', 
											])
		frames = [df1, df2]
		result = pd.concat(frames)
		excel_file = IO()
		xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')

		result.to_excel(xlwriter, 'sheetname')
		xlwriter.save()
		xlwriter.close()
		excel_file.seek(0)

		response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

		response['content-Disposition'] = 'attachment; filename=myfile.xlsx'
		return response

class CSVResponseMixin(object):
	csv_filename = 'csvfile.csv'

	def get_csv_filename(self):
		return self.csv_filename

	def render_to_csv(self, context):
		response = HttpResponse(content_type='text/csv')
		
		cd = 'attachment; filename="{0}"'.format(self.get_csv_filename())
		response['content-Disposition'] = cd

		writer = csv.DictWriter(response, fieldnames=fieldnames	)
		# writer.writeheader()
		for row in context:
			writer.writerow(row)

		return response

class DataView(CSVResponseMixin, View):

	def get(self, request, *args, **kwargs):
		selected_industry = request.session.get('selected_industry')
		selected_user = request.session.get('selected_user')
		qs = CompanyNetPercentage.objects.filter(user=selected_user)
		df = convert_to_dataframe(qs, fields=['gross_profit_margin_2015', 'gross_profit_margin_2016', 'gross_profit_margin_2017',
											'debtequity_ratio_2015', 'debtequity_ratio_2016', 'debtequity_ratio_2017'
											'netmargin_percentage_2015', 'netmargin_percentage_2016', 'netmargin_percentage_2017'])

		json = df.to_json(orient='records')


		context = {
					"data": json
				}

		
		return self.render_to_csv(context)






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

def feedback(request):
	if request.method == 'POST':
		form = feedbackform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
		form = feedbackform(),
	return render(request, 'operating/feedback.html', {'form': form})


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

	return render(request, "operating/login.html", context)



def logout_view(request):
    logout(request)


# def register_page(request):
# 	form = LoginForm(request.POST or None)
# 	if form.is_valid():	
# 		print(form.cleaned_data)
# 	return render(request, "auth/login.html", {})
	

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

	object_viewed_signal.send(instance.__class__, instance=context, request=request)
	return render(request, 'operating/rationop1.html', context)





def qs_to_local_csv(qs, fields=None, path=None, filename=None):
	if path is None:
		path = os.path.join(os.path.dirname(BASE_DIR), 'csvstorage')

		if not os.path.exists(path):
			os.mkdir(path)

	if filename is None:
		model_name = slugify(qs.model.__name__)
		file_name = "{}.csv".format(model_name)
	filepath = os.path.join(path, filename)
	lookups = get_lookup_fields(qs.model, fields=fields)
	dataset = qs_to_dataset(qs, fields)
	row_done = 0
	with open(filepath, 'w') as my_file:
		writer = csv.DictWriter(my_file, filenames=lookups)
		writer.writeheader()
		for data_item in dataset:
			writer.writerow(data_item)
			rows_done += 1
	print("{} rows completed".format(rows_done))


class Echo:
	def write (self, value):
		return value

class CSVDownloadView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		qs = ObjectViewed.objects.all()
		model_name = slugify(qs.model.__name__)
		filename = "{}.csv".format(model_name)
		fp = StringIO()
		pseudo_buffer = Echo()
		outcsv = csv.writer(pseudo_buffer)
		writer = csv.DictWriter(my_file, fieldnames=lookups)
		writer.writeheader()
		for data_item in dataset:
			writer.writerow(data_item)
		stream_file = file(fp)
		response = StreamingHttpResponse(stream_file,
										content_type ="text/csv")
		response['content-Disposition'] = 'attachment; filename="{}"'.format(filename)
		return response



# def user(request, user_id):
# 	user = get_object_or_404(User, pk=user_id)
# 	return render_to_response('')	






















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



