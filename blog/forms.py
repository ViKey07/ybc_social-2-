from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'autocomplete': 'off'}),
        }
