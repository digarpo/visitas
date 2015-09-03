from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserRegisterForm, LoginForm,UserModfForm,CompanyDocsForm
from django.views.generic import UpdateView,DetailView
from .models import User
from .functions import LogIn
from .forms import UserForm
from django.core.urlresolvers import reverse, reverse_lazy

def userlogin(request):
	if request.method == "POST":
		if 'register_form' in request.POST:
			user_register = UserRegisterForm(request.POST)
			if user_register.is_valid():
				User.objects.create_user(username = user_register.cleaned_data['username'],
				 email = user_register.cleaned_data['email'],
				 password = user_register.cleaned_data['password'],
                 first_name = user_register.cleaned_data['first_name'],
                 last_name = user_register.cleaned_data['last_name']
                )
				LogIn(request, user_register.cleaned_data['username'],
						user_register.cleaned_data['password'])
				return redirect('/')
		if 'login_form' in request.POST:
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				LogIn(request, login_form.cleaned_data['username'],
						login_form.cleaned_data['password'])
				return redirect('/')
	else:
		user_register = UserRegisterForm()
		login_form = LoginForm()
	return render(request, 'usuarios/login.html',
				{'user_register' : user_register, 'login_form' : login_form})

def userregister(request):
	if request.method == "POST":
		if 'register_form' in request.POST:
			user_register = UserRegisterForm(request.POST)
			if user_register.is_valid():
				User.objects.create_user(username = user_register.cleaned_data['username'],
				 email = user_register.cleaned_data['email'],
				 password = user_register.cleaned_data['password'],
                 # first_name = user_register.cleaned_data['first_name'],
                 # last_name = user_register.cleaned_data['last_name']
                )
				LogIn(request, user_register.cleaned_data['username'],
						user_register.cleaned_data['password'])
				return redirect('/')
		if 'login_form' in request.POST:
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				LogIn(request, login_form.cleaned_data['username'],
						login_form.cleaned_data['password'])
				return redirect('/')
	else:
		user_register = UserRegisterForm()
		login_form = LoginForm()
	return render(request, 'usuarios/registro.html',
				{'user_register' : user_register, 'login_form' : login_form})




def LogOut(request):
    logout(request)
    return redirect('/')


class EditUser(UpdateView):
    template_name = 'usuarios/editar_usuario.html'
    success_url = reverse_lazy('/')
    model = User
    form_class = UserModfForm


class DetailUser(DetailView):
    template_name = 'usuarios/detalle_usuario.html'
    model = User

class EditCompanyDocs(UpdateView):
    template_name = 'usuarios/editar_usuario.html'
    success_url = reverse_lazy('/')
    model = User
    form_class = CompanyDocsForm