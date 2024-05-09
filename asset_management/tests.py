from django.test import TestCase
from .models import Company

class CompanyModelTest(TestCase):

    def setUp(self):
        self.company_data = {
            'name': 'Test Company',
            'address': '123 Main Street',
            'contact_email': 'test@company.com',
            'phone_number': '555-555-5555',
        }

    def test_company_creation(self):
        company = Company.objects.create(**self.company_data)
        self.assertEqual(company.name, self.company_data['name'])
        self.assertEqual(company.address, self.company_data['address'])
        self.assertEqual(company.contact_email, self.company_data['contact_email'])
        self.assertEqual(company.phone_number, self.company_data['phone_number'])

    def test_company_str_method(self):
        company = Company.objects.create(**self.company_data)
        self.assertEqual(str(company), company.name)
