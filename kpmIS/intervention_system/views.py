from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required, permission_required

from intervention_system.models import Mentor, Student, Admin, Report, Appointment  # Import the Student model

def mylogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        role = request.POST["role"]

        if role == "1":  # Student login
            try:
                student = Student.objects.get(student_id=username, student_password=password)
                
                # Redirect to student page upon successful login
                return redirect('studMainPage', studId=student.student_id)
            except Student.DoesNotExist:
                # Handle invalid student ID or password
                message = {"message": "Invalid student ID or password"}
                return render(request, 'login_page.html', message)

        elif role == "2":  # Lecturer login
            try:
                lecturer = Mentor.objects.get(mentor_id=username, mentor_password=password)
    
                # Redirect to lecturer page upon successful login
                return redirect('lectMainPage', lectId=lecturer.mentor_id)
            except Mentor.DoesNotExist:
                # Handle invalid lecturer ID or password
                lectData = {"message": "Invalid Lecturer ID or password"}
                return render(request, 'login_page.html', lectData)

        elif role == "3":  # Admin login
            try:
                admin = Admin.objects.get(admin_id=username, admin_password=password)

                # Redirect to admin page upon successful login
                return redirect('adminMainPage', adminId=admin.admin_id)
            except Admin.DoesNotExist:
                # Handle invalid admin ID or password
                adminData = {"message": "Invalid Admin ID or password"}
                return render(request, 'login_page.html', adminData)

        else:
            # Handle invalid role
            message = {"message": "Invalid role"}
            return render(request, 'login_page.html', message)
    else:
        return render(request, 'login_page.html')

def studMainPage(request, studId):
    sel_student = Student.objects.get(student_id=studId)
    myreport = Report.objects.filter(student=sel_student).values()
    myapp = Appointment.objects.filter(student=sel_student).values()
    obj={
        'student':sel_student,
        'reports':myreport,
        'app':myapp
    }
    return render(request, 'student_mainpage.html',obj)

def studentProfile(request, studId):
    student = Student.objects.get(student_id=studId)

    obj ={
        'student':student,
    }
    return render(request,'student_profile.html',obj)   

def studEditProfile(request,studId):
    student = Student.objects.get(student_id=studId)
    if request.method=="POST":
        name = request.POST["name"]
        password = request.POST["pass"]
        addr = request.POST["addr"]
        phone = request.POST["phone"]

        student.student_name = name
        student.student_password = password
        student.student_address = addr
        student.student_phone = phone

        student.save()

        return redirect("studentProfile",studId=studId) 

    obj = {
        'student':student
    }
    return render(request, 'student_editprofile.html',obj)



































def lectMainPage(request, lectId):
    # display report related to lecturer
    reports = Report.objects.filter(mentor=lectId).values

    # display app related to lecturer
    app = Appointment.objects.filter(mentor=lectId).values

    # display related data about lecturer
    lecturer = Mentor.objects.get(mentor_id=lectId)

    # all student
    allstudent = Student.objects.all().values()

    obj = {
        "allReport":reports,
        "allApp":app,
        "lect":lecturer,
        'allStudent':allstudent
    }
    
    return render(request, 'lecturer_mainpage.html',obj)
def searchreport(request,lectId):
    searchName = Report.objects.filter(Q(report_date=request.GET.get('searchItem')))
    
    # display app related to lecturer
    app = Appointment.objects.filter(mentor=lectId).values

    # display related data about lecturer
    lecturer = Mentor.objects.get(mentor_id=lectId)

    # all student
    allstudent = Student.objects.all().values()

    obj = {
        "allReport":searchName,
        "allApp":app,
        "lect":lecturer,
        'allStudent':allstudent
    }
    return render(request, 'lecturer_mainpage.html',obj)
def lectReport(request, lectId):

    # display all students
    allstudent = Student.objects.all().values()
    
    # get lecturer data
    lecturer = Mentor.objects.get(mentor_id=lectId)

    if request.method == "POST":
        sid = request.POST["sel_studId"]
        men = request.POST["sel_lectId"]
        date = request.POST["date"]
        cat = request.POST["sel_category"]
        desc = request.POST["report_desc"]

        fksid = Student.objects.get(student_id=sid)
        fkmen = Mentor.objects.get(mentor_id=men)
        report = Report(student=fksid,mentor=fkmen, report_date=date,report_category=cat, report_text=desc)
        report.save()

        return redirect('lectMainPage',lectId=lectId)

    obj = {
        'allStudent':allstudent,
        'lect':lecturer

    }
    return render(request, 'lecturer_report.html', obj )

def deleteReport(request, lectId, recid):
    sel_report =  Report.objects.get(id=recid).delete()

