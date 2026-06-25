from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")

        user = authenticate(username=uname, password=password)

        if user is None:
            return render(
                request,
                "index.html",
                {"error": "Invalid Username or Password"}
            )

        login(request, user)
        return redirect("home")

    return render(request, "index.html")


@login_required(login_url="index")
def home(request):
    return render(request, "home.html")


def forgetpassword(request):
    if request.method == "POST":
        email = request.POST.get("email")

        try:
            send_mail(
                subject="Test Email",
                message="Hello Mousumi, Email integration is working successfully.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            return render(
                request,
                "forget.html",
                {"msg": "Email sent successfully"}
            )

        except Exception as e:
            return render(
                request,
                "forget.html",
                {"error": str(e)}
            )

    return render(request, "forget.html")