from django.db import models
from django.contrib.auth import authenticate, login, get_user_model

# Create your models here.
# class npmarginManager(models.Manager):
# 	def all(self):
# 		return self.get_queryset()

# 	def get_by_id(self, id):
# 		qs =  self.get_queryset().filter(id=id)
# 		if qs.count() == 1:
# 			return qs.first()
# 		return None

class Region(models.Model):
	region_name = models.CharField(max_length=20)

	def __str__(self):
		return str(self.region_name)

class Industry(models.Model):
	
	industry_name   = models.CharField(max_length=25)

	def __str__(self):
		return str(self.industry_name)


class UserName(models.Model):
	user_name   = models.CharField(max_length=25)

	def __str__(self):
		return self.user_name


class npmargin(models.Model):
	region   = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
	industry = models.ForeignKey(Industry, on_delete=models.CASCADE, null=True)
	netmargin_percentage_2015  = models.DecimalField(max_digits=5, decimal_places=2)
	netmargin_percentage_2016  = models.DecimalField(max_digits=5, decimal_places=2)
	netmargin_percentage_2017  = models.DecimalField(max_digits=5, decimal_places=2)
	gross_profit_margin_2015  = models.DecimalField(max_digits=5, decimal_places=2)
	gross_profit_margin_2016  = models.DecimalField(max_digits=5, decimal_places=2)
	gross_profit_margin_2017  = models.DecimalField(max_digits=5, decimal_places=2)
	debtequity_ratio_2015 = models.DecimalField(max_digits=5, decimal_places=2)	
	debtequity_ratio_2016 = models.DecimalField(max_digits=5, decimal_places=2)	
	debtequity_ratio_2017 = models.DecimalField(max_digits=5, decimal_places=2)	

	def __str__(self):
		return str(self.industry)



	#objects = npmarginManager()

	#def get_absolute_url(self):
		#return "/operating/{slug}/".format(slug=self.slug)


REGION_CHOICES=[
	('United States', 'United States'),
	('Aus, NZ & Canada', 'Aus, NZ & Canada'),
	('Europe', 'Europe'),
	('Emerging Markets', 'Emerging Markets'),
	('Japan','Japan'),
	]

INDUSTRY_CHOICES=[
	('Advertising', 'Advertising'),
	('aerospace', 'aerospace'),
	('air transport', 'air transport'),
	('apparel', 'apparel'),
	('Auto & Truck', 'Auto & Truck'),
	('Auto Parts', 'Auto Parts'),
	('Utility (Water)', 'Utility (Water)'),
	('Utility (General)', 'Utility (General)'),
	('Trucking', 'Trucking'),
	('Transportation (Railroads)', 'Transportation (Railroads)'),
	('Transportation', 'Transportation'),
	('Tobacco', 'Tobacco'),
	('Telecom. Services', 'Telecom. Services'),
	('Telecom. Equipment', 'Telecom. Equipment'),
	('Telecom (Wireless)', 'Telecom (Wireless)'),
	('Steel', 'Steel'),
	('Software (System & Application)', 'Software (System & Application)'),
	('Software (Internet)', 'Software (Internet)'),
	('Software (Entertainment)', 'Software (Entertainment)'),
	('Shoe', 'Shoe'),
	('Shipbuilding & Marine', 'Shipbuilding & Marine'),
	('Semiconductor Equip', 'Semiconductor Equip'),
    ('Semiconductor', 'Semiconductor'),
	('Rubber& Tires', 'Rubber& Tires'),
	('Retail (Special Lines)','Retail (Special Lines)'),
	('Retail (Online)', 'Retail (Online)'), 
	('Retail (Grocery and Food)', 'Retail (Grocery and Food)'),
	('Retail (General)', 'Retail (General)'),
	('Retail (Distributors)', 'Retail (Distributors)'),
	('Retail (Building Supply)', 'Retail (Building Supply)'),
	('Retail (Automotive)', 'Retail (Automotive)'),
	('Restaurant/Dining', 'Restaurant/Dining'),
	('Reinsurance', 'Reinsurance'),
	('Recreation', 'Recreation'),
	('Real Estate (Operations & Services)', 'Real Estate (Operations & Services)'),
	('Real Estate (General/Diversified)', 'Real Estate (General/Diversified)'),
	('Real Estate (Development)', 'Real Estate (Development)'),
	('R.E.I.T.', 'R.E.I.T.'),
	('Publishing & Newspapers', 'Publishing & Newspapers'),
	('Precious Metals', 'Precious Metals'),
	('Power','Power'), 
	('Paper/Forest Products', 'Paper/Forest Products'),
	('Packaging & Container', 'Packaging & Container'),
# Oilfield Svcs/Equip.
# Oil/Gas Distribution
# Oil/Gas (Production and Exploration)
# Oil/Gas (Integrated)
# Office Equipment & Services
# Metals & Mining
# Machinery
# Investments & Asset Management
# Insurance (Prop/Cas.)
# Insurance (Life)
# Insurance (General)
# Information Services
# Household Products
# Hotel/Gaming
# Hospitals/Healthcare Facilities
# Homebuilding
# Heathcare Information and Technology
# Healthcare Support Services
# Healthcare Products
# Green & Renewable Energy
# Furn/Home Furnishings
# Food Wholesalers
# Food Processing
# Financial Svcs. (Non-bank & Insurance)
# Farming/Agriculture
# Environmental & Waste Services
# Entertainment
# Engineering/Construction
# Electronics (General)
# Electronics (Consumer & Office)
# Electrical Equipment
# Education
# Drugs (Pharmaceutical)
# Drugs (Biotechnology)
# Diversified
# Construction Supplies
# Computers/Peripherals
# Computer Services
# Coal & Related Energy
# Chemical (Specialty)
# Chemical (Diversified)
# Chemical (Basic)
# Cable TV
# Business & Consumer Servi
# Building Materials
# Brokerage & Investment Ba
# Broadcasting
# Beverage (Soft)
# Beverage (Alcoholic)
# Banks (Regional)
# Bank (Money Center)
# )

	]



#User = get_user_model()
class CompanyNetPercentage(models.Model):
	user = models.CharField(max_length=25)
	#user 	 = models.ForeignKey(UserName, on_delete=models.CASCADE, null=True)
	region   = models.CharField(max_length=25, choices=REGION_CHOICES)
	industry  = models.CharField(max_length=25, choices=INDUSTRY_CHOICES)
	#industry = forms.ModelChoiceield(queryset= Industry.objects.values_list('name'))
	gross_profit_margin_2015 = models.IntegerField(default=0)
	gross_profit_margin_2016 = models.IntegerField(default=0)
	gross_profit_margin_2017 = models.IntegerField(default=0)
	debtequity_ratio_2015 = models.IntegerField(default=0)
	debtequity_ratio_2016 = models.IntegerField(default=0)
	debtequity_ratio_2017 = models.IntegerField(default=0)
	netmargin_percentage_2015  = models.DecimalField(max_digits=5, decimal_places=2)
	netmargin_percentage_2016  = models.DecimalField(max_digits=5, decimal_places=2)
	netmargin_percentage_2017  = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return str(self.user)

	def clean_user(self):
			user = self.cleaned_data.get('user')
			qs = CompanyNetPercentage.objects.filter(user=user)
			if qs.exists():
				raise forms.ValidationError("User already exists")
			return user

# class operatingmargin(models.Model):
# 	region   = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
# 	industry = models.ForeignKey(Industry, on_delete=models.CASCADE, null=True)
# 	opy2015  = models.IntegerField(default=0)
# 	opy2016  = models.IntegerField(default=0)
# 	opy2017  = models.IntegerField(default=0)

# 	def __str__(self):
# 		return str(self.industry)



class trialbalance(models.Model):
	user = models.CharField(max_length=25, default=0)
	region   = models.CharField(max_length=25, choices=REGION_CHOICES, default=0)
	industry  = models.CharField(max_length=25, choices=INDUSTRY_CHOICES, default=0)
	glcode = models.IntegerField(default=0)
	gldescription = models.CharField(max_length=60)
	classification = models.CharField(max_length=30)
	subclassification = models.CharField(max_length=30)
	debit_2017 = models.IntegerField(default=0)
	credit_2017 = models.IntegerField(default=0)
	debit_2016 = models.IntegerField(default=0)
	credit_2016 = models.IntegerField(default=0)
	debit_2015 = models.IntegerField(default=0)
	credit_2015 = models.IntegerField(default=0)

	def __str__(self):
		return str(self.gldescription)



















