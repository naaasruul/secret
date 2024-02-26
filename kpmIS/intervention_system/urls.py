from django.urls import path
from . import views

urlpatterns = [

    # user login
    path("", views.mylogin, name="login"),

    # to page student
    path("mystudent/<str:studId>/mainpage", views.studMainPage, name="studMainPage"),

    # student display profile
    path("mystudent/<str:studId>/profile", views.studentProfile, name="studentProfile"),

    # student update their profile
    path("mystudent/<str:studId>/profile/edit", views.studEditProfile, name="studEditProfile"),

# ----------------- LECTURER -----------------------------------------
    # to lecturer main page
    path("mylecturer/<str:lectId>/mainpage", views.lectMainPage, name="lectMainPage"),

    # lecturer make report
    path("mylecturer/<str:lectId>/mainpage/report", views.lectReport, name="lectReport"),
    # lecturer make appointment with student
    path("mylecturer/<str:lectId>/mainpage/appointment", views.lectApp, name="lectApp"),

    # lecturer display all student
    path("mylecturer/<str:lectId>/mainpage/allstudent", views.lect_displayAllStudent, name="lect_displayAllStudent"),

    # lecturer display all mentee
    path("mylecturer/<str:lectId>/mainpage/mentee", views.lect_displayMentee, name="lect_displayMentee"),

    # lecturer delete report
    path("mylecturer/<str:lectId>/deletereport/<str:recid>", views.deleteReport, name="deleteReport"),

    # lecturer delet app
    path("mylecturer/<str:lectId>/deleteapp/<str:recid>", views.deleteApp, name="deleteApp"),

    # lecturer edit their reports
    path("mylecturer/<str:lectId>/updatereport/<str:recid>", views.updateReport, name="updateReport"),

    # lecturer search report by date
    path("mylecturer/<str:lectId>/search", views.searchreport, name="searchreport"),

    # lecturer edit their appointment
    path("mylecturer/<str:lectId>/mainpage", views.lectMainPage, name="lectMainPage"),

    # lecturer edit their profile
    path("mylecturer/<str:lectId>/mainpage", views.lectMainPage, name="lectMainPage"),

# ----------------- LECTURER -----------------------------------------

# ------------------ Admin ---------------------------------------------
    # to admin mainpage
    path("myadmin/<str:adminId>/mainpage", views.adminMainPage, name="adminMainPage"),

    # admin view report
    path("myadmin/<str:adminId>/AllReport", views.adminAllReport, name="adminAllReport"),

    # admin view all app
    path("myadmin/<str:adminId>/AllAppointment", views.adminAllApp, name="adminAllApp"),

    # admin view student
    path("myadmin/<str:adminId>/AllStudent", views.adminAllStud, name="adminAllStud"),

    # admin add new student.
    path("myadmin/<str:adminId>/addStudent", views.adminAddStud, name="adminAddStud"),

    # admin add new mentor.
    path("myadmin/<str:adminId>/addMentor", views.adminAddMentor, name="adminAddMentor"),
    
]