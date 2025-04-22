from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from oc_lettings_site.views import index


class TestUrls(SimpleTestCase):
    """
    Test class to verify that URLs are correctly resolved.
    """
    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_admin_url_resolves(self):
        url = reverse('admin:index')
        self.assertEqual(resolve(url).namespace, 'admin')


class IndexViewTests(TestCase):
    """
    Test class to verify page view for status code, template used, and content.
    """
    def test_index_view(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Welcome to Holiday Homes')

    def test_404_page_with_invalid_url(self):
        response = self.client.get('/non_existant_url/')

        self.assertEqual(response.status_code, 404)
