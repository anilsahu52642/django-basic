from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm,UsernameField,SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _

class customloginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),
    )



class pchangeform(SetPasswordForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,'class':'form-control'}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']


    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password
