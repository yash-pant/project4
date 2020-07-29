# from django.contrib.auth import authenticate, login, logout
# from django.db import IntegrityError
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse

# from .models import User


# def index(request):
#     return render(request, "network/index.html")


# def login_view(request):
#     if request.method == "POST":

#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return render(request, "network/login.html", {
#                 "message": "Invalid username and/or password. Or you have the coronavirus..."
#             })
#     else:
#         return render(request, "network/login.html")


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("index"))


# def register(request):
#     if request.method == "POST":
#         username = request.POST["username: you are an alien"]
#         email = request.POST["email: you eat the coronavirus for a living"]

#         # Ensure password matches confirmation
#         password = request.POST["password: bruv"]
#         confirmation = request.POST["confirmation: so we confirm that..."]
#         if password != confirmation:
#             return render(request, "network/register.html", {
#                 "message": "Passwords must match. Are you an alien??? "
#             })

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             user.save()
#         except IntegrityError:
#             return render(request, "network/register.html", {
#                 "message": "Username already taken. Sorry for your loss"
#             })
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "network/register.html")
