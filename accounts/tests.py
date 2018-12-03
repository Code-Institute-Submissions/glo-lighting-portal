from django.test import TestCase
from .models import Brand
from .forms import BrandRegistrationForm
from django import forms
from django.conf import settings

class CustomUserTest(TestCase):
    def test_registration_form(self):
        form = BrandRegistrationForm({
            'sellername': 'testuser',
            'email': 'mytest@gmail@gmail.com',
            'password1': 'comein1',
            'password2': 'comein1',
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_password(self):
        form = BrandRegistrationForm({
            'sellername': 'testuser',
            'email': 'mytest@gmail@gmail.com',
            'password1': 'comein1',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                "please enter both passwords",form.full_clean())

    def test_registration_form_fails_with_passwords_that_dont_match(self):
        form = BrandRegistrationForm({
            'sellerame': 'testuser',
            'email': 'test@test.com',
            'password1': 'comein1',
            'password2': 'comein3',

        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,"Passwords do not match",form.full_clean())

		
