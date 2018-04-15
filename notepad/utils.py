# import pandas as pd


# def get_model_field_names(model, ignore_fields=['content_object']):
# 	model_fields = model._meta_get_fields()
# 	model_field_names = list(set([f.name for f in model_fields if f.name not in ignore_fields]))
# 	return model_field_names


# def get_lookup_fields(model, fields=None):
# 	model_field_names = get_model_field_names(model)
# 	if fields is not None:
# 		lookup_fields = []
# 		for x in fields:
# 			if "__" in x:
# 				lookup_fields.append(x)
# 			elif x in model_field_names:
# 				lookup_fields.append(x)
# 	else:
# 		lookup_fields = model_field_names

# 	return lookup_fields

# def qs_to_dataset(qs, fields=None):
# 	lookup_fields = get_lookup_fields(qs.model, fields=fields)
# 	return list(qs.values(*lookup_fields))


# def convert_to_dataframe(qs, fields=None, index=None):
# 	lookup_fields = get_lookup_fields(qs.model, fields=fields)
# 	index_col = None
# 	if index in lookup_fields:
# 		index_col = index
# 	elif "id" in lookup_fields:
# 		index_col = 'id'

# 	values = qs_to_dataset(qs, fields=fields)
# 	df = pd.DataFrame.from_records(values, colums=lookup_fields, index=index_col)
# 	return df

# def get_client_ip(request):
# 	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
# 	if x_forwarded_for:
# 		ip = x_forwarded_for.split(',')[0]
# 	else:
# 		ip = request.META.get('REMOTE_ADDR')
# 	return ip


