def updateReport(request, lectId, recid):
    sel_report = Report.objects.get(id=recid)
    if request.method == "POST":
        cat = request.POST["sel_category"]
        desc = request.POST["report_desc"]

        sel_report.report_category = cat
        sel_report.report_text = desc
        sel_report.save()

        return redirect('lectMainPage',lectId=lectId)
    
    return redirect('', lectId=lectId)

def deleteApp(request, lectId, recid):
    sel_app =  Appointment.objects.get(id=recid).delete()
    
    return redirect('lectMainPage', lectId=lectId)

def lectApp(request, lectId):
    # display all students
    allstudent = Student.objects.all().values()
    
    # get lecturer data
    lecturer = Mentor.objects.get(mentor_id=lectId)
    
    if request.method == "POST":
        sid = request.POST["sel_studId"]
        men = request.POST["sel_lectId"]
        date = request.POST["date"]

        ven = request.POST["venue"]
        time = request.POST["time"]
        purpose = request.POST["purpose"]
        desc = request.POST["desc"]

        fksid = Student.objects.get(student_id=sid)
        fkmen = Mentor.objects.get(mentor_id=men)
        app = Appointment(student=fksid,mentor=fkmen, appointment_date=date,
        appointment_venue = ven, appointment_time =time, appointment_description=desc,
        appointment_purpose=purpose)
        
        app.save()

        return redirect('lectMainPage',lectId=lectId)



    obj = {
        'allStudent':allstudent,
        'lect':lecturer

    }
    return render(request,'lecturer_appointment.html',obj)

# display all student
def lect_displayAllStudent(request, lectId):
    # all students
    allStudent = Student.objects.all().values()
    lecturer = Mentor.objects.get(mentor_id=lectId)

    obj = {
        'student':allStudent,
        'lect':lecturer
    }
    return render(request, 'lecturer_student.html',obj)

def lect_displayMentee(request, lectId):
    
    # mentee only
    lecturer = Mentor.objects.get(mentor_id=lectId)
    mentee = Student.objects.filter(mentor=lecturer).values()

    obj = {
        'student':mentee,
        'lect':lecturer
    }
    return render(request, 'lecturer_student.html',obj)



# admin
def adminMainPage(request, adminId):
    admin = Admin.objects.get(admin_id=adminId)
    obj={
        "admin":admin
    }
    return render(request, 'admin_mainpage.html',obj)

def adminAllReport(request, adminId):
    admin = Admin.objects.get(admin_id=adminId)
    reports = Report.objects.all().values()
    obj={
        "admin":admin,
        "reports":reports
    }
    return render(request, 'admin_allreport.html',obj)

def adminAllApp(request, adminId):
    admin = Admin.objects.get(admin_id=adminId)
    app = Appointment.objects.all().values()
    obj={
        "admin":admin,
        'apps':app
    }
    return render(request, 'admin_allapp.html',obj)

def adminAllStud(request, adminId):
    admin = Admin.objects.get(admin_id=adminId)
    student =Student.objects.all().values()
    obj={
        "admin":admin,
        'students':student
    }
    return render(request, 'admin_allstudent.html',obj)

def adminAddStud(request, adminId):
    admin = Admin.objects.get(admin_id=adminId)
    lecturer = Mentor.objects.all().values()
    if request.method=="POST":
        studid=request.POST['studid']
        password=request.POST['pass']
        studname=request.POST['studname']
        course=request.POST['course']
        men=request.POST['mentor']

        sel_mentor = Mentor.objects.get(mentor_id=men)

        new_student = Student(student_id=studid,student_password=password,student_name=studname,mentor=sel_mentor,student_course=course)

        new_student.save()
    obj={
        "admin":admin,
        'lect':lecturer
    }
    return render(request, 'admin_addstudent.html',obj)

def updateStudent(request,studId):
    student = Student.objects.get(student_id=adminId)
    if request.method=="POST":
        studid=request.POST['studid']
        password=request.POST['pass']
        studname=request.POST['studname']
        course=request.POST['course']
        men=request.POST['mentor']

        sel_mentor = Mentor.objects.get(mentor_id=men)

        new_student = Student(student_id=studid,student_password=password,student_name=studname,mentor=sel_mentor,student_course=course)

        new_student.save()
    obj={
        "student":stundet,
    }
    return render(request,'student_updateprofile.html',obj)

def adminAddMentor(request, adminId):
    admin = Admin.objects.get(admin_id=adminId)
    if request.method=="POST":
        menid=request.POST['menid']
        password=request.POST['pass']
        menname=request.POST['menname']
        sub=request.POST['sub']

        new_mentor = Mentor(mentor_id=menid,mentor_password=password,mentor_name=menname,mentor_sub=sub)
        new_mentor.save()
    obj={
        "admin":admin,
    }
    return render(request, 'admin_addmentor.html',obj)

