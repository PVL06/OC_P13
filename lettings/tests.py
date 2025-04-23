from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.db.utils import IntegrityError

from lettings.views import letting, index
from lettings.models import Letting, Address


class TestLettingsUrls(SimpleTestCase):
    """
    Test class to verify that URLs are correctly resolved.
    """
    def test_lettings_index_url_resolves(self):
        url = reverse('lettings_index')
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_resolves(self):
        url = reverse('letting', args=[1])
        self.assertEqual(resolve(url).func, letting)


class LettingsViewsTests(TestCase):
    """
    Test class for the views in the lettings app.
    """
    def setUp(self):
        self.address = Address.objects.create(
            number=10,
            street='test street',
            city='test city',
            state='TT',
            zip_code=99999,
            country_iso_code='TST'
        )
        self.letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )

    def test_index_view(self):
        response = self.client.get(reverse('lettings_index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertIn('lettings_list', response.context)
        self.assertIn(self.letting, response.context['lettings_list'])

    def test_letting_view(self):
        response = self.client.get(reverse('letting', args=[self.letting.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.context['title'], self.letting.title)
        self.assertEqual(response.context['address'], self.letting.address)

    def test_letting_view_with_bad_id(self):
        """
        Test that the letting view returns a 404 status code when the id does not exist.
        """
        non_existent_id = 2
        response = self.client.get(reverse('letting', args=[non_existent_id]))

        self.assertEqual(response.status_code, 404)


class AddressModelTests(TestCase):
    """
    Test class for the Address model.
    """
    def test_address_creation(self):
        address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.assertEqual(str(address), '123 Test Street')


class LettingModelTests(TestCase):
    """
    Test class for the Letting model.
    """

    def test_letting_creation_and_relation(self):
        address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        letting = Letting.objects.create(
            title='Test Letting',
            address=address
        )
        self.assertEqual(str(letting), 'Test Letting')
        self.assertEqual(letting.address, address)

    def test_letting_without_address(self):
        with self.assertRaises(IntegrityError):
            Letting.objects.create(title='Test Letting')
