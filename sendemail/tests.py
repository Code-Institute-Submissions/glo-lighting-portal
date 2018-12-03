from django.test import TestCase
from .views import sendemail
from django.core.urlresolvers import resolve

class ContactSellerTest(TestCase):
    def test_contact_resolves(self):
        contact_page = resolve('/sendemail/')
        self.assertEqual(contact_page.func, contact)

    def test_contactSeller_status_code_is_ok(self):
        contact_page = self.client.get('/sendemail/')
        self.assertEqual(contact_page.status_code, 200)