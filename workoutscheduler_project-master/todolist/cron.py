from . import si
from django.contrib.auth.models import User
from todolist.models import Calink


def my_scheduled_job():

	aa = []

	a = si.riri('openhack1.csv')

	for i in a:
		aa.append(i)

	a = si.riri('openhack2.csv')

	for i in a:
		aa.append(i)

	name  = User.objects.get(username = request.user.get_username())

	for a in aa:
		calink = Calink(
			owner = name,
			link = a 
			)

		calink.save()