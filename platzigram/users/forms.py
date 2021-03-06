"""User forms"""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """Sing up form"""
    attr = {'placeholder': 'username', 'class': 'form-control'}
    username = forms.CharField(min_length=4,
                               max_length=50,
                               widget=forms.TextInput(attrs=attr))
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs=attr)
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs=attr)
    )
    first_name = forms.CharField(min_length=2,
                                 max_length=50,
                                 widget=forms.TextInput(attrs=attr))
    last_name = forms.CharField(min_length=2,
                                max_length=50,
                                widget=forms.TextInput(attrs=attr))
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(attrs=attr)
    )

    def clean_username(self):
        """User must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')
        return data

    def save(self):
        """Create user an profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create(**data)
        profile = Profile(user=user)
        profile.save()


# class ProfileForm(forms.Form):
#     """Profile forms"""
#     website = forms.URLField(max_length=200, required=True)
#     biography = forms.CharField(max_length=500, required=False)
#     phone_number = forms.CharField(max_length=20, required=False)
#     picture = forms.ImageField()
