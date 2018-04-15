from django.db import models
from django.contrib.auth import authenticate, login, get_user_model
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from io import StringIO
from django.core.files import File
from django.db import models
from django.utils import timezone
from operating.utils import convert_to_dataframe
from .signals import object_viewed_signal
from .utils import get_client_ip

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
	('Oilfield Svcs/Equip.', 'Oilfield Svcs/Equip.'),
	('Oil/Gas Distribution', 'Oil/Gas Distribution'),
	('Oil/Gas (Production and Exploration)', 'Oil/Gas (Production and Exploration)'),
	('Oil/Gas (Integrated)', 'Oil/Gas (Integrated)'),
	('Office Equipment & Services', 'Office Equipment & Services'),
	('Metals & Mining', 'Metals & Mining'),
	('Machinery', 'Machinery'),
	('Investments & Asset Management', 'Investments & Asset Management'),
	('Insurance (Prop/Cas.)', 'Insurance (Prop/Cas.)'),
	('Insurance (Life)', 'Insurance (Life)'),
	('Insurance (General)', 'Insurance (General)'),
	('Information Services', 'Information Services'),
	('Household Products', 'Household Products'),
	('Hotel/Gaming', 'Hotel/Gaming'),
	('Hospitals/Healthcare Facilities', 'Hospitals/Healthcare Facilities'),
	('Homebuilding', 'Homebuilding'),
	('Heathcare Information and Technology', 'Heathcare Information and Technology'),
	('Healthcare Support Services', 'Healthcare Support Services'), 
	('Healthcare Products', 'Healthcare Products'),
	('Green & Renewable Energy', 'Green & Renewable Energy'),
	('Furn/Home Furnishings', 'Furn/Home Furnishings'),
	('Food Wholesalers', 'Food Wholesalers'),
	('Food Processing', 'Food Processing'),
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




class ObjectViewed(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
	content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
	object_id = models.PositiveIntegerField()
	ip_address = models.CharField(max_length=120, blank=True, null=True)
	content_object = GenericForeignKey('content_type', 'object_id')
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self, ):
		return "%s viewed: %s" %(self.content_object, self.timestamp)

	class Meta:
		ordering = ['-timestamp']
		verbose_name = 'Object Viewed'
		verbose_name_plural = 'Objects Viewed'

def object_viewed_recevier(sender, instance, request, *args, **kwargs):
	c_type = ContentType.get_for_model(sender)
	ip_adress = None
	try:
		ip_adress = get_client_ip(request)
	except:
		pass
	new_view_instance = ObjectViewed.objects.create(
				user=request.user,
				content_type=c_type,
				object_id=instance.id,
				ip_address=ip_address
				)
object_viewed_signal.connect(object_viewed_recevier)


class DataSetManager(models.Manager):
	def create_new(self, qs, fields=None):
		df  = convert_to_dataframe(qs, fields=fields)
		fp = StringIO()
		fp.write(df.to_csv())
		date = timezone.now().strftime("%m-%d-%y")
		model_name = slugify(qs.model.__name__)
		filename = "{}-{}.csv".format(model_name, date)
		obj = self.model(
			name = filename.replace('.csv', ''),
                app = slugify(qs.model._meta.app_label),
                model = qs.model.__name__,
                lables = fields,
                object_count = qs.count()
            )
		obj.save()
		obj.csvfile.save(filename, File(fp)) #saves file to the file field
		return obj

class DatasetModel(models.Model):
    name                = models.CharField(max_length=120)
    app                 = models.CharField(max_length=120, null=True, blank=True)
    model               = models.CharField(max_length=120, null=True, blank=True)
    lables              = models.TextField(null=True, blank=True)
    object_count        = models.IntegerField(default=0)
    csvfile             = models.FileField(upload_to='datasets/', null=True, blank=True)
    timestamp           = models.DateTimeField(auto_now_add=True)




class feedback(models.Model):
	feedback = models.CharField(max_length=10000)







