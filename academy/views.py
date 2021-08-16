from django.http.response import HttpResponseBadRequest
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import datetime

# Create your views here.


def detail_kelas(request, id_kelas):
    class_data = ClassData.objects.get(pk=id_kelas)
    return HttpResponse(class_data.name)


def form_registration(request):
    if(request.POST == {}):
        print("GET")
        return render(request, 'form_registration.html')
    else:
        if(request.user.is_authenticated):
            print(request.POST)
            user = request.user

            code_edu = 0
            if(request.post['education'] == 'SD'):
                code_edu = 1
            if(request.post['education'] == 'SMP'):
                code_edu = 2
            userData = StudentData.objects.create(
                name=request.POST['name'],
                placeOfBirth=request.POST['tempat-lahir'],
                dateOfBirth=datetime.datetime(''),
                gender='',
                address='',
                handphone='',
                education=code_edu,
                user=user,
            )
            userData.save()
            redirect('/')
        else:
            redirect('/login/')


def login_me(request):
    if(request.POST == {}):
        print("GET")
        return render(request, 'login.html')
    else:
        print("POST")
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if(user.user_level == 0):
                return redirect('/dashboard/')
            return redirect('/')
        else:
            return render(request, 'login.html', {'message': 'wrong username or password'})


def logout_me(request):
    logout(request)
    return redirect('/')


def register_class(request, id_class):
    if(request.POST == {}):
        print(request.GET)
        # if(request.user.is_authenticated):
        #     class_data = ClassData.objects.get(pk=id_class)
        #     student_data = StudentData.objects.get(user=request.user)

        #     student_class_yang_diambil = StudentAttendClass.objects.filter(student=student_data)
        #     for class_yang_diambil in student_class_yang_diambil :
        #         #cek apakah ada day yang sama dengan day yang mau didaftarin sekarang
        #         if(class_data.activeDay == class_yang_diambil.activeDay):
        #             id_branch = class_yang_diambil.branch.id
        #             branch_data = Branch.objects.get(pk=id_branch)
        #             classInBranch_Data = ClassInBranch.objects.filter(branch = branch_data)

        #             return render(request, 'register_class.html',{'message':'kelas bentrok','suggested_class_list':classInBranch_Data})

        return render(request, 'register_class.html', {'code unik': 'ABC'})

        # else :
        #     return redirect('/')
    else:
        print(request.POST)
        return render(request, 'register_class.html')


def register_user(request):
    if(request.POST == {}):
        print(request.GET)
        return render(request, 'register_user.html')
    else:
        print(request.POST)
        try:
            user = User.objects.create(
                username=request.POST['username'],
                user_level=2
            )
        except Exception as e:
            return render(request, 'register_user.html', {'message': 'Terjadi masalah pada username, silahkan coba username lain'})
        user.set_password(request.POST['password'])
        user.save()
        return redirect('/')


def dashboard(request, id_branch):
    if(request.user.is_authenticated):
        if(request.user.user_level == 0):
            # ngambil seluruh cabang
            branch_list = Branch.objects.all()
            # ngambil seluruh kelas
            class_list = ClassData.objects.all()

            # ngambil informasi cabang soekarno-hatta
            # branch_soekarno_hatta = Branch.objects.get(pk=1)

            # ngambil informasi untuk cabang sesuai dengan id
            branch_data = Branch.objects.get(pk=id_branch)

            # ngambil kelas yang ada di soekarnohatta
            class_in_branch = ClassInBranch.objects.filter(
                branch=branch_data)

            sum_profit = 0
            for i in class_in_branch:
                sum_profit += i.classRegistered.price
                print(i.classRegistered.name)
                print(i.classRegistered.price)

            # print(class_in_branch_1)
            return render(request, 'dashboard.html', {'branch': branch_data, 'class_list': class_in_branch, 'sum_profit': sum_profit})
        return HttpResponse("Anda tidak punya hak")
    else:
        return redirect('/login/')


def landing(request):
    return render(request, 'landing.html')
