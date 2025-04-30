from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from profiles.views import profile, index
from profiles.models import Profile


class TestLettingsUrls(SimpleTestCase):

    def test_profiles_index_url_resolves(self):
        url = reverse('profiles_index')
        self.assertEqual(resolve(url).func, index)

    def test_profile_url_resolves(self):
        url = reverse('profile', args=[1])
        self.assertEqual(resolve(url).func, profile)


class ProfilesViewsTests(TestCase):
    """
    Test class for the views in the profiles app.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Test City'
        )

    def test_index_view(self):
        response = self.client.get(reverse('profiles_index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertIn('profiles_list', response.context)
        self.assertIn(self.profile, response.context['profiles_list'])

    def test_profile_view(self):
        response = self.client.get(reverse('profile', args=[self.user.username]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.context['profile'], self.profile)

    def test_profile_view_with_bad_username(self):
        """
        Test that the profile view returns a 404 status code when the username does not exist.
        """
        non_existent_username = 'nonexistentuser'
        response = self.client.get(reverse('profile', args=[non_existent_username]))

        self.assertEqual(response.status_code, 404)


class ProfileModelTests(TestCase):
    """
    Test class for the Profile model.
    """

    def test_profile_model(self):
        """
        Test the Profile model for:
        creation, favorite_city field, string representation, user relation
        and favorite_city field not null.
        """
        user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        profile = Profile.objects.create(
            user=user,
            favorite_city='Paris'
        )

        self.assertTrue(Profile.objects.filter(user=user).exists())
        self.assertEqual(profile.favorite_city, 'Paris')
        self.assertEqual(str(profile), user.username)
        self.assertEqual(profile.user, user)

        with self.assertRaises(IntegrityError):
            Profile.objects.create(user=user)
