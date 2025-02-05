from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User

class UserRegisterFrom(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
        attrs={'class':'mb-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}),
        required=True
    )
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
        attrs={'class':'mb-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}),
        required=True
    )
    
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
        attrs={'class':'mb-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}),
        required=True
    )
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class LoginUser(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
        attrs={'class':'mb-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}),
        required=True
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
        attrs={'class':'mb-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}),
        required=True
    )
    
    class Meta:
        model = User
        fields = ['username', 'password1']