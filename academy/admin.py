from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(StudentData)
admin.site.register(ClassData)
admin.site.register(Branch)
admin.site.register(ClassInBranch)
admin.site.register(StudentAttendClass)
