from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import profitandlossform, balancesheetform
from django.db import connection
from .models import profitandloss, balancesheet



def importdata_view(request):

	if request.method == 'POST':
		form = profitandlossform(request.POST, prefix="plf")
		sub_form = balancesheetform(request.POST, prefix="bsf")

		if form.is_valid() and sub_form.is_valid:
			plf = form.save
			bsf = sub_form.save(plf)

			return redirect(my_custom_sql)
	else:
		form = profitandlossform(prefix="plf")
		sub_form = balancesheetform(prefix="bsf")

	return render(request, "prelim_analysis.html", {'form':form, 'sub_form':sub_form})


def my_custom_sql(request):
	cursor = connection.cursor()
	cursor.execute('''SELECT p.documentid, b.glcode, b.gldescriptions, b.amount FROM profitandloss p
					JOIN balancesheet b
					ON p.documentid = b.documentid''')
	ids = []
	for row in cursor.fetchall():
		id = row[0]
		ids.append(id)
	context = {"rows": ids}

	return render (request, "sql.html", context)