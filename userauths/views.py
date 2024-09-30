from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}. You account was created successfully.")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect("core:index")

    else:

        form = UserRegisterForm()

    context = {
        'form': form,
        }
    return render(request, "userauths/sign-up.html", context)


# def login_view










    # """
    #    Method :
    #        GET -  example.com/signup
    #        POST - example.com/signup body {username: user, password: password}
    #    1. accept user data
    #    2. update db with new use
    #    3. success/failure
    #    """
    # if request.method == "GET":
    #     form = UserRegisterForm()
    #     return render(request, "userauths/sign-up.html", {"form": form})
    #
    # if request.method == "POST":
    #     form = UserRegisterForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         return render(request,"userauths/sign-up.html", {"form": form})
    #     else:
    #         print(form.errors)
    #         return render(request, "userauths/sign-up.html", {"form": form})