import random
import string

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Announcemet, Course

# Create your views here.


def index(request):
    try:
        user = request.user
        courses = Course.objects.filter(courseStudent=user)
        return render(request, "index.html", {"courses": courses})
    except Exception as e:
        print(e)
        return render(request, "index.html")


def search(request):
    query = request.GET.get("query", "")
    courseName = Course.objects.filter(courseName__icontains=query, courseStudent=request.user)
    courseCode = Course.objects.filter(courseCode__icontains=query, courseStudent=request.user)
    courseDesc = Course.objects.filter(courseDesc__icontains=query, courseStudent=request.user)
    coursesection = Course.objects.filter(courseSection__icontains=query, courseStudent=request.user)
    courses = courseName.union(courseCode, courseDesc, coursesection)
    print(courses)
    return render(request, "search.html", {"courses": courses, 'query':query})


def classRoom(request, slug):
    course = get_object_or_404(Course, sno=slug)
    announcement = Announcemet.objects.filter(annMaterial=course)
    if request.method == "POST":
        if request.user in course.courseStudent.all():
            annMaterial = course
            annTitle = request.POST.get("annTitle", "")
            annContent = request.POST.get("annContent", "")
            try:
                annFile = request.FILES["annFile"]
                fs = FileSystemStorage()
                annFile = fs.save(f"{annFile.name}", annFile)
                announcement = Announcemet(annCreator=request.user,
                                           annMaterial=annMaterial, annFile=annFile, annTitle=annTitle, annContent=annContent)
                announcement.save()
                messages.success(
                request, "New Announcement was added to this Classroom")
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            except Exception as e:
                announcement = Announcemet(
                    annCreator=request.user, annMaterial=annMaterial, annTitle=annTitle, annContent=annContent)
                announcement.save()
                messages.success(
                request, "New Announcement was added to this Classroom")
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            messages.warning(
                request, "Sorry, you are not authorised to add announcements to this class")
            return redirect("/")
    else:
        if request.user in course.courseStudent.all():
                user = request.user
                courses = Course.objects.filter(courseStudent=user)
                context = {"courses": courses, "course": course,
                        "announcements": announcement}
                return render(request, "classroom.html", context)
        else:
            messages.warning(
                request, "Sorry, you are not authorized to enter into that class")
            return redirect("/")


def createClass(request):
    if request.method == "POST":
        courseCode = request.POST.get("courseCode", "")
        courseName = request.POST.get("courseName", "")
        courseSection = request.POST.get("courseSection", "")
        courseDesc = request.POST.get("courseDesc", "")
        str1 = ''.join((random.choice(string.ascii_letters) for x in range(3)))
        str1 += ''.join((random.choice(string.digits) for x in range(3)))
        sam_list = list(str1)
        random.shuffle(sam_list)
        courseRefNo = ''.join(sam_list)
        bgColors = ['danger', 'primary', 'success', 'dark', 'secondary']
        theme = random.choice(bgColors)

        course = Course(courseCode=courseCode, courseName=courseName, courseCreator=request.user,
                        courseSection=courseSection, courseDesc=courseDesc, courseRefNo=courseRefNo, theme=theme)
        course.save()
        course.courseStudent.add(request.user)
        course.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        messages.warning(request, "Sorry, You are not authorized to do that")
        return redirect("/")


def editclass(request, slug):
    course = get_object_or_404(Course, sno=slug)
    if request.method == "POST":
        course.courseCode = request.POST.get("courseCode", "")
        course.courseName = request.POST.get("courseName", "")
        course.courseSection = request.POST.get("courseSection", "")
        course.courseDesc = request.POST.get("courseDesc", "")
        course.save()
        print(course)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        messages.warning(request, "Osrry, you are not authorized to do that")
        return redirect("/")


def deleteclass(request, slug):
    if request.method == "POST":
        course = get_object_or_404(Course, courseRefNo=slug)
        course.delete()
        return redirect("/")
    else:
        return HttpResponse("404 Not Found")


def joinClass(request):
    if request.method == "POST":
        joincode = request.POST["joincode"]
        course = get_object_or_404(Course, courseRefNo=joincode)
        if request.user not in course.courseStudent.all():
            print(course)
            course.courseStudent.add(request.user)
            course.save()
            messages.info(request, "Congratulations! You have joined this classroom")
        else:
            messages.info(request, "Oops, You have already joined this classroom")
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        messages.warning(request, "Sorry, Unknown error occured")
        return redirect("/")

def people(request, slug):
    course = get_object_or_404(Course, sno=slug)
    courses = Course.objects.all()
    if request.user in course.courseStudent.all():
        context = {"courses": courses, "course": course}
        return render(request, "people.html", context)
    else:
        messages.warning(request, "Sorry, you are not authorized to enter into that class")
    return redirect("/")
    


# Authentication Functions
email = ""
sentOtp = ""


def sendOtp(request):
    if request.method == "POST":
        global email
        email = request.POST.get('email', "")
        global sentOtp
        sentOtp = ""
        for i in range(6):
            sentOtp += str(random.randrange(0, 10))
        print(sentOtp)

        subject, from_email, to = f"Otp for your Blogging account at Poster", 'rakeshgombi18@gmail.com', f'{email}'
        text_content = f'Your OTP for email verification at Poster is <strong>{sentOtp}'
        html_content = f''' <div style="background: #eee; padding: 15px; margin: 0; display: inline-block; border-radius:10px ">
                    <div class="container"
                    style="padding: 10px; border-radius: 10px; background-color: rgb(255, 255, 255); display: inline-block; margin:0 auto">
                    <h4>Hi There,</h4>
                    <p>Your OTP for email verification at Poster is <strong>{sentOtp} </strong></p>
                    <p>Good luck! Have a nice day😊</p>
                    </div>
                    <p style="text-align: center; color: rgb(93, 93, 93);">Thank you for blogging with poster</p>
                    </div>'''
        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    return redirect("/")


def handleSignUp(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        global email
        global sentOtp
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        otp = request.POST['otp']
        if otp == sentOtp:
            if pass1 == pass2:
                if len(pass1) < 8:
                    messages.warning(
                        request, 'Sorry, Minimum length of the password must be 8')
                elif not(username.isalnum()):
                    print(
                        'Sorry, useranme can only be combinations of alphabets and numbers')
                elif User.objects.filter(username=username).exists():
                    messages.warning(request, 'Sorry, Username already taken')
                elif User.objects.filter(email=email).exists():
                    messages.warning(
                        request, 'Sorry, Account with the same email already exists')
                else:
                    user = User.objects.create_user(
                        first_name=fname, last_name=lname,  username=username, email=email, password=pass1)
                    user = authenticate(username=username, password=pass1)
                    if user is not None:
                        login(request, user)
                    user.save()
                    messages.success(
                        request, 'Congratulations, Account created Successfully!')
            else:
                messages.warning(
                    request, 'Sorry, Passwords do not match! Try again')
        else:
            messages.warning(request, "Sorry, OTP does'nt match")
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        return HttpResponse("404 Error")


def handleLogIn(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginPassword = request.POST["loginPassword"]
        user = authenticate(username=loginusername, password=loginPassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back, login successful")
        else:
            messages.warning(
                request, "login failed, You do not have active registered account")
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        messages.warning(request, "Sorry, unknown error occured")
        return redirect("/")


def handleLogout(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
