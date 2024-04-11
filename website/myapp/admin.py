from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(ReserveTable)
admin.site.register(ExclusiveReserveTable)