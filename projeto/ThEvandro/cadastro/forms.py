from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password  

class CadastrarUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Adjust fields as necessary
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
