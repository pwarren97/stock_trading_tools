from django import forms
# from django.core.exceptions import ValidationError

suffix_following_label = ': '
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100, required=True, label_suffix=suffix_following_label)
    password = forms.CharField(widget = forms.PasswordInput(), required=True, label_suffix=suffix_following_label)
