from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, FormView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustonUserCreationForm

# Create your views here.
class RequestProfile(LoginRequiredMixin, View):
    """docstring for Profile."""
    def get(self, request) :
        return HttpResponse("Profile for "+request.user.get_full_name())


class Profile(DetailView):
    """docstring for Profile."""
    model = User


class ProfileEdit(UpdateView):
    """docstring for ProfileEdit."""
    model = User
    fields = ['first_name', 'last_name', 'email',]

class RegisterUser(FormView):
    """docstring for RegisterUser."""
    form_class = CustonUserCreationForm
    template_name = 'registration/register.html'


def depositVisa(request, *args, **kwargs):
    context = {
        'key':'value',
    }
    return render(request, 'accounts/deposit/visa.html', context)
