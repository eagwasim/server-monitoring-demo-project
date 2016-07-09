from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Server)
admin.site.register(ServerSpec)
admin.site.register(Stat)
admin.site.register(User);
