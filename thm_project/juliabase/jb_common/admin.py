# This file is part of JuliaBase.


from django.contrib import admin
from jb_common.models import UserDetails, Topic, Department

admin.site.register(UserDetails)
admin.site.register(Topic)
admin.site.register(Department)
