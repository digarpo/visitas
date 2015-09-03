from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email','password')
        widgets = {
            'username' : forms.TextInput(attrs =
                {
                    'class' : 'form-control',
                    'placeholder' : 'Ingresa un nombre de usuario'}),
            'email' : forms.TextInput(attrs =
                {
                    'type' : 'email',
                    'class' : 'form-control',
                    'placeholder' : 'Introduce un email'}),
            'password' : forms.TextInput(attrs =
                {
                    'type' :'password',
                    'class' : 'form-control',
                    'placeholder' : 'Introduce un password'
                })
        }

class LoginForm(forms.Form):

    username = forms.CharField(max_length=30,
                            widget=forms.TextInput(attrs={
                               'class' : 'form-control',
                               'placeholder' : 'Inserta tu nombre de usuario'
                           }))

    password = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={
                                   'type' : 'password',
                                   'class' : 'form-control',
                                   'placeholder' : 'Inserta tu password'
                               }))

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {}
        widgets = {
            'email' : forms.TextInput(attrs =
                {
                    'type' : 'email',
                    'class' : 'form-control',
                    'placeholder' : 'Introduce un email'}),
            'password' : forms.TextInput(attrs =
                {
                    'type' :'password',
                    'class' : 'form-control',
                    'placeholder' : 'Introduce un password'}),
            'first_name' : forms.TextInput(attrs =
                {
                    'type': 'first_name',
                    'class': 'form-control',
                    'placeholder': 'Introduce tu nombre'}),
            'last_name' : forms.TextInput(attrs=
                {
                    'type': 'last_name',
                    'class': 'form-control',
                    'placeholder': 'Introduce tu apellido'}),
            'avatar' : forms.ClearableFileInput(attrs=
                {
                    'type': 'last_name',
                    'class': 'form-control',
                    'placeholder': 'Introduce un avatar'})
        }

class UserModfForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('created','modified',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'first_name': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'last_name': forms.Select(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CompanyDocsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {}
        widgets = {
            'TC2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'safe': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ssocial':forms.ClearableFileInput(attrs={'class': 'form-control'}),
           # 'notETT':forms.Checkbox, choices =
            'risk':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'protection':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ICCo':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ICSyva':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'PRL03':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'PRL04':forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UserDocsWorkerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {}
        widgets = {
            #'TA2_date':
            'TA2_doc':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'medical':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'EPI_doc':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'medical_doc':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'information_doc':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'skill_doc':forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }
