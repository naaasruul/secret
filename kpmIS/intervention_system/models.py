from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required, permission_required

from django.db import models

# Create your models here.

class Mentor(models.Model):
    mentor_id = models.CharField(max_length=5, primary_key=True)
    mentor_name = models.CharField(max_length=200)
    mentor_password = models.CharField(max_length=128)
    mentor_phone = models.CharField(max_length=15, blank=True, default="Value not set")
    mentor_sub = models.CharField(max_length=15, blank=True, default="Value not set")
    # Add any other fields relevant to the mentor

class Student(models.Model):
    student_id = models.CharField(max_length=5, primary_key=True)
    student_name = models.CharField(max_length=200)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student_password = models.CharField(max_length=128)
    student_address = models.TextField(blank=True, null=True, default="Value not set")
    student_phone = models.CharField(max_length=15, blank=True, null=True, default="Value not set")
    student_course = models.CharField(max_length=15, blank=True, null=True, default="Value not set")
    # Add any other fields relevant to the student

class Admin(models.Model):
    admin_id = models.CharField(max_length=5, primary_key=True)
    admin_name = models.CharField(max_length=200)
    admin_password = models.CharField(max_length=128)
    # Add any other fields relevant to the admin

class Appointment(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_venue = models.CharField(max_length=100)
    appointment_time = models.TimeField()
    appointment_description = models.TextField(blank=True, null=True, default="-")
    appointment_purpose = models.TextField(blank=True, null=True, default="-")
    appointment_status = models.CharField(max_length=8, default="Pending...")
    # Add any other fields relevant to the appointment

class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    report_date = models.DateField(auto_now_add=True)
    report_category = models.CharField(max_length=100)
    report_text = models.TextField()
    # Add any other fields relevant to the report
