from django import forms
from django.forms import ModelChoiceField, ModelForm
from .models import Region, Industry, CompanyNetPercentage, trialbalance, feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# REGION_CHOICES=[
# 	('United States', 'United States'),
# 	('Aus, NZ & Canada', 'Aus, NZ & Canada'),
# 	('Europe', 'Europe'),
# 	('Emerging Markets', 'Emerging Markets'),
# 	('Japan','Japan'),
# 	]

# INDUSTRY_CHOICES=[
# 	('Advertising', 'Advertising'),
# 	('aerospace', 'aerospace'),
# 	('air transport', 'air transport'),
# 	('apparel', 'apparel'),
# 	]



class CompanyNetPercentageForm(ModelForm):
	class Meta:
		model = CompanyNetPercentage
		fields = ['user', 'region', 'industry', 'gross_profit_margin_2015', 'gross_profit_margin_2016', 'gross_profit_margin_2017', 'debtequity_ratio_2015','debtequity_ratio_2016', 'debtequity_ratio_2017',  'netmargin_percentage_2015', 'netmargin_percentage_2016', 'netmargin_percentage_2017']
		# def __int__(self, request, *args, **kwargs):
		# 	super(CompanyNetPercentageForm, self).__init__(*args, **kwargs)
		# 	self.fields[]
		def clean_user(self):
			user = self.cleaned_data.get('user')
			qs = CompanyNetPercentage.objects.filter(user=user)
			if qs.exists():
				raise forms.ValidationError("User already exists")
			return user


	# region   = forms.CharField(label='Please select the Region', widget=forms.Select(choices=REGION_CHOICES))
	# industry  = forms.CharField(label='Please select the Industry', widget=forms.Select(choices=INDUSTRY_CHOICES))
	# #industry = forms.ModelChoiceField(queryset= Industry.objects.values_list('name'))
	# npy2015  = forms.DecimalField(decimal_places=2, max_digits=20)
	# npy2016  = forms.DecimalField(decimal_places=2, max_digits=20)
	# npy2017  = forms.DecimalField(decimal_places=2, max_digits=20)


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class trialbalanceForm(forms.ModelForm):
	trialbalancefile = forms.FileField(
        label = 'Upload trialblanace as per the format' 
        )
	# user = forms.CharField(max_length=25)
	# region   = forms.CharField(max_length=25, choices=REGION_CHOICES)
	class Meta:
		model = trialbalance
		fields = ('user', 'region', 'industry',)

# class trialbalanceForm(forms.Form):
#  	trialbalancefile = forms.FileField(
#         label = 'Upload trialblanace as per the format' 
#         )

#  

class feedbackform(forms.ModelForm):
	feedback = forms.CharField(max_length=10000,
			widget=forms.TextInput(attrs={'autofocus': 'autofocus',
											'size': '100'}))

	class Meta:
		model = feedback
		fields = ('feedback',)