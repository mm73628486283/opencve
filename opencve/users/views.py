from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView

from users.forms import LoginForm, RegisterForm


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    redirect_authenticated_user = True


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, f"Registration successful, email sent to {user.email}"
            )
            return redirect("login")
    form = RegisterForm()
    return render(
        request=request, template_name="users/register.html", context={"form": form}
    )
