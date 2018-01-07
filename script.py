from django.contrib.auth.models import User
from rezerwacje.models import Rodzina
for user in User.objects.all():
	ro=Rodzina.objects.filter(user=user)
	if len(ro)==0:
		Rodzina.objects.create(user=user,liczebność=1).save()
	