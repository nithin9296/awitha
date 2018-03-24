from django import forms
from django.forms import ModelChoiceField, ModelForm

from .models import profitandloss, balancesheet

class profitandlossform(ModelForm):
	class Meta:
		model = profitandloss
		fields = ['documentid', 'glcode', 'gldescription', 'amount']


class balancesheetform(ModelForm):
	class Meta:
		model = balancesheet
		fields = ['documentid', 'glcode', 'gldescription', 'amount']