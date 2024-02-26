from django.contrib import admin
from .models import Mentor,Student,Appointment,Admin, Report

# Register your models here.
admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(Report)
admin.site.register(Admin)
admin.site.register(Appointment)

