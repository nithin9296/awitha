# from notepad.signals import object_viewed_signal

# class ObjectViewMixin(object):

# 	def dispatch(self, request, *args, **kwargs):
# 		try:
# 			instance = self.get_object()
# 		except DoesNotExist:
# 			instance = None
# 		if instance is not None:
# 			object_viewed_signal.send(instance._class_, instance=instance, request=request)
# 		return super(ObjectViewMixin, self).dispatch(request, *args, **kwargs)

