from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Spec.views import info_company_list, info_company_detail, seguridad_social_detail

class TestUrls(SimpleTestCase):
    
    def test_list_url_is_resolved(self):
        url = reverse('company')
        self.assertEquals(resolve(url).func, info_company_list)

    def test_info_company_detail(self):
        url = reverse('company_detail', args=[1])
        self.assertEquals(resolve(url).func, info_company_detail)

    def test_seguridad_social_detail(self):
        url = reverse('company_ss', args=[1])
        self.assertEquals(resolve(url).func, seguridad_social_detail)
