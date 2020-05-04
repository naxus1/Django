from django.test import TestCase, Client
from django.urls import reverse
from Spec.models import InfoCompany, SeguridadSocial
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.datail_url = reverse('company_detail', args=['com'])
    
    def test_project_list_GET(self):
        response = self.client.get(reverse('company'))
        self.assertEquals(response.status_code, 200)

    def test_project_detail_GET(self):
        response = self.client.get(reverse('company_detail', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_project_seguridad_social(self):
        response = self.client.get(self.datail_url)