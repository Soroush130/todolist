from django import forms 
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    def clean_re_password(self):
        re_password = self.cleaned_data['re_password']
        password = self.cleaned_data['password']
        if re_password != password:
            raise forms.ValidationError('re_password Not equl with password')

        return re_password

    def clean_username(self):
        username = self.cleaned_data['username']
        username_is_exists = User.objects.filter(username=username).exists()
        if username_is_exists == True:
            raise forms.ValidationError("User is exists")

        return username


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

class EditeProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']