from django.contrib import admin
from canaapp.models import Reservation, Contact,User,ImageModel,Manager
# Register your models here.

admin.site.register(Reservation)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(ImageModel)
admin.site.register(Manager)



